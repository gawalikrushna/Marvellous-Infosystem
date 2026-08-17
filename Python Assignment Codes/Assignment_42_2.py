import math

Border = "-" * 50


# Function to calculate Euclidean distance
def CalculateDistance(x1, y1, x2, y2):

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return distance


# Function to calculate distance from all data points
def CalculateAllDistances(data, x, y):

    distances = []

    for point, px, py, label in data:

        distance = CalculateDistance(x, y, px, py)

        distances.append((point, distance, label))

    return distances


# Function to sort distances
def SortDistances(distances):

    distances.sort(key=lambda item: item[1])

    return distances


# Function to predict class for a given K
def PredictClass(distances, k):

    # Check whether K is valid
    if k > len(distances):
        return "Invalid K"

    # Select K nearest neighbors
    nearest_neighbors = distances[:k]

    # Count classes
    class_count = {}

    for point, distance, label in nearest_neighbors:

        if label not in class_count:
            class_count[label] = 0

        class_count[label] += 1

    # Majority voting
    predicted_class = max(class_count, key=class_count.get)

    return predicted_class


# Main Function
def main():

    # Dataset
    data = [
        ("A", 1, 2, "Red"),
        ("B", 2, 3, "Red"),
        ("C", 3, 1, "Blue"),
        ("D", 6, 5, "Blue")
    ]

    # Accept new point
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    # Calculate distances
    distances = CalculateAllDistances(data, x, y)

    # Sort distances
    distances = SortDistances(distances)

    print()
    print("Prediction Results")
    print(Border)

    # Test different values of K
    k_values = [1, 3, 5]

    for k in k_values:

        predicted_class = PredictClass(distances, k)

        print(f"K = {k} -> {predicted_class}")


# Program execution
if __name__ == "__main__":
    main()