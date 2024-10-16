import json
from calendar import month_name

def read_data(filename=''):
    try:
        with open(filename) as f:
            readData = f.read()
            return json.dumps(readData)
    except FileNotFoundError:
        return {}

def write_data(data={}, filename=''):
    with open(filename) as f:
        toJson = json.dumps(data)
        writeData = f.write(toJson)

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
    print("========================= DAILY REPORT========================")
    print("Date                      Time Temperature  Humidity  Rainfall")
    print("====================  ======== ===========  ========  ========")

    printString = ""

    for key, value in data.items():
        if date in key:
            #parsing the date as ints:
            year = key[0:4]
            month = int(key[4:6]) #make it an int to use the month_name func
            day = key[6:8]
            hour = key[8:10]
            minute = key[10:12]
            second = key[12:14]
            temp = value['t']
            hum = value['h']
            rain = value['r']
            # print(month_name[month] + " " + day + ", " + year + "      " + hour.zfill(2) + ":" + minute.zfill(2) + ":" + second.zfill(2))
            # print(str(temp) + "        " + str(hum) + "        " + str(f"{rain:.2f}"))

            printString += month_name[month] + " " + day + ", " + year + "     " + hour.zfill(2) + ":" + minute.zfill(2) + ":" + second.zfill(2) + "          " + str(temp) + "        " + str(hum) + "      " + str(f"{rain:.2f}" + "\n")
    return printString

def report_historical(data = {}):
    print("============================== HISTORICAL REPORT ===========================")
    print("	              Minimum      Maximum      Minumum   Maximum   Total")
    print("Date                  Temperature  Temperature  Humidity  Humidity  Rainfall")
    print("====================  ===========  ===========  ========  ========  ========")
    
    noRepeats = []
    temp = ""   
    
    for key, value in data.items():
        date = key[0:9]
        if date in noRepeats:
            continue
        year = date[0:4]
        month = int(date[4:6])
        day = date[6:8]

        minTemp = min_temperature(data = data, date = date)
        maxTemp = min_temperature(data = data, date = date)
        minHum = min_temperature(data = data, date = date)
        maxHum = min_temperature(data = data, date = date)
        totRain = tot_rain(data = data, date = date)
        totalString = f"{month_name[month]:<10} {day:<2}, {year:<4}   {minTemp:>7} {maxTemp:>12} {minHum:>10} {maxHum:>9} {totRain:>8}\n"
        # print(totalString)
        temp += totalString
        noRepeats.append(date)

    return temp

