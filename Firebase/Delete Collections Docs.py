import firebase_admin
from firebase_admin import credentials, firestore
import json
from google.cloud.firestore import DocumentSnapshot, SERVER_TIMESTAMP
from google.cloud.firestore import DocumentReference
import firebase_admin
from firebase_admin import credentials, firestore
import json

COLLECTION_NAME = "courses"
DOCUMENT_TO_KEEP = "unIn0R1mxxB6x6dQFonD"  # Is document ko delete nahi karna

if not firebase_admin._apps:
        cred = credentials.Certificate("careerustaad-staging-firebase-adminsdk-fbsvc-43e41f3d55.json")
        firebase_admin.initialize_app(cred, {"storageBucket": "careerustaad-staging.firebasestorage.app"})

db = firestore.client()

# 🔥 Collection ke sare documents fetch karo
docs = db.collection(COLLECTION_NAME).stream()

for doc in docs:
    if doc.id != DOCUMENT_TO_KEEP:  # Agar ye specific document nahi hai, tabhi delete karo
        doc.reference.delete()
        print(f"🗑️ Deleted document: {doc.id}")
print("✅ All documents deleted except the specified one!")
