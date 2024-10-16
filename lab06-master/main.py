import weather


fileName = ''
weatherDict = {}

while True:

    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("5. Exit the program")

    choice = input()

    match str(choice):
        case '1':
            fileName = input("Enter data filename: ")
            weatherDict = weather.read_data(filename = fileName)

        case '2':
            date = input("Enter date (YYYYMMDD): ")
            time = input("Enter time (hhmmss): ")
            temp = input("Enter temperature: ")
            hum = input("Enter humidity: ")
            rain = input("Enter rainfall: ")
            fullDate = str(date) + str(time)
            tempDict = {fullDate: {'t' : temp, 'h': hum, 'r': rain}}
            weather.write_data(data = tempDict, filename = r'lab06-master\w.dat')
        
        case '3':
            date = input("Enter date (YYYMMDD): ")
            dailyReport = weather.report_daily(data = weatherDict, date = date)
            print(dailyReport)

        case '4':
            historicalReport = weather.report_historical(weatherDict)
            print(historicalReport)

        case '5':
            break

        case _:
            break
