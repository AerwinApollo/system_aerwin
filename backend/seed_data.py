import sqlite3
import os

DB_FILE = "system_aerwin/database/tracking_app.db"

# Ensure the database file exists before inserting data
if not os.path.exists(DB_FILE):
    print("❌ Error: Database file not found! Run database.py first.")
    exit()

# Connect to database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Insert test user
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Aerwin", "aerwin@example.com"))

# Insert test daily tracking entry
cursor.execute("""
    INSERT INTO daily_tracking (user_id, date, physical_status, spiritual_status, mental_status, emotional_status, energy_level, emotional_stability, mental_clarity, daily_reflection)
    VALUES (1, '2025-03-12', 'Done', 'Done', 'Skipped', 'Partial', 8, 7, 9, 'Felt pretty good today, had a great workout.')
""")

conn.commit()
conn.close()

print("✅ Test data inserted into database!")
