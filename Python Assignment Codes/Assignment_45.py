import pandas as pd
import matplotlib.pyplot as plt


Border = "-" * 60


# ============================================================
# Step 1 : Create DataFrame
# ============================================================

def CreateDataFrame():

    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82]
    }

    df = pd.DataFrame(data)

    # Calculate Total
    df["Total"] = (
        df["Math"]
        + df["Science"]
        + df["English"]
    )

    return df


# ============================================================
# Step 2 : Normalize Math scores using Min-Max Scaling
# ============================================================

def NormalizeMath(df):

    minimum = df["Math"].min()
    maximum = df["Math"].max()

    df["Math_Normalized"] = (
        (df["Math"] - minimum)
        / (maximum - minimum)
    )

    print()
    print(Border)
    print("Q1 : Min-Max Normalized Math Scores")
    print(Border)

    print(
        df[["Name", "Math", "Math_Normalized"]]
    )

    return df


# ============================================================
# Step 3 : Create Gender column and One-Hot Encoding
# ============================================================

def EncodeGender(df):

    # Sample gender data
    df["Gender"] = [
        "Male",
        "Male",
        "Female"
    ]

    print()
    print(Border)
    print("Q2 : Gender Column")
    print(Border)

    print(df)

    # One-Hot Encoding
    df = pd.get_dummies(
        df,
        columns=["Gender"],
        dtype=int
    )

    print()
    print("After One-Hot Encoding")
    print(Border)

    print(df)

    return df


# ============================================================
# Step 4 : Group students by Gender and calculate average marks
# ============================================================

def GenderAverage(df):

    # Create a temporary DataFrame because Q2
    # converts Gender into separate columns

    gender_data = pd.DataFrame({
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82],
        "Gender": ["Male", "Male", "Female"]
    })

    result = gender_data.groupby(
        "Gender"
    )[["Math", "Science", "English"]].mean()

    print()
    print(Border)
    print("Q3 : Average Marks by Gender")
    print(Border)

    print(result)


# ============================================================
# Step 5 : Pie Chart of Sagar's Subject Marks
# ============================================================

def SagarPieChart(df):

    sagar = df[
        df["Name"] == "Sagar"
    ].iloc[0]

    subjects = [
        "Math",
        "Science",
        "English"
    ]

    marks = [
        sagar["Math"],
        sagar["Science"],
        sagar["English"]
    ]

    print()
    print(Border)
    print("Q4 : Sagar's Subject Marks Pie Chart")
    print(Border)

    plt.figure()

    plt.pie(
        marks,
        labels=subjects,
        autopct="%1.1f%%"
    )

    plt.title("Sagar's Subject Marks")

    plt.show()


# ============================================================
# Step 6 : Add Status column
# ============================================================

def AddStatus(df):

    df["Status"] = df["Total"].apply(
        lambda total: "Pass"
        if total >= 250
        else "Fail"
    )

    print()
    print(Border)
    print("Q5 : Student Status")
    print(Border)

    print(
        df[["Name", "Total", "Status"]]
    )

    return df


# ============================================================
# Step 7 : Count number of students who passed
# ============================================================

def CountPassedStudents(df):

    passed = (
        df["Status"] == "Pass"
    ).sum()

    print()
    print(Border)
    print("Q6 : Number of Students Passed")
    print(Border)

    print(
        "Total Passed Students:",
        passed
    )


# ============================================================
# Step 8 : Export DataFrame to CSV
# ============================================================

def ExportCSV(df):

    filename = "Student_Final_Data.csv"

    df.to_csv(
        filename,
        index=False
    )

    print()
    print(Border)
    print("Q7 : Export DataFrame")
    print(Border)

    print(
        "DataFrame exported successfully to:",
        filename
    )


# ============================================================
# Step 9 : Histogram of Math Marks
# ============================================================

def MathHistogram(df):

    print()
    print(Border)
    print("Q8 : Math Marks Histogram")
    print(Border)

    plt.figure()

    plt.hist(
        df["Math"],
        bins=5
    )

    plt.xlabel("Math Marks")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Math Marks")

    plt.show()


# ============================================================
# Step 10 : Rename Math column to Mathematics
# ============================================================

def RenameMath(df):

    df = df.rename(
        columns={
            "Math": "Mathematics"
        }
    )

    print()
    print(Border)
    print("Q9 : Rename Math Column")
    print(Border)

    print(df)

    return df


# ============================================================
# Step 11 : Boxplot of English Marks
# ============================================================

def EnglishBoxplot(df):

    print()
    print(Border)
    print("Q10 : English Marks Boxplot")
    print(Border)

    plt.figure()

    plt.boxplot(
        df["English"]
    )

    plt.ylabel("English Marks")
    plt.title("English Marks Distribution and Outliers")

    plt.show()


# ============================================================
# Main Function
# ============================================================

def main():

    # Create DataFrame
    df = CreateDataFrame()

    print(Border)
    print("Original DataFrame")
    print(Border)

    print(df)

    df = NormalizeMath(df)

    df = EncodeGender(df)

    GenderAverage(df)

    SagarPieChart(df)

    df = AddStatus(df)

    CountPassedStudents(df)

    ExportCSV(df)

    MathHistogram(df)

    df = RenameMath(df)

    EnglishBoxplot(df)


# ============================================================
# Program Execution
# ============================================================

if __name__ == "__main__":
    main()