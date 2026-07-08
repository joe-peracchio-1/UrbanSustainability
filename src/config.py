import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
DUCKDB_PATH = DATA_DIR / "duckdb" / "sustainability.duckdb"
QDRANT_PATH = DATA_DIR / "qdrant"
RAW_DOCS_DIR = DATA_DIR / "raw_docs"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "urban-sustainability-agent")

WALKSCORE_API_KEY = os.getenv("WALKSCORE_API_KEY")
EPA_AQS_API_EMAIL = os.getenv("EPA_AQS_API_EMAIL")
EPA_AQS_API_KEY = os.getenv("EPA_AQS_API_KEY")
EIA_API_KEY = os.getenv("EIA_API_KEY")
NREL_API_KEY = os.getenv("NREL_API_KEY")
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
