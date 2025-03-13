import sqlite3
import os

# Ensure database directory exists
DB_DIR = "system_aerwin/database"
os.makedirs(DB_DIR, exist_ok=True)

# Define the correct database path
DB_FILE = os.path.join(DB_DIR, "tracking_app.db")

# Connect to SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# SQL schema
SCHEMA = """
-- USERS TABLE
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DAILY TRACKING TABLE (Logs habit tracking data)
CREATE TABLE IF NOT EXISTS daily_tracking (
    tracking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    date DATE NOT NULL UNIQUE,
    physical_status TEXT CHECK(physical_status IN ('Done', 'Skipped', 'Partial')),
    spiritual_status TEXT CHECK(spiritual_status IN ('Done', 'Skipped', 'Partial')),
    mental_status TEXT CHECK(mental_status IN ('Done', 'Skipped', 'Partial')),
    emotional_status TEXT CHECK(emotional_status IN ('Done', 'Skipped', 'Partial')),
    energy_level INTEGER CHECK(energy_level BETWEEN 1 AND 10),
    emotional_stability INTEGER CHECK(emotional_stability BETWEEN 1 AND 10),
    mental_clarity INTEGER CHECK(mental_clarity BETWEEN 1 AND 10),
    daily_reflection TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

-- STREAKS TABLE (Tracks longest and current streaks)
CREATE TABLE IF NOT EXISTS streaks (
    streak_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    longest_streak INTEGER DEFAULT 0,
    current_streak INTEGER DEFAULT 0,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);
"""

# Execute schema creation
cursor.executescript(SCHEMA)
conn.commit()
conn.close()

print(f"✅ Database initialized at {DB_FILE}!")
