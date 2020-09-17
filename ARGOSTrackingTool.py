#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Taylor Stoni (taylor.stoni@duke.edu)
# Date:   Fall 2020
#--------------------------------------------
#reading this line into a variable name
#pretend we read one line of data from the file
lineString= '20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0'
print(lineString)

#split the string into a list of data items 
lineData = lineString.split()

#extract items in list into variables 
record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

#Print the location of Sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, Lon:{obs_lon} on {obs_date}")


