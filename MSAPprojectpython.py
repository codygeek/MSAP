import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data= pd.read_csv("C:\\Users\\hardik\\Desktop\\rdatacsv.csv")
pred=pd.DataFrame(data,columns=['MatchNo','Opponent','Season','Runs'])

r=data['Runs']
o=data['Opponent'].unique()
print(o)

sumEng=0
sumNew=0
sumWi=0
sumAu=0
sumSl=0

for itr in pred.iterrows():

    if itr[1][1]  == 'England':
        sumEng += itr[1][3]
    elif itr[1][1]  == 'New Zealand':
        sumNew += itr[1][3]
    elif itr[1][1]  == 'Australia':
        sumAu += itr[1][3]
    elif itr[1][1]  == 'West Indies':
        sumWi += itr[1][3]
    elif itr[1][1]  == 'SriLanka':
        sumSl += itr[1][3]
print(sumEng)
print(sumNew)
print(sumAu)
print(sumWi)
print(sumSl)

maxRuns  = np.array([sumEng,sumNew,sumAu,sumWi,sumSl])
dict = {}
for OpponentName, TotalRuns in zip(o, maxRuns):
    dict[OpponentName] = TotalRuns

print(dict)

plt.bar(dict.keys(),dict.values(),color=('bisque','yellow','green','purple','magenta'),edgecolor='black')
plt.xlabel("Opponents")
plt.ylabel("Runs")
plt.tick_params(axis='x', colors='blue')
plt.tick_params(axis='y', colors='green')
plt.title("Maximum runs scored against opponent(s)")
plt.show()

plt.scatter(data['Opponent'],data['Runs'],color='red')
plt.title('Maximum Runs scored against opponent(s)',fontsize=14)
plt.xlabel('Opponent',fontsize=14)
plt.ylabel('Runs', fontsize=14)
plt.grid(True)
plt.show()
