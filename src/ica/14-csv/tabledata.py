def lookup_office (name, table):
    if name in table:
        person_info = table[name]
        building = person_info.get('Building')
        office = person_info.get('Office')
        return building, office
    else:
        print(f"Sorry, no office information found for {name}.")
        return None, None

def lookup_by_date (name, day, table):
    