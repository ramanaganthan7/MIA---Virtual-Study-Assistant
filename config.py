"""
Configuration settings for MIA – Virtual Study Assistant
"""
import os
from dotenv import load_dotenv

load_dotenv()

# UI Configuration
PAGE_TITLE = "MIA – Study Assistant"
PAGE_ICON = "🤖"
LAYOUT = "wide"
SIDEBAR_STATE = "expanded"

# File Processing
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
CHROMA_COLLECTION_NAME = "mia-chroma"
CHROMA_PERSIST_DIR = "./.chroma"

# Model Configuration
LLM_TEMPERATURE = 0
TAVILY_SEARCH_RESULTS = 2

# Supported Extensions
SUPPORTED_EXTENSIONS = [
    "pdf", "docx", "doc", "csv", "xlsx", "xls",
    "txt", "md", "py", "js", "html", "xml"
]

# UI Messages
UPLOAD_PLACEHOLDER_TITLE = "📤 Throw the Files to MIA so She Can Learn!"
UPLOAD_PLACEHOLDER_TEXT = "MIA will analyse your material and help you prepare for exams."
QUESTION_PLACEHOLDER = "What is the important questions in this document?"
# File Categories
FILE_CATEGORIES = {
    "📄 Documents": ["PDF (.pdf)", "Word (.docx, .doc)", "Text (.txt, .md)"],
    "📊 Data Files": ["Excel (.xlsx, .xls)", "CSV (.csv)"],
    "💻 Code Files": ["Python (.py)", "JavaScript (.js)", "HTML (.html)", "XML (.xml)"]
}
