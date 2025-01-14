# PO Processor

A Python application for processing and extracting data from purchase orders (POs) using customizable templates.

## Features

- 📄 PDF Purchase Order processing
- 🎯 Visual template creation - point and click to select fields
- 🔧 Customizable field extraction
- 📊 Data validation and preprocessing
- 💾 Export to multiple formats
- 🔄 Google Drive integration
- 🎨 User-friendly GUI interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Prcorals/po-processor.git
cd po-processor
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Google Drive credentials (optional):
   - Go to Google Cloud Console
   - Create a new project
   - Enable Drive API
   - Create OAuth 2.0 credentials
   - Download and save as `credentials.json`

## Usage

1. Start the application:
```bash
python src/po_gui.py
```

2. Create a template:
   - Click "Create New Template"
   - Load a sample PO
   - Click and drag to select fields
   - Configure field properties
   - Save template

3. Process POs:
   - Select a PDF file
   - Choose the appropriate template
   - Click "Process PO"
   - Review extracted data
   - Export or upload to Drive

## Templates

Templates can be created visually using the Template Builder. For each field you can specify:

- Field type (text, number, date, table)
- Position on page
- Validation rules
- Preprocessing options
- Custom extraction logic

Example template structure:
```json
{
  "name": "Sample Template",
  "fields": {
    "po_number": {
      "type": "text",
      "page": 0,
      "x1": 100,
      "y1": 100,
      "x2": 200,
      "y2": 120,
      "required": true
    }
  }
}
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.