# string 
data = "CLOSE LONG 50"
data1 = data.split(" ")

# dictionary json
คำสั่งตัวอย่าง = {
            'ACTION': 'OPEN SHORT', # << USE
            'AMOUNT_COIN' : '0.1', # << USE
            'AMOUNT_USDT' : '30.00',
            'LEV' : '[PB-BTC-06]', 
            'SYMBOL' : 'BTCBUSD', # << USE
            'PASSWORD': "xxxxx", # << USE
            'FACTOR' : "10" # << USE....
        }

data = คำสั่งตัวอย่าง["ACTION"]
data = คำสั่งตัวอย่าง["AMOUNT_COIN"]
print(data)




