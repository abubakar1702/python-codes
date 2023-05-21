class Car:
    def open(self):
        print("Car is being opened")
        return self

    # here if we doesn't write return self, it will return None

    def start(self):
        print("Car is being started")
        return self

    def drive(self):
        print("Car is being driven")
        return self


car = Car()
car.open().start().drive()
