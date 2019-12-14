# 2019-2020 Programação 1 (LTI)
# Grupo 30
# 55371 Augusto Gouveia
# 54983 Carlota Valério

import sys
import readFiles
import dateTime
import organize
import constants
import writeFiles


def allocate(fileNameDrones, fileNameParcels):
    """
    Assign given drones to given parcels.
    
    Requires: fileNameDrones, fileNameParcels are str, with the names
    of the files representing the list of drones and parcels, respectively,
    following the format indicated in the project sheet.
    Ensures: Two output files, respectively, with the listing of scheduled
    transportation of parcels and the updated listing of drones, following the format
    and naming convention indicated in the project sheet.
    """
    fileNameDate = fileNameDrones[20:].strip(".txt") + "-" + fileNameDrones[17:19] + "-" + fileNameDrones[12:16]
    fileNameHour = fileNameDrones[6:8] + ":" + fileNameDrones[9:11]

    droneList = readFiles.readlistdrones(fileNameDrones)  # this is the list of the drones from the drone file
    parcelsList = readFiles.readlistparcels(fileNameParcels)  # this is the list of the parcels from the parcel file
    header = readFiles.readHeader(fileNameDrones)
    droneAssignment = []  # this will be the list of parcels with assigned drones that will be sent to the timetable
    droneAssignmentCancelled = []  # this will be the list of cancelled parcels that will be sent to the timetable

    for i in parcelsList:
        # assign the available drones for each delivery
        availableDroneList = []
        for d in droneList:
            if constants.getLocationParcel(i) == constants.getLocationDrone(d):   # the drone must be located in the
                # same zone as the request
                totalDistance = int(constants.getDistanceParcel(i))*2
                droneRange = float(constants.getMaxDistanceDrone(d))*1000
                if totalDistance <= droneRange:  # the drone must have enough range to get to the request location
                    # and come back
                    packageWeight = int(constants.getWeightParcel(i))
                    droneMaxWeight = int(constants.getMaxWeightDrone(d))
                    if packageWeight <= droneMaxWeight:  # the drone must be able to take the weight of the package
                        deliveryDistance = int(constants.getDistanceParcel(i))
                        droneMaxDistance = int(constants.getMaxDistanceDrone(d))
                        if deliveryDistance <= droneMaxDistance:  # the distance of the request can't be bigger than
                            # the drone's max distance
                            availableDroneList.append(d)  # if it meets all these requirements, the drone is assigned
                            # to its respective parcel

        delivery = []
        if len(availableDroneList) == 1:  # if there is only one drone assigned then that will be the drone to use
            delivery = availableDroneList[0].copy()
        elif len(availableDroneList) > 1:  # if there is more than one drone assigned we have to pick only one
            delivery = organize.untieDrones(availableDroneList).copy()  # unties the drones and picks the winner

        if delivery:  # if there is an assigned drone
            # The delivery date/hour will the the latest one between the request date/hour and the drone availability
            if dateTime.getHours(constants.getHourDrone(delivery)) < dateTime.getHours(constants.getHourParcel(i)):
                delivery[7] = constants.getHourParcel(i)
            elif dateTime.getHours(constants.getHourDrone(delivery)) == dateTime.getHours(constants.getHourParcel(i)):
                if dateTime.getMinutes(delivery[7]) < dateTime.getMinutes(constants.getHourParcel(i)):
                    delivery[7] = constants.getHourParcel(i)

            # we need to verify if the time needed to deliver the parcel exceeds the closing time (20:00)
            # if it does, then the date/time is set to the next day at the opening time (08:00)
            delivery[6] = dateTime.finalDateTimeCustomer(constants.getDateDrone(delivery), constants.getHourDrone(delivery), constants.getTimeParcel(i))[0]
            delivery[7] = dateTime.finalDateTimeCustomer(constants.getDateDrone(delivery), constants.getHourDrone(delivery), constants.getTimeParcel(i))[1]

            # now we assign the date, hour, name of the parcel and name of the drone assigned to a new list
            # this will be the list that will be sent to the timetable
            droneAssignment.append([constants.getDateDrone(delivery), constants.getHourDrone(delivery), constants.getNameParcel(i), constants.getNameDrone(delivery)])

            # now we need to update the mileage and range on the drone assigned
            newMileage = float(constants.getMileageDrone(delivery)) + (float(constants.getDistanceParcel(i))*2)/1000
            newRange = float(constants.getRangeDrone(delivery)) - (float(constants.getDistanceParcel(i))*2)/1000

            # here we're going to search for every drone on the drone list for the one that was assigned to the delivery
            # and update its available date, time, mileage and range
            for d in droneList:
                if constants.getNameDrone(delivery) == constants.getNameDrone(d):
                    d[6] = dateTime.finalDateTime(constants.getDateDrone(delivery), constants.getHourDrone(delivery), constants.getTimeParcel(i))[0]  # date
                    d[7] = dateTime.finalDateTime(constants.getDateDrone(delivery), constants.getHourDrone(delivery), constants.getTimeParcel(i))[1]  # time
                    d[4] = round(newMileage, 1)  # mileage
                    d[5] = round(newRange, 1)  # range

        else:  # if no drone was assigned to the delivery we're going to join the parcel to the cancelled list
            droneAssignmentCancelled.append([constants.getDateParcel(i), constants.getHourParcel(i), constants.getNameParcel(i), "cancelled"])

    # now we need to order these lists
    # the parcel list will be ordered by assigned date/hour and lexicographically, both ascending
    droneAssignment = organize.orderTimetable(droneAssignment, droneAssignmentCancelled)
    # the drone list will be ordered by availability, remaining range and lexicographically, all ascending
    droneList = organize.orderDroneList(droneList)

    # finally, these tables are sent to the functions that create the output files
    writeFiles.writeTimetable(header, droneAssignment, fileNameDate, fileNameHour)
    writeFiles.writeDroneList(header, droneList, fileNameDate, fileNameHour)


