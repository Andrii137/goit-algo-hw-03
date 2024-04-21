from datetime import datetime

def get_days_from_today(date):
    try:
        string_to_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        delta = current_date - string_to_date
        return delta.days
    except ValueError:
        return ('Wrong date format')

result = get_days_from_today('2022-10-15')
print(f'Різниця днів: {result}')