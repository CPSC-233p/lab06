import json
from calendar import month_name

def read_data(filename=''):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    

def write_data(data={}, filename=''):
    with open(filename, 'w') as f:
        json.dump(data, f)


def max_temperature(data={}, date=''):
    temp = []
    for key, value in data.items():
        if date in key:
            #handle the value to get temp
            temp.append(value['t'])
    temp.sort()
    return temp[len(temp) - 1]

def min_temperature(data={}, date=''):
    temp = []
    for key, value in data.items():
        if date in key:
            #handle the value to get temp
            temp.append(value['t'])
    temp.sort()
    return temp[0]

def max_humidity(data={}, date=''):
    temp = []
    for key, value in data.items():
        if date in key:
            #handle the value to get temp
            temp.append(value['h'])
    temp.sort()
    return temp[len(temp) - 1]

def min_humidity(data={}, date=''):
    temp = []
    for key, value in data.items():
        if date in key:
            #handle the value to get temp
            temp.append(value['h'])
    temp.sort()
    return temp[0]

def tot_rain(data={}, date=''):
    temp = []
    for key, value in data.items():
        if date in key:
            #handle the value to get temp
            temp.append(value['r'])
    rainSum = sum(temp)
    return rainSum

def report_daily(data={}, date=''):

    printString = ""

    printString += "========================= DAILY REPORT ========================\n"
    printString += "Date                      Time  Temperature  Humidity  Rainfall\n"
    printString += "====================  ========  ===========  ========  ========\n"

    for key, value in data.items():
        if key == None:
            continue
        if date in key:
            #parsing the date as ints:
            year = key[0:4]
            month = int(key[4:6]) #make it an int to use the month_name func
            day = int(key[6:8])
            hour = key[8:10]
            minute = key[10:12]
            second = key[12:14]
            temp = value['t']
            hum = value['h']
            rain = value['r']
            # printString += month_name[month] + " " + str(day) + ", " + year + "      " + hour.zfill(2) + ":" + minute.zfill(2) + ":" + second.zfill(2) + "           " + str(temp) + "        " + str(hum) + "      " + f"{rain:.2f}" + "\n"
            printString += f"{month_name[month]} {str(day)}, {year}      {hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}           {str(temp)}        {str(hum)}      {rain:.2f}\n"

    # if printString.endswith("\n"):
    #     return printString[:-1]
    return printString

def report_historical(data = {}):
    
    noRepeats = []
    temp = ""   
    temp += "============================== HISTORICAL REPORT ===========================\n"
    temp += "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    temp += "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    temp += "====================  ===========  ===========  ========  ========  ========\n"
    
    for key, value in data.items():
        date = key[0:8]
        if date in noRepeats:
            continue
        year = date[0:4]
        month = int(date[4:6])
        day = int(date[6:8])

        minTemp = min_temperature(data = data, date = date)
        maxTemp = max_temperature(data = data, date = date)
        minHum = min_humidity(data = data, date = date)
        maxHum = max_humidity(data = data, date = date)
        totRain = tot_rain(data = data, date = date)
        # totalString = f"{month_name[month]:<10} {str(day):<2}, {year:<4}   {minTemp:>7} {maxTemp:>12} {minHum:>10} {maxHum:>9} {f"{totRain:.2f}":>8}\n"
        totalString = f"{month_name[month]} {str(day)}, {year}               {minTemp}           {maxTemp}        {minHum}        {maxHum}      {totRain:.2f}\n"

        temp += totalString
        noRepeats.append(date)
    return temp
