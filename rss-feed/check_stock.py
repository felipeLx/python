import yfinance as yf

symbols = ["RECV3.SA","GRND3F.SA","AGRO3F.SA","GRND3F.SA","BFBI39.SA","GSGI34F.SA","S2HO34.SA","AGRO3F.SA","OFSA3.SA"]

a = yf.Ticker('GRND3F.SA').info
print(a)

"""
for symbol in symbols:
    a = yf.Ticker(symbol).info
    if not a['dayHigh']:
        print('not dayHigh')
    else:
        print('have dayHigh')
"""