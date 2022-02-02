class Car(object):
    def __init__(self,model,color,company,engine,speed_limit,horsepower):
        self.color = color
        self.model = model
        self.company = company
        self.engine = engine
        self.speed_limit = speed_limit
        self.horsepower = horsepower

    def start(self):
        print("started")

    def stop(self):
        print("stop")

    def accelerate(self):
        print("accelerate it")

    def changegear(self):
        print("Gear Changed")
    
asparkowl = Car("model","yellow","aspark","engine","401.1 km/h","horsepower")
print(asparkowl.company)
