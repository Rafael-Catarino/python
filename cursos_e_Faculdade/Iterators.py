cars = ["HRV", "Polo", "Jetta", "Cruze", "Fusion", "Golf", "Focus", "Onyx", "Fit"]
itCars = iter(cars)

while itCars:
    try:
        print(next(itCars))
    except StopIteration:
        # print("fim da lista")
        break
