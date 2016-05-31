# -*- coding: utf-8 -*-
# try something like
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def index():
    if request.vars.p and request.vars.i and request.vars.m and request.vars.n and request.vars.t:
        session.p = int (request.vars.p)
        session.i = float (request.vars.i)
        session.m = int (request.vars.m)
        session.n = int (request.vars.n)
        session.t = int (request.vars.t)
        session.interest = interestrates(session.p, session.i, session.m, session.n, session.t)
        redirect(URL('index'))
    return dict()

def thousands(x, pos):
    return '$%1.1f k' % (x*1e-3)

def interestrates(p,i, added_per_year, n,t):
    Total_Amount = p
    scalar = p # $100,000
    x_axis = [0]
    y_axis = [0]
    scalar_line = [0]

    for year in range(0,t): # For each year starting from year 0 to final year
        Total_Amount  = Total_Amount*pow( (1+(i/n)), (n*1) ) + added_per_year# The total amount after some amount of years
        print Total_Amount
        #Total_Amount = added_per_year # The amount added per year (like each month)
        x_axis.append(year)
        y_axis.append(Total_Amount)
        scalar += added_per_year 
        # This is just scalar portion, only using principal and amount added
        scalar_line.append(scalar)

    formatter = FuncFormatter(thousands)
    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)
    #plt.figure()
    exp_line = plt.bar(x_axis, y_axis, label = 'Compound', color = 'g')
    scalar_line = plt.bar(x_axis, scalar_line, label = 'Scalar', color = 'b')

    plt.title('Compount Interest')
    plt.legend(loc = 'best')
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.savefig('applications/blash/static/compound.png')
    return Total_Amount
