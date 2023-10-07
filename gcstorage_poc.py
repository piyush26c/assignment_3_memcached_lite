from google.cloud import storage
import json

def create_bucket(bucket_name):
    # Create a client for interacting with the GCP Storage API, using the ServiceAccount key file
    gcsclient = storage.Client.from_service_account_json('piyush-chaudhari-fall2023-9600b4eeb5b1.json')
    # Creates the new bucket
    bucket = gcsclient.create_bucket(bucket_name, location='US-EAST1')
    print(f"Bucket {bucket.name} created.")


def upload_file(bucket_name):
    # Create a client for interacting with the GCP Storage API, using the ServiceAccount key file
    gcsclient = storage.Client.from_service_account_json('piyush-chaudhari-fall2023-9600b4eeb5b1.json')
    # Create a bucket object
    bucket = gcsclient.bucket(bucket_name)
    # Set the name of the file you want to upload
    file_name = 'key_value.json'
    # Create a blob object from the file
    blob = bucket.blob(file_name)
    # Read the contents of the file
    with open(file_name, 'rb') as f:
        contents = f.read()
    # Upload the file to the bucket
    blob.upload_from_string(contents)
    print(f'File {file_name} uploaded to {blob.public_url}')

def read_file(bucket_name):
    # Read the data from Google Cloud Storage
    read_storage_client = storage.Client.from_service_account_json('piyush-chaudhari-fall2023-9600b4eeb5b1.json')

    # Set buckets and filenames
    filename = "key_value.json"

    # get bucket with name
    bucket = read_storage_client.get_bucket(bucket_name)

    # get bucket data as blob
    blob = bucket.get_blob(filename)

    # convert to string
    json_data_string = blob.download_as_string()
    print(json_data_string)
    json_data = json.loads(json_data_string.decode("utf-8"))

    print(type(json_data))
    print(json_data)
    json_data["key2"] = "piyushnekiyahaichange1"
    read_storage_client.get_bucket(bucket_name).blob(filename).upload_from_string(json.dumps(json_data, indent=4).encode("utf-8"))
    print("Update operation successful.")

if __name__ == "__main__":
    # The name for the new bucket
    bucket_name = "eccassignment3_bucket"
    
    # create_bucket(bucket_name)
    # upload_file(bucket_name=bucket_name)
    read_file(bucket_name=bucket_name)