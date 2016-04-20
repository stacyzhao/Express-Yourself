import re

def words(value):
    words = re.findall(r'([\w\-]+)', value)
    if len(words) > 0:
        return words
    else:
        return None

def phone_number(value):
    number = re.findall(r'(\(?\d{3}\)?[\-\.\s]?)(\d{3}[\-\.]?)(\d{4})', value)
