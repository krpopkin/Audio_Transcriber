import sqlite3
import json
from google.cloud import storage
from datetime import timedelta
import time
import gradio_ui_transcribe
import gradio_ui_view_transcripts

# Configuration for the SQLite database and Google Cloud Storage
db_path = "transcriptions.db"
bucket_name = 'compliance-companion-transcription-prd'

# Initialize Google Cloud Storage client
storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)

# Helper function to create a new database connection
def get_db_connection():
    return sqlite3.connect(db_path)

# Functions to run "Transcribe" and "View Transcripts" directly
def run_transcribe():
    return gradio_ui_transcribe.create_gradio_interface()

def run_view_transcripts():
    return gradio_ui_view_transcripts.create_gradio_interface()

# Filter on selected title
def filter_titles(query=None):
    """Fetch and filter titles based on a search query."""
    connection = get_db_connection()
    try:
        query = f"%{query}%" if query else "%"
        sql_query = "SELECT title FROM transcriptions WHERE title LIKE ?"
        result = connection.execute(sql_query, (query,)).fetchall()
        return [row[0] for row in result]
    finally:
        connection.close()

# Get language and transcription
def fetch_language_and_transcript(title):
    """Fetches the signed audio link and language based on the title."""
    connection = get_db_connection()
    try:
        sql_query = "SELECT language, transcript_link FROM transcriptions WHERE title = ?"
        result = connection.execute(sql_query, (title,)).fetchone()
        if result:
            language, transcript = result
            return language, transcript
        return None, None
    finally:
        connection.close()

def load_transcription_details(title):
    """Fetches and returns language and transcription text for a given title."""
    language, transcription = fetch_language_and_transcript(title)
    return language, transcription