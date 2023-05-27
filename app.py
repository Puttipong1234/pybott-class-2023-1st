import json

import MetaTrader5 as mt5
from flask import Flask, request

from bot_function import closeLong, closeShort, openLong, openShort
from forex_function import close_orders, orders

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Pybott!</p>"

@app.route("/webhook/settrade")
def webhook_set():
    return "this is set trade route"

@app.route("/webhook/crypto",methods=["GET","POST"])
def webhook():
    if request.method == "POST":
        print("ได้รับข้อมูล เตรียมการทำคำสั่งซื้อขาย")
        signal = request.data.decode("utf-8")
        signal = json.loads(signal)
        
        action = signal["ACTION"].split(" ")[0] # open , close
        side = signal["ACTION"].split(" ")[1] # long , short
        amount = float(signal["AMOUNT_COIN"])
        sym = signal["SYMBOL"]
        
        if action == "OPEN":
            if side == "LONG":
                openLong(symbol=sym,amount=amount)
            elif side == "SHORT":
                openShort(symbol=sym,amount=amount)
        
        elif action == "CLOSE":
            if side == "LONG":
                closeLong(symbol=sym,amount=amount)
            elif side == "SHORT":
                closeShort(symbol=sym,amount=amount)
        
        return request.data
    else:
        return "This is webhook for BOT trade"

@app.route('/webhook/forex', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        
        mt5.initialize()
        
        print("Signal from tradingview")
        print("Preparing for an order")
        print("Data incoming : " + str(request.data))
        
        # รับ Data แปลงให้เป็น dictionary
        signal = request.data.decode("utf-8")
        signal = json.loads(signal)
        
        # แยกแยะแล้วจัดเก็บใส่ตัวแปร
        symbol = signal["symbol"]
        lot = float(signal["lot"])
        action = signal["action"].split(" ")[0]
        side = signal["action"].split(" ")[1]
        
        partial = 100
        if action == "CLOSE":
            partial = int(signal["action"].split(" ")[2])
        
        
        # ทำการเปิด orders + ป้องกันการเกิด requote
        while True:
            r = ""
            if action == "OPEN":
                if side == "LONG":
                    r = orders(symbol, lot)
                elif side == "SHORT":
                    r = orders(symbol, lot,buy=False)
            
            elif action == "CLOSE":
                if side == "LONG":
                    r = close_orders(symbol,True ,lot*(partial/100))
                elif side == "SHORT":
                    r = close_orders(symbol,False ,lot*(partial/100))
                    
        # + ป้องกันการเกิด requote
            if r == "Requote":
                time.sleep(0.5)
                continue
            else:
                break
        
        mt5.shutdown()
        
        return request.data , 200
    else:
        return "This is a FOREX service"

if __name__ == '__main__':
    app.run(debug=True)
    