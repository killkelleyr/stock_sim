import os, requests, json

class quote():
    def __init__(self, ticker):
        #url = 'https://{PLATFORM}.iexapis.com/stable/stock/{TICKER}/quote?token={TOKEN}'.format(PLATFORM=os.environ['API_PLATFORM'], TICKER=ticker, TOKEN=os.environ['API_TOKEN'])
        url = 'https://sandbox.iexapis.com/stable/stock/{TICKER}/quote?token=Tpk_0d40efa9983f42f0bb5c509cdf5a1236'.format(TICKER=ticker)
        response = json.loads(requests.get(url))
        
        print(response.symbol)