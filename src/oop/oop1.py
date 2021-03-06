# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# class vehicle
class Vehicle:
    pass

# class FlightVehicle
class FlightVehicle(Vehicle):
    pass

# class Starship
class Starship(FlightVehicle):
    pass

# class GroundVehicle
class GroundVehicle(Vehicle):
    pass

# class Airplane
class Airplane(FlightVehicle):
    pass

# class Car
class Car(GroundVehicle):
    pass

# class Car
class Motorcycle(GroundVehicle):
    pass