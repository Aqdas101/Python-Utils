import firebase_admin
from firebase_admin import credentials, firestore
import json
from google.cloud.firestore import DocumentSnapshot, SERVER_TIMESTAMP
from google.cloud.firestore import DocumentReference
import firebase_admin
from firebase_admin import credentials, firestore
import json

collection_name = "courses"

# Firebase credentials load karo
if not firebase_admin._apps:
        cred = credentials.Certificate("careerustaad-staging-firebase-adminsdk-fbsvc-43e41f3d55.json")
        firebase_admin.initialize_app(cred, {"storageBucket": "careerustaad-staging.firebasestorage.app"})


db = firestore.client()

docs = db.collection(collection_name).stream()

def serialize_firestore_doc(doc):
    data = doc.to_dict()
    for key, value in data.items():
        if isinstance(value, firestore.SERVER_TIMESTAMP.__class__):  # Convert timestamp
            data[key] = value.isoformat()
        elif isinstance(value, DocumentReference):  # Convert Firestore references
            data[key] = value.path
    return data

backup_data = {doc.id: serialize_firestore_doc(doc) for doc in docs}

# Backup JSON file save karo with `default=str`
with open("BackupsFirestore/courses.json", "w") as f:
    json.dump(backup_data, f, indent=4, default=str)
