import os
import git
import markdown
from weasyprint import HTML

# Configuration
GITHUB_USERNAME = "yourusernname"  # Replace with your GitHub username
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # 🔹 Uses an environment variable (secure)
GITHUB_REPO_URL = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/yourgit.git"

LOCAL_REPO_DIR = "repo_clone"
MARKDOWN_FOLDER = "windows"  # Folder inside the repo containing .md files
OUTPUT_FOLDER = "pdf_output"

# Clone or update the repository
if os.path.exists(LOCAL_REPO_DIR):
    repo = git.Repo(LOCAL_REPO_DIR)
    repo.remotes.origin.pull()
else:
    git.Repo.clone_from(GITHUB_REPO_URL, LOCAL_REPO_DIR)

# Ensure the output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# CSS Styling for Bullet Points & Headings in PDFs
custom_css = """
<style>
    body { font-family: Arial, sans-serif; line-height: 1.5; margin: 20px; }
    h1, h2, h3 { color: #333; }
    ul, ol { margin: 10px 0; padding-left: 20px; }
    li { margin-bottom: 5px; }
    code { font-family: monospace; background: #f4f4f4; padding: 2px 5px; }
</style>
"""

# Convert Markdown files to PDFs (including subfolders)
markdown_dir = os.path.join(LOCAL_REPO_DIR, MARKDOWN_FOLDER)

for root, _, files in os.walk(markdown_dir):
    for file in files:
        if file.endswith(".md"):
            md_path = os.path.join(root, file)

            try:
                # Read markdown content
                with open(md_path, "r", encoding="utf-8") as f:
                    md_content = f.read()

                # Convert markdown to HTML (with proper list support)
                html_content = markdown.markdown(md_content, extensions=["extra"])

                # Define output path while maintaining folder structure
                relative_path = os.path.relpath(root, markdown_dir)
                output_dir = os.path.join(OUTPUT_FOLDER, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                pdf_filename = os.path.splitext(file)[0] + ".pdf"
                pdf_path = os.path.join(output_dir, pdf_filename)

                # Convert HTML to PDF with CSS styling
                HTML(string=f"{custom_css}{html_content}").write_pdf(pdf_path)

                print(f"✅ Converted {md_path} -> {pdf_path}")

            except Exception as e:
                print(f"❌ Error converting {md_path}: {e}")

print("🎉 All Markdown files have been converted to PDFs.")
