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

# Buat User Baru (POST)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = data.get('user_id')  # Pastikan ID unik
    db.collection('Users').document(user_id).set(data)
    return jsonify({"message": "User created successfully"}), 201

# Ambil Data User (GET)
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_ref = db.collection('Users').document(user_id)
    user = user_ref.get()
    if user.exists:
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "User not found"}), 404

# Update Data User (PUT)
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    db.collection('Users').document(user_id).update(data)
    return jsonify({"message": "User updated successfully"}), 200

# Hapus User (DELETE)
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    db.collection('Users').document(user_id).delete()
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)