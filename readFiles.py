# 2019-2020 Programação 1 (LTI)
# Grupo 30
# 55371 Augusto Gouveia
# 54983 Carlota Valério


def readlistparcels(fileName):
    """
    Reads the parcels' file and assigns each parcel to a sub-list, returning a list of all the parcels in the file.

    Requires: A string representing the file name.
    Ensures: A list representing the parcels.
    """
    
    file = open(fileName, 'r')
    outputparcelslist = []

    for i in range(7):
        file.readline()
    
    while i := file.readline():
        if i != "\n":
            destinatary = i.rstrip().split(", ")
            outputparcelslist.append(destinatary)

    file.close()
    return outputparcelslist



def readlistdrones(fileName):
    """
    Reads the drones' file and assigns each drone to a sub-list, returning a list of all the drones in the file.

    Requires: A string representing the file name
    Ensures: A list representing the drones.
    """

    file = open(fileName, 'r')
    
    droneslist = []
    for i in range(7):
        file.readline()

    while i := file.readline():
        if i != "\n":

            drone = i.rstrip().split(", ")
            droneslist.append(drone)
    file.close()
    return droneslist


def readHeader(fileName):
    """
    Reads the header from a given file and returns a list representing the header's main information.

    Requires: A string representing the file name.
    Ensures: A list representing the header's main information (time, date and company).
    """
    
    file = open (fileName, 'r')
    
    file.readline()
    hours = file.readline().strip().replace("h", ':')
    file.readline()
    date = file.readline().strip()
    file.readline()
    company = file.readline().replace("\n", '').strip(' ')

    information = (hours, date, company)
    file.close()
    return list(information)
