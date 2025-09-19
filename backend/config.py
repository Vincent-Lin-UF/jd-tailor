import os
from pathlib import Path

INDEX_DIR = Path(os.getenv("INDEX_DIR", ".data"))
SQLITE_PATH = Path(os.getenv("SQLITE_PATH", ".data/meta.db"))
USE_QDRANT = os.getenv("USE_QDRANT", "false").lower == "true"
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")

INDEX_DIR.mkdir(parents=True, exist_ok=True)