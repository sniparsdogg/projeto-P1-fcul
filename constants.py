# 2019-2020 Programação 1 (LTI)
# Grupo 30
# 55371 Augusto Gouveia
# 54983 Carlota Valério

def getNameDrone(drone):
    """
    Returns the name of the drone.

    Requires: a list representing the drone.
    Ensures: a string representing the drone's name.
    """
    return drone[0]


def getLocationDrone(drone):
    """
    Returns the location of the drone.

    Requires: A list representing the drone.
    Ensures: A string representing the drone's location.
    """
    return drone[1]


def getMaxWeightDrone(drone):
    """
    Returns the max weight of the drone.

    Requires: A list representing the drone.
    Ensures: A string representing the drone's max weight.
    """
    return drone[2]


def getMaxDistanceDrone(drone):
    """
    Returns the max distance of the drone.

    Requires: A list representing the drone.
    Ensures: A string representing the drone's max distance.
    """
    return drone[3]


def getMileageDrone(drone):
    """
    Returns the mileage of the drone.

    Requires: A list representing the drone.
    Ensures: A string representing the drone's mileage.
    """
    return drone[4]


def getRangeDrone(drone):
    """
    Returns the range of the drone.

    Requires: A list representing the drone.
    Ensures: A string representing the drone's range.
    """
    return drone[5]


def getDateDrone(drone):
    """
    Returns the availability date of the drone.

    Requires: A list representing the drone.
    Ensures: A string representing the drone's availability date.
    """
    return drone[6]


def getHourDrone(drone):
    """
    Returns the availability hour of the drone.

    Requires: A list representing the drone.
    Ensures: A string representing the drone's availability.
    """
    return drone[7]


def getNameParcel(parcel):
    """
    Returns the name of the parcel.

    Requires: A list representing the parcel.
    Ensures: A string representing the parcel's name.
    """
    return parcel[0]


def getLocationParcel(parcel):
    """
    Returns the location of the parcel.

    Requires: A list representing the parcel.
    Ensures: A string representing the parcel's location.
    """
    return parcel[1]


def getDateParcel(parcel):
    """
    Returns the requested of the parcel.

    Requires: A list representing the parcel.
    Ensures: A string representing the parcel's requested date.
    """
    return parcel[2]


def getHourParcel(parcel):
    """
    Returns the requested hour of the parcel.

    Requires: A list representing the parcel.
    Ensures: A string representing the parcel's requested hour.
    """
    return parcel[3]


def getDistanceParcel(parcel):
    """
    Returns the distance of the parcel.

    Requires: A list representing the parcel.
    Ensures: A string representing the parcel's distance.
    """
    return parcel[4]


def getWeightParcel(parcel):
    """
    Returns the weight of the parcel.

    Requires: A list representing the parcel.
    Ensures: A string representing the parcel's weight.
    """
    return parcel[5]

def getTimeParcel(parcel):
    """
    Returns the time required to deliver the parcel.

    Requires: A list representing the parcel.
    Ensures: A string representing the parcel's required time to deliver.
    """
    return parcel[6]


def getHourHeader(header):
    """
    Returns the hour of the given header's information.

    Requires: A list representing the header's information.
    Ensures: A string representing the header's hour.
    """
    return header[0]


def getDateHeader(header):
    """
    Returns the date of the given header's information.

    Requires: A list representing the header's information.
    Ensures: A string representing the header's date.
    """
    return header[1]


def getCompanyHeader(header):
    """
    Returns the company of the given header's information.

    Requires: A list representing the header's information.
    Ensures: A string representing the header's company.
    """
    return header[2]