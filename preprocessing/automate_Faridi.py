import pandas as pd
import os

def preprocess_data(input_path, output_path):
    
    # 1. Loading Data
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} ora ditemokake!")
        return None
    
    df = pd.read_csv(input_path)
    print(f"Lagi mroses data saka: {input_path}")

    # 2. Handling Missing Values (Kudu padha karo notebook)
    # Ngisi Purchase Amount nganggo Median
    if 'Purchase Amount (USD)' in df.columns:
        df['Purchase Amount (USD)'] = df['Purchase Amount (USD)'].fillna(df['Purchase Amount (USD)'].median())
    
    # Ngisi Review Rating nganggo Mean
    if 'Review Rating' in df.columns:
        df['Review Rating'] = df['Review Rating'].fillna(df['Review Rating'].mean())

    # 3. Feature Selection
    # Mbusak kolom sing ora dibutuhake kanggo model (ID lan Tanggal)
    cols_to_drop = ['Customer Reference ID', 'Date Purchase', 'Item Purchased']
    df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

    # 4. Encoding Categorical Data
    # Ngowahi Payment Method dadi angka (Credit Card = 1, Cash = 0)
    if 'Payment Method' in df.columns:
        mapping = {'Credit Card': 1, 'Cash': 0}
        df['Payment Method'] = df['Payment Method'].map(mapping)

    # 5. Simpen Hasil Preprocessing
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"Nggawe folder anyar: {output_path}")

    final_file_path = os.path.join(output_path, 'fashion_sales_processed.csv')
    df.to_csv(final_file_path, index=False)
    
    print(f"--- Preprocessing Berhasil ---")
    print(f"Hasil disimpen ing: {final_file_path}")
    print(f"Jumlah baris: {len(df)}")
    
    return df

if __name__ == "__main__":
    # Atur path sesuai struktur folder repository [cite: 14, 18]
    INPUT_FILE = '../Fashion_Retail_Sales_Raw.csv'
    OUTPUT_FOLDER = 'dataset_preprocessing'
    
    # Jalankan fungsi
    preprocess_data(INPUT_FILE, OUTPUT_FOLDER)