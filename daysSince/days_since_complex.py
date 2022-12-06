# this program doesn't currently need leap year logic, but the GUI version I build at a later date will.
def leap_year(inp):
    # if (year is not divisible by 4) then (it is a common year)
    # else if (year is not divisible by 100) then (it is a leap year)
    # else if (year is not divisible by 400) then (it is a common year)
    # else (it is a leap year)
    # turn input into an integer
    inp = int(inp)
    # check if not divisible by 4
    if inp % 4 != 0:
        return False
    # check if divisible by 4 but not 100
    elif inp % 4 == 0 and inp % 100 != 0:
        return True
    # check if divisible by 4 but not 400
    elif inp % 4 == 0 and inp % 400 != 0:
        return False
    # if divisible by 4, divisible by 100, and divisible by 400, return True
    else:
        return True

# was going to make this way more complicated and probably still will
class Date:
    # instantiation method
    def __init__(self,inp):
        # import regex library and separate the date string into year, month, and day
        import re
        groups = re.match('([0-9]{2})-([0-9]{2})-([0-9]{4})',inp)
        self.year = groups.group(3)
        self.month = groups.group(1)
        self.day = groups.group(2)
    # print them if necessary. this class is not used in this version of this module.
    def print_stuff(self):
        print(f'Year is {self.year}')
        print(f'Month is {self.month}')
        print(f'Day is {self.day}')

# breaking down the number of days (if this function is called) to years, months, weeks, and days
def day_breakdown(days):
    # just in case
    days = int(days)
    # declare response string
    response = ''
    # if there are 365 or more days, years will be included
    if days >= 365:
        # determine the number of years first
        years = int(days/365)
        # gramatically correct in the event of 1 year vs multiple years
        if years == 1:
            response += f'{years} year, '
        else:
            response += f'{years} years, '
        # the remainder should be divvied up into months
        rem_months = days % 365
        # if the remainder is 30 or more, there will be months in the response string
        if rem_months >= 30:
            # determine the number of months
            months = int(rem_months/30)
            # gramatically correct response
            if months == 1:
                response += f'{months} month, '
            else:
                response += f'{months} months, '
            # remainder will now be divvied up into weeks
            rem_weeks = rem_months % 30
            # if the remainder is 7 or more, there will be weeks in the response string
            if rem_weeks >= 7:
                # determine the number of weeks
                weeks = int(rem_weeks/7)
                # gramatically correct response
                if weeks == 1:
                    response += f'{weeks} week, '
                else:
                    response += f'{weeks} weeks, '
                # the remainder will now just be days
                rem_days = rem_weeks % 7
                if rem_days == 1:
                    response += f'{rem_days} day, '
                else:
                    response += f'{rem_days} days, '
            # if the remainder after month calculation is less than 7, there will not be weeks in the response string. we can skip straight to days.
            elif rem_weeks < 7:
                if rem_weeks == 1:
                    response += f'{rem_weeks} day, '
                else:
                    response += f'{rem_weeks} days, '
        # if it's more than a year, less than 1 year 1 month, and more than 1 year 1 week, process
        elif rem_months < 30 and rem_months > 7:
            # determine the number of weeks
            weeks = int(rem_months/7)
            # gramatically correct response
            if weeks == 1:
                response += f'{weeks} week, '
            else:
                response += f'{weeks} weeks, '
            # determine the number of days leftover
            rem_days = rem_months % 7
            # gramatically correct response, also accounts for zero
            if rem_days == 1:
                response += f'{rem_days} day, '
            else:
                response += f'{rem_days} days, '
        # if it's more than a year, but less than 1 year 1 week, process
        elif rem_months < 7:
            #gramatically correct response, also accounts for zero
            if rem_months == 1:
                response += f'{rem_months} day, '
            else:
                response += f'{rem_months} days, '
    # if it's less than a year, process
    elif days < 365:
        # if it is 30 or more, there will be months in the response string
        if days >= 30:
            # determine the number of months
            months = int(days/30)
            # gramatically correct response
            if months == 1:
                response += f'{months} month, '
            else:
                response += f'{months} months, '
            # remainder will now be divvied up into weeks
            rem_weeks = days % 30
            # if the remainder is 7 or more, there will be weeks in the response string
            if rem_weeks >= 7:
                # determine the number of weeks
                weeks = int(rem_weeks/7)
                # gramatically correct response
                if weeks == 1:
                    response += f'{weeks} week, '
                else:
                    response += f'{weeks} weeks, '
                # the remainder will now just be days
                rem_days = rem_weeks % 7
                if rem_days == 1:
                    response += f'{rem_days} day, '
                else:
                    response += f'{rem_days} days, '
            # if the remainder after month calculation is less than 7, there will not be weeks in the response string. we can skip straight to days.
            elif rem_weeks < 7:
                if rem_weeks == 1:
                    response += f'{rem_weeks} day, '
                else:
                    response += f'{rem_weeks} days, '
        # if it's more than a year, less than 1 year 1 month, and more than 1 year 1 week, process
        elif rem_months < 30 and rem_months > 7:
            # determine the number of weeks
            weeks = int(rem_months/7)
            # gramatically correct response
            if weeks == 1:
                response += f'{weeks} week, '
            else:
                response += f'{weeks} weeks, '
            # determine the number of days leftover
            rem_days = rem_months % 7
            # gramatically correct response, also accounts for zero
            if rem_days == 1:
                response += f'{rem_days} day, '
            else:
                response += f'{rem_days} days, '
        # if it's more than a year, but less than 1 year 1 week, process
        elif rem_months < 7:
            #gramatically correct response, also accounts for zero
            if rem_months == 1:
                response += f'{rem_months} day, '
            else:
                response += f'{rem_months} days, '
    return response

