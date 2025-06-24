import json
import os

def estimatePrice(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def getEstimate(mileage):
    if not os.path.exists("data.json"):
        raise Exception("data.json do not exist: train again")
    else:
        with open("data.json", "r") as f:
            data = json.load(f)
        if len(data) < 6:
            print(len(data))
            raise Exception("should train again data.json not complete")
        norm= (mileage - data["min_mile"]) / (data["max_mile"] - data["min_mile"])
        normPrice = estimatePrice(norm, data["theta0"], data["theta1"])
        denormed = normPrice * (data["max_price"] - data["min_price"]) + data["min_price"]
        if denormed < 0:
            denormed = 0
        print(denormed)



def main():
    mileage = input("what is the mileage of your vehicule ?" )
    if mileage.isnumeric():
        getEstimate(float(mileage))
    else:
        raise TypeError({f" your mileage should be a integer"})

main()
