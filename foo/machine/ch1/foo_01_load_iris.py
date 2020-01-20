from sklearn.datasets import load_iris

# load iris data
iris_dataset = load_iris()

# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])
print("Keys of iris_dataset:\n", iris_dataset.keys())

# desc
# print(iris_dataset['DESCR'])
print(iris_dataset['DESCR'][:193] + "\n...")

# target_names
# ['setosa' 'versicolor' 'virginica']
print("Target names:\n", iris_dataset['target_names'])

# feature_names
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print("Feature names:\n", iris_dataset['feature_names'])

# data
# <class 'numpy.ndarray'>
print("Type of data:", type(iris_dataset['data']))
# (150, 4)
print("Shape of data:", iris_dataset['data'].shape)
print("First five rows of data:\n", iris_dataset['data'][:5])

# target
# <class 'numpy.ndarray'>
print("Type of target:", type(iris_dataset['target']))
# (150,)
print("Shape of target:", iris_dataset['target'].shape)
print("Target:\n", iris_dataset['target'])
