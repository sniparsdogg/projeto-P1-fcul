# Drone Delivery Project - FCUL
Following the project sheet, this project consists of taking two input files (drone list and parcels requested), assigning a drone to each parcel and creating two output files: a timetable for the deliveries and an updated drone list.

## How does it work?
For a drone to be assigned to a parcel, they have to:
- Be in the location of the parcel
- Be able to take the weight of the parcel
- Have enough battery life to get there and back to the base
- Make sure that the distance of the parcel doesn't exceed its max distance

If more than one drone is assigned to a parcel, they go through some tiebreakers. Thus, the assigned drone is the one that:
- Is available earlier
- Has the most battery life
- Has the least mileage

If no drone satisfies these conditions, the respective parcel is cancelled.
