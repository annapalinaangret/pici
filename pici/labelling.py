import pandas as pd
import janitor
import numpy as np
from abc import ABC, abstractmethod
from typing import overload
from pandas.api.types import CategoricalDtype
from pici.datatypes import CommunityDataLevel
import os
import plotly.graph_objects as go
import plotly.express as px
from statsmodels.stats import inter_rater
import krippendorff
import simpledorff


class LabelStats:

    def __init__(self, labels):
        self.labels = labels

    def labellers(self):
        return self.labels.data["labeller"].nunique()

    def unique_cases(self):
        return self.labels.data["url"].nunique()

    def label_counts(self, normalize=False):
        d = self.labels.data[self.labels.labels.keys()]
        if not normalize:
            return d.sum()
        else:
            return d.sum() / d.shape[0]

    def label_counts_by_labeller(self, normalize=False):
        d = self.labels.data[list(self.labels.labels.keys()) + ["labeller"]]
        d = d.groupby(by="labeller")

        if normalize:
            return d.mean()
        else:
            return d.sum()

    def label_correlation(self):
        return self.labels.data[list(self.labels.labels.keys())].corr()

    def plot_label_correlation(self):
        corr = self.label_correlation()
        fig = go.Figure()
        fig.add_trace(
            go.Heatmap(
                x=corr.columns,
                y=corr.index,
                z=np.array(corr),
                text=corr.values,
                texttemplate='%{text:.2f}'
            )
        )
        return fig


    def total_agreement(self):
        """
        Get percentage of cases where all labellers agree (per label).

        Returns:
            agreement: Pandas.DataFrame with 'label', '% perfect agreement', 'n'

        """
        res = []
        for label_name, label_type in self.labels.labels.items():
            a = self.labels.data.drop_duplicates(subset=['url', 'labeller'], keep='last')
            a = a.pivot(index="url", columns="labeller", values=label_name)#.dropna()

            if not a.empty:
                """
                if str(label_type) == 'bool':
                    a['all_agree'] = a.apply(np.std, axis=1) == 0
                elif str(label_type) == 'category':
                    def is_unique(s):
                        x = s.to_numpy()
                        return (x[0] == x).all()
                    a['all_agree'] = a.apply(is_unique, axis=1)
                """

                # TODO: fix this... counting np.nan :(
                a = a.reset_index().drop(columns="url")
                b = a.copy()
                b['unique_value'] = a.nunique(axis=1) == 1
                b['num_labellers'] = a.count(axis=1)
                b['valid'] = b.num_labellers >= 2
                b['all_agree'] = b.unique_value.where(b.valid, np.nan)

                if 'all_agree' in b.columns:
                    n_all = b.all_agree.count()
                    n_agree =  b.all_agree.sum()

                    # if True in a.all_agree.value_counts(normalize=True):
                    #    agr = a.all_agree.value_counts(normalize=True)[True]

                    res.append((label_name, n_agree/n_all, n_all))
        agreement = pd.DataFrame(res, columns=["label", "% perfect agreement", "n"])

        return agreement


class Labels(ABC):
    """
    TODO: add documentation
    """

    DEFAULT_COLS = {
        'community': 'community_name',
        'url': 'url',
        'labeller': 'labeller'
    }

    def __init__(self, data: pd.DataFrame = None, cols: dict = DEFAULT_COLS):
        """

        Args:
            data:
            cols:
        """
        # for c in cols.keys():
        #     if c not in data.columns:
        #         raise KeyError(f"Required column {c} not in data")
        self._data = None
        if data is not None:
            self.append(data, cols)
        self.stats = LabelStats(self)

    def append(self, data: pd.DataFrame, cols: dict = DEFAULT_COLS, drop_labellers=None):
        bool_cols = [
            l for l, t in self.labels.items() if l in data.columns and t == "bool"
        ]
        data[bool_cols] = data[bool_cols].fillna(0)
        data = data.astype(object)
        data = data.astype({
            l: t for l, t in self.labels.items() if l in data.columns
        })
        data = self._generate_extra_labels(data)
        data = data.astype(self.labels)
        data = data.rename(columns=cols)
        if drop_labellers is not None:
            data = data[~data["labeller"].isin(drop_labellers)]
        if self._data is None:
            self._data = data
        elif isinstance(self._data, pd.DataFrame) and isinstance(data, pd.DataFrame):
            self._data = pd.concat([self._data, data])
        else:
            raise Exception("Could not add data, wrong type(s)")

        return self

    @property
    def data(self):
        return self._data

    def data_by_community(self, community_name):
        return self.data[
            self.data['community_name'] == community_name
        ]

    """
    @property
    def _required_cols(self):
        return self._cols.values() + self.labels.keys()
    """

    @property
    def labels(self) -> dict:
        raise NotImplementedError

    @property
    def level(self) -> CommunityDataLevel:
        raise NotImplementedError

    @abstractmethod
    def _generate_extra_labels(self, data):
        pass

    def __str__(self):
        return (
            f"{type(self)}\n"
            f"   Level: {self.level.value}\n"
            f"   Labelled entities: {self.data.shape[0]}\n"
            f"   Labels (cols): {len(self.labels.values())}\n"
            f"   Labellers: {len(self.data['labeller'].unique())}\n"
            f"   Communities: {len(self.data['community_name'].unique())}\n"
        )

    def rating_table(self, label_name, communities=None, custom_filter=None, allow_missing_data=False):
        """
        Get the rating table for one label to be used, e.g., with ``statsmodels.stats.inter_rater``.

        Args:
            communities: List of communities to include in table, if ``None``, include all communities
            label_name: label to be returned in table
            allow_missing_data: whether to drop columns with missing ratings

        Returns:
            rating table: labels as 2-dim table with raters (labellers) in rows and ratings in columns.
        """
        d = self.data
        if communities is not None:
            d = self.data[self.data['community_name'].isin(communities)]
        if custom_filter is not None:
            d = self.data[custom_filter]


