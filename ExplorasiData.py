import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Dataset/Data_Nasabah.csv', delimiter=';')

print("\nLima Baris Pertama data:")
print(data.head())

print("\nInformasi Data:")
print(data.info())

print("\nStatistik Deskriptif:")
print(data.describe())

print("\nJumlah Nilai Unik Setiap Kolom:")
for column in data.columns:
    print(f"{column}: {data[column].nunique()}")


# Analisis Distribusi Data Numerik
numerical_features = data.select_dtypes(include=['number']).columns
for feature in numerical_features:
    plt.figure(figsize=(8,6))
    sns.histplot(data[feature], kde=True)
    plt.title(f"Distribusi {feature}")
    plt.show()

# Analisis Korelasi antar Variabel
numerical_data = data.select_dtypes(include=['number'])
correlation_matrix = numerical_data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matrix Korelasi")
plt.show()

# Analisis Data Kategorikal
categorical_features = data.select_dtypes(include=['object']).columns
for feature in categorical_features:
   plt.figure(figsize=(8,6))
   sns.countplot(x=feature, data=data)
   plt.title(f"Jumlah Kemunculan {feature}") 
   plt.xticks(rotation=45)
   plt.show()

# Analisis Nilai Hilang (Missing Values)
missing_values = data.isnull().sum()
print("\nJumlah Nilai Hilang Setiap Kolom:")
print(missing_values)

# Analisis Outlier (Nilai Aneh)
for feature in numerical_features:
    plt.figure(figsize=(8,6))
    sns.boxplot(x=data[feature])
    plt.title(f"Deteksi Outlier pada {feature}")
    plt.show()

# Menampilkan distribusi data untuk kolom tertentu
# (misalnya, 'Umur')
plt.figure(figsize=(8,6))
sns.histplot(data['umur'], kde=True)
plt.title('Distribusi Umur')
plt.xlabel('Umur')
plt.ylabel('Frekuensi')
plt.show()

# Analisis hubungan antara dua variable (misalnya, 'Umur' dan 'Pendapatan')
plt.figure(figsize=(8,6))
sns.scatterplot(x='umur', y='pendapatan', data=data)
plt.title('Hubungan antara Umur dan Pendapatan')
plt.xlabel('Umur')
plt.ylabel('Pendapatan')
plt.show()

# Menampilkan distribusi data untuk kolom 'Jenis Kelamin'
plt.figure(figsize=(6,4))
sns.countplot(x='jenis_kelamin', data=data)
plt.title('Distribusi Jenis Kelamin')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Jumlah')
plt.show()

# menampilkan hubungan antara 'Jenis Kelamin' dan 'Pendapatan'
plt.figure(figsize=(8,6))
sns.boxplot(x='jenis_kelamin', y='pendapatan', data=data)
plt.title('Hubungan antara Jenis Kelamin dan Pendapatan')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Pendapatan')
plt.show()