import requests

# Karena jalan di laptop sendiri, kita pakai alamat localhost
# JANGAN LUPA: Terminal server harus tetap terbuka saat menjalankan ini!
API_URL = "http://127.0.0.1:8000/presensi"

# Ganti dengan nama foto yang ada di folder Anda
FILE_FOTO = "5231911003_ulen_16.jpg" 

print(f"🚀 Mencoba presensi ke: {API_URL}")

try:
    with open(FILE_FOTO, "rb") as f:
        files = {"file": f}
        response = requests.post(API_URL, files=files)
    
    if response.status_code == 200:
        hasil = response.json()
        print("\n✅ HASIL DARI SERVER:")
        print(f"   Nama      : {hasil['nama']}")
        print(f"   Kemiripan : {hasil['jarak_kemiripan']}")
        print(f"   Status    : {'DITERIMA' if hasil['dikenali'] else 'DITOLAK'}")
    else:
        print("\n❌ Error:", response.text)

except FileNotFoundError:
    print("❌ Foto tidak ditemukan. Pastikan nama file benar.")
except Exception as e:
    print("❌ Gagal connect ke server. Pastikan terminal uvicorn masih nyala.")