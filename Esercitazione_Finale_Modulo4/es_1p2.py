# estraimo le prime 20 istanze della colonna AAPL delle azioni di Apple, e visualizziamo il grafico tramite pyplot, in modo che:
#* il grafico sia rosso
#* la linea sia tratteggiata
#* vi sia un pallino come marker
#* l'asse delle ascisse si chiami "Data"
#* l'asse dell ordinate si chiami "Valore"
#* il titolo del grafico sia "Azioni Apple"
#* il markerfacecolor sia nero
#* la linea abbia spessore uguale a 2 
from plotly import express as px
import matplotlib.pyplot as plt
stocks = px.data.stocks()
print(stocks)
stocks_a=stocks.loc[:19, "AAPL"]
y= stocks_a
x = range(len(y))
plt.plot(stocks_a, color="red", linewidth=2.0, marker="o",
markersize=10, markerfacecolor="black", linestyle="--")
plt.title("Azioni Apple")
plt.xlabel("Data")
plt.ylabel("Valore")
plt.show()
print(stocks_a)

