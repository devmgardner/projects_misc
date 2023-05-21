import xml.etree.ElementTree as ET, re, requests as rq
import json

#$events
def eventscrape(player):
    url = f'https://secure.runescape.com/m=adventurers-log/rssfeed?searchName={player}'
    response = rq.get(url)
    if response.status_code == 404:
        return "Error"
    data = ET.fromstring(response.text)
    feed = data[0].findall('item')
    feed_list = []
    for item in feed:
        title = item.find('title').text
        description = re.sub('\t','',re.sub('\n','',item.find('description').text))
        link = item.find('link').text
        date = item.find('pubDate').text
        itemid = re.match('.*[&id=-](?P<id>\d*)',item.find('link').text).group('id')
        feed_list.append((date, title, description, itemid, link))
    return feed_list

#too much info
def quests(player):
    url = f'https://apps.runescape.com/runemetrics/quests?user={player}'
    data = rq.get(url).json()
    for i in data['quests']:
        if i['status'] == 'STARTED':
            i['status'] = 'Started'
        elif i['status'] == 'COMPLETED':
            i['status'] = 'Completed'
        elif i['status'] == 'NOT_STARTED':
            i['status'] = 'Not Started'
        if i['difficulty'] == 0:
            i['difficulty'] = 'Novice'
        elif i['difficulty'] == 1:
            i['difficulty'] = 'Intermediate'
        elif i['difficulty'] == 2:
            i['difficulty'] = 'Experienced'
        elif i['difficulty'] == 3:
            i['difficulty'] = 'Master'
        elif i['difficulty'] == 4:
            i['difficulty'] = 'Grandmaster'
        elif i['difficulty'] == 5:
            i['difficulty'] = 'Special'
    return data['quests']

#$quests
def apiscrape(player):
    apiurl = f'https://apps.runescape.com/runemetrics/profile/profile?user={player}&activities=20'
    apidata = rq.get(apiurl).json()
    if "error" in apidata.keys():
        return "Error"
    name = apidata['name']
    rank = apidata['rank']
    melee = apidata['melee']
    combatlevel = apidata['combatlevel']
    ranged = apidata['ranged']
    totalxp = apidata['totalxp']
    questscomplete = apidata['questscomplete']
    questsnotstarted = apidata['questsnotstarted']
    questsstarted = apidata['questsstarted']
    totalskill = apidata['totalskill']
    magic = apidata['magic']
    skills = json.dumps(apidata['skillvalues'])
    activities = json.dumps(apidata['activities'])
    return (name, rank, melee, combatlevel, ranged, totalxp, questscomplete, questsnotstarted, questsstarted, totalskill, magic, skills, activities)


def xpaverages(player):
    averagelist = []
    url = 'https://apps.runescape.com/runemetrics/xp-monthly?searchName={x}&skillid={y}'
    for i in range(28):
        try:
            data = rq.get(url.format(x=player, y=str(i)))
            averagexpgain = data.json()['monthlyXpGain'][0]['averageXpGain']
            totalgain = data.json()['monthlyXpGain'][0]['totalGain']
            lastmonthgain = data.json()['monthlyXpGain'][0]['monthData'][11]['xpGain']
            averagelist.append((i,f'{averagexpgain:,}',f'{totalgain:,}',f'{lastmonthgain:,}'))
        except IndexError:
            averagexpgain = 0
            totalgain = 0
            lastmonthgain = 0
            averagelist.append((i,f'{averagexpgain:,}',f'{totalgain:,}',f'{lastmonthgain:,}'))
    return averagelist

#$combat
def combat(player):
    if apiscrape(player) == "Error":
        return "Error"
    return apiscrape(player)[3]

#$totalskill
def totalskill(player):
    if apiscrape(player) == "Error":
        return "Error"
    return apiscrape(player)[9]

#$totalxp
def totalxp(player):
    if apiscrape(player) == "Error":
        return "Error"
    return apiscrape(player)[5]

#$rank
def rank(player):
    if apiscrape(player) == "Error":
        return "Error"
    return apiscrape(player)[1]


def skills(player):
    return apiscrape(player)[11]


def questscomplete(player):
    return apiscrape(player)[6]


