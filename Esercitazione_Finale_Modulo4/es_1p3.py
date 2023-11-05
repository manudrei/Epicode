from plotly import express as px
import matplotlib.pyplot as plt
stocks = px.data.stocks()
print(stocks)
stocks_a=stocks["AAPL"]
stocks_g=stocks["GOOG"]
stocks_am=stocks["AMZN"]
stocks_fb=stocks["FB"]
stocks_n=stocks["NFLX"]
stocks_mi=stocks["MSFT"]
plt.plot(stocks_g)
plt.plot(stocks_a)
plt.plot(stocks_am)
plt.plot(stocks_fb)
plt.plot(stocks_n)
plt.plot(stocks_mi)
plt.legend(["GOOGLE", "APPLE", "AMAZON", "FACEBOOK", "NETFLIX", "MICROSOTF"] , loc=4)
plt.show()