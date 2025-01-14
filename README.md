# PO Processor

A Python application for processing purchase orders (POs) with visual field selection.

## Features

- Visual field selection from PDFs
- Data extraction with multiple field types
- Template saving and loading
- Support for text, numbers, dates, and currency

## Installation

```bash
# Clone the repository
git clone https://github.com/Prcorals/po-processor.git
cd po-processor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python src/po_gui.py
```

2. Load a PDF:
   - Click 'Open PDF'
   - Select your PO document

3. Select fields:
   - Selection mode is enabled by default
   - Click and drag on the PDF to select fields
   - Enter field name and type

4. Process data:
   - View extracted data in the right panel
   - Save templates for reuse

## Contributing

Pull requests are welcome. For major changes, please open an issue first.