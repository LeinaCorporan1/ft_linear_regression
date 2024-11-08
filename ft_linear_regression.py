import pandas as pd
import numpy as np


def load(path: str) -> pd.DataFrame:
    """
    This function loads a CSV file from the given path and returns a pandas DataFrame.
    If the file is not in CSV format or is not found, it handles the exceptions accordingly.

    Parameters:
    path (str): The file path of the CSV file.

    Returns:
    pd.DataFrame: The DataFrame obtained from the CSV file.
    None: If the file is not found.

    Raises:
    AssertionError: If the file is not in CSV format.
    """

    try:
        # Check if the file is in CSV format
        if not path.lower().endswith(("csv")):
            # Raise an error if the file is not in CSV format
            raise AssertionError("Only csv formats are supported.")

        try:
            # Try to load the CSV file into a DataFrame
            df = pd.read_csv(path)
        except FileNotFoundError:
            # Print an error message if the file is not found
            print("File not found.")
            # Return None if the file is not found
            return None

        # Print the dimensions of the loaded DataFrame
        print(f"Loading dataset of dimensions {df.shape}")

        # Return the loaded DataFrame
        return df

    except AssertionError as error:
        # Print the details of the AssertionError
        print(AssertionError.__name__ + ":", error)

def estimatePrice(mileage,theta):
    estimated = mileage.dot(theta)
    return estimated

def linear_regression(data, learning_rate, iterations):
    m = len(data)
    theta = np.random.randn(2, 1)
    mileage_data = np.reshape(data['km'].values,(m,1)).astype(float)

    price = data['price'].values
    price = np.reshape(price, (m,1)).astype(float)
    print(mileage_data)
    # normalize data so it can be in a range between 0 and 1 : ease way to improve perffomance of an algorithm
    xmin = np.min(mileage_data)
    xmax = np.max(mileage_data)
    for i in range(len(mileage_data)):
        mileage_data[i] = (mileage_data[i] - xmin) / (xmax - xmin)
    mileage = np.hstack((mileage_data, np.ones(mileage_data.shape)))
    print(mileage)
    for i in range(0, iterations):
        theta = theta - learning_rate * (1 / m * mileage.T.dot(estimatePrice(mileage, theta) - price))
    print(theta)
    return theta


def main ():
    car_dataset= load('data.csv')
    car_db = car_dataset.values
    print(type(car_db))
    learning_rate = 0.07
    iterations = 1000

    linear_regression(car_dataset, learning_rate, iterations)

if __name__ == "__main__":
    main()
