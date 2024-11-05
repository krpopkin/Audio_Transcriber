"""
This script submits an audio or video for transcription.  

Key Links:
Input file: https://console.cloud.google.com/storage/browser/kenp-transcriber-tool/uploads?project=amw-compliance-companion-prd&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))
API: https://compliance-companion-ml-api-568357518051.us-east4.run.app/docs#/default/transcribe_v1_v1_ml_transcription_post
Pipeline: https://console.cloud.google.com/vertex-ai/pipelines/runs?project=amw-compliance-companion-prd
Transcription Results bucket: https://console.cloud.google.com/storage/browser/compliance-companion-transcription-prd;tab=objects?project=amw-compliance-companion-prd&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&prefix=&forceOnObjectsSortingFiltering=true
"""

import requests
import uuid
import json
import numpy as np
import database_queries
import sqlite3

#globals
bucket_name = "kenp-transcriber-tool"

def get_unique_id():
    #query to obtain id's already used
    query_string = "SELECT external_request_id FROM transcriptions;"
    connection = sqlite3.connect('transcriptions.db')
    cursor = connection.cursor()
    cursor.execute(query_string)
    records = cursor.fetchall()
    
    #create unique id
    existing_ids = {x[0] for x in records}
    while True:
        external_request_id = "kenp-" + str(np.random.randint(1, 10000))
        if external_request_id not in existing_ids:
            break  

    return external_request_id   

# Transcription request
def call_cc_transcription_api(uploaded_file, language):
    url = "https://compliance-companion-ml-api-568357518051.us-east4.run.app/v1/ml/transcription"

    external_request_id = get_unique_id()

    media_uri = 'gs://' + bucket_name + '/' + uploaded_file
    
    data = {
        "request_context": 
        {
            "external_request_id": external_request_id,
            "callback_url": "",
            "api_request_id": ""
        },
        "media_uri": media_uri,
        "specified_language": language
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        
    except requests.exceptions.RequestException as e:
        # Catch any request errors and print them
        print(f"An error occurred: {e}")

    results = 'Transcription started. Id is:' + str(external_request_id)
    
    #update transcription database
    audio_link = 'gs://kenp-transcriber-tool/' + uploaded_file
    transcript_link = ''
    database_queries.update_database(uploaded_file, language, external_request_id, audio_link, transcript_link)

    return results

# Main
# if __name__ == "__main__":
#     call_cc_transcription_api()