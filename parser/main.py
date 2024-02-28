from bs4 import BeautifulSoup
import re

# Open the HTML file in read mode
with open(r'C:\dev\WealthifyMainV2\src\services\CashSavings\templates\statements\template.html', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    html_content = file.read()

# Define a function to escape special characters
def escape_special_characters(text):
    # Escape backslashes and double quotes for JavaScript strings
    escaped_text = text.replace('\\', '\\\\').replace('"', '\\"')
    return escaped_text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements with text content and escape special characters
for element in soup.find_all(text=True):
    element.replace_with(escape_special_characters(element))

# Write the modified HTML content to a new file
output_file_path = r'C:\dev\WealthifyMainV2\src\services\CashSavings\templates\statements\modified_template.html'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(soup.prettify())

print(f"Modified HTML content has been written to {output_file_path}")
