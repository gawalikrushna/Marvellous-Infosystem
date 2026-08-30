import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# ------------------------------------------------------------
# Step 1 : Get Data
# ------------------------------------------------------------

def GetData():
    df = pd.read_csv("Advertising.csv")

    print("Dataset:")
    print(df)

    return df


# ------------------------------------------------------------
# Step 2 : Clean, Prepare and Manipulate Data
# ------------------------------------------------------------

def PrepareData(df):

    # Input features
    X = df[["TV", "radio", "newspaper"]]

    # Target feature
    Y = df["sales"]

    return X, Y


# ------------------------------------------------------------
# Step 3 : Train Data
# ------------------------------------------------------------

def TrainData(X, Y):

    # Divide dataset into two parts
    # 50% Training and 50% Testing
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    # Create Linear Regression model
    model = LinearRegression()

    # Train model
    model.fit(X_train, Y_train)

    return model, X_test, Y_test


# ------------------------------------------------------------
# Step 4 & Step 5 : Test Data and Display Results
# ------------------------------------------------------------

def TestData(model, X_test, Y_test):

    # Predict sales
    Y_pred = model.predict(X_test)

    print("\n----------------------------------------")
    print("Predicted Sales and Expected Sales")
    print("----------------------------------------")

    for expected, predicted in zip(Y_test, Y_pred):

        print(
            f"Expected Sales : {expected:.2f}   "
            f"Predicted Sales : {predicted:.2f}"
        )

    # Calculate performance
    mse = mean_squared_error(Y_test, Y_pred)
    r2 = r2_score(Y_test, Y_pred)

    print("\n----------------------------------------")
    print("Model Performance")
    print("----------------------------------------")

    print("Mean Squared Error :", round(mse, 2))
    print("R2 Score           :", round(r2, 2))


# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------

def main():

    print("========================================")
    print("----------MARVELLOUS ADVERTISING ML MODEL----------")
    print("========================================")

    # Step 1
    df = GetData()

    # Step 2
    X, Y = PrepareData(df)

    # Step 3
    model, X_test, Y_test = TrainData(X, Y)

    # Step 4 & Step 5
    TestData(model, X_test, Y_test)


if __name__ == "__main__":
    main()