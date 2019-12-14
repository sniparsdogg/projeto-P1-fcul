# 2019-2020 Programação 1 (LTI)
# Grupo 30
# 55371 Augusto Gouveia
# 54983 Carlota Valério

import constants as c
import dateTime


def writeTimetable(header, timetable, date, hour):
    """
    Creates a file representing the timetable.

    Requires: header and timetable are lists, each representing the header's information and the parcels assigned,
    respectively. date and hour are strings, each representing the date and time to use on the file, respectively.
    Ensures: An output file representing the timetable.
    """
    fileNameDate = date.split("-")
    fileNameHour = hour.split(":")
    fileName = "timetable" + fileNameHour[0] + "h" + fileNameHour[1] + "_" + fileNameDate[2] + "y" + fileNameDate[1] + "m" + fileNameDate[0] + ".txt "
    outFile = open(fileName, 'w')
    outFile.write("Time:\n")
    outFile.write(c.getHourHeader(header).replace(":", "h") + "\n")
    outFile.write("Day:\n")
    outFile.write(c.getDateHeader(header) + "\n")
    outFile.write("Company:\n")
    outFile.write(c.getCompanyHeader(header) + "\n")
    outFile.write("Timeline:\n")
    for i in timetable:
        count = 0
        string = ""
        for info in i:
            if count == 0:
                string += str(info).replace(" ", "")
            else:
                string += ", " + str(info)
            count += 1
        string += "\n"
        outFile.write(string)
    outFile.close()


def writeDroneList(header, droneList, date, hour):
    """
    Creates a file representing the updated drone list.

    Requires: header and droneList are lists, each representing the header's information and the updated drone list,
    respectively. date and hour are strings, each representing the date and time to use on the file, respectively.
    Ensures: An output file representing the updated drone list.
    """
    time = dateTime.sumMinutes(hour,30).split(":")
    fileNameDate = date.split("-")
    fileName = "drones" + time[0] + "h" + time[1] + "_" + fileNameDate[2] + "y" + fileNameDate[1] + "m" + fileNameDate[0] + ".txt"
    outFile = open(fileName, 'w')
    outFile.write("Time:\n")
    outFile.write(time[0] + "h" + time[1] + "\n")
    outFile.write("Day:\n")
    outFile.write(c.getDateHeader(header)+"\n")
    outFile.write("Company:\n")
    outFile.write(c.getCompanyHeader(header)+"\n")
    outFile.write("Drones:\n")
    for i in droneList:
        count = 0
        string = ""
        for info in i:
            if count == 0:
                string += str(info)
            else:
                string += ", " + str(info)
            count += 1
        string += "\n"
        outFile.write(string)
    outFile.close()