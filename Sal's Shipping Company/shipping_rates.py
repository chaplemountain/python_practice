premium_ground_shipping = 125

def ground_shipping(weight):
  if (weight <= 2):
    return weight * 1.50 + 20
  elif (weight <= 6):
    return weight * 3 + 20
  elif (weight <= 10):
    return weight * 4 + 20
  else:
    return weight * 4.75 + 20

def drone_shipping(weight):
  if (weight <= 2):
    return weight * 4.5
  elif (weight <= 6):
    return weight * 9
  elif (weight <= 10):
    return weight * 12
  else:
    return weight * 14.25

def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  if (ground < drone and ground < premium_ground_shipping):
    return "Ground Shipping is the cheapest @ $" + str(ground)
  elif (drone < ground and drone < premium_ground_shipping):
    return "Drone Shipping is the cheapest @ $" + str(drone)
  else:
    return "Premium Ground Shipping is the cheapest @ $" + str(premium_ground_shipping)
  
ground = ground_shipping(8.4)
print(ground)

drone = drone_shipping(1.5)
print(drone)

test1 = cheapest_shipping(4.8)
test2 = cheapest_shipping(41.5)
print(test1)
print(test2)

