# Program inpu
cars = 100
people_per_car = 4
drivers = 30
passengers = 90

# Compute the dependent values
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * people_per_car
average_people_per_car = ( drivers + passengers ) / cars_driven
people_in_last_car = ( drivers + passengers - 1 ) % people_per_car + 1

# Output the results
print("There are", cars, "cars available.") 
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.") 
print("We can transport", carpool_capacity, "people today.") 
print("We have", passengers, "to carpool today.") 
print("We need to put about", average_people_per_car, "in each car.")
print("There are", people_in_last_car, "people in the last car.")
