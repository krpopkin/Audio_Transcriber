#Miscellaneous queries to manage database
import sqlite3

#Database columns
def get_column_names():
    conn = sqlite3.connect('transcriptions.db')
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA table_info(transcriptions);")
    columns = [column[1] for column in cursor.fetchall()]
    
    conn.close()
    print(columns)

# Create a sqlite database
def create_database():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS transcriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        language TEXT NOT NULL,
        external_request_id TEXT,
        audio_link TEXT,
        transcript_link TEXT,
        entered_on DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    '''
    connection = sqlite3.connect('transcriptions.db')
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()
    print("Database and table created successfully.")

#update database
def update_database(title, language, external_request_id, audio_link, transcript_link):
    connection = sqlite3.connect('transcriptions.db')
    cursor = connection.cursor()

    insert_query = '''
    INSERT INTO transcriptions (title, language, external_request_id, audio_link, transcript_link)
    VALUES (?, ?, ?, ?, ?);
    '''

    record = (title, language, external_request_id, audio_link, transcript_link)
    cursor.execute(insert_query, record)
    connection.commit()
    connection.close()

#update specific row in the database
import sqlite3

def update_transcript_link(transcript_link, external_request_id):
    # Connect to the SQLite database
    connection = sqlite3.connect('transcriptions.db')
    cursor = connection.cursor()
    
    # Update the transcript_link field where external_request_id matches the provided parameter
    update_query = '''
    UPDATE transcriptions
    SET transcript_link = ?
    WHERE external_request_id = ?;
    '''
    
    cursor.execute(update_query, (transcript_link, external_request_id))
    connection.commit()
    connection.close()
    print(f"Transcript link updated successfully for external_request_id: {external_request_id}")

#get all records
def get_all_records():
    query_string = "SELECT * FROM transcriptions;"
    
    connection = sqlite3.connect('transcriptions.db')
    cursor = connection.cursor()
    cursor.execute(query_string)
    records = cursor.fetchall()
    
    # Print the records
    if records:
        for record in records:
            print(record)
    else:
        print("No records found in the transcriptions table.")
    
    connection.close()

#delete all records
def delete_all_records():
    connection = sqlite3.connect('transcriptions.db')
    cursor = connection.cursor()
    delete_query = 'DELETE FROM transcriptions;'
    cursor.execute(delete_query)
    connection.commit()
    print(f"{cursor.rowcount} records deleted.")
    connection.close()

import sqlite3

def delete_record_by_external_request_id(external_request_id):
    # Connect to the SQLite database
    connection = sqlite3.connect('transcriptions.db')
    cursor = connection.cursor()

    # Define the delete query
    delete_query = '''
    DELETE FROM transcriptions
    WHERE external_request_id = ?;
    '''

    # Execute the delete query
    cursor.execute(delete_query, (external_request_id,))
    connection.commit()
    connection.close()

    print(f"Record with external_request_id = '{external_request_id}' deleted successfully.")

#add a column
def add_transcript_link_column():
    connection = sqlite3.connect('transcriptions.db')
    cursor = connection.cursor()
    
    # Add the new column 'transcript_link' to the 'transcriptions' table
    alter_table_query = '''
    ALTER TABLE transcriptions
    ADD COLUMN transcript_link TEXT;
    '''
    
    cursor.execute(alter_table_query)
    connection.commit()
    connection.close()
    print("Column 'transcript_link' added successfully.")


if __name__ == '__main__':
    #create_database()
    #update_database('test upload', 'Spanish', 'KenP-4567')
    #delete_all_records()
    delete_record_by_external_request_id("kenp-8739")
    get_all_records()
    #get_column_names()