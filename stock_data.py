import requests
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

stock=input("Enter Stock Symbol i.e Amazon as AMZN: ")


url= "https://query1.finance.yahoo.com/v7/finance/download/"+ stock.upper() + "?period1=1277769600&period2=1686096000&interval=1d&events=history&includeAdjustedClose=true"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
now = datetime.now()
dt_string = now.strftime("%d%m%H%M")

content=requests.get(url, headers=headers).content
with open(dt_string + stock.upper() + ".csv", "wb") as file:
    file.write(content)

df = pd.read_csv(dt_string + stock.upper() + ".csv")

fig = go.Figure(data=go.Scatter(x=df['Date'],y=df['Close'], mode='lines'))
fig.show()

