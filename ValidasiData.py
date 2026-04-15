import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

df = pd.read_csv('Dataset/Data_Nasabah.csv', delimiter=';')

# Memeriksa konsistensi data, memeriksa apakah kolom umur hanya berisi nilai positif
print("\nValidasi Umur:")
if df['umur'].min() < 0:
    print("Terdapat nilai umur negatif, perlu diperiksa lebih lanjut.")
else:
    print("Nilai umur valid")

# Memeriksa apakah kolom jenis kelamin hanya berisi laki laki atau perempuan
print("\nValidasi Jenis Kelamin:")
invalid_gender = df['jenis_kelamin'].apply(lambda x: x not in ['Laki-Laki', 'Perempuan']).sum()
if invalid_gender > 0:
    print(f"Terdapat {invalid_gender} nilai jenis kelamin yang tidak valid")
else:
    print("Nilai jenis kelamin valid")

#  Mendeteksi dan Menangani Duplikat 
duplicat_rows = df.duplicated().sum()
if duplicat_rows > 0:
    print(f"\nTerdapat {duplicat_rows} baris data duplikat")
    # df = df.drop_duplicates() # Hapus baris duplikat jika dirasa perlu
else:
    print("\nTidak ada baris data duplikat.")

# Memvalidasi Rentang Data
print("\nValidasi Saldo Rata-rata")
if df['saldo_rata_rata'].max() > 1972000: #ganti dengan batas atas yang sesuai
    print("Terdapat nilai saldo rata - rata yang tidak realistis, perlu diperiksa.")
else:
    print("Nilai saldo rata-rata dalam rentang yang wajar.")



