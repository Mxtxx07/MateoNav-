from car import Car
from accountDrives import Driver
from accountUser import User
from route import Route
from payment import Payment

class Trip(Car, Driver, User, Route, Payment):
    idTrip    = int
    user      = User("", "", "", "", "")
    driver    = Driver("", "", "", "", "","")
    route     = Route("", "", "", "")
    payment   = Payment("", "", "", "" ,"")
    car       = Car("", "", "", "", "", "")

    def __init__(self, idTrip, user, driver, route, payment, car):
        self.idTrip    = idTrip
        self.user      = user
        self.driver    = driver
        self.route     = route
        self.payment   = payment
        self.car       = car