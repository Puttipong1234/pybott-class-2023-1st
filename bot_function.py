apikey = "xxx"
apisecret = "xxx"
testing = True # False กรณี รันบนaccountจริง

import ccxt
exchange = ccxt.binance({
    'apiKey':apikey,
    'secret':apisecret,
    'options': {
        'defaultType':"future"
    }
})
exchange.set_sandbox_mode(testing)

def openLong(symbol="BTCUSDT",amount="0.1"):
    
    param = {"positionSide":"LONG",}

    exchange.create_order(symbol=symbol,
                        type="market",
                        side="buy",
                        amount=amount,
                        params=param)

def closeLong(symbol="BTCUSDT",amount="0.1"):
    
    param = {"positionSide":"LONG",}

    exchange.create_order(symbol=symbol,
                        type="market",
                        side="sell",
                        amount=amount,
                        params=param)

def openShort(symbol="BTCUSDT",amount="0.1"):
    
    param = {"positionSide":"SHORT",}

    exchange.create_order(symbol=symbol,
                        type="market",
                        side="sell",
                        amount=amount,
                        params=param)

def closeShort(symbol="BTCUSDT",amount="0.1"):
    
    param = {"positionSide":"SHORT",}

    exchange.create_order(symbol=symbol,
                        type="market",
                        side="buy",
                        amount=amount,
                        params=param)