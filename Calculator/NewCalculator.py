import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def interestrates(p,i, n,t, added_per_year):
    Total_Amount = 0
    scalar = p
    x_axis = [0]
    y_axis = [0]
    scalar_line = [0]
    
    
    for year in range(0,t): # For each year starting from year 0 to final year
        Total_Amount  = p*pow( (1+(i/n)), (n*year) ) + added_per_year# The total amount after some amount of years
        print Total_Amount
        #Total_Amount = added_per_year # The amount added per year (like each month)
        x_axis.append(year)
        y_axis.append(Total_Amount)
        scalar += added_per_year 
        # This is just scalar portion, only using principal and amount added
        scalar_line.append(scalar)
    
    plt.figure()
    exp_line = plt.bar(x_axis, y_axis, label = 'exp', color = 'g')

    scalar_line = plt.bar(x_axis, scalar_line, label = 'scalar', color = 'b')
    
    #lines = plt.plot(a, b)
    plt.title('Compount Interest')
    plt.legend(loc = 'upper center')
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.show()
    return Total_Amount
    

principal = 100000
interest = .10
times_per_year = 1 # Times the interest is compounded
time_in_years = 20 # Time in years
amount_added_year = 12000 # amount added per year

interestrates(principal, interest, times_per_year, time_in_years, amount_added_year)
