from config import key 
import requests 
import time  
import csv
stocks = ['AAPL', 'DIS', 'CLOV', 'AMZN', 'GOOGL']
#use a for loop to extract or requests the closing price of different dates from 03-29-2021 to 03-25-2022
for stock in stocks:

  url= f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&limit=300&apiKey={key}"
  data = requests.get(url)
  json_data = data.json()
  results = json_data['results']
  
  stock_data = []
  for day in results:
    closing_price= day['c']
    time_price = day['t']
    
    date = time.strftime('%Y-%m-%d', time.localtime(time_price/1000))
    #create a dictionary of date and closing price 
    stock_dict = {
      'Date':date,
      'Closing_Price':closing_price
      }
    stock_data.append(stock_dict)
    
    with open(f"{stock}.csv",'w', newline='') as file:
      writer = csv.DictWriter(file, fieldnames=["Date", "Closing_Price"])
      writer.writeheader()
      writer.writerows(stock_data)
      
    