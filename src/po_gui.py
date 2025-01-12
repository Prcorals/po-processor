import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import json
import threading
from typing import Optional, Dict
from po_processor import POProcessor
from google.oauth2.credentials import Credentials

class POGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PO Processor")
        self.root.geometry("800x600")
        
        # State variables
        self.current_file: Optional[Path] = None
        self.processing_thread: Optional[threading.Thread] = None
        self.processor: Optional[POProcessor] = None
        
        self._load_config()
        self._setup_styles()
        self._create_widgets()
        
    def _load_config(self):
        """Load configuration from config.json"""
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
    
    def _save_config(self):
        """Save configuration to config.json"""
        with open('config.json', 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def _setup_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.configure('Header.TLabel', font=('Helvetica', 16, 'bold'))
        style.configure('Settings.TLabelframe', padding=10)
    
    def _create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # File selection section
        self._create_file_section()
        
        # Preview section
        self._create_preview_section()
        
        # Progress section
        self._create_progress_section()
        
        # Settings button
        self.settings_btn = ttk.Button(
            self.main_frame,
            text="Settings",
            command=self._show_settings
        )
        self.settings_btn.grid(row=3, column=0, pady=10)
        
    def _create_file_section(self):
        """Create file selection widgets"""
        # File selection frame
        file_frame = ttk.LabelFrame(
            self.main_frame,
            text="File Selection",
            padding=10
        )
        file_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # File path display
        self.file_path_var = tk.StringVar(value="No file selected")
        ttk.Label(
            file_frame,
            textvariable=self.file_path_var,
            wraplength=500
        ).pack(side=tk.LEFT, expand=True)
        
        # Browse button
        ttk.Button(
            file_frame,
            text="Browse",
            command=self._browse_file
        ).pack(side=tk.RIGHT)
        
        # Process button
        self.process_btn = ttk.Button(
            file_frame,
            text="Process PO",
            command=self._process_po,
            state=tk.DISABLED
        )
        self.process_btn.pack(side=tk.RIGHT, padx=5)
    
    def _create_preview_section(self):
        """Create preview widgets"""
        preview_frame = ttk.LabelFrame(
            self.main_frame,
            text="Preview",
            padding=10
        )
        preview_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Preview text
        self.preview_text = tk.Text(
            preview_frame,
            height=10,
            width=70,
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.preview_text.pack(expand=True, fill=tk.BOTH)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(
            preview_frame,
            orient=tk.VERTICAL,
            command=self.preview_text.yview
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.preview_text['yscrollcommand'] = scrollbar.set
    
    def _create_progress_section(self):
        """Create progress tracking widgets"""
        progress_frame = ttk.LabelFrame(
            self.main_frame,
            text="Progress",
            padding=10
        )
        progress_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            length=300,
            mode='determinate',
            variable=self.progress_var
        )
        self.progress_bar.pack(expand=True, fill=tk.X)
        
        # Status label
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(
            progress_frame,
            textvariable=self.status_var
        )
        self.status_label.pack()
    
    def _show_settings(self):
        """Show settings dialog"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("400x300")
        
        frame = ttk.Frame(settings_window, padding=10)
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Google Drive folder ID
        ttk.Label(frame, text="Drive Folder ID:").grid(row=0, column=0, sticky=tk.W)
        drive_folder_entry = ttk.Entry(frame, width=40)
        drive_folder_entry.insert(0, self.config['drive_folder_id'])
        drive_folder_entry.grid(row=0, column=1, pady=5)
        
        # Bubble.io settings
        ttk.Label(frame, text="Bubble API Key:").grid(row=1, column=0, sticky=tk.W)
        bubble_key_entry = ttk.Entry(frame, width=40)
        bubble_key_entry.insert(0, self.config['bubble_api_key'])
        bubble_key_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Bubble Endpoint:").grid(row=2, column=0, sticky=tk.W)
        bubble_endpoint_entry = ttk.Entry(frame, width=40)
        bubble_endpoint_entry.insert(0, self.config['bubble_endpoint'])
        bubble_endpoint_entry.grid(row=2, column=1, pady=5)
        
        def save_settings():
            self.config.update({
                'drive_folder_id': drive_folder_entry.get(),
                'bubble_api_key': bubble_key_entry.get(),
                'bubble_endpoint': bubble_endpoint_entry.get()
            })
            self._save_config()
            settings_window.destroy()
            messagebox.showinfo("Success", "Settings saved successfully!")
        
        ttk.Button(
            frame,
            text="Save",
            command=save_settings
        ).grid(row=3, column=0, columnspan=2, pady=20)
    
    def _browse_file(self):
        """Open file browser dialog"""
        filepath = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")]
        )
        if filepath:
            self.current_file = Path(filepath)
            self.file_path_var.set(self.current_file.name)
            self.process_btn['state'] = tk.NORMAL
            self._preview_file()
    
    def _preview_file(self):
        """Show preview of selected file"""
        if not self.current_file:
            return
            
        try:
            # Initialize processor if needed
            if not self.processor:
                # You'll need to implement credentials handling
                credentials = Credentials.from_authorized_user_file('token.json')
                self.processor = POProcessor(credentials, self.config['drive_folder_id'])
            
            # Extract data for preview
            po_data = self.processor.extract_po_data(self.current_file)
            
            # Update preview text
            self.preview_text['state'] = tk.NORMAL
            self.preview_text.delete(1.0, tk.END)
            self.preview_text.insert(tk.END, json.dumps(po_data, indent=2))
            self.preview_text['state'] = tk.DISABLED
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to preview file: {str(e)}")
    
    def _process_po(self):
        """Process the selected PO file"""
        if not self.current_file or not self.processor:
            return
            
        def process_thread():
            try:
                self.status_var.set("Processing...")
                self.progress_var.set(0)
                self.process_btn['state'] = tk.DISABLED
                
                # Process file
                success = self.processor.process_po(self.current_file)
                
                # Update UI
                self.root.after(0, lambda: self._update_status(
                    "Success!" if success else "Failed",
                    100 if success else 0
                ))
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    "Error",
                    f"Failed to process PO: {str(e)}"
                ))
            finally:
                self.root.after(0, lambda: self._enable_processing())
        
        # Start processing in background
        self.processing_thread = threading.Thread(target=process_thread)
        self.processing_thread.start()
    
    def _update_status(self, status: str, progress: float):
        """Update status and progress bar"""
        self.status_var.set(status)
        self.progress_var.set(progress)
    
    def _enable_processing(self):
        """Re-enable processing button"""
        self.process_btn['state'] = tk.NORMAL

def main():
    root = tk.Tk()
    app = POGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()