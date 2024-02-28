from bs4 import BeautifulSoup
import json

def escape_html_special_characters(html):
    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Get the text content of the HTML
    text = soup.get_text()
    
    # Escape special characters for JSON
    escaped_text = json.dumps(text)[1:-1]

    return escaped_text

# Example usage
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Example</title>
</head>
<body>
    <p>This is a paragraph with special characters: &lt; &gt; &amp;</p>
</body>
</html>
"""

escaped_html = escape_html_special_characters(html)
print(escaped_html)
