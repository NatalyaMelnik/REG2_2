import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = r'(\+7|8)?\s{0,}\({0,}(\d{3})\){0,}[-\s]{0,}(\d{3})[-\s]*(\d{2})[-\s]*(\d+)\s?\(*(доб.)*\s{0,}(\d{4}){0,}\)*'
substitution = r'+7(\2)\3-\4-\5 \6\7'
new_list = []
for row in contacts_list:
    new_row = ','.join(row)
    format_new = re.sub(pattern, substitution, new_row)
    strings_new = format_new.split(",")
    new_list.append(strings_new)

lst = []
for contact in new_list:
    new_date = []
    full_name = " ".join(contact[0:3])  # первые три строки должны содержать полное имя контакта ФИО
    res = full_name.rstrip()
    new_date.append(res)
    new_date.append(contact[3])
    new_date.append(contact[4])
    new_date.append(contact[5])
    new_date.append(contact[6])
    lst.append(new_date)

telbook = {}
for strings in lst:
    if strings[0][:5] in telbook:
        name = telbook[strings[0][:5]]
    else:
        telbook[strings[0][:5]] = strings

new_list_phonbook = list(telbook.values())

with open("phonebook.csv", "w", newline='', encoding="UTF-8") as f:
    datawriter = csv.writer(f, delimiter=' ')
    datawriter.writerows(new_list_phonbook)

if __name__ == '__main__':
    # print(new_list[0][0:3])
    # pprint(contacts_list)
    print(lst)
    pprint(new_list_phonbook)
