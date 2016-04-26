import urllib2
import time
import datetime
import sys, getopt

stocksToPull = "AAPL",'GOOGL','MSFT','AMZN','EBAY','TSLA'

def pullData(stock, timeRange = '1y'):

    try:
        print 'Currently pulling', stock
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range='+timeRange+'/csv'
        saveFileLine = stock+'.txt' # File containing stock info
        
        # Determine if there is a file named stock.txt to get lastUnix time
        try:
            readExistingData = open(saveFileLine,'r').read() # open up the stock.txt
            splitExisting = readExistingData.split('\n') # break each row
            mostRecentLine = splitExisting[-2] # second last line, since last line is blank
            lastUnix = mostRecentLine.split(',')[0] #Get the unix date  
        except Exception, e:
            print str(e)
            time.sleep(1)
            lastUnix = 0
    
        # Open the stock.txt code
        saveFile = open(saveFileLine,'a') # with intention to append
        sourceCode = urllib2.urlopen(urlToVisit).read() #open the source code to read
        splitSource = sourceCode.split('\n') # split each line by line
    
        # if time stamp is greater than time stamp there, just update those.
        for eachLine in splitSource:
            if 'values' not in eachLine:
                splitLine = eachLine.split(',')
                if len(splitLine) == 6:
                    if int(splitLine[0]) > int(lastUnix):
                        lineToWrite = eachLine + '\n'
                        saveFile.write(lineToWrite)
                    
        saveFile.close()
        
        print 'Pulled',stock
        print 'Sleeping....'
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1)
    
        
    except Exception,e:
        print 'main loop',str(e)
 
for eachStocks in stocksToPull:    
    pullData(eachStocks) 
        

"""
def main(argv):
    
    timeRange = ''
    
    try:
        # The options, ex: -h or -i, and the arguments, ex: <example>
        options, arguments = getopt.getopt(argv,"hi:r:",["range="])
    except getopt.GetoptError:
        print 'BetterPull.py -r/-range <Range>'
        sys.exit(2)
    for option, argument in options:
        if option == '-h':
            print 'BetterPull.py -r/-range <Range>'
            sys.exit()
        elif option in ("-r", "--range"):
            timeRange = argument
    print 'Time range is "', timeRange
    
    for eachStocks in stocksToPull:    
        pullData(eachStocks)
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
"""
    
    
    
