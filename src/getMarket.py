import urllib.request
import json

# マーケット 概要、ID
summary = json.loads(urllib.request.urlopen("https://www.coinexchange.io/api/v1/getmarketsummaries").read())
firstMarketID = summary['result'][0]['MarketID']
summaryVol = len(summary['result'])

# マーケットデータ
market = json.loads(urllib.request.urlopen("https://www.coinexchange.io/api/v1/getmarkets").read())

for i in range(summaryVol - int(firstMarketID)):
    MarketNumber = int(firstMarketID) + i - 1
    print(
        "ticker: ", market['result'][MarketNumber]['MarketAssetCode'], market['result'][MarketNumber]['BaseCurrencyCode'], 
        "LastPrice: ", summary['result'][MarketNumber]['LastPrice'], 
        "HighPrice: ", summary['result'][MarketNumber]['HighPrice'], 
        "LowPrice: ", summary['result'][MarketNumber]['LowPrice'], 
        "Volume: ", summary['result'][MarketNumber]['Volume']
        )



