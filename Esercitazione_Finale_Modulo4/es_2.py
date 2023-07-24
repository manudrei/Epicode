## Esercizio 2

from plotly import express as px
election = px.data.election()
# disegnamo un grafico a barre dove confrontiamo i voti totali presi dai tre candidati
election=px.data.election()
election.set_index("district",inplace=True)
plt.figure(figsize=[5,8])
election.total.plot(kind="barh")
plt.yticks(fontsize=9)
plt.grid(axis="x")
#visualizziamo un grafico a barre comparativo dove si confrontano i voti presi nei primi 4 distretti
election.sort_values("total",inplace=True)
distretti=election.iloc[:4, :3]
distretti.plot(kind="bar")
plt.grid(axis="y")
plt.savefig("grafico_a_barre_app.png", dpi=600)
distretti.plot(kind="barh", stacked=True)
plt.grid(axis="x")
plt.savefig("grafico_a_barre_imp.png", dpi=600)

