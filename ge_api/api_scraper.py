import requests as rq, sqlite3 as sq, os, sys, time

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

dbcon = sq.connect(os.path.join(currentdir, 'GE-04-30-22.sqlite'))
dbcur = dbcon.cursor()
dbcur.execute("""CREATE TABLE IF NOT EXISTS "items" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"type"	TEXT,
	"description"	TEXT,
	"price"	INTEGER,
	PRIMARY KEY("id")
);
""")

categoriesurl = 'https://services.runescape.com/m=itemdb_rs/api/catalogue/category.json'
itemsurl = 'https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json'

params = {}
catlist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]
print(f'catlist is {catlist}')
categories = {}
for category in catlist:
    params['category'] = category
    response = rq.get(categoriesurl, params=params)
    if response.status_code == 404:
        continue
    elif response.status_code != 404:
        response = response.json()
        categories[category] = ([a['letter'] for a in response['alpha']], [a['items'] for a in response['alpha']])
print(f'categories are {categories}')

for category in categories.keys():
    params['category'] = category
    for letter in categories[category][0]:
        params['alpha'] = letter
        for i in range(int(categories[category][1][categories[category][0].index(letter)]/12)):
            if int(categories[category][1][categories[category][0].index(letter)]) == 0:
                continue
            time.sleep(5)
            params['page'] = i+1
            print(f'params are {params}')
            data = rq.get(itemsurl, params=params)
            print(f'current url is {data.url}')
            if data.status_code == 404:
                continue
            elif data.status_code != 404:
                data = data.json()['items']
                for item in data:
                    try:
                        dbcur.execute("insert into items values (?, ?, ?, ?, ?)",(item['id'],item['name'],item['type'],item['description'],item['current']['price'],))
                    except sq.IntegrityError:
                        continue
            dbcon.commit()
