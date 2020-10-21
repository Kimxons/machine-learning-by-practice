from numpy import asarray
from sklearn.preprocessing import OneHotEncoder

data = asarray([['red'],['green'],['blue']])
encoder = OneHotEncoder(sparse=False)
onehot = encoder.fit_transform(data)

print(data)
print(onehot)
