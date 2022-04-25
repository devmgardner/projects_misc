from xml.dom import pulldom
import psutil as ps
#returns active load percentage in categories
def cpu():
    pull_data = ps.cpu_times_percent(interval=0.5)
    data = {}
    data['user'], data['system'], data['idle'], data['iowait'] = pull_data[0], pull_data[2], pull_data[3], pull_data[4]
    statement = f"User:\t{data['user']}\nSystem:\t{data['system']}\nIdle:\t{data['idle']}\nIOWait:\t{data['iowait']}"
    return statement
#returns average load over 1, 5, and 15 minutes
def avgload():
    pull_data = [x / ps.cpu_count() * 100 for x in ps.getloadavg()]
    data = {}
    data['1min'], data['5min'], data['15min'] = pull_data[0], pull_data[1], pull_data[2]
    statement = f"1 minute load average:\t{data['1min']}\n5 minute load average:\t{data['5min']}\n15 minute load average:\t{data['15min']}"
    return statement
print(cpu)
print(avgload)

#while True:
#    print(cpu())