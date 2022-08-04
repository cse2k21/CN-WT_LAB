import pandas as pd 
import numpy as np
data = pd.read_csv('enjoysport.csv')
a = np.array(data.iloc[:])
print("The total number of training instances are ",len(a))
print("The total number of attributes in an instances are ",len(a[0]))
num_att = len(a[0])-1
hypo = ['0']*num_att
print(hypo)
for i in range(len(a)):
  if a[i][num_att]=="yes":
    for j in range(num_att):
      if hypo[j] == '0' or hypo[j]==a[i][j]:
        hypo[j] = a[i][j]
      else:
        hypo[j]='?'
    print("The Hypothesis for the training instance ",i+1,"is :\n",hypo)
print("The Maximumly Specific Hypothesis for the given training instance is :\n",hypo)
