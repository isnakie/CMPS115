import math
import matplotlib.pyplot as plt 

principle = int( input("Starting principle: "))
interest = int( input("Your interest rate: "))
month = int( input("How much added per month? "))
number = int( input("Number of compounts per year: "))
years = int( input("How many number of years: "))

percentage = interest/100

a = [];
b = [];
c = [];

def interestrates(p,i,m,n,t):
	compound = p;
	for x in range(1, t):
		add = pow((1+(i/n)), (n*x) )
		value = compound*add
		compound = compound + m;
		c.append(compound);
		a.append(x);
		b.append(value);
	plt.figure()
	lines = plt.plot(a, b)
	plt.setp(lines, color='b', linewidth = 5.0)
	plt.plot(a, c)
	plt.setp(lines, color = 'y', linewidth = 5.0)
	plt.savefig('compound.png')
	plt.show()
	return(value)



result = interestrates(principle, percentage, month, number, years)
print(result)