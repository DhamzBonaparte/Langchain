from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
# Sample Markdown Template

## Overview
This is a test markdown snippet designed to help you verify formatting, headings, and code blocks.

---

## Code Example
Here is how you write a simple function in Python:

\`\`\`python
def greet(name):
    return f"Hello, {name}!"

print(greet("Tester"))
\`\`\`

---

## Features Checklist
* **Clean Formatting:** Uses proper headings and lists.
* **Code Blocks:** Fully syntax-highlighted and easy to copy.
* **Separation:** Uses horizontal rules to keep sections distinct.
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN, chunk_size=200, chunk_overlap=0
)

res = splitter.split_text(text)
print(len(res))
print(res[0])
