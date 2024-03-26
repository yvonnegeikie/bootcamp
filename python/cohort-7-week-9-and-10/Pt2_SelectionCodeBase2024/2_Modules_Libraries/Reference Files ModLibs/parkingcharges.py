import time # Import (module) time

startTimeSecs = time.time()
print(startTimeSecs)
formattedStarTime = time.ctime(startTimeSecs)
print(formattedStarTime)
hours = int(input("Input hours of parking required ( 2, 4, or 12)"))
numInSecs = hours * 60 * 60
if hours == 2:
    parkingCharge = 5.00
elif hours == 4:
    parkingCharge = 8.00
else:
    parkingCharge =15.00
endTimeInSecs = startTimeSecs + numInSecs
print("\nTime now :", formattedStarTime )
endFormattedTimed = time.ctime(endTimeInSecs)
print("Expires On: ", endFormattedTimed)
print(f"Parking Charge = {parkingCharge}")



"Add notes below to explain the application in your own words"