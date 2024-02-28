from bs4 import BeautifulSoup
import json
import re

# Open the HTML file in read mode
with open(r'C:\dev\WealthifyMainV2\src\services\CashSavings\templates\statements\template.html', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    html_content = file.read()

# Define a function to escape special characters
def escape_special_characters(text):
    escaped_text = re.sub(r'(["\'\\])', r'\\\1', text)
    return escaped_text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements with text content and escape special characters
for element in soup.find_all(text=True):
    element.replace_with(escape_special_characters(element))

# Print the modified HTML content
print(soup.prettify())