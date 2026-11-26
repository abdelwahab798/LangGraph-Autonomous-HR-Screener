import fitz
from pathlib import Path
from typing import List
from src.core.logger import get_logger

logger = get_logger("PDFParser")

def extract_text_from_pdf(pdf_path: str | Path) -> str:
    """Extracts clean text from a single PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text_pages = []
        for page in doc:
            text_pages.append(page.get_text("text"))
        doc.close()
        
        full_text = "\n".join(text_pages).strip()
        return full_text
    except Exception as e:
        logger.error(f"Failed to parse PDF {pdf_path}: {e}")
        raise e

def load_cvs_from_folder(folder_path: str | Path) -> List[str]:
    """Reads all PDF CVs in a folder and returns a list of extracted texts."""
    folder = Path(folder_path)
    cvs_texts: List[str] = []
    
    for pdf_file in sorted(folder.glob("*.pdf")):
        logger.info(f"Extracting text from: {pdf_file.name}")
        text = extract_text_from_pdf(pdf_file)
        if text:
            cvs_texts.append(text)
            
    logger.info(f"Successfully loaded {len(cvs_texts)} CVs.")
    return cvs_texts