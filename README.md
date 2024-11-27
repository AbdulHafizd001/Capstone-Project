# Dokumentasi Proyek API dengan Flask dan Firestore
API ini dibangun menggunakan **Flask** sebagai framework backend dan **Google Firestore** sebagai basis data NoSQL. Dengan API ini, Anda dapat mengelola data pengguna secara dinamis melalui operasi **CRUD (Create, Read, Update, Delete)**.

---

## 📋 Pendahuluan
API ini dirancang untuk mempermudah integrasi dengan aplikasi lain yang membutuhkan pengelolaan data pengguna. Dengan dukungan teknologi yang ringan dan fleksibel, Anda dapat menggunakannya sebagai bagian dari proyek Anda.

---

## 🏗 Arsitektur
- **Flask**: Framework backend untuk membangun API.
- **Google Firestore**: Basis data NoSQL untuk menyimpan informasi pengguna.

---

## 🔧 Persyaratan
Pastikan Anda telah menginstal:
- **Python**: Versi 3.x
- **Flask**: Framework aplikasi web.
- **firebase-admin**: Library Python untuk integrasi dengan Firebase dan Firestore.

---

## 📦 Instalasi Dependensi
Jalankan perintah berikut di direktori proyek untuk menginstal dependensi:
```
pip install -r requirements.txt
```
File requirements.txt:
```
Flask
firebase-admin
```

## ⚙️ Konfigurasi Awal
1. Buat Service Account Key untuk Firestore<br>
- Masuk ke Firebase Console.
- Pilih proyek yang relevan, buka Project Settings.
- Pada tab Service Accounts, buat Private Key untuk Firestore.

2. Simpan file JSON ke folder proyek Anda:<br>
```C:\msib-abdul\capstone-project\database_firestore\serviceAccountKey.json.```<br>

3. Struktur Direktori Proyek<br>
Berikut struktur direktori yang disarankan:<br>
```
capstone-project/
├── app.py                  # File utama aplikasi
├── requirements.txt        # File dependensi
└── database_firestore/
    └── serviceAccountKey.json  # Kunci layanan Firestore
```
<br><br>
## 🚀 Kode Utama (app.py)
Kode lengkap API:
```python
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

# Path ke file serviceAccountKey.json
cred = credentials.Certificate("C:\\msib-abdul\\capstone-project\\database_firestore\\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Koneksi ke Firestore
db = firestore.client()

app = Flask(__name__)

# Endpoint CRUD untuk Koleksi Users

# Create User (POST)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = data.get('user_id')  # Pastikan ID unik
    db.collection('Users').document(user_id).set(data)
    return jsonify({"message": "User created successfully"}), 201

# Retrieve User (GET)
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_ref = db.collection('Users').document(user_id)
    user = user_ref.get()
    if user.exists:
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "User not found"}), 404

# Update User (PUT)
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    db.collection('Users').document(user_id).update(data)
    return jsonify({"message": "User updated successfully"}), 200

# Delete User (DELETE)
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    db.collection('Users').document(user_id).delete()
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
## 🖥 Menjalankan Aplikasi<br>
Pastikan dependensi telah diinstal dan Firestore terhubung.<br>
Jalankan perintah berikut di terminal untuk memulai server:<br>
```python
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

```API akan berjalan di:``` http://127.0.0.1:5000

## 🛠 Pengujian API dengan Postman
Gunakan Postman untuk menguji endpoint API berikut:

### - POST /users<br>
Tambahkan pengguna baru.<br>
URL: http://127.0.0.1:5000/users<br>
Body (JSON):<br>
```python
{
  "user_id": "user1",
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### - GET /users/<user_id><br>
Ambil data pengguna berdasarkan user_id.<br>
URL: http://127.0.0.1:5000/users/user1

### - PUT /users/<user_id>
Perbarui data pengguna.<br>
URL: http://127.0.0.1:5000/users/user1
Body (JSON):
```python
{
  "email": "new.email@example.com"
}
```

### - DELETE /users/<user_id>
Hapus data pengguna.<br>
URL: http://127.0.0.1:5000/users/user1
<br><br>
## 🔮 Langkah Selanjutnya<br>
Hosting API: Pertimbangkan untuk hosting API di platform seperti:

