import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Optional, Callable

class FieldConfigDialog:
    def __init__(self, parent, field_data: Optional[Dict] = None):
        self.window = tk.Toplevel(parent)
        self.window.title("Configure Field")
        self.window.geometry("400x500")
        self.window.transient(parent)
        
        self.field_data = field_data or {}
        self.result = None
        
        self._create_widgets()
        
    # Rest of the implementation...