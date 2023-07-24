from plotly import express as px
import matplotlib.pyplot as plt
stocks = px.data.stocks()
print(stocks)
stocks_g=stocks["GOOG"] # estraiamo i dati della colonna GOOG relative all'andamento delle azioni di Google, e visualizziamolo mediante pyplot
plt.plot(stocks_g)
plt.show()
#estraiamo le prime 5 righe della colonna GOOG e della colonna date, e usiamoli come ascisse e ordinate su un grafico mediante pyplot.
y= stocks.loc[:4,"GOOG"]
x= stocks.loc[:4,"date"]
plt.plot(x,y)
plt.xlabel("date")
plt.ylabel("GOOG");
# facciamo lo stesso per le ultime 5 righe del dataset
x1= stocks.tail(5)["date"]
y1= stocks.tail(5)["GOOG"]
plt.plot(x1,y1)
plt.xlabel("date")
plt.ylabel("GOOG");