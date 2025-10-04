import pytesseract
import PIL


def OCR(image_path):
    '''Extraction of text from image using OCR i.e. by pytesseract library.'''
    try:
        text = pytesseract.image_to_string(PIL.open(image_path))
        return text
    except Exception as e:
        print(f"Could not process image {image_path}: {e}")
        return ""


def parse_and_group(text, data_dict):
    '''Parsing of the text and assigining a group heading, updation of data dict.
    Looks for headings with ':' and groups by the first part'''
    lines = text.split('\n')
    for line in lines:
        if ':' in line:
            heading, content = line.split(':', 1)
            heading = heading.strip()
            content = content.strip()
            if heading not in data_dict:
                data_dict[heading] = []
            data_dict[heading].append(content)
    return data_dict

# Only For Output And Showing Wrking Purposes.
sample = '''
Title: Shopping List
Milk: 2 L
Bread: 1 loaf
Butter: 200g
Note: Remember to buy eggs!
'''

data = {}
data = parse_and_group(sample, data)

print(data)
