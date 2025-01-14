import tkinter as tk
from tkinter import ttk, messagebox
import json
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image, ImageTk

class TemplateBuilder:
    def __init__(self, parent, pdf_path):
        self.window = tk.Toplevel(parent)
        self.window.title("Template Builder")
        self.window.geometry("1200x800")
        
        self.pdf_path = pdf_path
        self.current_page = 0
        self.fields = {}
        self.selection_start = None
        self.template_name = tk.StringVar()
        
        self._load_templates()
        self._create_widgets()
        self._load_pdf()
        
    # Rest of the implementation...