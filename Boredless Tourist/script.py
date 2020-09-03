destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#pull destination index
def get_destination_index(destination):
   destination_index = destinations.index(destination)
   return destination_index

#get traveler location
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

#test traveler location function
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
