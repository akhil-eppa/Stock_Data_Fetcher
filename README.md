# Stock_Data_Fetcher
Script to automate fetching of stocks based on various parameters

# Prerequisites
Required Packages
* yfinance
* pandas
* datetime

```
pip install <package-name>
```

<hr>

# Usage 
```
from get_stock_details import stock_fetcher
obj=stock_fetcher()
data=obj.fetch_data("TATAMOTORS.NS","2020-06-30",duration=-30)
```

# Parameter for fetch_data
* stock ticker name : If stock belongs to NSE, add ".NS" prefix to ticker name.
* reference date : This date is a reference date. Format is "YYYY-MM-DD". Stocks for n days after the reference data or n days before the reference date can be fetched.
* duration : If the duration 'd' is negative, fetch from d days prior upto the reference date. If the duration is positive, fetch from current date upto d days after. Reference date is inclusive in both ranges.


Sample script is **test.py**. 
Fetched stock data for example stocks present in **Fetched_Stocks** folder.
