# PO Processor

A Python application for extracting data from purchase orders (POs) using visual field selection.

## Features

- 📄 Visual PDF viewer with navigation
- 🖱️ Click-and-drag field selection
- 📝 Multiple field types support (text, number, date, currency)
- 💾 Template saving and loading
- 📤 Data extraction and export

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Prcorals/po-processor.git
cd po-processor
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python src/po_gui.py
```

2. Using the Application:
   - Click "Open PDF" to load your purchase order
   - Navigate pages using Previous/Next buttons
   - Click and drag to select fields
   - Name each field and choose its type
   - See extracted data in the right panel

3. Field Selection:
   - Click and drag on the PDF to select a field
   - Enter field name in the popup dialog
   - Choose field type:
     - text: General text content
     - number: Numeric values
     - date: Date values
     - currency: Monetary values

4. Field Management:
   - Selected fields appear as blue boxes on the PDF
   - Extracted values show in the right panel
   - Right-click fields to edit or delete them

## Dependencies

- PyMuPDF (fitz)
- tkinter
- Pillow
- pandas

## Quick Start

1. Load a PDF:
   - Click "Open PDF"
   - Select your purchase order document
   - PDF will display in main window

2. Select Fields:
   - Click and drag to select a field
   - Enter field name and type
   - Selected fields are highlighted in blue
   - Extracted text appears in right panel

3. Navigate:
   - Use Previous/Next buttons to change pages
   - Fields are preserved across pages
   - Right panel shows all extracted data