class LabelCollection:
    """
    TODO: add documentation
    """

    def __init__(self, labels=[]):
        self._labels = []
        for l in labels:
            self.append(l)

    @property
    def labels(self):
        return self._labels

    def by_level(self, level):
        data = [l.data for l in self.labels if l.level == level]
        if len(data) == 1:
            return data[0]
        elif len(data) > 1:
            return pd.merge(data)
        else:
            return None

    @property
    def all_label_names(self):
        return [k for l in self.labels for k in l.labels.keys()]

    def add(self, labels: Labels):
        ln = set(self.all_label_names)
        new_ln = set(labels.labels.keys())
        duplicates = set.intersection(ln, new_ln)
        if len(duplicates) > 0:
            raise Exception(f"Could not add labels, labels {duplicates} already exist!")
        else:
            self._labels.append(labels)

    def append(self, labels: Labels):
        appended = False
        for l in self._labels:
            if type(labels) is type(l) and labels.level == l.level:
                l.append(labels.data)
                appended = True
        if not appended:
            try:
                self.add(labels)
            except:
                raise Exception("Could not append or add labels.")

        return self.labels

    def __str__(self):
        s = ""
        for l in self.labels:
            s += l.__str__()

        return s



class InnovationLabels(Labels):
    """
    TODO: add documentation
    """

    LIMESURVEY_LABELLER = 'userid'
    LIMESURVEY_COMMUNITY = 'community'
    LIMESURVEY_URL = 'thread{}'

    LIMESURVEY_LABEL_COLS = {
        'labelling[t{}_idea]': 'label_idea',
        'labelling[t{}_eval]': 'label_evaluation',
        'labelling[t{}_impl]': 'label_implementation',
        'labelling[t{}_mod]': 'label_modification',
        'labelling[t{}_impro]': 'label_improvement',
        'labelling[t{}_inno]': 'label_potential'
    }

    LIMESURVEY_NUM_THREADS = 5

    POTENTIAL_DTYPE = CategoricalDtype(
        categories=[0, 1, 2], ordered=True
    )

    labels = {
        'label_idea': 'bool',
        'label_evaluation': 'bool',
        'label_implementation': 'bool',
        'label_modification': 'bool',
        'label_improvement': 'bool',
        'label_potential': POTENTIAL_DTYPE,
    }

    level = CommunityDataLevel.TOPICS

    def _generate_extra_labels(self, data):
        try:
            activities = data[[
                'label_idea', 'label_evaluation', 'label_implementation',
                'label_modification', 'label_improvement'
            ]]
            data["label_any_activity"] = activities.any(axis=1)
            self.labels['label_any_activity'] = 'bool'
        except KeyError:
            pass

        try:
            data["label_has_potential"] = data["label_potential"] > 0
            self.labels["label_has_potential"] = 'bool'
        except KeyError:
            pass

        # TODO: this belongs somewhere else...
        def id_from_url(url:str):
            id = None
            if "openenergymonitor.org" in url:
                id = url.split("/")[-1]
            elif "openstreetmap.org" in url:
                id = url.split("=")[-1]
            elif "davehakkens.nl" in url:
                id = url.split("/")[-1]

            return id

        data["id"] = data["url"].apply(id_from_url)

        return data

    """
    @staticmethod
    def _ls_label_map(thread_number):
        ls_col_map = {}
        for sh, label in InnovationLabels.LIMESURVEY_LABEL_SHORTHANDS.items():
            ls_col = InnovationLabels.LS_LABEL_COL_TEMPLATE.format(thread_number, sh)
            col = InnovationLabels.LABEL_COL_TEMPLATE.format(label)
            ls_col_map[ls_col] = col

        return ls_col_map
    """

    def from_limesurvey(self, limesurvey_results, drop_labellers=None):
        """
        Adds label entries from Limesurvey results format. Limesurvey results can contain multiple
        labelled threads per response. For each thread i and associated url and labels, the data
        must contain one column, e.g.:
        "thread1" (=url), "labelA1", "labelB1", ..., "thread2", "labelA2", "labelB2", ...

        Args:
            limesurvey_results: String (path to file) or Pandas.DataFrame

        Returns:

        """
        df = None
        if isinstance(limesurvey_results, pd.DataFrame):
            df = limesurvey_results
        elif isinstance(limesurvey_results, str):
            filename, ext = os.path.splitext(limesurvey_results)
            if ext == ".csv":
                df = pd.read_csv(filename + ext)
            elif ext == ".xlsx":
                df = pd.read_excel(filename + ext)

        dfs = []
        # split df by thread number, rename cols, then re-concat parts
        for i in range(1, self.LIMESURVEY_NUM_THREADS+1):
            label_cols = {
                k.format(i): v for k, v in self.LIMESURVEY_LABEL_COLS.items()
            }
            id_cols = {
                self.LIMESURVEY_LABELLER: 'labeller',
                self.LIMESURVEY_COMMUNITY: 'community_name',
                self.LIMESURVEY_URL.format(i): 'url'
            }
            df_i = df.rename(columns=label_cols).rename(columns=id_cols)[
                list(label_cols.values()) + list(id_cols.values())
            ]
            dfs.append(df_i)

        data = pd.concat(dfs)

        return self.append(
            data,
            cols={c: c for c in id_cols.values()},
            drop_labellers=drop_labellers
        )





