import math

Border = "-" * 50


# Function to calculate Euclidean distance
def CalculateDistance(x1, y1, x2, y2):

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return distance


# Function to calculate distance from all students
def CalculateAllDistances(data, study_hours, attendance):

    distances = []

    for student_hours, student_attendance, result in data:

        distance = CalculateDistance(
            study_hours,
            attendance,
            student_hours,
            student_attendance
        )

        distances.append((distance, result))

    return distances


# Function to sort distances
def SortDistances(distances):

    distances.sort(key=lambda item: item[0])

    return distances


# Function to predict result using KNN
def PredictResult(distances, k):

    # Select K nearest students
    nearest_neighbors = distances[:k]

    pass_count = 0
    fail_count = 0

    # Majority voting
    for distance, result in nearest_neighbors:

        if result == "Pass":
            pass_count += 1

        else:
            fail_count += 1

    if pass_count > fail_count:
        return "Pass"

    else:
        return "Fail"


# Main Function
def main():

    # Dataset
    data = [
        (2, 60, "Fail"),
        (5, 80, "Pass"),
        (6, 85, "Pass"),
        (1, 50, "Fail")
    ]

    # Accept input
    study_hours = float(
        input("Enter Study Hours: ")
    )

    attendance = float(
        input("Enter Attendance: ")
    )

    # Calculate distances
    distances = CalculateAllDistances(
        data,
        study_hours,
        attendance
    )

    # Sort distances
    distances = SortDistances(distances)

    # Select K
    k = 3

    # Predict result
    predicted_result = PredictResult(
        distances,
        k
    )

    print()
    print("Predicted Result:", predicted_result)


# Program execution
if __name__ == "__main__":
    main()