def skilllevels(player):
    allskills = json.loads(apiscrape(player)[11])
    leveldict = {}
    for skill in allskills:
        if skill['id'] == 0:
            leveldict['Attack'] = skill['level']
        elif skill['id'] == 1:
            leveldict['Defence'] = skill['level']
        elif skill['id'] == 2:
            leveldict['Strength'] = skill['level']
        elif skill['id'] == 3:
            leveldict['Constitution'] = skill['level']
        elif skill['id'] == 4:
            leveldict['Ranged'] = skill['level']
        elif skill['id'] == 5:
            leveldict['Prayer'] = skill['level']
        elif skill['id'] == 6:
            leveldict['Magic'] = skill['level']
        elif skill['id'] == 7:
            leveldict['Cooking'] = skill['level']
        elif skill['id'] == 8:
            leveldict['Woodcutting'] = skill['level']
        elif skill['id'] == 9:
            leveldict['Fletching'] = skill['level']
        elif skill['id'] == 10:
            leveldict['Fishing'] = skill['level']
        elif skill['id'] == 11:
            leveldict['Firemaking'] = skill['level']
        elif skill['id'] == 12:
            leveldict['Crafting'] = skill['level']
        elif skill['id'] == 13:
            leveldict['Smithing'] = skill['level']
        elif skill['id'] == 14:
            leveldict['Mining'] = skill['level']
        elif skill['id'] == 15:
            leveldict['Herblore'] = skill['level']
        elif skill['id'] == 16:
            leveldict['Agility'] = skill['level']
        elif skill['id'] == 17:
            leveldict['Thieving'] = skill['level']
        elif skill['id'] == 18:
            leveldict['Slayer'] = skill['level']
        elif skill['id'] == 19:
            leveldict['Farming'] = skill['level']
        elif skill['id'] == 20:
            leveldict['Runecrafting'] = skill['level']
        elif skill['id'] == 21:
            leveldict['Hunter'] = skill['level']
        elif skill['id'] == 22:
            leveldict['Construction'] = skill['level']
        elif skill['id'] == 23:
            leveldict['Summoning'] = skill['level']
        elif skill['id'] == 24:
            leveldict['Dungeoneering'] = skill['level']
        elif skill['id'] == 25:
            leveldict['Divination'] = skill['level']
        elif skill['id'] == 26:
            leveldict['Invention'] = skill['level']
        elif skill['id'] == 27:
            leveldict['Archaeology'] = skill['level']
    return leveldict


def skillxp(player):
    allskills = json.loads(apiscrape(player)[11])
    xpdict = {}
    for skill in allskills:
        skill['xp'] /= 10
        if skill['id'] == 0:
            xpdict['Attack'] = skill['xp']
        elif skill['id'] == 1:
            xpdict['Defence'] = skill['xp']
        elif skill['id'] == 2:
            xpdict['Strength'] = skill['xp']
        elif skill['id'] == 3:
            xpdict['Constitution'] = skill['xp']
        elif skill['id'] == 4:
            xpdict['Ranged'] = skill['xp']
        elif skill['id'] == 5:
            xpdict['Prayer'] = skill['xp']
        elif skill['id'] == 6:
            xpdict['Magic'] = skill['xp']
        elif skill['id'] == 7:
            xpdict['Cooking'] = skill['xp']
        elif skill['id'] == 8:
            xpdict['Woodcutting'] = skill['xp']
        elif skill['id'] == 9:
            xpdict['Fletching'] = skill['xp']
        elif skill['id'] == 10:
            xpdict['Fishing'] = skill['xp']
        elif skill['id'] == 11:
            xpdict['Firemaking'] = skill['xp']
        elif skill['id'] == 12:
            xpdict['Crafting'] = skill['xp']
        elif skill['id'] == 13:
            xpdict['Smithing'] = skill['xp']
        elif skill['id'] == 14:
            xpdict['Mining'] = skill['xp']
        elif skill['id'] == 15:
            xpdict['Herblore'] = skill['xp']
        elif skill['id'] == 16:
            xpdict['Agility'] = skill['xp']
        elif skill['id'] == 17:
            xpdict['Thieving'] = skill['xp']
        elif skill['id'] == 18:
            xpdict['Slayer'] = skill['xp']
        elif skill['id'] == 19:
            xpdict['Farming'] = skill['xp']
        elif skill['id'] == 20:
            xpdict['Runecrafting'] = skill['xp']
        elif skill['id'] == 21:
            xpdict['Hunter'] = skill['xp']
        elif skill['id'] == 22:
            xpdict['Construction'] = skill['xp']
        elif skill['id'] == 23:
            xpdict['Summoning'] = skill['xp']
        elif skill['id'] == 24:
            xpdict['Dungeoneering'] = skill['xp']
        elif skill['id'] == 25:
            xpdict['Divination'] = skill['xp']
        elif skill['id'] == 26:
            xpdict['Invention'] = skill['xp']
        elif skill['id'] == 27:
            xpdict['Archaeology'] = skill['xp']
    return xpdict


