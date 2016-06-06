# CMPS 115 Spring 2016, UCSC, Prof Richard Juillig

LINK: http://blash.pythonanywhere.com/

For Stock Market Analysis

Team Members: Sean Sjahrial, Johnnie Chang, Kenny Wong and Derrick Do.

Blash ("Buy Low and Sell High") is a web app that aims to:

* provide data visualization of the market, especially the S&P500
* Start new investors by familiarizing basic indexes on the stock with easy to access graphs of each stock
* inform stock investing decisions
* predict the performance of a given stock service primarily beginner investors


Presentation of initial release plan on Google Docs:
https://docs.google.com/presentation/d/1gQyPqirFqX-o5z9DUBfU0sNMPeKLkrqgLCxlR3oECEg/edit

Word Doc of initial release plan on Google Docs:
https://docs.google.com/document/d/1rVmr_9q1shaeTMGO8x8knxlVR_NAsB9we5suiWivGqI/edit


Prediction models: <br />
Linear regression -> Weighted average (Recent is higher weighted) -> GARCH

Reason we are not planning to use SQL: <br />
SQL, in my experience (Sean), is really useful when dealing with different types of datatypes other than integers. So if we decide to pull more information like (the day's highs, lows, dividend yields, ask price, etc...) then we would use SQL. The user would be able to customize their viewing options. 
As of right now, we are starting small and only working with simple data.


Tutorial for Stock Market: (An introduction into stock market) <br />
A stock is a portion of the companies assests, and people are able to buy stocks for the purpose of making a profit. This can happen when a person buys a stock, that stock value increases and they sell it (known as captial gain), or when a company gives you money just for owning their stock (known as a dividend).  <br />
Another way to make money is to buy bonds, which are more secure than stocks but less profitable. <br/>
Finally, "shorts" are a way to go "against" a company. If you believe that a company will do poorly, you can sell shorts, then when they do poorly, their stocks will be cheaper, and you buy back the shorts, thus making a profit from their loss.


The market does not have a set pattern, but follows general trends such as:
* In short term trading, a company doing well will continue to do well, generally about 3 months 
* In long term trading, a company doing well, will reverse its profits, generally the cycle is about 3~5 years



