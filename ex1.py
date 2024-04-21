import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        today_date = datetime.date.today()
        delta = today_date - given_date
        return delta.days
    except ValueError:
        raise ValueError("The date format should be 'YYYY-MM-DD'")


result = get_days_from_today("2021-10-09")
print(result)