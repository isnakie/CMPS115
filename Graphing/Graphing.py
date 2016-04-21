import time
import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick
matplotlib.rcParams.update({'font.size': 10 })

eachStock = 'AAPL', 'TSLA'

def movingaverage(values,window):
    weights = np.repeat(1.0, window)/window
    # Simple moving average, smas
    smas = np.convolve(values,weights, 'valid')
    return smas

def graphData(stock, MA1, MA2):
    try:
        # variable for txt file, read in next part
        stockFile = stock+'.txt'
        
        # multiple variables: Date,close, high, low, open, volume
        # for the first element[0], date, read it as YearMonthDay
        date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',', unpack=True,
                                                            converters={0:mdates.strpdate2num('%Y%m%d')})
    
# Version 1.2: CandleStick        
# -------------------------------------------------------------------------------------------        
        # Using the data read in to put into candlestick array
        x = 0 
        y = len(date)
        candleAr = []
        while x<y:
            appendLine = date[x],openp[x],closep[x],highp[x],lowp[x],volume[x]
            candleAr.append(appendLine)
            x+=1
# -------------------------------------------------------------------------------------------        
    
# Version 1.3: Moving Averages    
# -------------------------------------------------------------------------------------------        
        # using close data with either moving average
        Av1 = movingaverage(closep, MA1)
        Av2 = movingaverage(closep, MA2)
        # Starting point of data since we need at least 12 or 26 data points to get an SMAS
        SP = len(date[MA2-1:])
# -------------------------------------------------------------------------------------------        
        
        
        fig = plt.figure(facecolor = '#07000d')
        # Version 1.0
        # How many graphs appear on png, in this case, it has place for 2 and we are choosing slot 1
        # ax1 = plt.subplot(2,1,1)
        
# Version 1.1
# -------------------------------------------------------------------------------------------        
        # Making the graph format more detailed
        ax1 = plt.subplot2grid((5,4), (0,0), rowspan=4, colspan=4, axisbg='#30414D') 
        #Black = #07000d
# -------------------------------------------------------------------------------------------        
        # Version 1.0
        # Plotting the different information taken
        #ax1.plot(date, openp)
        #ax1.plot(date, highp)
        #ax1.plot(date, lowp)
        #ax1.plot(date, closep)
        
# Version 1.2: CandleStick
# -------------------------------------------------------------------------------------------        
        # Calling the Candlestick function made from the previous while loop
        candlestick(ax1, candleAr, width=0.7, colorup='#9eff15', colordown='#ff1717') 
# -------------------------------------------------------------------------------------------        
        
# Version 1.3: Moving Averages    
# -------------------------------------------------------------------------------------------        
        # Graphing
        ax1.plot(date[-SP:],Av1[-SP:])
        ax1.plot(date[-SP:],Av2[-SP:])

# -------------------------------------------------------------------------------------------        
        
        #Version 1.0
        #ax1.grid(True)
        # Changes color to white
        ax1.grid(True, color='w')
        # Shows a max of 10 dates on x-axis, formats it it Year-Month-Day
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        
# Version 1.2: CandleStick
# -------------------------------------------------------------------------------------------         
        # Changes to lighter color
        ax1.yaxis.label.set_color("w")
        ax1.spines['bottom'].set_color("#5998ff")
        ax1.spines['top'].set_color("#5998ff")
        ax1.spines['left'].set_color("#5998ff")
        ax1.spines['right'].set_color("#5998ff")
        ax1.tick_params(axis='y', colors = 'w')
        plt.ylabel('Stock price')
        # Later, used to tell filler the minimum to fill to.
        volumeMin = volume.min()
# -------------------------------------------------------------------------------------------         
        
        # Version 1.0
        # This time we are choosing slot 2 for location of graphs
        # ax2 = plt.subplot(2,1,2, sharex=ax1)
        
# Version 1.2: CandleStick
# -------------------------------------------------------------------------------------------        
        # Making the graph format more detailed, also make it black
        ax2 = plt.subplot2grid((5,4), (4,0), sharex=ax1, rowspan=4, colspan=4, axisbg='#30414D') 
        #Black = #07000d
# -------------------------------------------------------------------------------------------        
        
        # Version 1.1
        #ax2.bar(date, volume)
        
#Version 1.2: CandleStick
# -------------------------------------------------------------------------------------------        
        # Changes the bars into teal colored, and facecolored with some fill
        ax2.plot(date,volume, '#00ffe8', linewidth = .8)
        # Using the volumeMin to start as bottom, for stylistic purpose
        ax2.fill_between(date, volumeMin, volume, facecolor='#00ffe8', alpha=0.5)
# -------------------------------------------------------------------------------------------        

        ax2.axes.yaxis.set_ticklabels([])
        ax2.grid(True)
        
# Version 1.2: CandleStick
# -------------------------------------------------------------------------------------------         
        ax2.spines['bottom'].set_color("#5998ff")
        ax2.spines['top'].set_color("#5998ff")
        ax2.spines['left'].set_color("#5998ff")
        ax2.spines['right'].set_color("#5998ff")
        ax2.tick_params(axis='x', colors = 'w')
        ax2.tick_params(axis='y', colors = 'w')

# -------------------------------------------------------------------------------------------         

        # rotate the date on x-axis for visual appeasement 
        # This is redundant, as we don't need this, it is remained blacked out
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(90)
# Version 1.2: CandleStick
# -------------------------------------------------------------------------------------------         
        # Changed the Volume label to white form Version 1.0, and shifted left
        plt.ylabel('Volume', color='w', labelpad=20)
# -------------------------------------------------------------------------------------------         
        
        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)
        
        # all adjustments on format of graph png
        plt.subplots_adjust(left=.10, bottom=.14, right=.93, top=.95, wspace=.20, hspace=0)
        plt.xlabel('Date')
        #Version 1.0, adjusted above to match the new scheme of png.
        #plt.ylabel('Volume')
        plt.suptitle(stock+' Stock Price',color='w')
        plt.setp(ax1.get_xticklabels(), visible=False)
                
        plt.show() # show the plot
        fig.savefig('example.png', facecolor=fig.get_facecolor())
        
    except Exception, e:
        print 'failed main loop',str(e)
        
       
for stock in eachStock: 
    # Default values are the open days in 2 weeks and month, generally normal moving average
    graphData(stock, 12, 26)
    time.sleep(555)
    
    
    
    
    