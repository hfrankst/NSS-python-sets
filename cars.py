showroom = set(['Grand Cherokee', 'Yukon', 'Tahoe', 'M5', 'Tahoe'])
print(len(showroom)) #showing the length of the showroom
print(showroom) #prints the showroom set, and doesn't print repeated items in the set
showroom.update(['Prius', 'F-150']) # adding to the showroom
print(showroom)
showroom.discard('Prius') # removes item from the set
print(showroom)

junkyard = set(['Beetle', 'Corvette', 'Yukon', 'M5', 'Toureg', 'Impala', 'AMG'])
print('These cars are in both sets: ' + str(junkyard.intersection(showroom))) #showing the shared items between the sets

print(showroom.union(junkyard)) # combining the two sets into a larger one
