library('xlsx')

data=read.xlsx('C:\\Users\\hardik\\Desktop\\Dataset.xlsx', sheetIndex = 1)
print(data)

print("Opponent key:Australia=1,England=2,SriLanka=3,NewZealand=4,West Indies=5")

Opponent.factors=factor(data$Opponent)
data$Opponent=as.numeric(Opponent.factors)

Season.factors=factor(data$Season)
data$Season=as.numeric(Season.factors)

model=lm(Runs~MatchNo+Opponent+Season,data=data)
pred=data.frame(
  MatchNo=c(101,102,103,104,105),
  Opponent=c(2,4,5,3,3),
  Season=c(1,2,1,2,1))

predresult=predict(model,pred)

print(predresult)
par(mfrow=c(1,2))
plot(predresult,
main="Prediction result",
ylab="Runs",
xlab="Opponents")
pie(predresult,
main="Prediction result",radius=1)    
    


