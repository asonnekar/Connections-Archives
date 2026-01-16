import json


with open('connections.json', 'r') as file:
    data = json.load(file)

def suffix(date):
    if date== 11:
        return 'th'
    date = date %10
    if date == 1:
        return 'st'
    elif date == 2:
        return 'nd'
    elif date ==3:
        return 'rd'
    else:
        return 'th'
    

def getMonth(month):
    months = ['January', 'February', 'March', 'April','May','June','July','August','September', 'October', 'November','December']
    return months[month-1]
    
date_list = []
for x in data:
    ident = x['id']
    date = x['date'].split('-')

    month = getMonth(int(date[1]))
    day = int(date[2])
    year = int(date[0])
    suf = suffix(day)
    ans = x['answers']
    date_list.append(f'Connections #{ident} - {month} {day}{suf}, {year}')

    yellow = ans[0]
    green = ans[1]
    blue= ans[2]
    purple= ans[3]



    yellow_group = yellow['group']
    green_group = green['group']
    blue_group = blue['group']
    purple_group = purple['group']

    yellow_ans = yellow['members']
    green_ans = green['members']
    blue_ans = blue['members']
    purple_ans = purple['members']
    print(date_list)
    

