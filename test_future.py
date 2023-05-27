apikey = "xxx"
apisecret = "xxx"

import ccxt
# print(ccxt.exchanges)
# binance , hedge mode , cross margin
exchange = ccxt.binance({
    'apiKey':apikey,
    'secret':apisecret,
    'options': {
        'defaultType':"future"
    }
})
exchange.set_sandbox_mode(True)

result = exchange.fetch_balance(
    params={
        'type':'future',
        'marginMode':'cross',
    }
)
# print(result["info"]["assets"])

assets = result["info"]["assets"]
for asset in assets:
    if asset["asset"] == "USDT" or asset["asset"] == "BUSD":
        print("มี " + asset["asset"] 
              + " อยู่ในพอร์ต " 
              + str(asset["walletBalance"]) 
              + asset["asset"])

# มี USDT อยู่ในพอร์ต : 1222 USDT
# มี BUSD อยู่ในพอร์ต : 1222 BUSD

# fetch open high low close
# res = exchange.fetch_ohlcvc(symbol="BTCUSDT",timeframe='5m')
# print(res)

# PLACE ORDER
try:
    exchange.set_position_mode(hedged=True)

except Exception as e:
    print("warning : " + e)

# open long
param = {
    "positionSide":"LONG",
}

exchange.create_order(symbol="BTCUSDT",
                      type="market",
                      side="buy",
                      amount=0.1,
                      params=param)

import time
time.sleep(10)

# close long
param = {
    "positionSide":"LONG",
}

exchange.create_order(symbol="BTCUSDT",
                      type="market",
                      side="sell",
                      amount=0.1,
                      params=param)

# open short
param = {
    "positionSide":"SHORT",
}

exchange.create_order(symbol="BTCUSDT",
                      type="market",
                      side="sell",
                      amount=0.2,
                      params=param)

time.sleep(10)

# close short
param = {
    "positionSide":"SHORT",
}

exchange.create_order(symbol="BTCUSDT",
                      type="market",
                      side="buy",
                      amount=0.1,
                      params=param)


