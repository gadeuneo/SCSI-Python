#James Gardner

tripDist = 226 # total miles in the trip
bikeSpeed = 15 # typcial bicycling speed miles per hour

tripTime = tripDist / bikeSpeed # in hours
tripHours = int(tripTime)
tripMins = int ( round( (tripTime - tripHours) * 60) )
print
print "To bike", tripDist, "miles, at",
print bikeSpeed, "miles per hour,",
print "takes", tripHours, "hours and", tripMins, "minutes"



