# CMPS 115 Spring 2016, UCSC, Prof Richard Juillig

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
