
def getFuel(mass):
    fuel = (int(mass/3) - 2)
    if (fuel <= 0):
        return 0
    else:
        return fuel + getFuel(fuel)

if __name__ == '__main__':
    masses = []
    totalFuel = 0
    isZero = False

    massFile = open('masses.txt', 'r')
    for line in massFile:
        integerMass = int(line)
        masses.append(integerMass)
        totalFuel += getFuel(integerMass)
        
    print("Sum of all used fuel:", totalFuel)
