"""
    Visit the link to see what the algorithm is based on
    http://www.highprogrammer.com/alan/numbers/mrp.html
"""


def mrz_generator(citizenship="", document_no="", document_id="", sex="", date=""):
    count_c = 0
    multiplication = 7
    for character in document_no or date:
        try:
            count_c += int(character) * multiplication
        except:
            count_c += (ord(character) - 55) * multiplication

        if multiplication == 7:
            multiplication -= 4
        elif multiplication == 3:
            multiplication -= 2
        elif multiplication == 1:
            multiplication = 7

    if date:
        return "{}{}{}".format(sex, date, count_c % 10)
    elif document_no:
        return "ID{}{}{}{}<<<<".format(citizenship, document_no, count_c % 10, document_id)


def mrz(citizenship, document_no, document_id, sex, birth_date, expire_date, first_name, last_name):
    v1 = mrz_generator(citizenship=(citizenship[:3]).upper(),
                       document_no=document_no, document_id=document_id)
    v2 = mrz_generator(date=birth_date.strftime('%y-%m-%d').replace("-", ""))
    v3 = mrz_generator(sex=sex[0], date=expire_date.strftime('%y-%m-%d').replace("-", "")) + \
         (citizenship[:3]).upper() + "<" * 12
    v4 = last_name.upper() + "<<" + first_name.upper() + "<" * (28 - len(first_name+last_name))
    return v1+v2+v3+v4
