# -*- coding: utf-8 -*-
# try something like
import matplotlib.pyplot as plt, mpld3

def index():
    session.graph1 = graph1()
    session.graph2 = graph2()
    return dict()

def graph1():
    fig = plt.figure()
    plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
    return mpld3.fig_to_html(fig);

def graph2():
    fig = plt.figure()
    plt.plot([1,5,9,2,6], 'ks-', mec='w', mew=5, ms=20)
    return mpld3.fig_to_html(fig);
