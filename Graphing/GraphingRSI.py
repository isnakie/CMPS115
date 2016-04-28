import time
import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt, mpld3
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick
import pylab
matplotlib.rcParams.update({'font.size': 10 })

eachStock = 'AAPL', 'TSLA'

def movingaverage(values,window):
    weights = np.repeat(1.0, window)/window
    # Simple moving average, smas
    smas = np.convolve(values,weights, 'valid')
    return smas

def rsiFunc(prices,n=14):
    # relative strength index, its a momentum graph. It will give information about overbought
    # or oversold. If its over 70, then its overbought and users may want to sell soon
    # if its under 30, then its oversold and user may want to buy some.
    # 14 is default days to take up's and down's closing
    deltas = np.diff(prices) # difference of prices
    seed = deltas[:n+1] # 
    up = seed[seed>0].sum()/n # average of days closing up: take the index if that index is positive
    down = -seed[seed<0].sum()/n # average of days closing down: take the index if that index is negative
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)
    for i in range(n, len(prices)):
        delta = deltas[i-1]
        if delta > 0:
            upval = delta
            downval = 0.   
        else: 
            upval = 0.
            downval= -delta
            
        up = (up*(n-1)+upval)/n
        down = (down* (n-1)+downval)/n
        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)  
    return rsi

def convertUnixTime(UnixTime):
    for time in UnixTime:
        print time
        #ConvertedDate = datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d')
        print ConvertedDate
    return ConvertedDate
    
def convertPythonDateTime(DateTime):
    # Since it looks like matplotlib.dates.formatter does not work on work in mpld3...
    # I have to manually make a function    
    print DateTime
    delta = datetime.timedelta(days=1)
    startDate = datetime.date(2015,5,5)#mdates.num2epoch(0)
    endDate = datetime.date(2016,3,5)#mdates.num2epoch(DateTime[-1])
    print delta
    print startDate
    print endDate
    newDate = mdates.drange(startDate, endDate, delta)
    print 'test'

    return newDate 
    
def constantFunc(value,rangeFunc):
    count = len(rangeFunc)
    ConstantList = np.zeros(count)
    for i in range(0,count):
        ConstantList[i] = value
    return ConstantList
    
def graphDataRSI(stock, MA1, MA2):
    try:
        stockFile = stock+'.txt'
        date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',', unpack=True, converters={0:mdates.strpdate2num('%Y%m%d')})
        
        x = 0 
        y = len(date)
        candleAr = []
        while x<y:
            appendLine = date[x],openp[x],closep[x],highp[x],lowp[x],volume[x]
            candleAr.append(appendLine)
            x+=1
        
        # using close data with either 12 or 26 day moving average
        Av1 = movingaverage(closep, MA1)
        Av2 = movingaverage(closep, MA2)
        # Starting point of data since we need at least 12 or 26 data points to get an SMAS
        SP = len(date[MA2-1:])
        
        label1=str(MA1)+' SMA'
        label2=str(MA2)+' SMA'
        
        fig = plt.figure(facecolor = 'gray') # blue = '30414D'
        
        ax0 = plt.subplot2grid((5,4), (0,0), rowspan=1, colspan=4, axisbg='#30414D')
        
        rsi = rsiFunc(closep)
        rsiBottomColor = 'green'
        rsiTopColor = 'red'
        
        ax0.plot(date,rsi, 'w', linewidth=1.5)
        #ax0.axhline(70, color = rsiTopColor)
        #ax0.axhline(70, color = rsiTopColor) # These did not work in mpld3
        ax0.plot(date, constantFunc(70,date), 'red')
        ax0.plot(date, constantFunc(30,date), color = rsiBottomColor)
        ax0.spines['bottom'].set_color("#5998ff")
        ax0.spines['top'].set_color("#5998ff")
        ax0.spines['left'].set_color("#5998ff")
        ax0.spines['right'].set_color("#5998ff")
        ax0.tick_params(axis='x', colors = 'black')
        ax0.tick_params(axis='y', colors = 'black')
        ax0.set_yticks([30,70])
        ax0.yaxis.label.set_color('black')
        #plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='both'))
        plt.ylabel('RSI')
        
        # How many graphs appear on png, in this case, it has place for 2 and we are choosing slot 1
        # ax1 = plt.subplot(2,1,1)
        ax1 = plt.subplot2grid((5,4), (1,0), rowspan=4, colspan=4, axisbg='#30414D') 
        #Black = #07000d Blue = #30414D
        # Calling the Candlestick function made from the previous while loop
        candlestick(ax1, candleAr, width=0.7, colorup='#9eff15', colordown='#ff1717') 
        # Graphing the date vs moving average starting from SP to current
        ax1.plot(date[-SP:],Av1[-SP:],'#5998ff', label = label1, linewidth=1.5)
        ax1.plot(date[-SP:],Av2[-SP:],'#e1edf9', label = label2, linewidth=1.5)
        # Shows a max of 10 dates on x-axis, formats it it Year-Month-Day
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        
        ax1.yaxis.label.set_color("black")
        ax1.spines['bottom'].set_color("#5998ff")
        ax1.spines['top'].set_color("#5998ff")
        ax1.spines['left'].set_color("#5998ff")
        ax1.spines['right'].set_color("#5998ff")
        ax1.tick_params(axis='y', colors = 'black')
        ax1.tick_params(axis='x', colors = 'black')
        plt.ylabel('Stock price')
        
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
        
        volumeMin = 0 #volume.min()


        maLeg = plt.legend(loc=9, ncol=2, prop={'size':10}, fancybox=True)
        maLeg.get_frame().set_alpha(0.4)
        textEd = pylab.gca().get_legend().get_texts()
        pylab.setp(textEd[0:5], color = 'w')
        
# Version 1.4: Volume Overlay
# -------------------------------------------------------------------------------------------         
        # Overlay, but it doesn't work in mpld3
        ''' 
        ax1v = ax1.twinx()
        # Using the volumeMin to start as bottom, for stylistic purpose
        ax1v.fill_between(date, volumeMin, volume, facecolor='#00ffe8', alpha=0.5)
        ax1v.axes.yaxis.set_ticklabels([])
        ax1v.grid(False)
        ax1v.spines['bottom'].set_color("#5998ff")
        ax1v.spines['top'].set_color("#5998ff")
        ax1v.spines['left'].set_color("#5998ff")
        ax1v.spines['right'].set_color("#5998ff")
        ax1v.set_ylim(0,5*volume.max())
        ax1v.tick_params(axis='x', colors = 'black')
        ax1v.tick_params(axis='y', colors = 'black')
        '''
        
        # all adjustments on format of graph png
        plt.subplots_adjust(left=.10, bottom=.15, right=.93, top=.95, wspace=.20, hspace=0)
        plt.xlabel('Date')
        plt.suptitle(stock+' Stock Price',color='black')
        plt.setp(ax0.get_xticklabels(), visible=False)
        #plt.show() # show the plot
        mpld3.show()
        fig.savefig('example.png', facecolor=fig.get_facecolor())
        
    except Exception, e:
        print 'failed main loop',str(e)
        
       
for stock in eachStock: 
    # Default values are the open days in 2 weeks and month, generally normal moving average
    graphDataRSI(stock, 12, 26)
    time.sleep(555)
    
    
    
    
    
