import datetime
import yfinance as yf
import pandas as pd

class stock_fetcher:
    def __init__(self):
        #Adjustment for 1 day duration
        self.adjust=datetime.timedelta(days=1)
       
    def process_data(self,data):
        #Dividends and Stock Splits are usually 0, so dropping them
        data.drop(["Dividends","Stock Splits"],axis=1,inplace=True)
        #Date is produced as an index.
        #Need to create a column out of it.
        data.insert(0,"Date",data.index)
        #Replace Data as index with row number as index
        ind=[i for i in range(data.shape[0])]
        data=data.set_index([pd.Index(ind)])
        #Rearranging the columns in an appropriate order
        cols=["Date","Open","High","Low","Volume","Close"]
        data=data[cols]
        #Returning Processed data
        return data 

    def write_data(self, name, data):
        '''
        If there exists a dot in the stock ticker name, 
        remove it as this may cause discrepencies in file names.
        '''
        if "." in list(name):
            name="".join([i for i in list(name) if i!="."])
        #Storing file name
        file=name+".csv"
        #Writitng data to csv file
        data.to_csv(file)

    def fetch_data(self, name, curr_date, duration):
        #Converting data string provided in "YYYY-MM-DD" format to datatime object
        curr=datetime.datetime.strptime(curr_date, "%Y-%m-%d")
        #Get Yahoo Finance Ticker name from symbol name
        sym=yf.Ticker(name)
        #If negatve duration
        if duration<0:
            #Go back d days including current day, hence the minus one
            d=datetime.timedelta(days=abs(duration)-1)
            #Get starting data
            start=curr-d
            #Download data in given data range
            data=sym.history(start=start,end=curr+self.adjust)
        else:
            #Go forward d days including current date
            d=datetime.timedelta(days=duration)
            #Get ending date
            end=curr+d
            #Download data in given data range
            data=sym.history(start=curr+self.adjust, end=end)
        '''
        Processing downloaded data.
        Changing index, dropping unnecessary columns and reordering columns
        '''
        data=self.process_data(data)
        #Write processed data to a csv file named according to the stock's ticker name
        self.write_data(name,data)
        return data