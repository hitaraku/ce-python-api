import urllib.request
import json

# マーケットデータ
market = json.loads(urllib.request.urlopen("https://www.coinexchange.io/api/v1/getmarkets").read())

# マーケット 概要、ID
summary = json.loads(urllib.request.urlopen("https://www.coinexchange.io/api/v1/getmarketsummaries").read())

print(
    "ticker: ", market['result'][0]['MarketAssetCode'], market['result'][0]['BaseCurrencyCode'], 
    "LastPrice: ", summary['result'][0]['LastPrice'], 
    "HighPrice: ", summary['result'][0]['HighPrice'], 
    "LowPrice: ", summary['result'][0]['LowPrice'], 
    "Volume: ", summary['result'][0]['Volume']
    )



