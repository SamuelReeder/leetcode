class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spots = [0, big, medium, small]
        self.occupied = [0, 0, 0, 0]

    def addCar(self, carType: int) -> bool:
        if self.occupied[carType] == self.spots[carType]:
            return False

        self.occupied[carType] += 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
