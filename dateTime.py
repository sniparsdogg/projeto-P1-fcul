# 2019-2020 Programação 1 (LTI)
# Grupo 30
# 55371 Augusto Gouveia
# 54983 Carlota Valério

def getHours(time):
    """
    Returns the hour slice from the time string.

    Requires: A string representing the time.
    Ensures: An Integer representing the hour slice.
    """
    hour = time.split(":")[0]
    return int(hour)


def getMinutes(time):
    """
    Returns the minutes slice from the time string.

    Requires: A string representing the time.
    Ensures: An Integer representing the minutes slice.
    """
    minutes = time.split(":")[1]
    return int(minutes)


def getDay(date):
    """
    Returns the day slice from the date string.

    Requires: A string representing the date.
    Ensures: An Integer representing the day slice.
    """
    day = date.split("-")[2]
    return int(day)


def getMonth(date):
    """
    Returns the month slice from the date string.

    Requires: A string representing the date.
    Ensures: An Integer representing the month slice.
    """
    month = date.split("-")[1]
    return int(month)


def getYear(date):
    """
    Returns the year slice from the date string.

    Requires: A string representing the date.
    Ensures: An Integer representing the year slice.
    """
    year = date.split("-")[0]
    return int(year)


def sumMinutes(time,minutes):
    """
    Sums given minutes to a given time.

    Requires: Two strings, one with the time and another with the minutes to sum.
    Ensures: A string representing the new time.
    """
    addMinutes = int(minutes)
    addHours = 0

    finalHours = int(getHours(time))
    finalMinutes = int(getMinutes(time))

    if (addMinutes >= 60) :
        while (addMinutes >= 60):
            addMinutes -= 60
            addHours += 1
            finalHours += addHours
    finalMinutes += addMinutes
    if finalMinutes >= 60:
            finalMinutes -= 60
            finalHours += 1

    if finalHours < 10:
        finalHours = "0" + str(finalHours)

    if finalMinutes < 10:
        finalMinutes = "0" + str(finalMinutes)

    return str(finalHours) + ":" + str(finalMinutes)


def finalDateTimeCustomer(date, time, minutes):
    """
    Returns the final date/time for the timetable.

    Requires: date, time and minutes are strings, each representing the date, time and minutes to sum respectively.
    Ensures: The date and time at which the drone will start the parcel delivery.
    """

    deliveryHours = int(getHours(time))
    deliveryMinutes = int(getMinutes(time))
    deliveryYear = int(getYear(date))
    deliveryMonth = int(getMonth(date))
    deliveryDay = int(getDay(date))

    if (getHours(sumMinutes(time, minutes)) >= 20) and (getMinutes(sumMinutes(time, minutes))) > 0:
        deliveryDay += 1
        deliveryHours = "08"
        deliveryMinutes = "00"

        if deliveryDay > 30:
            deliveryDay = 1
            deliveryMonth += 1

        if deliveryMonth > 12:
            deliveryMonth = 1
            deliveryYear += 1

        if deliveryDay < 10:
            deliveryDay = str(0) + str(deliveryDay)

        finalDate = str(deliveryYear) + "-" + str(deliveryMonth) + "-" + str(deliveryDay)
        finalTime = str(deliveryHours) + ":" + str(deliveryMinutes)
        return finalDate, finalTime

    if int(deliveryHours) < 10:
        deliveryHours = "0" + str(deliveryHours)

    if int(deliveryMinutes) < 10:
        deliveryMinutes = "0" + str(deliveryMinutes)

    finalTime = str(deliveryHours) + ":" + str(deliveryMinutes)
    return date, finalTime


def finalDateTime(date,time,minutes):
    """
    Returns the final date/time for the updated drone table.

    Requires: date, time and minutes are strings, each representing the date, time and minutes to sum respectively.
    Ensures: The date and time at which the drone will be available for another delivery.
    """
    deliveryHours = int(getHours(time))
    deliveryMinutes = int(getMinutes(time))
    deliveryYear = int(getYear(date))
    deliveryMonth = int(getMonth(date))
    deliveryDay = int(getDay(date))

    addMinutes = int(minutes)
    addHours = 0
    
    if (addMinutes >= 60) :
 
        while (addMinutes >= 60):
            addMinutes -= 60
            addHours += 1
        deliveryHours += addHours
    deliveryMinutes += addMinutes
    if deliveryMinutes >= 60:
            deliveryMinutes -= 60
            deliveryHours += 1


    if (deliveryHours >= 20 and deliveryMinutes > 0):
        addHours += deliveryHours - 20
        deliveryHours = 8 + addHours
        deliveryMinutes = addMinutes
        deliveryDay += 1
        
    if (deliveryDay > 30):
        deliveryDay = 1
        deliveryMonth += 1

    if deliveryMonth > 12:
        deliveryMonth = 1
        deliveryYear += 1

    if deliveryDay < 10:
        deliveryDay = str(0)+str(deliveryDay)

    if deliveryHours < 10:
        deliveryHours = "0" + str(deliveryHours)

    if deliveryMinutes < 10:
        deliveryMinutes = "0" + str(deliveryMinutes)

    finalDate = str(deliveryYear) + "-" + str(deliveryMonth) + "-" + str(deliveryDay)
    finalTime = str(deliveryHours) + ":" + str(deliveryMinutes)
    return(finalDate, finalTime)

