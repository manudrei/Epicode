## Esercizio 3

import seaborn as sns
titanic=sns.load_dataset('titanic')
# Quanti ponti c'erano sulla nave?
ponti=set(titanic["deck"])
len(ponti)
titanic.isnull().sum()
##possiamo optare di inserire i valori dell'età in base alla media della tariffa pagata
titanic.groupby("age").fare.mean()
#tramite seaborn visualizziamo un jointplot sulle colonne fare e age
sns.jointplot(data=titanic, x="fare", y="age")

## Seconda parte esercizio

#Visualizzare un grafico con la differenza tra il numero di passeggeri di ogni classe di imbarco
sns.countplot(data=titanic, x="class")
#stessa cosa con la colonna alive
sns.countplot(data=titanic, x="alive")
#Qual' era la distribuzione delle tariffe (fare)?
plt.hist(titanic["fare"])
#Proviamo con un boxplot e con uno swarmplot
sns.boxplot(data=titanic, x="class", y="age")
#swarmplot
sns.swarmplot(data=titanic, x="class", y="age")
#visualizziamo un kdeplot per la colonna age
sns.kdeplot(data=titanic["age"])
#Visualizziamo un boxplot e un lmplot rispetto alle colonne fare e survived che cose ne deduciamo?
sns.boxplot(data=titanic, x="survived", y="fare")
#lmplot
sns.lmplot(data=titanic, x="survived", y="fare")


## Terza Parte

px.scatter(data_frame=titanic, x="age", y="deck", color="survived", size="fare", symbol="sex", category_orders={"deck": list("ABCDEFG")})
#### Possiamo dunque dire che la maggior parde dei deceduti sono situati sul ponte C, mentre sul ponte B, avendo pagato una tariffa maggiore sono sopravvissute più persone.