# breaking down the time into hours, minutes, and seconds
def time_breakdown(hms):
    import re
    # separate hours, minutes, and seconds into groups and assign them to variables
    # yes i'm aware i can one-line this and i choose not to
    groups = re.match('([0-9]{1,2}):([0-9]{2}):([0-9.]*)',hms)
    hours = groups.group(1)
    minutes = groups.group(2)
    seconds = groups.group(3)
    # format the response string
    response = f'{hours} hours, {minutes} minutes, and {seconds} seconds ago.'
    return response

# bread and butter of the script
def find_difference(now,then):
    # timedelta is used to process the difference in time
    from datetime import timedelta
    import re
    # get the timedelta difference in seconds between the two dates
    difference = timedelta(seconds=now-then)
    # start the response string
    response = 'The starting date/datetime was '
    # check if "days" is included in the timedelta, because if so we have more work to do
    if 'days' in str(difference):
        # separate the timedelta into the number of days and the number of hours/minutes/seconds
        groups = re.match(f'([0-9]*) days, (.*)',str(difference))
        # set the number of days to a variable, and run our earlier breakdown function on it
        days = int(groups.group(1))
        days = day_breakdown(days)
        # set the hours/minutes/seconds to a variable
        hms = groups.group(2)
        hms = time_breakdown(hms)
        # add the days response string first
        response += days
        # then add the hms response string
        response += hms
    # if the string "days" isn't in the timedelta, it's because it's less than 24 hours. we can simply convert to a string and append that to our response string.
    else:
        response += f'{str(difference)} ago.'
    return response

# main function
def main(inp):
    # import the time module and get the current time in seconds (with hella decimals) in local time
    import time, traceback
    now = time.time()
    # check the input length to determine the format.
    if len(inp) == 10:
        # use the strptime method of the time library to convert the input into the proper object type
        # then use the mktime method of the time library to convert that into seconds
        # i've also just now decided to wrap it in a try/except in case of improper input
        try:
            then = time.mktime(time.strptime(inp,'%m-%d-%Y'))
        except Exception as e:
            print(str(e))
            print(traceback.format_exc())
    # same story here
    elif len(inp) > 10:
        try:
            then = time.mktime(time.strptime(inp,'%m-%d-%Y %H:%M:%S'))
        except Exception as e:
            print(str(e))
            print(traceback.format_exc())
    # run the find_difference function and print the result
    difference = find_difference(now,then)
    print(difference)

if __name__ == "__main__":
    main(input("Enter your starting date formatted 'MM-DD-YYYY' or 'MM-DD-YYYY HH:MM:SS'> "))