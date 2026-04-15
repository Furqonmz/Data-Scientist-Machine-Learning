import pandas as pd 

df = pd.read_csv('Dataset/Data_Nasabah.csv', delimiter=";")

print("Jumlah data (Baris, Kolom):", df.shape)

print("\nInformasi tipe data dan skema pengkodean:")
print(df.info())

print("\nStatistik deskriptif untuk data numerik:")
print(df.describe())

print("\nBeberapa baris pertama data:")
print(df.head())

print("\nJumlah nilai unik untuk setiap kolom:")
for column in df.columns:
    print(f"{column}: {df[column].nunique()}")