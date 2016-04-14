import math

principle = int( input("Starting principle: "))
interest = int( input("Your interest rate: "))
number = int( input("Number of compounts per year: "))
years = int( input("How many number of years: "))

percentage = interest/100

a = [];
b = [];

def interestrates(p,i,n,t):
	for x in range(1, t):
		add = pow((1+(i/n)), (n*x) )
		value = p*add
		a.append(x);
		b.append(value);
	return(value)

trace0 = go.Scatter(
	x = a,
	y = b,
	name = 'Years',
	line = dict(
		color = ('rgb(205, 12, 24)'),
		width = 4
		)
	)

data = [trace0]

layout = dict(	title = 'Compound interest',
				xaxis = dict( title = 'Number of years'),
				yaxis = dict( title = 'Money'),
	)

fig = dict( data=data, layout=layout )
py.iplot( fig, filename='styled-line' )

result = interestrates(principle, percentage, number, years)
print(result)