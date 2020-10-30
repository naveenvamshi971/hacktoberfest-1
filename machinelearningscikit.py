from sklearn import datasets #sklearn lib
data = datasets.load_boston() #boston dataset

print(data.keys())
print(data.DESCR)
