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
#Create a variable pointing to the data file
file_name = './Data/Raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Create two empty dictionary objects
date_dict = {}
coord_dict = {}

#Iterate through all lines in the line list
for lineString in line_list:
    #First way of iterating:
    if lineString[0]== '#' or lineString[0]=='u' : 
        continue
        
    #If first character is within this tuple, will evaluate to true and continue
    #if lineString[0]==("#","u"):
        #continue
    

    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    #if obs_lc not in ("1", "2", "3"):
        #continue
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #Print the location of sara if lc is 1,2, or 3
    if obs_lc in ("1", "2", "3"):
        print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat, obs_lon) #created a tuple form the lat, lon

    