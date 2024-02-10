from datetime import datetime, timedelta, date
from time import localtime, time

# Створюємо функцію 
def get_upcoming_birthdays(users: list) -> list:
    # Створюємо два списки 
    # Один для днів народження які будуть за 7 днів
    upcoming_birthdays = []
    # Інший для тих які будут не скоро
    birthdays = []

    # Створюємо змінну today для того шоб позначити сьогоднішню дату
    today = date(2024, 12, 30)
    today_year_day = list(localtime(time()))[7]

    # Створюємо цикл в якому ми перебираємо кожний словник переданого списку 
    for user in users:
        # Створюємо список з кортежом ключ, значення словника для легкого доступу та дістаємо з відти кортеж 
        items = list(user.items())[0]
        # Присвоюємо значення ключа та його значення
        key, value = items
        # Робимо з дати народження об'єкт datetime
        date_time_bd = datetime.strptime(value, '%Y.%m.%d').date()
        # Створюємо змінну яка буде дорівнювати даті народження але цього року
        birthday = datetime(year=today.year, month=date_time_bd.month, day=date_time_bd.day)
        birthday_next_year = datetime(year=today.year + 1, month=date_time_bd.month, day=date_time_bd.day)
        birthday_year_day = list(localtime(datetime.timestamp(birthday)))[7]

        print(birthday_year_day, today_year_day)

		# Перевіряємо чи вже було день народження
        if birthday_year_day - today_year_day <= 7 and birthday_year_day - today_year_day >= 0:
            while birthday.weekday() in (5, 6):
                birthday += timedelta(days=1)
            upcoming_birthdays.append({'name': key, 'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')})
        elif birthday_year_day - today_year_day > 7:
            # Якщо було то додаємо дату наступного дня народження до списку днів народження
            birthdays.append({'name': key, 'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')})
        elif birthday_year_day - today_year_day < 0:
            # Якщо було то додаємо дату наступного дня народження до списку днів народження
            birthdays.append({'name': key, 'congratulating_date': datetime.strftime(birthday_next_year, '%Y.%m.%d')})
        

    return upcoming_birthdays, birthdays


users = [
    {'Egor': '2007.12.29'},
    {'Misha': '2010.02.05'}
]

upcoming_birthdays = get_upcoming_birthdays(users)

print(f'Upcoming birthdays in 7 days: {upcoming_birthdays[0]}\nOther Birthdays: {upcoming_birthdays[1]}')