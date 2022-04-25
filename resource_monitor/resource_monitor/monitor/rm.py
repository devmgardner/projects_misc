import psutil as ps, os, platform
#returns active load percentage in categories
def cpu():
    pull_data = ps.cpu_times_percent(interval=0.5)
    data = {}
    data['user'], data['system'], data['idle'], data['iowait'] = pull_data[0], pull_data[2], pull_data[3], pull_data[4]
    statement = f"----------------\nCPU Usage:\n----------------\nUser:\t{data['user']}%\nSystem:\t{data['system']}%\nIdle:\t{data['idle']}%\nIOWait:\t{data['iowait']}%\n----------------"
    return statement
#returns average load over 1, 5, and 15 minutes
def avgload():
    if platform.system() == 'Windows':
        pull_data = [x / ps.cpu_count() * 100 for x in ps.getloadavg()]
    else:
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
def disk_stats():
    part_data = ps.disk_partitions()
    io_data = ps.disk_io_counters(perdisk=True)
    data = {}
    def convert_to_bytes(inp):
        values = [("TB",1099511627776), ("GB",1073741824), ("MB",1048576), ("KB",1024)]
        for i in values:
            if inp > i[1]:
                inp /= i[1]
                return f'{round(inp,4)}{i[0]}'
            else:
                continue
    for i in part_data:
        du = ps.disk_usage(i[1])
        data[i[0]] = {}
        data[i[0]]['total'] = f'{convert_to_bytes(du[0])} - {du[0]}'
        data[i[0]]['used'] = f'{convert_to_bytes(du[1])} - {du[1]}'
        data[i[0]]['free'] = f'{convert_to_bytes(du[2])} - {du[2]}'
        data[i[0]]['percents'] = f"{round(data[i[0]]['used']/data[i[0]]['total'],4)}% used, {round(data[i[0]]['free']/data[i[0]]['total'],4)}% free"
        data[i[0]]['mountpoint'] = i[1]
        data[i[0]]['type'] = i[2]
    statements = []
    statements.append(f'----------------')
    statements.append(f'Disk Usage Stats')
    statements.append(f'----------------')
    for name in data.keys():
        statements.append(f'++++++++++++++++')
        statements.append(f'Name is:\t{name}')
        statements.append(f"Mount point is:\t{data[name]['mountpoint']}")
        statements.append(f"Filesystem type is:\t{data[name]['type']}")
        statements.append(f"Total space is:\t{data[name]['total']}")
        statements.append(f"Total space used is:\t{data[name]['used']}")
        statements.append(f"Total space free is:\t{data[name]['free']}")
        statements.append(data[name]['percents'])
        statements.append(f'++++++++++++++++')
    statements.append(f'----------------')
    statements.append(f'Disk I/O Stats')
    statements.append(f'----------------')
    for i in io_data.keys():
        statements.append(f'++++++++++++++++')
        statements.append(f'Name is:\t{i}')
        statements.append(f"Read count is:\t{io_data[i][0]}")
        statements.append(f"Write count is:\t{io_data[i][1]}")
        statements.append(f"Read bytes are:\t{convert_to_bytes(io_data[i][2])}")
        statements.append(f"Write bytes are:\t{convert_to_bytes(io_data[i][3])}")
        statements.append(f"Read time is:\t{io_data[i][4]*1000}")
        statements.append(f"Write time is:\t{io_data[i][5]*1000}")
        statements.append(f'++++++++++++++++')
    statements.append(f'----------------')
    return '\n'.join(statements)
print(cpu())
print(avgload())
print(phys_memory())
print(disk_stats())
#while True:
#    print(cpu())