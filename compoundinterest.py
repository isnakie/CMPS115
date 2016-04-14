import math
import plotly.plotly as py
import plotly.graph_objs as go

principle = int( input("Starting principle: "))
interest = int( input("Your interest rate: "))
month = int( input("How much added per month? "))
number = int( input("Number of compounts per year: "))
years = int( input("How many number of years: "))

percentage = interest/100

a = [];
b = [];

def interestrates(p,i,m,n,t):
	compound = p;
	for x in range(1, t):
		add = pow((1+(i/n)), (n*x) )
		value = compound*add
		compound = p + m;
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

result = interestrates(principle, percentage, month, number, years)
print(result)