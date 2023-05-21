#0-8 normal
#8-12 time.half
#12-16 time.double
#next shift time.double
class Paycheck:
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
    def define_weeks(self):
        self.weeks = input(f'Enter number of weeks on this check> ')
        try:
            self.weeks = int(self.weeks)
        except ValueError:
            print(f'ERROR: Please enter an integer.')
            self.define_weeks()
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
        def calculate_ot(self):
            if self.hours > 12:
                self.true_hours += 14
                self.true_hours += ((self.hours-12)*2)
            elif self.hours > 8 and self.hours <= 12:
                self.true_hours += 8
                self.true_hours += ((self.hours-8)*1.5)
            elif self.hours <= 8:
                self.true_hours += self.hours
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
                d.calculate_ot()
                self.days[i].append(d)
    #
    def calculate_total_pay(self):
        for week in self.days.keys():
            for ind,day in enumerate(self.days[week]):
                if ind == 0:
                    self.total_pay += (day.true_hours * (self.taxes/100) * self.pay)
                elif ind != 0 and ind < 5:
                    if self.days[week][ind-1].hours >= 16:
                        self.total_pay += (day.hours * 2 * (self.taxes/100) * self.pay)
                    elif self.days[week][ind-1].hours < 16:
                        self.total_pay += (day.true_hours * (self.taxes/100) * self.pay)
                elif ind == 5:
                    self.total_pay += (day.hours * 1.5 * (self.taxes/100) * self.pay)
                elif ind == 6:
                    self.total_pay += (day.hours * 2 * (self.taxes/100) * self.pay)
#
ups = Paycheck()
ups.define_pay()
ups.define_taxes()
ups.define_weeks()
ups.define_days()
ups.calculate_total_pay()
print(f'Total pay based on entered information is ${round(ups.total_pay,2)}')