"""
The "STS for Keras" toolkit.  Contains various Keras blocks that make
putting together and comfortably running neural STS models a breeze.
"""

import numpy as np


def graph_input_anssel(si0, si1, y, f0=None, f1=None, s0=None, s1=None, kw=None, akw=None):
    """ Produce Keras task specification from vocab-vectorized sentences. """
    gr = {'si0': si0, 'si1': si1, 'score': y}
    if f0 is not None:
        gr['f0'] = f0
        gr['f1'] = f1
    if s0 is not None:
        # This is useful for non-neural baselines
        gr['s0'] = s0
        gr['s1'] = s1
    if kw is not None:
        # yodaqa-specific keyword weight counters
        gr['kw'] = kw
        gr['akw'] = akw
    return gr


def graph_nparray_anssel(gr):
    """ Make sure that what should be nparray is nparray. """
    for k in ['si0', 'si1', 'f0', 'f1', 'score', 'kw', 'akw', 'bm25']:
        if k in gr:
            gr[k] = np.array(gr[k])
    return gr


def graph_input_sts(si0, si1, y, f0=None, f1=None, s0=None, s1=None):
    """ Produce Keras task specification from vocab-vectorized sentences. """
    import pysts.loader as loader
    gr = {'si0': si0, 'si1': si1, 'classes': loader.sts_labels2categorical(y)}
    if f0 is not None:
        gr['f0'] = f0
        gr['f1'] = f1
    if s0 is not None:
        # This is useful for non-neural baselines
        gr['s0'] = s0
        gr['s1'] = s1
    return gr


def graph_input_slice(gr, sl):
    """ Produce a slice of the original graph dataset.

    Example: grs = graph_input_slice(gr, slice(500, 1000)) """
    grs = dict()
    for k, v in gr.items():
        grs[k] = v[sl]
    return grs
