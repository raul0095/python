import urllib.request
import xml.etree.ElementTree as ET

# Prompt for URL
url = input('Enter URL: ')
print(f'Retrieving {url}')

# Read XML data from the URL
data = urllib.request.urlopen(url).read()
print(f'Retrieved {len(data)} characters')

# Parse XML
tree = ET.fromstring(data)

# Find all comment counts
counts = tree.findall('.//count')

# Extract integers and compute the sum
numbers = [int(count.text) for count in counts]
print('Count:', len(numbers))
print('Sum:', sum(numbers))
