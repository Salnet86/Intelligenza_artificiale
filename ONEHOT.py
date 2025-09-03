

INPUT = "come stai"
input_words = INPUT.strip().split()
parola = "ciao come stai ciao buona giornata".strip().split()
count=0
vettore=[]
vocabolario=[]
One_Hot=[]
for i in range(len(parola)):
    vettore.append(parola[i])
    if vettore[i]==parola[i]:
        count+=1
        if len(vettore[i])!=count:
            vocabolario.append(vettore[i])



One_Hot = []




for i in range(len(vocabolario)):
    Parole=False
    for j in range(len(input_words)):
        if vocabolario[i] == input_words[j]:
            Parole=True
    if Parole:
        One_Hot.append(1)
    else:
        One_Hot.append(0)






print(One_Hot)


'''
for i in range(len(vocabolario)):
    if vocabolario[i] in input_words:  # controllo corretto
        One_Hot.append(1)
    else:
        One_Hot.append(0)

print(One_Hot)

'''

