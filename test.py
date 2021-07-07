from get_stock_details import stock_fetcher
obj=stock_fetcher()
file=open("stocks.txt","r")
data=file.read()
stocks=data.split("\n")
for stock in stocks:
    data=obj.fetch_data(stock,"2020-06-30",duration=-30)
    #print(data)