import networkx as nx
from itertools import product
import copy
import Chapter1_3

def composition(k, text):
    """
    Solve the String Composition Problem.
    Input: An integer k and a string Text.
    Output: Compositionk(Text), where the k-mers 
    are written in lexicographic order.
    """
    kmers = []
    for i in range(len(text) - k + 1):
        kmers.append(text[i:i+k])
    return sorted(kmers)

def debruijn(k, text):
    """
    Construct the de Bruijn graph of a string.
    Input: An integer k and a string Text.
    Output: DeBruijnk(Text).
    """
    # build pattern list of len(text)_k+1 kmers from text
    patterns = composition(k, text)
    #
    return debruijn_from_kmer(patterns)

def debruijn_from_kmer(kmers):
    """
    Construct the de Bruijn graph from a set of k-mers.
    Input: A collection of k-mers Patterns.
    Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
    """
    g = []
    # build a prefixing pattern dict
    dprefix = {}
    for e in kmers:
        prefix = e[:-1]
        dprefix.setdefault(prefix, []).append(e[1:])
    # build lexicographically sorted adjacency list
    for k in sorted(dprefix.keys()):
        g.append( (k,sorted(dprefix[k])) )
    #build graph object
    G=nx.DiGraph()
    for i in g:
        for j in i[1]:
            G.add_edge(i[0],j)
    return G

def overlap(patterns):
    """
    Solve the Overlap Graph Problem (restated below).
    Input: A collection Patterns of k-mers.
    Output: The overlap graph Overlap(Patterns), 
    in the form of an adjacency list.
    """
    # build a prefixing pattern dict
    dprefix = {}
    ladj = []
    for e in patterns:
        prefix = e[:-1]
        dprefix.setdefault(prefix, []).append(e)
    for e in sorted(patterns):
        suffix = e[1:]
        for ee in dprefix.get(suffix, []):
            ladj.append((e,ee))
    #build graph object
    G=nx.DiGraph()
    for i in ladj:
        G.add_edge(i[0],i[1])
    return G