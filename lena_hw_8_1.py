"""
1. «Дата»
"""


class Date:

    def __init__(self, day_month_year):
        self.date_str = str(day_month_year)
        print(f"Date: {day_month_year}")

    @classmethod
    def digitize(cls, day_month_year):
        my_list = day_month_year.split("-")
        res_list =[]
        for i in my_list:
            res_list.append(int(i))
        return res_list

    @staticmethod
    def validation(date_list):
        if 1 <= date_list[0] <= 31:
            if 1 <= date_list[1] <= 12:
                if 0 <= date_list[2] <= 2020:
                    print(f"All right")
                else:
                    print(f"The year is not valid.")
            else:
                print(f"The month is not valid.")
        else:
            print(f"The day is not valid.")


my_date = Date("32-03-1988")
print(my_date.digitize(my_date.date_str))
my_date.validation(my_date.digitize(my_date.date_str))
print(Date.digitize("08-12-2020"))
Date.validation(Date.digitize("08-12-2020"))
