import tkinter as tk
from tkinter import ttk
from typing import Dict

class PreviewWindow(tk.Toplevel):
    def __init__(self, parent, po_data: Dict):
        super().__init__(parent)
        self.title("PO Preview")
        self.geometry("800x600")
        
        # Create main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # Create notebook for tabbed interface
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Summary tab
        self.summary_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.summary_frame, text="Summary")
        self._create_summary_tab(po_data)
        
        # Line Items tab
        self.items_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.items_frame, text="Line Items")
        self._create_line_items_tab(po_data)
        
        # Raw Data tab
        self.raw_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.raw_frame, text="Raw Data")
        self._create_raw_tab(po_data)
        
        # Add buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, pady=10)
        
        ttk.Button(
            button_frame,
            text="Process",
            command=self._on_process
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Close",
            command=self.destroy
        ).pack(side=tk.LEFT)

    def _create_summary_tab(self, po_data: Dict):
        """Create summary view with key PO information"""
        # Header
        header_frame = ttk.Frame(self.summary_frame)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(
            header_frame,
            text=f"PO Number: {po_data.get('po_number', 'N/A')}",
            font=('Helvetica', 12, 'bold')
        ).pack(side=tk.LEFT)
        
        # Key details in a grid
        details_frame = ttk.LabelFrame(self.summary_frame, text="Details", padding=10)
        details_frame.pack(fill=tk.X)
        
        details = [
            ("Vendor:", po_data.get('vendor', 'N/A')),
            ("Date:", po_data.get('date', 'N/A')),
            ("Total Amount:", f"${po_data.get('total_amount', 0):,.2f}"),
            ("Status:", po_data.get('status', 'New')),
            ("Payment Terms:", po_data.get('payment_terms', 'N/A')),
            ("Shipping Method:", po_data.get('shipping_method', 'N/A'))
        ]
        
        for i, (label, value) in enumerate(details):
            ttk.Label(details_frame, text=label).grid(row=i, column=0, sticky=tk.W, pady=2)
            ttk.Label(details_frame, text=value).grid(row=i, column=1, sticky=tk.W, pady=2, padx=10)

    def _create_line_items_tab(self, po_data: Dict):
        """Create table view of line items"""
        # Create treeview
        columns = ('item_no', 'description', 'quantity', 'unit_price', 'total')
        tree = ttk.Treeview(self.items_frame, columns=columns, show='headings')
        
        # Define column headings
        headings = {
            'item_no': 'Item #',
            'description': 'Description',
            'quantity': 'Qty',
            'unit_price': 'Unit Price',
            'total': 'Total'
        }
        
        for col, heading in headings.items():
            tree.heading(col, text=heading)
            tree.column(col, width=100)
        
        # Adjust description column width
        tree.column('description', width=300)
        
        # Insert line items
        for item in po_data.get('line_items', []):
            tree.insert('', tk.END, values=(
                item.get('item_no', ''),
                item.get('description', ''),
                item.get('quantity', ''),
                f"${item.get('unit_price', 0):,.2f}",
                f"${item.get('total', 0):,.2f}"
            ))
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.items_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack widgets
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def _create_raw_tab(self, po_data: Dict):
        """Create raw data view"""
        # Create text widget with scrollbar
        text_widget = tk.Text(
            self.raw_frame,
            wrap=tk.WORD,
            width=80,
            height=20
        )
        scrollbar = ttk.Scrollbar(self.raw_frame, orient=tk.VERTICAL, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        # Pack widgets
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Insert raw data
        import json
        text_widget.insert(tk.END, json.dumps(po_data, indent=2))
        text_widget.configure(state='disabled')

    def _on_process(self):
        """Handle process button click"""
        # You can implement this to trigger PO processing
        self.destroy()  # Close preview window after processing