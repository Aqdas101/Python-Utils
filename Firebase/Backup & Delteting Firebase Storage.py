from firebase_admin import credentials, storage, firestore

import firebase_admin
import os

if not firebase_admin._apps:
        cred = credentials.Certificate("careerustaad-staging-firebase-adminsdk-fbsvc-43e41f3d55.json")
        firebase_admin.initialize_app(cred, {"storageBucket": "careerustaad-staging.firebasestorage.app"})


bucket = storage.bucket()

# 🔹 Backup directory ensure karein
backup_folder = "BackupsFirestore\images"
os.makedirs(backup_folder, exist_ok=True)

blobs = bucket.list_blobs(prefix="images/")

for blob in blobs:
    if blob.name.startswith("images/tmp"):  # Sirf "temp_" wali images download karni hain
        filename = os.path.join(backup_folder, os.path.basename(blob.name))
        blob.download_to_filename(filename)
        print(f"✅ Downloaded: {filename}")

        # Ab delete bhi karna hai
        blob.delete()
        print(f"❌ Deleted: {blob.name}")

print("🎉 Backup & Delete Complete!")

# 🔹 Storage ke sare files list karein
