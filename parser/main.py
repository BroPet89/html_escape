from bs4 import BeautifulSoup
import simplejson as json
import bs4
import re


with open(r'C:\dev\WealthifyMainV2\src\services\CashSavings\templates\statements\template.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

doctype_tag = soup.find(text=lambda text: isinstance(text, bs4.Doctype))
if doctype_tag:
    doctype_string = str(doctype_tag)
    doctype_tag.extract()
    soup.insert(0, doctype_string)


def encode_to_json(soup):

    html_string = str(soup)

    # Encode the HTML string to JSON format
    encoded_json = json.JSONEncoderForHTML().encode(html_string)

    return encoded_json


def escape_special_characters_for_json(text):

    text = text.replace('"', '\\"')

    # Escape forward slash in HTML end tags
    text = text.replace('</', '<\\/')

    # Add a space between the tag name and the slash on self-closing tags
    text = re.sub(r'(<\w+)\s*\/>', r'\1 />', text)

    # Encode quotation marks within HTML content
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    return text


# Find all elements with text content and escape special characters for JSON
for element in soup.find_all(text=True):
    element.replace_with(escape_special_characters_for_json(element))

html_content_single_line = soup.prettify().replace('\n', '').replace('  ', '')

output_file_path = r'C:\dev\WealthifyMainV2\src\services\CashSavings\templates\statements\modified_template.html'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(html_content_single_line)

print(f"Modified HTML content has been written to {output_file_path}")
