from fileinput import filename
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("major-project-17a89-firebase-adminsdk-0qkgt-f38c07ef81.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'major-project-17a89.appspot.com'
})

bucket = storage.bucket()
blob = bucket.blob("img")
blob.upload_from_filename(filename="example.jpg")
blob.make_public()
print(blob.public_url)