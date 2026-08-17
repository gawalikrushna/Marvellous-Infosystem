import math

Border = "-" * 50


# Function to calculate Euclidean distance
def CalculateDistance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance


# Function to calculate distances from new point
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


# Function to select K nearest neighbors
def SelectKNearest(distances, k):
    return distances[:k]


# Function to predict class using majority voting
def PredictClass(nearest_neighbors):

    class_count = {}

    for point, distance, label in nearest_neighbors:

        if label not in class_count:
            class_count[label] = 0

        class_count[label] += 1

    predicted_class = max(class_count, key=class_count.get)

    return predicted_class


# Function to display nearest neighbors
def DisplayNeighbors(nearest_neighbors):

    print()
    print("Nearest Neighbors:")

    for point, distance, label in nearest_neighbors:
        print(f"{point} - Distance: {distance:.2f}")


# Main Function
def main():

    # Dataset
    data = [
        ("A", 1, 2, "Red"),
        ("B", 2, 3, "Red"),
        ("C", 3, 1, "Blue"),
        ("D", 6, 5, "Blue")
    ]

    # Accept input
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    # Calculate distances
    distances = CalculateAllDistances(data, x, y)

    # Sort distances
    distances = SortDistances(distances)

    # Select K = 3
    k = 3
    nearest_neighbors = SelectKNearest(distances, k)

    # Display nearest neighbors
    DisplayNeighbors(nearest_neighbors)

    # Predict class
    predicted_class = PredictClass(nearest_neighbors)

    print()
    print("Predicted Class:", predicted_class)


# Program execution
if __name__ == "__main__":
    main()