import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import sys
import json

def get_csv():
    if len(sys.argv) < 2:
        raise Exception("Please provide the path to a CSV file as a command-line argument.")
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        raise Exception("The provided file is not a CSV.")
    try:
        dataset = pd.read_csv(filename)
    except Exception as e:
        raise Exception(f"Error reading the CSV file: {e}")
    if dataset.empty:
        raise Exception("The CSV file is empty.")
    if len(dataset.columns) < 2:
        raise Exception("The CSV file must contain at least two columns (e.g., mileage, price).")
    return dataset

def normalize(data):
    min_data = data.min()
    max_data = data.max()
    extend_data = max_data - min_data
    norm_data = np.array([(value - min_data) / extend_data for value in data])
    return min_data, max_data, norm_data


def load(dataset):
    min_mile , max_mile , norm_mile = normalize(dataset[dataset.columns[0]])
    min_price , max_price , norm_price = normalize(dataset[dataset.columns[1]])
    data = {
        "min_price":int(min_price),
        "max_price":int(max_price),
        "min_mile": int(min_mile),
        "max_mile": int(max_mile)
    }
    with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
    return norm_mile, norm_price

def estimatePrice(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def mse(price , estimatedPrice, m)-> float:
    e =  sum((float(p) - ep) ** 2 for p, ep in zip(price, estimatedPrice)) / m
    return e

def display(mse,price, mileage, regression):
    plt.title("Regression lineaire sur les prix des vehicules")
    plt.scatter(mileage, price, color='blue', label='Données réelles (prix)')
    plt.plot(mileage, regression, color='red', label="regression lineaire")
    plt.legend()
    plt.xlabel('km')
    plt.ylabel('price')
    plt.text(
    0.05, 0.1,
    f'MSE = {mse:.2e}',
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment='bottom',
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.5)
    )
    plt.show()

def accuracy(real_price, predicted_price, mse):
    count = sum([abs(real - predicted) <= mse for real , predicted in zip(real_price, predicted_price)])
    return  100 * count / len(real_price)

def train(n_price,n_mileage, m):
    theta0 = 0
    theta1 = 0
    rate = 0.07
    predidectPrice = np.zeros(len(n_price))
    while mse(n_price, predidectPrice, m) >= 0.021:
        sum0 = sum((estimatePrice(mile, theta0, theta1) - cost) for mile, cost in zip(n_mileage, n_price))
        sum1 = sum((estimatePrice(mile, theta0, theta1) - cost) * mile for mile, cost in zip(n_mileage, n_price))
        theta0 -= rate * (1 / m) * sum0
        theta1 -= rate * (1 / m) * sum1
        predidectPrice = [estimatePrice(mile,theta0, theta1) for mile in n_mileage]
    with open("data.json", "r") as f:
        data = json.load(f)
    data["theta0"] = theta0
    data["theta1"] = theta1
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    predidectPrice = [value  * (data["max_price"] - data["min_price"]) + data["min_price"] for value in predidectPrice]
    return predidectPrice

def main():

    dataset = get_csv()
    price = np.array(dataset[dataset.columns[1]])
    mileage = np.array(dataset[dataset.columns[0]])
    n_mileage, n_price = load(dataset)
    regression = train(n_price, n_mileage, len(n_mileage))
    ms = mse(price, regression, len(n_mileage))
    print(f"{accuracy(price, regression, math.sqrt(ms))}% of accuracy")
    display(ms, price, mileage, regression)


if __name__ == '__main__':
    main()

