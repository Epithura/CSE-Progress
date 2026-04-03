class Car:
    def __init__(self, make, model, year, mileage, tanksize):
        self.make = make
        self.model = model
        self.year = int(year)
        self.mileage = int(mileage)
        self.tanksize = int(tanksize)

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} {self.mileage}")

    def get_mileage(self):
        print(self.mileage)

    def calculate_mileage(self, kms):
        self.mileage = kms // self.tanksize

def main():
    import sys
    l = sys.stdin.read().strip().split('\n')

    n = int(l[0])
    car_info = l[1].split()
    car = Car(*car_info)

    for line in l[2:]:
        parts = line.strip().split()

        if parts[0] == "calculate_mileage":
            kms = int(parts[1])
            car.calculate_mileage(kms)

        elif parts[0] == "get_mileage":
            car.get_mileage()

        elif parts[0] == "display_info":
            car.display_info()


if __name__ == "__main__":
    main()
