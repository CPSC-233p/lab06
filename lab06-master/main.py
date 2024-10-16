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
            print("Filename: " + fileName )
            weatherDict = weather.read_data(filename = fileName)
            print(weatherDict)

        case '2':
            date = input("Enter date (YYYYMMDD): ")
            time = input("Enter time (hhmmss): ")
            temp = input("Enter temperature: ")
            hum = input("Enter humidity: ")
            rain = input("Enter rainfall: ")
            fullDate = str(date) + str(time)
            tempDict = {fullDate: {'t' : temp, 'h': hum, 'r': rain}}
            weather.write_data(data = tempDict, filename = fileName)
        
        case '3':
            date = input("Enter date (YYYMMDD): ")
            r = weather.report_daily(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205')
            # dailyReport = weather.report_daily(data = weatherDict, date = date)
            print(r)

        case '4':
            historicalReport = weather.report_historical(data = weatherDict)

        case '5':
            break

        case _:
            break