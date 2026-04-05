import requests

url = "https://eodhd.com/api/fundamentals/AAPL.US?api_token=demo&fmt=json"

response = requests.get(url)

#print(response)

 print("End")