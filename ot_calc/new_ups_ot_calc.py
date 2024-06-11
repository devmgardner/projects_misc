from typing import Union
import time

# region ref info
# If scheduled for 8 hour shifts:
# --Hours 0-8 are normal pay
# --Hours 8-12 are 1.5x pay
# --Hours 12+ are 2x pay
# If scheduled for 10 hour shifts:
# --Hours 0-10 are normal pay
# --Hours 10-12 are 1.5x pay
# --Hours 12+ are 2x pay
# If scheduled for 13 hour shifts:
# --3x13 is paid as 40
# --Hours 0-13 are normal pay
# --Hours 13+ are 2x pay
# Less than 8 hours between shifts:
# --Next shift is double pay

# 06-11-24 info
# pay rate: 17.99/hour
# schedule: 4x10s
# to pay off: 5466
# endregion


def get_stripped_input(msg: str) -> Union[float, bool]:
    """
    Get input from the user, convert to float, and return.
    :param msg: The message to display to the user.
    :return: A float of the user's input, or False.
    """

    text = input(msg).strip()
    if ' ' in text:
        text = text.replace(' ', '')
    if '$' in text:
        text = text.replace('$', '')
    if ',' in text:
        text = text.replace(',', '')

    try:
        to_return = float(text)
        return to_return
    except ValueError:
        return False


class Paycheck:
    def __init__(self):
        self.pay = 0
        self.weeks = 0
        self.taxes = 0
        self.total_pay = 0
        self.days = []
        self.schedule = None
        self.days_per_week = 0

    class Day:
        def __init__(self, week: int, day: int, daily_hours: Union[int, float]):
            self.actual_hours = 0
            self.true_hours = 0

            self.week = week
            self.day = day
            self.daily_hours = daily_hours

        def get_values(self):
            # region defining hours
            while True:
                hours = get_stripped_input(f'Enter number of hours worked on week {self.week}, day {self.day}\n>>> ')
                if not hours:
                    print('You must enter a number.')
                    continue
                else:
                    self.actual_hours = hours
                    break
            # endregion

        def calculate_ot(self):
            if self.daily_hours == 8:
                if self.actual_hours > 12:
                    diff = (self.actual_hours - 12) * 2
                    self.true_hours = diff + 14
                elif 8 < self.actual_hours <= 12:
                    diff = (self.actual_hours - 8) * 1.5
                    self.true_hours = diff + 8
                else:
                    self.true_hours = self.actual_hours
            elif self.daily_hours == 10:
                if self.actual_hours > 12:
                    diff = (self.actual_hours - 12) * 2
                    self.true_hours = diff + 13
                elif 10 < self.actual_hours <= 12:
                    diff = (self.actual_hours - 10) * 1.5
                    self.true_hours = diff + 10
                else:
                    self.true_hours = self.actual_hours
            elif self.daily_hours == '13':
                if self.actual_hours > 13:
                    diff = (self.actual_hours - 13) * 2
                    self.true_hours = diff + 13
                else:
                    self.true_hours = self.actual_hours

    def get_values(self):
        # region defining pay
        while True:
            pay = get_stripped_input('Enter pay rate per hour\n>>> ')
            if not pay:
                print('You must enter a number.')
                continue
            else:
                self.pay = pay
                break
        # endregion

        # region defining taxes
        while True:
            taxes = get_stripped_input('Enter how much you take home after taxes.\n>>> ')
            if not taxes:
                print('You must enter a number.')
                continue
            else:
                self.taxes = taxes
                break
        # endregion

        # region defining schedule
        while True:
            schedule = get_stripped_input('How many hours are your normal daily scheduled shifts?\n>>> ')
            if not schedule:
                print('You must enter a number.')
                continue
            else:
                self.schedule = schedule
                break
        # endregion

        # region defining weeks
        while True:
            weeks = get_stripped_input('How many weeks to calculate?\n>>> ')
            if not weeks:
                print('You must enter a number.')
                continue
            else:
                self.weeks = int(weeks)
                break
        # endregion

        # region defining days per week
        while True:
            days = get_stripped_input('How many days to work each week?\n>>> ')
            if not days:
                print('You must enter a number.')
                continue
            else:
                self.days_per_week = int(days)
                break
        # endregion

    def define_days(self):
        for _w in range(self.weeks):
            week = _w + 1
            for _d in range(self.days_per_week):
                day = _d + 1
                self.days.append(self.Day(week, day, self.schedule))

    def calculate_pay(self):
        total_hours = 0
        self.get_values()
        self.define_days()

        for day in self.days:
            day.get_values()
            day.calculate_ot()
            total_hours += day.true_hours

        self.total_pay = total_hours * (self.pay * (self.taxes / 100))

    def data_dump(self):
        self.calculate_pay()
        now = int(time.time())
        with open(f'{now}.txt', 'w') as file:
            for day in self.days:
                file.write(f'Week #{day.week}, Day #{day.day}:\n'
                           f'{day.actual_hours} hours worked, {day.true_hours} hours paid.\n\n')

            file.write(f'Final total is $ {new_check.total_pay:,.02f}')


if __name__ == '__main__':
    new_check = Paycheck()
    new_check.calculate_pay()

    print(f'Total pay with provided inputs is: $ {new_check.total_pay:,.02f}')
