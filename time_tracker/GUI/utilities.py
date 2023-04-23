import requests as rq
#
def send_data(p_source,p_number,p_name,start,stop):
    package = {}
    package['project_source'] = p_source
    package['project_number'] = p_number
    package['project_name'] = p_name
    package['start_time'] = start
    package['stop_time'] = stop
    url = 'https://time.devinmgardner.com/api'
    response = rq.get(url,json=package)
    print(response)