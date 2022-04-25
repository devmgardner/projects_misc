from xml.dom import pulldom
import psutil as ps, os
#returns active load percentage in categories
def cpu():
    pull_data = ps.cpu_times_percent(interval=0.5)
    data = {}
    data['user'], data['system'], data['idle'], data['iowait'] = pull_data[0], pull_data[2], pull_data[3], pull_data[4]
    statement = f"----------------\nCPU Usage:\n----------------\nUser:\t{data['user']}%\nSystem:\t{data['system']}%\nIdle:\t{data['idle']}%\nIOWait:\t{data['iowait']}%\n----------------"
    return statement
#returns average load over 1, 5, and 15 minutes
def avgload():
    pull_data = [x / ps.cpu_count() * 100 for x in os.getloadavg()]
    data = {}
    data['1min'], data['5min'], data['15min'] = pull_data[0], pull_data[1], pull_data[2]
    statement = f"CPU Averages:\n----------------\n1 minute load average:\t{round(data['1min'],2)}%\n5 minute load average:\t{round(data['5min'],2)}%\n15 minute load average:\t{round(data['15min'],2)}%\n----------------"
    return statement
#returns total physical memory (excluding swap) and available memory (excluding swap)
def phys_memory():
    pull_data = ps.virtual_memory()
    data = {}
    def convert_to_bytes(inp):
        values = [("TB",1099511627776), ("GB",1073741824), ("MB",1048576), ("KB",1024)]
        for i in values:
            if inp > i[1]:
                inp /= i[1]
                return f'{round(inp,4)}{i[0]}'
            else:
                continue
    data['total'], data['available'] = convert_to_bytes(pull_data[0]), convert_to_bytes(pull_data[1])
    statement = f"Memory Usage:\n----------------\nTotal physical memory:\t{data['total']}\nTotal available memory:\t{data['available']}\nUsed memory percentage:\t{round(((pull_data[0]-pull_data[1])/pull_data[0])*100,4)}%\n----------------"
    return statement

print(cpu())
print(avgload())
print(phys_memory())
#while True:
#    print(cpu())