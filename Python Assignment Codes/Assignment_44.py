import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


Border = "-" * 60


# ============================================================
# Step 1 : Create DataFrame and display basic information
# ============================================================

def CreateDataFrame():

    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82]
    }

    df = pd.DataFrame(data)

    return df


def DisplayBasicInformation(df):

    print(Border)
    print("Q1 : DataFrame")
    print(Border)

    print(df)

    print()
    print("Shape :", df.shape)
    print("Columns :", df.columns.tolist())

    print()
    print("Data Types:")
    print(df.dtypes)


# ============================================================
# Step 2 : Descriptive Statistics
# ============================================================

def DisplayStatistics(df):

    print()
    print(Border)
    print("Q2 : Descriptive Statistics")
    print(Border)

    print(df.describe())


# ============================================================
# Step 3 : Add Total Column
# ============================================================

def AddTotal(df):

    df["Total"] = (
        df["Math"]
        + df["Science"]
        + df["English"]
    )

    print()
    print(Border)
    print("Q3 : Total Marks")
    print(Border)

    print(df)

    return df


# ============================================================
# Step 4 : Students with Science > 85
# ============================================================

def DisplayScienceStudents(df):

    print()
    print(Border)
    print("Q4 : Science Marks Greater Than 85")
    print(Border)

    result = df[df["Science"] > 85]

    print(result)


# ============================================================
# Step 5 : Replace Pooja with Puja
# ============================================================

def ReplaceName(df):

    df["Name"] = df["Name"].replace(
        "Pooja",
        "Puja"
    )

    print()
    print(Border)
    print("Q5 : After Replacing Pooja with Puja")
    print(Border)

    print(df)

    return df


# ============================================================
# Step 6 : Sort by Total in Descending Order
# ============================================================

def SortByTotal(df):

    df = df.sort_values(
        by="Total",
        ascending=False
    )

    print()
    print(Border)
    print("Q6 : Sorted DataFrame")
    print(Border)

    print(df)

    return df


# ============================================================
# Step 7 : Bar Plot
# ============================================================

def DisplayBarPlot(df):

    print()
    print(Border)
    print("Q7 : Bar Plot")
    print(Border)

    plt.figure()

    plt.bar(
        df["Name"],
        df["Total"]
    )

    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.title("Student Names vs Total Marks")

    plt.show()


# ============================================================
# Step 8 : Line Chart of Amit's Marks
# ============================================================

def DisplayAmitMarks(df):

    print()
    print(Border)
    print("Q8 : Amit's Marks")
    print(Border)

    amit = df[df["Name"] == "Amit"].iloc[0]

    subjects = [
        "Math",
        "Science",
        "English"
    ]

    marks = [
        amit["Math"],
        amit["Science"],
        amit["English"]
    ]

    plt.figure()

    plt.plot(
        subjects,
        marks,
        marker="o"
    )

    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit's Marks Across Subjects")

    plt.show()


# ============================================================
# Step 9 : Missing Values and Fill with Mean
# ============================================================

def HandleMissingValues():

    data2 = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [np.nan, 76, 88],
        "Science": [91, np.nan, 85]
    }

    df2 = pd.DataFrame(data2)

    print()
    print(Border)
    print("Q9 : Before Filling Missing Values")
    print(Border)

    print(df2)

    df2["Math"] = df2["Math"].fillna(
        df2["Math"].mean()
    )

    df2["Science"] = df2["Science"].fillna(
        df2["Science"].mean()
    )

    print()
    print("After Filling Missing Values")
    print(Border)

    print(df2)

    return df2


# ============================================================
# Step 10 : Drop English Column
# ============================================================

def DropEnglish(df):

    df = df.drop(
        columns=["English"]
    )

    print()
    print(Border)
    print("Q10 : After Dropping English Column")
    print(Border)

    print(df)

    return df


# ============================================================
# Main Function
# ============================================================

def main():

    df = CreateDataFrame()

    DisplayBasicInformation(df)

    DisplayStatistics(df)

    df = AddTotal(df)

    DisplayScienceStudents(df)

    df = ReplaceName(df)

    df = SortByTotal(df)

    DisplayBarPlot(df)

    DisplayAmitMarks(df)

    HandleMissingValues()

    df = DropEnglish(df)


# ============================================================
# Program Execution
# ============================================================

if __name__ == "__main__":
    main()