"""
Created on April 13, 2016
Reads a csv file containing stock market data and
shows and saves a plot of the trend line,
given optinal starting and ending date information.
Call makeChart() with return value of readFile()
and a list of prices, e.g., ['Open','Close'].
@author: Johnnie
"""

import argparse
import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
import time
from datetime import datetime

shortMonths = [4, 6, 9, 11]

def readFile(file, startY=None, startM=None, startD=None, endY=None, endM=None, endD=None):
  """
  Read the input csv file and return a pandas.DataFrame containing the data.
  :param file: The file name of the csv containing the market data.
  :param startY, startM, startD, endY, endM, endD:
      Optional parameters specifying the timeframe; defaults to the begining and end
      of the current year.
  :type startY, startM, startD, endY, endM, endD: int
  """

  # Read in the file and parse the date strings.
  market = pd.read_csv(file, header = 0)
  parsedDates = []
  format = '%m/%d/%y' # Yahoo Finance data date format
  for d in market['Date']:
    parsedDates.append(datetime.strptime(d, format))
  market['parsed'] = parsedDates

  earliestDate = market['parsed'][0]
  latestDate = market['parsed'][len(market['parsed'])-1]

  # Start date defaults to the beginning of the current year.
  startDate = datetime(2016, 1, 1)
  if startY:
    startDate = datetime(startY, startDate.month, startDate.day)
  if startM:
    startDate = datetime(startDate.year, startM, startDate.day)
  if startD:
    startDate = datetime(startDate.year, startDate.month, startD)
  
  # End date defaults to the end of the current year.
  endDate = datetime(2016, 12, 31)
  if endY:
    endDate = datetime(endY, endDate.month, endDate.day)
  if endM:
    y,m,d = endDate.year, endM, endDate.day
    # Last day of Feb and other shorter months is not 31st.
    if endM == 2:
      d = 28
    elif endM in shortMonths:
      d = 30
    endDate = datetime(y, m, d)
  if endD:
    endDate = datetime(endDate.year, endDate.month, endD)

  # @TODO Should this be handled in an interface file?
  # Start date should not be later than end date
  if startDate > endDate:
    print("Weird input: starting date later than ending date")
    return None

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
  :param prices: list of strings specifying the prices to be in the plot
  """

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

