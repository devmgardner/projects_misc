import psutil as ps
def cpu():
    pull_data = ps.cpu_times_percent(interval=0.5)
    data = {}
    data['user'], data['system'], data['idle'], data['iowait'] = pull_data[0], pull_data[2], pull_data[3], pull_data[4]
    statement = f"User:\t{data['user']}\nSystem:\t{data['system']}\nIdle:\t{data['idle']}\nIOWait:\t{data['iowait']}"
    return statement
while True:
    print(cpu())