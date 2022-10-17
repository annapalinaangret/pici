"""
Metrics using the posts' text content.

By level of observation:

**posts**

- [number_of_words][pici.metrics.text.number_of_words]
- [posts_word_occurrence][pici.metrics.text.posts_word_occurrence]

"""

from pici.reporting import metric, posts_metric, topics_metric
from pici.datatypes import CommunityDataLevel, MetricReturnType
from pici.helpers import num_words, word_occurrences
import pandas as pd
from bs4 import BeautifulSoup
import nltk
import numpy as np


@posts_metric
def number_of_words(community):
    """
    The number of words in a post (removing html).

    Args:
        community (pici.Community):

    Returns:
        results (dict of str:int):
            - ``number of words``
    """

    return {
        'number of words': community.posts[community.text_column].apply(
            num_words
        )
    }


@posts_metric
def posts_word_occurrence(community, words, normalize=True):
    """
    Counts the occurrence of a set of words in each post.

    Args:
        community (pici.Community):
        words (list of str): List of words to count in post texts.
        normalize (bool): Normalize occurrence count by text length.

    Returns:
        results (dict of str:int):
            - ``occurrence of <word>`` for each provided ``word``
    """

    def countw(t):
        if normalize:
            nw = num_words(t)
            return {
                k: v / nw if nw > 0 else 0
                for k, v in word_occurrences(t, words).items()
            }
        else:
            return word_occurrences(t, words)

    results = community.posts[
        community.text_column].apply(countw).apply(pd.Series)

    return {'occurrence of {c}': results[c] for c in results.columns}


@topics_metric
def number_of_words_per_post(community):
    words = community.posts.groupby(
        by=community.topic_column)
    first_words = words.first()['number_of_words']
    words = words['number_of_words']

    return {
        'elaboration - number of words (first)': first_words,
        'elaboration - number of words (total)': words.apply(np.sum),
        'elaboration - number of words (mean)': words.apply(np.mean),
        'elaboration - number of words (min)': words.apply(np.min),
        'elaboration - number of words (max)': words.apply(np.max),
        'elaboration - number of words (sd)': words.apply(np.std),
    }