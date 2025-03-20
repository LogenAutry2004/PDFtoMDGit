# Markdown to PDF Converter with GitHub Integration

This script automates the process of:
1. Cloning or updating a private GitHub repository.
2. Searching a specified folder (including subdirectories) for Markdown (`.md`) files.
3. Converting all Markdown files to PDFs while maintaining the folder structure.
4. Applying CSS styling to ensure proper formatting of bullet points, headings, and inline code.

## Features
- Automatically clones or updates a private GitHub repository
- Recursively scans all subdirectories for Markdown files
- Converts Markdown files to PDFs while maintaining the folder structure
- Applies custom CSS to improve the appearance of the generated PDFs
- Uses environment variables for secure GitHub authentication
- Implements error handling to prevent script failures

## Prerequisites
Ensure you have Python 3 installed. Install the required dependencies using:

```bash
pip install -r requirements.txt
```