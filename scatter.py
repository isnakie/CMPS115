"""
Created on April 13, 2016
Reads a csv file containing stock market data and
shows and saves a plot of the trend line,
given optional starting and ending date information.
Call makeChart() with return value of readFile()
and a list of prices, e.g., ['Open','Close'].
@author: Johnnie Chang
"""

import argparse
import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
import time
from datetime import datetime

# Months with 30 days.
shortMonths = [4, 6, 9, 11]

def readFile(inFile=None, startY=None, startM=None, startD=None,\
             endY=None, endM=None, endD=None, dateFormat=None):
  """
  Read the input csv file and return a pandas.DataFrame containing the data.
  :param file: The file name of the csv containing the market data.
  :param startY, startM, startD, endY, endM, endD:
      Optional parameters specifying the timeframe; defaults to the begining and end
      of the current year.
  :type startY, startM, startD, endY, endM, endD: int
  """

  # Default to reading "StockDataFixed.csv" as input file.
  file = "StockDataFixed.csv"
  if inFile:
    file = inFile

  # Read in the file and parse the date strings.
  try:
    market = pd.read_csv(file, header = 0)
  except OSError as ose:
    print("Please reconsider your input file:", ose)
    return
  parsedDates = []
  # Yahoo Finance data date format: mm/dd/yy.
  format = '%m/%d/%y'
  # Use user format if given.
  if dateFormat:
    format = dateFormat

  # Parse date information into a new column.
  try:
    for d in market['Date']:
      parsedDates.append(datetime.strptime(d, format))
  except ValueError as ve:
    print("Please reconsider your date format:",ve)
    print()
    return
  market['parsed'] = parsedDates

  #
  latestDate = market['parsed'][0]
  earliestDate = market['parsed'][len(market['parsed'])-1]
  thisY = datetime.today().year
  defaultStartDate = datetime(thisY, 1, 1)
  #defaultEndDate = datetime(thisY, 12, 31)
  defaultEndDate = latestDate
  print('The data used starts on', earliestDate.strftime("%B %d, %Y"),\
        'and ends on', latestDate.strftime("%B %d, %Y."))
  print()

  # Start date defaults to the beginning of the current year.
  startDate = defaultStartDate
  if startY:
    try:
      startDate = datetime(startY, startDate.month, startDate.day)
    except ValueError as ve:
      print("Please reconsider your starting year.")
      print()
  if startM:
    try:
      startDate = datetime(startDate.year, startM, startDate.day)
    except ValueError as ve:
      print("Please reconsider your starting month.")
      print()
  if startD:
    try:
      startDate = datetime(startDate.year, startDate.month, startD)
    except ValueError as ve:
      print("Please reconsider your starting day.")
      print()

  # Start date should not be earlier than the earliest date in the data.
  if startDate < earliestDate:
    print("Your starting date is earlier than the earliest date in the data.")
    print("Adjusting starting date to earliest date.")
    print()
    startDate = earliestDate

  # End date defaults to the end of the current year.
  endDate = defaultEndDate
  #endDate = latestDate
  if endY:
    try:
      endDate = datetime(endY, endDate.month, endDate.day)
    except ValueError as ve:
      print("Please reconsider your ending year.")
      print()
  if endM:
    y,m,d = endDate.year, endM, endDate.day
    # Last day of Feb and other shorter months is not 31st.
    if endM == 2:
      d = 28
    elif endM in shortMonths:
      d = 30
    try:
      endDate = datetime(y, m, d)
    except ValueError as ve:
      print("Please reconsider your ending month.")
      print()
  if endD:
    try:
      endDate = datetime(endDate.year, endDate.month, endD)
    except ValueError as ve:
      print("Please reconsider your ending year.")
      print()

  # End date should not be later than the latest date.
  if endDate > latestDate:
    print("Your ending date is later than the latest date in the data.")
    print("Adjusting ending date to latest date.")
    print()
    endDate = latestDate

  # Start date should not be later than end date.
  if startDate > endDate:
    print("The ending date is earlier than the starting date.")
    print("Adjusting ending date to the latest date.")
    endDate = latestDate

  #print('start:',startDate, 'end:',endDate)

  # if startDate < earliestDate:
  #   print("Weird input:")
  # if endDate > latestDate:  
  #   print("Weird input:")

  # Update the contents: only keep data after start date and before end date.
  market = market[market.parsed > startDate]
  market = market[market.parsed < endDate]

  return market

def makeChart(market, prices):
  """
  Generates connected scatter plot, shows and saves to png.
  :param market:
  :param prices: list of strings specifying the prices to be in the plot.
  """

  # The readFile() call was not done successfully.
  # TODO other data types given?
  #print(type(market))
  if market == None:
    print("Please fix errors in input first.")
    print()
    return

  # Empty list of prices to plot.
  if len(prices) == 0:
    print("Please input the prices to plot.")
    print()
    return

  plt.figure()
  colors = ['b','g','r','c','m','y','k']
  plt.xticks(rotation=30)
  for i in range(len(prices)):
    price = prices[i]
    color = colors[i]
    plt.plot(market['parsed'], market[price], c=color, label=price)

  plt.xlabel('Date')
  plt.ylabel('USD')
  plt.title(' '.join(prices) + ' Price Trend')
  plt.legend(loc="best")
  plt.savefig('day_'+'_'.join(prices)+'.png')
  plt.show()

