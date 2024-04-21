import datetime

def get_upcoming_birthdays(users):
    today = datetime.date.today()
    upcoming_birthdays = []

    for user in users:
        name = user['name']
        birthdate = datetime.datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday_this_year = birthdate.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta = birthday_this_year - today
        if 0 <= delta.days <= 7:
            if birthday_this_year.weekday() in (5, 6): 
                days_to_add = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + datetime.timedelta(days=days_to_add)
            else:
                congratulation_date = birthday_this_year
                
            upcoming_birthdays.append({
                'name': name,
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.04.23"},
    {"name": "Jane Smith", "birthday": "1990.04.27"}
]
print(get_upcoming_birthdays(users))
