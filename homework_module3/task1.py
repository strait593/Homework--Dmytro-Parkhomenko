from datetime import datetime

def get_days_from_today(required_date):

    current_date = datetime.now()
    
    date_obj = datetime.strptime(required_date, "%Y.%m.%d")

    if date_obj > current_date:
        print("I can't see the future boss")

    days_left = current_date - date_obj

    return print(f"The {required_date} was {days_left.days} days ago")

get_days_from_today('2023.01.01')

#Output: "The 2023.01.01 was 1124 days ago"