# 2019-2020 Programação 1 (LTI)
# Grupo 30
# 55371 Augusto Gouveia
# 54983 Carlota Valério

import dateTime as dt
import constants as c


def untieDrones(droneList):
    """
    Unties the drones assigned to a parcel and returns the winner

    Requires: A list representing the drones assigned
    Ensures: A list representing the winning drone
    """

    # untie factor: the one first available
    if dt.getDay(droneList[0][6]) == dt.getDay(droneList[1][6]):
        if dt.getHours(droneList[0][7]) <= dt.getHours(droneList[1][7]):
            if dt.getMinutes(droneList[0][7]) < dt.getMinutes(droneList[1][7]):
                return droneList[0]
            elif dt.getMinutes(droneList[0][7]) > dt.getMinutes(droneList[1][7]):
                return droneList[1]
        elif dt.getHours(droneList[0][7]) > dt.getHours(droneList[1][7]):
            return droneList[1]
    elif dt.getDay(droneList[0][6] < dt.getDay(droneList[1][6])):
        return droneList[0]
    elif dt.getDay(droneList[0][6] > dt.getDay(droneList[1][6])):
        return droneList[1]

    # untie factor: the one with the most range
    if float(droneList[0][5]) > float(droneList[1][5]):
        return droneList[0]
    elif float(droneList[0][5]) < float(droneList[1][5]):
        return droneList[1]

    # untie factor: the one with the least mileage
    if float(droneList[0][4]) < float(droneList[1][4]):
        return droneList[0]
    elif float(droneList[0][4]) > float(droneList[1][4]):
        return droneList[1]

    # untie factor: first one ordered lexicographically
    else:
        return droneList[0]


def orderTimetable(parcelsAssigned, parcelsCancelled):
    """
    Sorts the lists with the cancelled and assigned parcels and returns a list with the correct order.

    Requires: parcelsAssigned and parcelsCancelled are both lists, representing the assigned and cancelled parcels
    respectively
    Ensures: A list following the order as indicated in the project sheet: first the ones cancelled, ordered
    lexicographically ascending, then the ones assigned, ordered by assigned date/hour and lexicographically, both
    ascending
    """
    timetable = []
    finalParcelsAssigned = parcelsAssigned.copy()
    finalParcelsCancelled = parcelsCancelled.copy()
    finalParcelsCancelled = sorted(finalParcelsCancelled, key=lambda x: (x[2]))  # sorts the cancelled parcels list
    # using the name as the key
    finalParcelsAssigned = sorted(finalParcelsAssigned, key=lambda x: (dt.getDay(x[0]), dt.getHours(x[1]), dt.getMinutes(x[1]), x[2]))
    # sorts the assigned parcels list using the date, time and name as keys

    # then aggregates both lists on one final list
    timetable.extend(finalParcelsCancelled)
    timetable.extend(finalParcelsAssigned)
    return timetable

def orderDroneList(droneList):
    """
    Sorts the updated drone list and returns a list with the correct order

    Requires: a list representing the drones with the updated values
    Ensures: a list following the order as indicated in the project sheet: sorted by date/time available, range and
    lexicographically, all ascending
    """
    orderedDrones = droneList.copy()
    orderedDrones = sorted(orderedDrones, key=lambda x: (dt.getDay(c.getDateDrone(x)), dt.getHours(c.getHourDrone(x)), dt.getMinutes(c.getHourDrone(x)), -float(c.getRangeDrone(x)), c.getNameDrone(x)))
    # sorts the ordered drones list using the date, time, range and name as keys
    return orderedDrones
