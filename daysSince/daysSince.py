def main(inp):
    import time
    now = time.time()
    if len(inp) == 10:
        then = time.mktime(time.strptime(inp,'%m-%d-%Y'))
    elif len(inp) > 10:
        then = time.mktime(time.strptime(inp,'%m-%d-%Y %H:%M:%S'))
    from datetime import timedelta
    difference = timedelta(seconds=now-then)
    print(f"The starting date/datetime was {difference}s ago.")

if __name__ == "__main__":
    main(input("enter your starting date formatted 'MM-DD-YYYY' or 'MM-DD-YYYY HH:MM:SS'> "))