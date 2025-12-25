import pandas as pd
import os

def run_preprocessing(input_path, output_path):
    print(f"Memulai preprocessing untuk: {input_path}")
    
    # 1. Memuat Dataset
    if not os.path.exists(input_path):
        print("Error: File mentah tidak ditemukan!")
        return
    
    df = pd.read_csv(input_path)
    
    # 2. Pembersihan Data (Berdasarkan analisis di notebook)
    # Mengonversi tanggal ke format datetime
    df['Date Purchase'] = pd.to_datetime(df['Date Purchase'])
    
    # Menangani nilai kosong pada Review Rating (contoh: dengan median)
    if df['Review Rating'].isnull().sum() > 0:
        median_rating = df['Review Rating'].median()
        df['Review Rating'] = df['Review Rating'].fillna(median_rating)
        print(f"- Mengisi missing values di 'Review Rating' dengan median: {median_rating}")

    # Menangani nilai kosong pada Purchase Amount (jika ada)
    if df['Purchase Amount (USD)'].isnull().sum() > 0:
        df['Purchase Amount (USD)'] = df['Purchase Amount (USD)'].interpolate()
        print("- Mengisi missing values di 'Purchase Amount (USD)' dengan interpolasi")

    # 3. Menyimpan Hasil
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Preprocessing selesai! File disimpan di: {output_path}")
    print(f"Total baris data: {len(df)}")

if __name__ == "__main__":
    # Sesuaikan path sesuai struktur folder Anda
    RAW_DATA = "../Fashion_Retail_Sales_raw/Fashion_Retail_Sales.csv"
    CLEAN_DATA = "Fashion_Retail_Sales_preprocessed/Fashion_Retail_Sales_Cleaned.csv"
    
    run_preprocessing(RAW_DATA, CLEAN_DATA)