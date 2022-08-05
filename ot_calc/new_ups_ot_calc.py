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
class Paycheck():
    def __init__(self):
        self.pay = self.weeks = self.taxes = self.total_pay = 0
        self.days = {}
    #
    def define_pay(self):
        self.pay = input(f'Enter pay rate per hour> ')
        try:
            self.pay = float(self.pay)
        except ValueError:
            print(f'ERROR: Please enter an integer or float.')
            self.define_pay()
    #
    def define_taxes(self):
        self.taxes = input(f'Enter take-home amount after taxes. For example, if you take home 72.5% of your pay after taxes, enter "72.5"> ')
        try:
            self.taxes = float(self.taxes)
        except ValueError:
            print(f'ERROR: Please enter an integer or float.')
            self.define_taxes()
    #
    class Day:
        def __init__(self):
            self.hours = self.true_hours = 0
        #
        def define_hours(self):
            self.hours = input(f'Enter number of hours worked> ')
            try:
                self.hours = float(self.hours)
            except ValueError:
                print(f'ERROR: Please enter an integer or float.')
                self.define_hours()
        #
        def calculate_ot(self,sched):
            if sched == '8':
                if self.hours > 12:
                    self.true_hours += 14
                    self.true_hours += ((self.hours-12)*2)
                elif self.hours > 8 and self.hours <= 12:
                    self.true_hours += 8
                    self.true_hours += ((self.hours-8)*1.5)
                elif self.hours <= 8:
                    self.true_hours += self.hours
            elif sched == '10':
                if self.hours > 12:
                    self.true_hours += 14
                    self.true_hours += ((self.hours-12)*2)
                elif self.hours > 10 and self.hours <= 12:
                    self.true_hours += 10
                    self.true_hours += ((self.hours-10)*1.5)
                elif self.hours <= 10:
                    self.true_hours += self.hours
            elif sched == '13':
                if self.hours > 13:
                    self.true_hours += 13
                    self.true_hours += ((self.hours-13)*2)
                elif self.hours <= 13:
                    self.true_hours += self.hours
    #
    def define_schedule(self):
        self.sched = input(f'How many hours are your normal scheduled shifts?> ')
        while sched not in ['8','10','13']:
            print(f'ERROR: Please enter 8, 10, or 13.')
            self.sched = input(f'How many hours are your normal scheduled shifts?> ')
    #
    def define_days(self):
        for i in range(self.weeks):
            days = input(f'Enter number of days worked in week {i+1}> ')
            try:
                days = int(days)
            except ValueError:
                print(f'ERROR: Please enter an integer.')
                self.define_days()
            self.days[i] = []
            for d in range(days):
                print(f'Defining day {d+1}')
                d = self.Day()
                d.define_hours()
                d.calculate_ot(self.sched)
                self.days[i].append(d)