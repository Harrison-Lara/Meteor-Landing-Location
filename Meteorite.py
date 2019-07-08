########################################################################
#
# CS 101
# Program #4
# Name: Harrison Lara
# Email: hrlwwd@mail.umkc.edu
#
# PROBLEM:
# We need to obtain the two files from the user. One with the data and the other
# file to write the data we are searching for within the parameters to. Then we
# have to ask for the lat and long so we know what area and then the radius to
# look within as well. Then we will close the file and see if the user wants to
# go through the simulation again or not. 
#
# ALGORITHM:
# Greet user ‘Hello Space Enthusiast!’
# Ask user for input of file ‘Which file is holding your meteorite data?’ (try/except, function)
# Ask user for output file ‘Which file do you want to use to place the preferred data?’ (try/except, function)
# Encode the files fh = open("sample.txt", "r", encoding="utf¬8")
# Ask user for input of lat. and long. (try/except, split string into two degrees) (try/except, function)
# Longitude [180,-180] and Latitude [90,-90]
# 'Enter the Latitude and Longitude separated by a comma: ‘
# Ask user for input of ‘What is the radius in miles of meteorite landings?’
#
# deltaLong = long2 − long1 deltaLat = lat2 − lat1 a = (sin(deltaLat/2)) cos(lat1) cos(lat2) sin(deltaLong/2))
# 2 + c * c * ( 2 c = 2 * atan2(√a, √1 − a) d = 3961 * c # 3961 is the radius of the earth in miles
#
# Make sure the header of the input file is written to the output file
# Read input file to find the data that fits the users input and write to output file
# Ask user if they want to run the program again or not Y/YES/N/NO (try/except, function)
#
# ERROR HANDLING:
#
#
# OTHER COMMENTS:
#
########################################################################

# imports
import math

count = 0

    # distance calculation function
def distance(lat1, long1, lat2, long2):
        lat1 = math.radians(lat1)
        long1 = math.radians(long1)
        lat2 = math.radians(lat2)
        long2 = math.radians(long2)

        deltaLong = long2 - long1
        deltaLat = lat2 - lat1
        a = (math.sin((deltaLat / 2)) ** 2) + math.cos(lat1) * math.cos(lat2) * (math.sin((deltaLong / 2)) ** 2)
        c = (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))
        d = 3961 * c  # radius of the earth in miles
        return d

searching = True
while searching:
                
            # greet user
        print('Hello Space Enthusiast!')

            # ask for input file
        while True:
            try:
                askFile = open(input("Which file is holding your meteorite data?"), "r", encoding="utf-8")
                break

            except IOError and FileNotFoundError:
                print('The file does not exist')

            # Ask for output file
        while True:
            try:
                placeData = open(input('What file do you want to use to place the preferred data?'),'w')
                break
            except IOError and FileNotFoundError:
                print('The file does not exist')

            # ask for lat
        while True:
            try:
                lat1 = (float(input('Enter the first latitude: ')))
                if lat1 - 90 <= lat1 <= 90:
                    break
            except ValueError:
                print('You must enter coordinates within range')

            # ask for long
        while True:
            try:
                long1 = (float(input('Enter the first longitude: ')))
                if -180 <= long1 <= 180:
                    break
            except ValueError:
                print('You must enter coordinates within range')

            # ask for radius
        while True:
            try:
                radius = (float(input('What is the radius in miles you would like to search within?')))
                break
            except TypeError and ValueError:
                print('The radius must be a number')

        print(askFile.readline(),file=placeData)
        loop_is_active = True
        while loop_is_active == True:
            try:
                for line in askFile:    #slicing for long and lat in file
                    count += 1          #taking lat and long and doing calculation
                    meteorlist = line[161::].strip()
                    meteorlist = meteorlist.strip("(")
                    meteorlist = meteorlist.strip(")")
                    meteorlist = meteorlist.split(",")
                    meteorlist[0] = meteorlist[0].strip()
                    meteorlist[1] = meteorlist[1].strip()
                    meteorlist[0] = float(meteorlist[0])
                    meteorlist[1] = float(meteorlist[1])
                    meteorlat = meteorlist[0]
                    meteorlong = meteorlist[1]
                    if distance(lat1, long1, meteorlat, meteorlong) < radius:
                        if line[161::].strip() != "(0.0, 0.0)":
                            print(line, file=placeData)
                    if count == 45716:
                        loop_is_active = False

            except IndexError:
                continue

        askFile.close()
        placeData.close() #close files
                        

