"" '' # Objectives
"" '' # Understand the difference between keys and value
"" '' # Understand what is a record(database)
"" '' # Use keys and values to create a dictionary data structure

"" '' # Notes:

"" '' # Read data structures and record for 2 minutes
"" '' # Data structures are used to store data in an organised and accessible way. 
"" '' # A list is a data structure.  Another example of a data structure is a record.  
"" '' # You might have heard of the word record if you have ever created a database before. 

"" '' # A record allows you to store a collection of attributes for a single entity.
"" '' # Data structure: record: An entity can be any object, place, person, or thing. 
"" '' # Attributes are properties or characteristics of that entity.  
"" '' # Attributes are sometimes referred to as fields. 




"To Do: Predict, then Run, and then Investigate"
# create a dictionary 
dict1 = {"fname":"James Bond", "address":"Secret", "interests":"Spying", "age":42}
print(dict1) # prints all in above line 
print(dict1["address"]) # Secret 

# example on use from songs project 
songsDict = {"SongID":2, "Title":"Jam", "Artist":"Kelly", "Genre":"Rap"}
print(songsDict["Genre"])

"Using dictionary methods"
print("\n")
# D.items() -> a set-like object providing a view on D's items
print(dict1.items()) # method will return everything in the dictionary 
dItems = songsDict
print(dItems)

# D.keys() -> a set-like object providing a view on D's keys
print("\n")
dKeys = dict1.keys()
print(dKeys)

# D.values() -> an object providing a view on D's values
print("\n")
dVals = dict1.values()
print(dVals) 

# iterate over dictionary key value pairs 
for aKey, aValue in dict1.items():
    print(f"\nKey: {aKey} and value: {aValue}")

for aKey in dict1.keys():
    print(f"\nKey: {aKey}")

for aValue in dict1.values():
    print(f"\n value: {aValue}")

# update a dictionary
dict1.update(songsDict) # take all key value pairs in songDict and insert them into dict1 dictionary 
print(dict1)

# update a dictionary
dict1.update({"somekey": "somevalue"}) # whatever content you want will be added 
print(dict1)


# remove items from dictionary 
dict1.pop("fname") # removed the key value pairs on the key provided 
print(dict1) 

dict1.popitem() # removed the last key value pairs from the dictionary 
print(dict1) # prints {} empty  dictionary because it has all been deleted 

dict1.clear() # delete all key pairs 
print(dict1)