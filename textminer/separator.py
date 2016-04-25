import re


def words(value):
    words_re = re.findall(r'([\w\-]+[^\d\s]+)', value)
    if len(words_re) >= 1:
        return words_re
    else:
        return None


def phone_number(value):
    phone_numbers = {}
    ptrn = r'\(?(\d{3})\)?[\-\.\s]?(\d{3})[\-\.]?(\d{4})'
    number = re.match(ptrn, value)
    if number is None:
        return None
    phone_numbers['area_code'] = number.group(1)
    phone_numbers['number'] = number.group(2) + '-' + number.group(3)
    return phone_numbers


# def money(value):
#     moola = {}
#     ptrn = r'(\$)+(\d{1,})'
# # #     # (\.\d{2})?(\,\d{3})*
# # # #     # ([\$])+(\d{1,4}[\,\.]?)'
#     currency = re.match(ptrn, value)
#     moola['currency'] = currency.group(1)
#     moola['amount'] = float(currency.group(2)
#     return moola

 # elif currency.group(3) is None:
    #     money['amount'] = float(currency.group(2) + float(currency.group(3))
    # else:
    #     money['amount'] = float(currency.group(2) + float(currency.group(3)) + float(currency.group(4))
#     return money


def zipcode(value):
    code = {}
    if len(value) == 10:
        ptrn = r'(\d{5})-?(\d{4})?'
        zip_code = re.match(ptrn, value)
        code['zip'] = zip_code.group(1)
        if zip_code.group(2) is None:
            code['plus4'] = None
        else:
            code['plus4'] = zip_code.group(2)
        # print (code['plus4'])
    else:
        return None
    return code


def date(value):
    dates = {}
    ptrn = r'(\d)[\/]?(\d)[\/]?(\d+)'
    split_date = re.match(ptrn, value)
    dates['month'] = split_date.group(1)
    dates['day'] = split_date.group(2)
    dates['year'] = split_date.group(3)
    print (dates)

    return dates
