import math

def interestrates(p,i,n,t):
	add = pow((1+(i/n)), (n*t) )
	value = p*add
	return(value)

principle = int( input("Starting principle: "))
interest = int( input("Your interest rate: "))
number = int(input("Number of compounts per year: "))
years = int(input("How many number of years: "))

percentage = interest/100

result = interestrates(principle, percentage, number, years)
print(result)