inputFileName1, inputFileName2 = sys.argv[1:]

try:
    headerDrones = readFiles.readHeader(inputFileName1)
    headerParcels = readFiles.readHeader(inputFileName2)

    # these lines will extract the date and time from the file names
    # this is done by slicing the string to get only the relevant information
    droneFileNameHour = inputFileName1[6:8] + ":" + inputFileName1[9:11]
    droneFileNameDate = inputFileName1[20:].strip(".txt")+ "-" + inputFileName1[17:19] + "-" + inputFileName1[12:16]
    parcelsFileNameHour = inputFileName2[7:9] + ":" + inputFileName2[10:12]
    parcelsFileNameDate = inputFileName1[20:].strip(".txt") + "-" + inputFileName1[17:19] + "-" + inputFileName1[12:16]

    # the program runs two assertion tests to make sure the header info is consistent with the file name info
    # if not, it throws an input error
    assert droneFileNameDate == constants.getDateHeader(headerDrones) and droneFileNameHour == constants.getHourHeader(headerDrones), "Input error: name and header inconsistent in file " + inputFileName1 + "."
    assert parcelsFileNameDate == constants.getDateHeader(headerParcels) and droneFileNameHour == constants.getHourHeader(headerParcels), "Input error: name and header inconsistent in file " + inputFileName2 + "."

    # the program runs one more assertion test to make sure the headers from the drones and parcels files are consistent
    # with each other
    # if not, it throws an input error
    assert constants.getHourHeader(headerDrones) == constants.getHourHeader(headerParcels) and constants.getDateHeader(headerDrones) == constants.getDateHeader(headerParcels) and constants.getCompanyHeader(headerDrones) == constants.getCompanyHeader(headerParcels), "Input error: inconsistent files " + inputFileName1 +" and "+ inputFileName2 + "."

    # if everything checks out, it begins to assign the drones to the parcels
    allocate(inputFileName1, inputFileName2)

# if an error is thrown, the program will print the message error to the screen
except AssertionError as error:
    print(error)
