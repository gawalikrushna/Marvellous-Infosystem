import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


Border = "-" * 50

# Step 1: Get Data
def GetData(filename):

    df = pd.read_csv(filename)

    print(Border)
    print("Dataset Loaded Successfully!")
    print(df.head())
    print(Border)

    print("\nDataset Shape:")
    print(df.shape)
    print(Border)

    return df


# Step 2: Clean, Prepare and Manipulate Data
def PrepareData(df):

    print("\nMissing Values:")
    print(df.isnull().sum())
    print(Border)

    # Remove duplicate records
    df = df.drop_duplicates()

    print("\nDataset after removing duplicates:")
    print(df.shape)
    print(Border)

    # Separate input and output
    X = df.drop("Class", axis=1)
    Y = df["Class"]

    print("\nInput Features:")
    print(X.columns)
    print(Border)

    print("\nTarget:")
    print(Y.name)
    print(Border)

    return X, Y


# Step 3: Train Data
def TrainModel(X, Y):

    # Split data into training and testing data
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.20,
        random_state=42,
        stratify=Y
    )

    print("\nTraining Data:", X_train.shape)
    print("Testing Data:", X_test.shape)
    print(Border)

    # Create Machine Learning Model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # Train model
    model.fit(X_train, Y_train)

    print("\nModel Training Completed!")
    print(Border)

    return model, X_test, Y_test


# Step 4: Test Data
def TestModel(model, X_test, Y_test):

    # Make predictions
    Y_pred = model.predict(X_test)

    print("\nActual Values:")
    print(Y_test.values)
    print(Border)

    print("\nPredicted Values:")
    print(Y_pred)
    print(Border)

    return Y_pred


# Step 5: Calculate Accuracy
def CalculateAccuracy(Y_test, Y_pred):

    accuracy = accuracy_score(Y_test, Y_pred)

    print("\nMODEL ACCURACY")
    print("--------------------------------")
    print("Accuracy:", accuracy)
    print("Accuracy Percentage:", accuracy * 100, "%")
    print(Border)

    return accuracy


# Confusion Matrix
def DisplayConfusionMatrix(Y_test, Y_pred):

    cm = confusion_matrix(Y_test, Y_pred)

    print("\nConfusion Matrix:")
    print(cm)
    print(Border)

    return cm


# Classification Report
def DisplayClassificationReport(Y_test, Y_pred):

    print("\nClassification Report:")
    print(classification_report(Y_test, Y_pred))
    print(Border)


# Accuracy Visualization
def DisplayAccuracyGraph(accuracy):

    plt.figure(figsize=(6, 4))

    plt.bar(
        ["Accuracy"],
        [accuracy * 100]
    )

    plt.ylabel("Accuracy (%)")
    plt.title("Wine Classification Model Accuracy")
    plt.ylim(0, 100)

    plt.show()


# Main Function
def main():

    # Step 1: Get Data
    df = GetData("WinePredictor.csv")

    # Step 2: Clean, Prepare and Manipulate Data
    X, Y = PrepareData(df)

    # Step 3: Train Data
    model, X_test, Y_test = TrainModel(X, Y)

    # Step 4: Test Data
    Y_pred = TestModel(model, X_test, Y_test)

    # Step 5: Calculate Accuracy
    accuracy = CalculateAccuracy(Y_test, Y_pred)

    # Display Confusion Matrix
    DisplayConfusionMatrix(Y_test, Y_pred)

    # Display Classification Report
    DisplayClassificationReport(Y_test, Y_pred)

    # Display Accuracy Graph
    DisplayAccuracyGraph(accuracy)

if __name__ == "__main__":
    main()