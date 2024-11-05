from google.cloud import storage
import database_queries

# globals
storage_client = storage.Client()
bucket_name = 'compliance-companion-transcription-prd'
bucket = storage_client.get_bucket(bucket_name)
prefix = ''
page_size=100

from google.cloud import storage
import json

def retrieve_transcript(file_path):
    blob = bucket.blob(file_path)
    content = blob.download_as_text()
    transcript = json.loads(content)
    return transcript['original_text']

def search_for_transcription(search_string):
    # Search CS to see if the transcription results are there yet
    search_string = search_string.replace('Transcription started. Id is:','').replace('Transcription for ','').replace(' is in progress. Results not available yet','')
    blobs_iterator = bucket.list_blobs(prefix=prefix, max_results=page_size)

    # Manually handle pagination
    next_page_token = None
    while True:
        # Get the current page of blobs
        blobs = storage_client.list_blobs(bucket_name, prefix=prefix, max_results=page_size, page_token=next_page_token)
        
        # Convert the iterator to a list for easier manipulation
        blob_list = list(blobs)

        # Print all blob names and check for a match with the search string
        for blob in blob_list:
            if search_string in blob.name:
                transcript = retrieve_transcript(blob.name)
                database_queries.update_transcript_link(transcript, search_string)
                return transcript  # Return the first match

        # Check if there is a next page token
        next_page_token = blobs.next_page_token
        if not next_page_token:
            break  # Exit the loop when no more pages are available

    result = "Transcription for " + search_string + " is in progress. Results not available yet"
    return result
