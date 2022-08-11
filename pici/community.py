import glob
from abc import ABC, abstractmethod
import logging
from collections import Counter
import datetime

import pandas as pd

from pici.registries import MetricRegistry


LOGGER = logging.getLogger(__name__)


class Community(ABC):
    """
    Abstract community class.

    """

    _co_contributor_graph = None
    _commenter_graph = None
    _posts = None
    _metrics = None
    _data = None

    def __init__(self, name, data, start=None, end=None, attr=None):
        if name is not None:
            self.name = name
        if attr is None:
            self._attr = self.DEFAULT_ATTRIBUTES
        else:
            self._attr = attr
        self._set_data(data, start, end)

    def date_range(self, start=None, end=None):
        return type(self).__name__(self._data, start, end)

    def timeslice(self, posts, col, start, end):
        if start is None and end is None:
            return posts
        elif start is not None and end is not None:
            return posts[(posts[col] >= start) & (posts[col] < end)]
        elif start is None and end is not None:
            return posts[posts[col] < end]
        else:
            return posts[posts[col] >= start]

    @property
    @abstractmethod
    def DEFAULT_ATTRIBUTES(self):
        raise NotImplementedError("Property not set")

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError("Property not set")

    @property
    @abstractmethod
    def date_column(self):
        raise NotImplementedError("Property not set")

    @property
    @abstractmethod
    def contributor_column(self):
        raise NotImplementedError("Property not set")

    @property
    @abstractmethod
    def topic_column(self):
        raise NotImplementedError("Property not set")

    @property
    def contributors(self):
        return self._contributors

    @property
    def posts(self):
        return self._posts

    @property
    def topics(self):
        return self._topics

    @property
    def metrics(self):
        if self._metrics is None:
            self._metrics = MetricRegistry(self)

        return self._metrics

    def contributor_by_id(self, c_id):
        return self.contributors.loc[c_id]

    def contributor_by_post_id(self, p_id):
        return self.contributors.loc[self.posts.loc[p_id].contributor_id]

    def contributors_by_topic_id(self, t_id):
        return self.topics.loc[t_id].c

    @property
    def co_contributor_graph(self):
        if self._co_contributor_graph is None:
            self._co_contributor_graph = self._generate_co_contributor_graph()

        return self._co_contributor_graph

    @property
    def commenter_graph(self):
        if self._commenter_graph is None:
            self._commenter_graph = self._generate_commenter_graph()

        return self._commenter_graph

    @abstractmethod
    def _generate_co_contributor_graph(self):
        pass

    @abstractmethod
    def _generate_commenter_graph(self):
        pass

    @abstractmethod
    def _set_data(self, data, start=None, end=None):
        pass


class CommunityFactory(ABC):

    cache_date_format = '%Y-%m-%d-%H-%M-%S'

    def __init__(self, cache_dir='.', cache_nrows=None):
        self.cache_dir = cache_dir
        self.cache_nrows = cache_nrows
        self._data = None

    def _cache_exists(self):

        files = [f'{self.cache_dir}/{self.name}_{d}_*.csv'
                 for d in self.cache_data]

        found = all([
            any(glob.iglob(f'{self.cache_dir}/{self.name}_{d}_*.csv'))
            for d in self.cache_data
        ])

        if not found:
            LOGGER.warning("Cache does not exist."
                           "Did not find some files when looking for "
                           + ", ".join(files))

        return found

    def load_cache(self):
        cache = {
            k: glob.glob(f'{self.cache_dir}/{self.name}_{k}_*.csv')
            for k in self.cache_data
        }

        # get most recent date for which every cached file exists
        all_dates = [
            fn.split("_")[-1].split(".")[0]
            for k in cache.keys()
            for fn in cache[k]
        ]
        d_counts = Counter(all_dates)
        valid_dates = [
            d for d in d_counts if d_counts[d] == len(self.cache_data)
        ]

        most_recent_date = sorted(
            valid_dates,
            key=lambda x: datetime.datetime.strptime(
                x, self.cache_date_format),
            reverse=True
        )[0]

        self._data = {
            k: pd.read_csv(
                f'{self.cache_dir}/{self.name}_{k}_{most_recent_date}.csv',
                nrows=self.cache_nrows
            )
            for k in self.cache_data
        }

    def add_data_to_cache(self, data):
        date_now = datetime.date.today().strftime(self.cache_date_format)
        for k, d in data.items():
            d.to_csv(f'{self.cache_dir}/{self.name}_{k}_{date_now}.csv')

    def create_community(self, name=None, use_cache=True,
                         start=None, end=None):
        if use_cache and self._cache_exists():
            LOGGER.info("Loading community from cache...")
            self.load_cache()
        else:
            LOGGER.warning("No data in cache. Scraping community data...")
            self.scrape_data()

        return self._create_community(name, start, end)

    def load_labels(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def cache_data(self):
        pass

    @abstractmethod
    def scrape_data(self):
        pass