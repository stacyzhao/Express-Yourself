import re

def binary(value):
    return re.search(r'^[01]+', value)

def binary_even(value):
    return re.search(r'[01]+0$', value)
    pass

def hex(value):
    return re.search(r'^[a-f0-9]+$', value, re.IGNORECASE)

def word(value):
    return re.search(r'^[\w-]+[a-z]+$', value)

# def words(value):
#     match_words = re.findall(r'^[\w-]+[a-z]+$', value)
#     return match_words

def phone_number(value):
    return re.search(r'^(\(?\d{3}\)?[\-\.\s]?)(\d{3}[\-\.]?)(\d{4})', value)

def money(value):
    return re.search(r'^\$[\d]+([,][\d]{3})*(\.[\d]{2})?$', value)

def zipcode(value):
    return re.search(r'^\d{5}(?:[-\s]\d{4})?$', value)

def date(value):
    return re.search(r'^(([\d]{4}\-)|([\d]{1,2}\/))(([\d]{1,2}\-)|([\d]{1,2}\/))(([\d]{1,2})|([\d]{4}))$', value)
