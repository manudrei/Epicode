studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith",
"Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend",
"Frontend", "Data Analyst", "Backend"]
i=0 # La consegna del sesto esercizio è poco chiara, comunque usero l'append per tutti i studenti e li aggiungerò a corsi
while i <= len(studenti)-1:
    index=studenti[i]
    corsi.append(index)
    i+=1
print(corsi)

lun_stu=len(studenti)
lun_corsi=len(corsi)

if lun_corsi == lun_stu :
    print("Hanno la stessa lunghezza")
else:
    print("Non hanno la stessa lunghezza")
