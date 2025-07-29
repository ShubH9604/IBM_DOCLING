## 📄 IBM DocLing

We integrated [IBM DocLing](https://github.com/IBM/DocLing), an open-source document understanding tool, to extract structured data from PDFs and image-based documents. DocLing supports multiple backends and enrichment modules for:

- Layout understanding
- OCR (Optical Character Recognition)
- Table parsing
- Visual language models

### 🧪 Evaluation Summary

DocLing was tested on **50 unique bank statement formats** (Indian and international):

- ✅ **Fully Parsed Files**: 33 files were successfully and accurately parsed, with proper table and header extraction.
- ⚠️ **Minor Parsing Issues**: 16 files had small mismatches in row/column alignment, but overall structure was preserved.
- ❌ **Parsing Failure**: 1 file failed due to complex formatting (e.g., irregular layouts or embedded fonts).
- 🧠 **Header Recognition**: Detected and extracted header sections with high accuracy across all files.
- 💡 **Best Performance**: Excellent results on digitally generated PDFs with structured layouts.

📊 **Detailed report**: [Docling_Parsing_Report.xlsx](./Docling_Parsing_Report.xlsx)

### 🚧 Known Limitations

- Lacks custom training/tuning support in the open-source version.
- Struggles with:
  - Handwritten notes
  - Scanned documents
  - Stylized or irregular layouts

### ✅ Why DocLing?

DocLing proves to be a powerful tool for document parsing, especially effective for table-heavy formats like **bank statements**. It's ideal for structured, machine-readable PDFs in large-scale applications.
