stringa=input("Inserisci sei caratteri")

while len(stringa) != 6: #Si potrebbe fare anche con un if else ma non chiede all'utente di rimettere i caratteri giusti
    
    if len(stringa) > 6 or len(stringa) < 6:
        print("La stringa non è di 6 caratteri, non vabene")
        stringa=input("Inserisci sei caratteri")
    else:
        break
        

print(stringa[0:3] + "..." + stringa [3:6])