class Car(object):
    def __init__(self,make, model, year, daily_rate):
        self.make        = make 
        self.model       = model 
        self.year        = year 
        self.daily_rate  = daily_rate 
        self.is_rented   = False
    
    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            print(f"{self.make} {self.model} ({self.year}) rented for $ {self.daily_rate} per day.")
        else:
            print(f"{self.make} {self.model} ({self.year}) is not available for rent")

class RentalSystem(object):
    def __init__(self):
        self.cars = []
    
    def add_car(self,make, model, year, daily_rate):
        car = Car(make, model, year, daily_rate)
        self.cars.append(car)
    
    def rent_car(self,make, model, year):
        for car in self.cars:
            if car.make == make and car.model == model and car.year == year:
                car.rent()
                return 
        print("{make} {model} ({year}) not found in the rental system")

rs = RentalSystem()
rs.add_car("Toyota","Camry",2020,50)       
rs.add_car("Honda","Civic",2019,30)       
rs.add_car("BMW","X5",2022,100)     
rs.rent_car("Toyota","Camry",2020)