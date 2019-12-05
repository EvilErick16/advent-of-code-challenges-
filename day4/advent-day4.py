# Erick Juarez

def isCombination(num):
    for x in range(len(num)):
        if x != 0:
            curr = num[x]
            prev = num[x-1]
            if (curr < prev):
                return False
    
    return hasDouble(num)

def hasDouble(num):
    for x in range(len(num)):
        if x != 0:
            curr = num[x]
            prev = num[x-1]
            if (curr == prev):
                return True
    return False

if __name__ == '__main__':
    combinations = 0
    for i in range(123257, 647016):
        numbers = [int(j) for j in str(i)]

        if isCombination(numbers):
            combinations +=1

    print("Possible combinations: ", combinations)