import json

def groupByDate(date):
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
        if date == x['date']:
            dateNew = x['date'].split('-')
            ans = x['answers']
            day = int(dateNew[2])
            year = int(dateNew[0])
            month = getMonth(int(dateNew[1]))
            suf = suffix(day)
            title = f'Connections #{ident} - {month} {day}{suf}, {year}'
            output = {
                'id': ident,
                'date': date,
                'title': title,
                'answers': ans
            }
            return output
        
        

        
    return None;
    

        
        