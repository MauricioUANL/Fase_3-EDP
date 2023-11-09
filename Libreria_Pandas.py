import pandas as pd
import numpy as np

s= pd.Series([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
s.count()
print(s.count())

s.sum()
print(s.sum())

s.cumsum()
print(s.cumsum())

s.value_counts()
print(s.value_counts())

s.value_counts(normalize=True)

s.min()
print(s.min())


s.max()
print(s.max())

s.mean()
print(s.mean())

s.std()
print(s.std())


s.describe()
print(s.describe())


import pandas as pd

s = pd.Series([1, 2, 3, 4])
s*2
print(s)

s%2
print(s)

s = pd.Series(['a', 'b', 'c'])
s*5
print(s)


from math import log
s = pd.Series([1, 2, 3, 4])
s.apply(log)
print(s.apply(log))

s = pd.Series(['a', 'b', 'c'])
s.apply(str.upper)
print(s.apply(str.upper))

s = pd.Series({'Matematicas': 6.0, 'Economia': 4.5, 'Programacion': 8.5})
print(s[s > 5])

s = pd.Series({'Matematicas': 6.0, 'Economia': 4.5, 'Programacion': 8.5})
print(s.sort_values())

print(s.sort_index(ascending = False))


s = pd.Series(['a', 'b', None, 'c', np.NaN, 'd'])
s
print(s)

s.dropna()
print(s.dropna())

datos = {'nombre': ['Maria', 'Luis', 'Carmen', 'Antonio'],
         'edad': [18, 22, 20, 21],
         'grado': ['Economia', 'Medicina', 'Arquitectura', 'Economia'],
         'correo': ['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
         }
df = pd.DataFrame(datos)
print(df)


df = pd.DataFrame([['Maria', 18], ['Luis', 22], ['Carmen', 20]], columns = ['Nombre', 'Edad'])
print(df)


df = pd.DataFrame([{'Nombre': 'Maria', 'Edad': 18}, {'Nombre': 'Luis', 'Edad': 22}, {'Nombre': 'Carmen'}])
print(df)


df = pd.DataFrame(np.random.randn(4, 3), columns = ['a', 'b', 'c'])
print(df)


df = pd.read_csv( '...', sep = ';')