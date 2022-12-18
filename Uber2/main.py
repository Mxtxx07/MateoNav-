from account import Account
from accountUser import User
from accountDrives import Driver
from car import Car
from payment import Payment
from paymentCard import PaymentCard
from paymentCash import PaymentCash
from paymentUber import PaymentUber
from route import Route
from uberx import UberX
from uberXL import UberXL
from uberConfort import UberConfort
from uberFlash import UberFlash
from uberPet import UberPet
from trip import Trip


# EMPIEZA LA EJECUCION!!!

if __name__ == "__main__":
    
    print("Usuarios:")
    usuario1 = User(1, "David", 23, "davidgmail.com", "0923131234")
    print(vars(usuario1))
    
    usuario2 = User(2, "Marcos", 29, "marcosgmail.com", "0927354619")
    print(vars(usuario2))
    
    print("Drivers:")
    driver1  = Driver(1, "Manuel Perez", "Masculino", "0935264719", 36 ,"LTE234")
    print(vars(driver1))
    
    driver2  = Driver(2, "Lucas Erazo", "Masculino", "0932844719", 26 ,"ASD354")
    print(vars(driver2))
    
    print("Carros:")
    carro1   = Car("MTR-212", "Chevrolet", "Gris", "2000", "Matriz-12323552", Driver(1, "Manuel Perez", "Masculino", "0935264719", 36 ,"LTE234"))
    print(vars(carro1))
    print(vars(carro1.driver))
    
    carro2   = Car("RPS-212", "Chevrolet", "AZUL", "2005", "Matriz-12432442", Driver(2, "Lucas Erazo", "Masculino", "0932844719", 26 ,"ASD354"))
    print(vars(carro2))
    print(vars(carro2.driver))
    
    print("UberX:")
    uberx1  = UberX("UNS-203", "Ferrari", "Rojo", "1986", "Matriz-2415363666", Driver(3, "Xavier Vera", "Masculino", "0986354232", 30, "ASF241"))
    print(vars(uberx1))
    print(vars(uberx1.driver))
    
    uberx2  = UberX("PQR-203", "Toyota", "negro", "1926", "Matriz-23030400", Driver(4, "Jean Carbajal", "Masculino", "0982345423", 25, "ASF241"))
    print(vars(uberx2))
    print(vars(uberx2.driver))
    
    print("UberXl:")
    uberxl1  = UberXL("TUS-221", "TOYOTA", "verde", "2001", "Matriz-241523466", 4, Driver(5, "Dany Vega", "Masculino", "0986354232", 30, "ASF241"))
    print(vars(uberxl1))
    print(vars(uberxl1.driver))
    
    uberxl2  = UberXL("PRR-143", "Mazda", "blanco", "2013", "Matriz-230312120", 6, Driver(6, "Micaela Molina", "Femenino", "0982344123", 20, "LKD241"))
    print(vars(uberxl2))
    print(vars(uberxl2.driver))
    
    print("UberPet:")
    uberPet1 = UberPet("UTS-143", "Chevrolet", "GRIS", "2004", "Matriz-230123120", 1,Driver(7, "Monica guaman", "Femenino", "0415312323", 23, "OPD211"))
    print(vars(uberPet1))
    print(vars(uberPet1.driver))
    
    uberPet2 = UberPet("PRS-103", "Toyota", "blanco", "2013", "Matriz-264632120", 1,Driver(8, "Joel revelo", "masculino", "09823412543", 40, "USD211"))
    print(vars(uberPet2))
    print(vars(uberPet2.driver))
    
    print("UberFlash:")
    uberflash1 = UberFlash("NSA-143", "Ferrari", "blanco", "1960", "Matriz-230412120", "S55-145", "E3E", Driver(9, "Cesar revelo", "masculino", "098234132423", 20, "UFD211"))
    print(vars(uberflash1))
    print(vars(uberflash1.driver))
    
    uberflash2 = UberFlash("KKA-143", "cHEVROLET", "blanco", "2003", "Matriz-2304578120", "S55-145", "E3E", Driver(10, "Jonathan Carvajal", "masculino", "09814152423", 19, "YTS567"))
    print(vars(uberflash2))
    print(vars(uberflash2.driver))
    
    print("UberConfort:")
    uberConfort1 =UberConfort("KKA-143", "cHEVROLET", "blanco", "2003", "Matriz-2304578120", 1, 6, "Tapizado de cuero", Driver(11, "Cesar revelo", "masculino", "098234132423", 20, "UFD211"))
    print(vars(uberConfort1))
    print(vars(uberConfort1.driver))
    
    
    print("Trip:")
    trip1 = Trip(1, User(1, "Lucas", 25, "lucasgmail.com", "094323423"), Driver(12, "David Mantuano", "Masculino" , "0942342234", 30 ,"PSD123"), Route([12,25],[25,40], 60, 300),Payment(1, 5.50,User(1, "Lucas", 25, "lucasgmail.com", "094323423"),Driver(12, "David Mantuano", "Masculino" , "0942342234", 30 ,"PSD123"),"Efectivo"),Car("MTR-212", "Chevrolet", "Gris", "2000", "Matriz-12323552", Driver(1, "Manuel Perez", "Masculino", "0935264719", 36 ,"LTE234")))
    print(vars(trip1))
    print(vars(trip1.driver))
    print(vars(trip1.user))
    print(vars(trip1.route))
    print(vars(trip1.payment))
