import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# melihat dimensi dataset
print("Dimensi dataset:", df.shape)

# melihat 5 baris pertama dataset
print('\nLima baris pertama dataset:\n', df.head())

# Melihat informasi dataset
print("\nInformasi dataset:\n", df.info())

# Melihat deskripsi statistik dataset
print("\nDeskripsi statistik dataset\n", df.describe())

# Melihat distribusi kelas target
print("\nDistribusi kelas target:\n", df['target'].value_counts())

# Melihat korelasi antar variabel
print("\nKorelasi antar variabel:\n", df.corr())

# Mengecek Missing Value 
print("\nMissing Values:", df.isnull().sum())

# membuat visualisasi
# df.hist(figsize=(10,8))
# plt.show()

# plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c=df['target'])
# plt.xlabel('Sepal Length')
# plt.ylabel('Petal Length')
# plt.show()

# Deteksi Outlier
# df.boxplot(figsize=(10,6))
# plt.show()

# Heatmap korelasi
# import seaborn as sns
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# plt.show()

# Distribusi Target
# sns.countplot(x='target', data=df)
# plt.show()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test,y_pred))