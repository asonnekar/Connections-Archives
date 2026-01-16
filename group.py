import json

def groupByDate():
    with open('connections.json', 'r') as file:
        data = json.load(file)

    def suffix(date):
        if date>=11 and date <=13:
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
    
    connections_dict = dict()   

    date_list = []
    for x in data:
        ident = x['id']
        date = x['date'].split('-')

        month = getMonth(int(date[1]))
        day = int(date[2])
        year = int(date[0])
        suf = suffix(day)
        ans = x['answers']
        date = f'Connections #{ident} - {month} {day}{suf}, {year}'
        date_list.append(date)

        connections_dict[date] = ans
    print(connections_dict)
    return connections_dict

        
        