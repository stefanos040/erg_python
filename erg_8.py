import random

class SmartFanaria():

    def __init__(self, name):
        self.amaountOfCars = random.randint(0,50)
        self.name = name

    def greenLight(self):
        
        self.x = random.randint(5,10) 

        if self.amaountOfCars<10: 
            self.x = random.randint(0,self.amaountOfCars)

        self.carsOut = self.x
        print("To ",self.name, " einai prasino kai exei " , self.amaountOfCars, " aytokinhta kai feygoun ", self.carsOut )        
        self.amaountOfCars = self.amaountOfCars - self.x

    def redLight(self):
        
        self.carsIn = random.randint(0,5)
        print("To ",self.name, " einai kokkino kai exei " , self.amaountOfCars, " aytokinhta kai erxontai " , self.carsIn)
        self.amaountOfCars = self.amaountOfCars + self.carsIn

# Main

fanari1 = SmartFanaria("R")
fanari2 = SmartFanaria("G")
fanari3 = SmartFanaria("O")

while fanari1.amaountOfCars!=0 or fanari2.amaountOfCars!=0 or fanari3.amaountOfCars!=0: 
    if fanari1.amaountOfCars > fanari2.amaountOfCars and fanari1.amaountOfCars > fanari3.amaountOfCars:
        fanari1.greenLight()
        fanari2.redLight()
        fanari3.redLight()
    elif fanari2.amaountOfCars > fanari1.amaountOfCars and fanari2.amaountOfCars > fanari3.amaountOfCars :
        fanari2.greenLight()
        fanari1.redLight()
        fanari3.redLight()
    elif fanari3.amaountOfCars > fanari1.amaountOfCars and fanari3.amaountOfCars > fanari2.amaountOfCars :
        fanari3.greenLight()
        fanari1.redLight()
        fanari2.redLight()
    else : #se periptwsi pou ta aytokinhta tous einai isa arithmitika
        fanaria = [fanari1 , fanari2 , fanari3]
        temp = random.choice(fanaria)
        fanaria.remove(temp) 
        
        temp.greenLight()
        fanaria[0].redLight()
        fanaria[1].redLight()

print(fanari1.amaountOfCars , " R")
print(fanari2.amaountOfCars , " G")
print(fanari3.amaountOfCars , " O")