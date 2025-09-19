import sqlite3
from typing import List, Tuple, Dict
from pathlib import Path
import re

from pypdf import PdfReader

from .config import SQLITE_PATH

# -- database metadata --
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

# -- pdf/text extraction --
def extract_text_pdf(pdf_bytes: bytes) -> str:
    reader = PdfReader(io_bytes:=__import__("io").BytesIO(pdf_bytes))
    out = []
    for page in reader.pages:
        out.append(page.extract_text() or "")
    return "\n".join(out)

def normalize_whitespace(s: str) -> str:
    return re.sub(r"[ \t]+", " ", s).strip()