def skillxpp(player):
    allskills = json.loads(apiscrape(player)[11])
    xppdict = {}
    for skill in allskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            xppdict['Attack'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 1:
            xppdict['Defence'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 2:
            xppdict['Strength'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 3:
            xppdict['Constitution'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 4:
            xppdict['Ranged'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 5:
            xppdict['Prayer'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 6:
            xppdict['Magic'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 7:
            xppdict['Cooking'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 8:
            xppdict['Woodcutting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 9:
            xppdict['Fletching'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 10:
            xppdict['Fishing'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 11:
            xppdict['Firemaking'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 12:
            xppdict['Crafting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 13:
            xppdict['Smithing'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 14:
            xppdict['Mining'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 15:
            xppdict['Herblore'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 16:
            xppdict['Agility'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 17:
            xppdict['Thieving'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 18:
            xppdict['Slayer'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 19:
            xppdict['Farming'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 20:
            xppdict['Runecrafting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 21:
            xppdict['Hunter'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 22:
            xppdict['Construction'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 23:
            xppdict['Summoning'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 24:
            xppdict['Dungeoneering'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 25:
            xppdict['Divination'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 26:
            xppdict['Invention'] = round(skill['xp']/36073511, 2)
        elif skill['id'] == 27:
            xppdict['Archaeology'] = round(skill['xp']/13034431, 2)
    return xppdict


def skillxpp1(player):
    allskills = json.loads(apiscrape(player)[11])
    xpp1dict = {}
    for skill in allskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            xpp1dict['Attack'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 1:
            xpp1dict['Defence'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 2:
            xpp1dict['Strength'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 3:
            xpp1dict['Constitution'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 4:
            xpp1dict['Ranged'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 5:
            xpp1dict['Prayer'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 6:
            xpp1dict['Magic'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 7:
            xpp1dict['Cooking'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 8:
            xpp1dict['Woodcutting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 9:
            xpp1dict['Fletching'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 10:
            xpp1dict['Fishing'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 11:
            xpp1dict['Firemaking'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 12:
            xpp1dict['Crafting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 13:
            xpp1dict['Smithing'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 14:
            xpp1dict['Mining'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 15:
            xpp1dict['Herblore'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 16:
            xpp1dict['Agility'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 17:
            xpp1dict['Thieving'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 18:
            xpp1dict['Slayer'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 19:
            xpp1dict['Farming'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 20:
            xpp1dict['Runecrafting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 21:
            xpp1dict['Hunter'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 22:
            xpp1dict['Construction'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 23:
            xpp1dict['Summoning'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 24:
            xpp1dict['Dungeoneering'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 25:
            xpp1dict['Divination'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 26:
            xpp1dict['Invention'] = round(skill['xp']/80618654, 2)
        elif skill['id'] == 27:
            xpp1dict['Archaeology'] = round(skill['xp']/104273167, 2)
    return xpp1dict


def skillxpp2(player):
    allskills = json.loads(apiscrape(player)[11])
    xpp2dict = {}
    for skill in allskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            xpp2dict['Attack'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 1:
            xpp2dict['Defence'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 2:
            xpp2dict['Strength'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 3:
            xpp2dict['Constitution'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 4:
            xpp2dict['Ranged'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 5:
            xpp2dict['Prayer'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 6:
            xpp2dict['Magic'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 7:
            xpp2dict['Cooking'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 8:
            xpp2dict['Woodcutting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 9:
            xpp2dict['Fletching'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 10:
            xpp2dict['Fishing'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 11:
            xpp2dict['Firemaking'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 12:
            xpp2dict['Crafting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 13:
            xpp2dict['Smithing'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 14:
            xpp2dict['Mining'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 15:
            xpp2dict['Herblore'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 16:
            xpp2dict['Agility'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 17:
            xpp2dict['Thieving'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 18:
            xpp2dict['Slayer'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 19:
            xpp2dict['Farming'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 20:
            xpp2dict['Runecrafting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 21:
            xpp2dict['Hunter'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 22:
            xpp2dict['Construction'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 23:
            xpp2dict['Summoning'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 24:
            xpp2dict['Dungeoneering'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 25:
            xpp2dict['Divination'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 26:
            xpp2dict['Invention'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 27:
            xpp2dict['Archaeology'] = round(skill['xp']/200000000, 2)
    return xpp2dict


def skillxpc(player):
    allskills = json.loads(apiscrape(player)[11])
    xpcdict = {}
    for skill in allskills:
        skill['xp'] = "{:,}".format(skill['xp']/10)
        if skill['id'] == 0:
            xpcdict['Attack'] = skill['xp']
        elif skill['id'] == 1:
            xpcdict['Defence'] = skill['xp']
        elif skill['id'] == 2:
            xpcdict['Strength'] = skill['xp']
        elif skill['id'] == 3:
            xpcdict['Constitution'] = skill['xp']
        elif skill['id'] == 4:
            xpcdict['Ranged'] = skill['xp']
        elif skill['id'] == 5:
            xpcdict['Prayer'] = skill['xp']
        elif skill['id'] == 6:
            xpcdict['Magic'] = skill['xp']
        elif skill['id'] == 7:
            xpcdict['Cooking'] = skill['xp']
        elif skill['id'] == 8:
            xpcdict['Woodcutting'] = skill['xp']
        elif skill['id'] == 9:
            xpcdict['Fletching'] = skill['xp']
        elif skill['id'] == 10:
            xpcdict['Fishing'] = skill['xp']
        elif skill['id'] == 11:
            xpcdict['Firemaking'] = skill['xp']
        elif skill['id'] == 12:
            xpcdict['Crafting'] = skill['xp']
        elif skill['id'] == 13:
            xpcdict['Smithing'] = skill['xp']
        elif skill['id'] == 14:
            xpcdict['Mining'] = skill['xp']
        elif skill['id'] == 15:
            xpcdict['Herblore'] = skill['xp']
        elif skill['id'] == 16:
            xpcdict['Agility'] = skill['xp']
        elif skill['id'] == 17:
            xpcdict['Thieving'] = skill['xp']
        elif skill['id'] == 18:
            xpcdict['Slayer'] = skill['xp']
        elif skill['id'] == 19:
            xpcdict['Farming'] = skill['xp']
        elif skill['id'] == 20:
            xpcdict['Runecrafting'] = skill['xp']
        elif skill['id'] == 21:
            xpcdict['Hunter'] = skill['xp']
        elif skill['id'] == 22:
            xpcdict['Construction'] = skill['xp']
        elif skill['id'] == 23:
            xpcdict['Summoning'] = skill['xp']
        elif skill['id'] == 24:
            xpcdict['Dungeoneering'] = skill['xp']
        elif skill['id'] == 25:
            xpcdict['Divination'] = skill['xp']
        elif skill['id'] == 26:
            xpcdict['Invention'] = skill['xp']
        elif skill['id'] == 27:
            xpcdict['Archaeology'] = skill['xp']
    return xpcdict


def charquests(player):
    return quests(player)

#$maxlevels
def maxcape(player):
    if apiscrape(player) == "Error":
        return "Error"
    allskills = json.loads(apiscrape(player)[11])
    maxlevel = 0
    for skill in allskills:
        if skill['level'] < 99:
            maxlevel += (99 - skill['level'])
    return maxlevel

#$maxxp
def maxxp(player):
    if apiscrape(player) == "Error":
        return "Error"
    allskills = json.loads(apiscrape(player)[11])
    xpreq = 0
    for skill in allskills:
        skill['xp'] /= 10
        if skill['id'] == 0:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 1:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 2:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 3:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 4:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 5:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 6:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 7:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 8:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 9:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 10:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 11:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 12:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 13:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 14:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 15:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 16:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 17:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 18:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 19:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 20:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 21:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 22:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 23:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 24:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 25:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
        elif skill['id'] == 26:
            if skill['xp'] < 36073511:
                xpreq += (36073511 - skill['xp'])
        elif skill['id'] == 27:
            if skill['xp'] < 13034431:
                xpreq += (13034431 - skill['xp'])
    return xpreq
