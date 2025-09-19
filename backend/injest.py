import sqlite3

from .config import SQLITE_PATH

def _db():
    conn = sqlite3.connect(SQLITE_PATH)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS docs(
        doc_id TEXT PRIMARY KEY,
        kind TEXT,
        title TEXT
    )""")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS chunks(
        doc_id TEXT,
        chunk_id INTEGER,
        text TEXT,
        start_line INTEGER,
        end_line INTEGER,
        PRIMARY KEY(doc_id, chunk_id)
    )""")
    conn.commit()
    return conn