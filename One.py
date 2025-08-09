import pandas as pd


labels = ['Sunny', 'Overcast', 'Rain', 'Sunny', 'Rain']


one_hot = pd.get_dummies(labels)


print(one_hot)

