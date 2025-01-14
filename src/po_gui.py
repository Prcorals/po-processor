import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import json
import threading
import fitz  # PyMuPDF for PDF rendering
from typing import Optional, Dict
from PIL import Image, ImageTk
from po_processor import POProcessor
from template_builder import TemplateBuilder

class POGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PO Processor")
        self.root.geometry("1200x800")
        
        # State variables
        self.current_file: Optional[Path] = None
        self.processing_thread: Optional[threading.Thread] = None
        self.processor: Optional[POProcessor] = None
        self.current_template = None
        self.pdf_doc = None
        self.current_page = 0
        
        self._load_config()
        self._load_templates()
        self._setup_styles()
        self._create_widgets()
        
    def _load_config(self):
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {
                'drive_folder_id': '',
                'bubble_api_key': '',
                'bubble_endpoint': ''
            }
            self._save_config()
            
    # Rest of the implementation...