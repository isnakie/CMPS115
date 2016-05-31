import math
import numpy as np

def index():
    if request.vars.sym:
        session.sym = request.vars.sym
        redirect(URL('index'))
    graphURL = "https://blash.pythonanywhere.com/blash/static/prices/"+str(session.sym)+".html"
    TitleString = str(session.sym)
    if session.sym is None:
        TitleString = "AAPL"

    WatchForm = SQLFORM(db.StockList).process()
    WatchListRows = db(db.StockList).select()
    for row in WatchListRows:
        row.update(Current_Price=getPrice(row.Symbol))
        
    rowNumber = 0
    return locals()


def getPrice(stock):
    stockFile = '/home/blash/web2py/applications/blash/static/prices/'+str(stock)+'.txt'
    date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',', unpack=True)
    #Perhaps we can get this information from the Graphing.py instead of reading the file over again.
    return closep[-1]

def show():
    company = db.StockList(request.args(0))
    session.sym = company.Symbol
    redirect("http://blash.pythonanywhere.com/stocks")
    return locals()
