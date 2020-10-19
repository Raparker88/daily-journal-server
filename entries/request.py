import sqlite3
import json
from models import Entry, Mood



def get_all_entries(value=""):
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        if len(value) > 0:
            db_cursor.execute("""
            SELECT
                e.id,
                e.date,
                e.entry,
                e.mood_id,
                e.concepts,
                m.label
            FROM entries e
            JOIN Moods m ON e.mood_id = m.id
            WHERE e.entry LIKE ?
            """, ('%' + value + '%', ))
        else:
            db_cursor.execute("""
            SELECT
                e.id,
                e.date,
                e.entry,
                e.mood_id,
                e.concepts,
                m.label
            FROM entries e
            JOIN Moods m ON e.mood_id = m.id
            """)

        # Initialize an empty list to hold all location representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            entry = Entry(row['id'], row['date'], row['entry'], row['mood_id'], row['concepts'])
            mood = Mood("", row['label'])
            entry.mood = mood.__dict__

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)

# Function with a single parameter
def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.entry,
            e.mood_id,
            e.concepts,
            m.label
        FROM entries e
        JOIN Moods m ON e.mood_id = m.id
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entry(data['id'], data['date'], data['entry'], data['mood_id'], data['concepts'])
        mood = Mood('', data['label'])
        entry.mood = mood.__dict__

        return json.dumps(entry.__dict__)

def create_entry(entry):

    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entries
            ( date, entry, mood_id, concepts )
        VALUES
            ( ?, ?, ?, ?);
        """, (entry['date'], entry['entry'],
              entry['moodId'], entry['concept'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        entry['id'] = id


    return json.dumps(entry)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Entries
        WHERE id = ?
        """, (id, ))

        
def update_entry(id, new_entry):

    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Entries
            SET
                date = ?,
                entry = ?,
                mood_id = ?,
                concepts = ?
        WHERE id = ?
        """, (new_entry['date'], new_entry['entry'],
              new_entry['moodId'], new_entry['concept'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True