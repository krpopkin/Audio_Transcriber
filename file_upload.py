#Upload file selected on local drive to Cloud Storage

from google.cloud import storage

#Globals
client = storage.Client()
bucket_name = "kenp-transcriber-tool"
bucket = client.get_bucket(bucket_name)
uploaded_file_name = None

# Upload the file to Cloud Storage
def upload_file(file):
    #upload to CS
    file_name = f"uploads/{file.name.split('/')[-1]}"  #destination bucket and folder
    uploaded_file_name = file_name
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file.name)
    return file_name