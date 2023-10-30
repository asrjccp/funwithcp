def make_record(checkin, checkout,place):
    lst = (checkin, checkout, place)
    return lst

def get_checkin(record):
    return record[0]

def get_checkout(record):
    return record[1]

def get_place(record):
     return record[2]

# main
print(get_checkin(make_record("1150","1240","Sentosa")))
