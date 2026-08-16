import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay

Border = "-"*50

#######################################################################################

# 1. Python program to load the file student performance ml. csv using pandas. Display:

#    1.First 5 records

#    2.Last 5 records

#    3.Total number of rows and columns

#    4.List of column names

#    5.Data types of each column

#########################################################################################

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)
print(Border)
print("**********Dataset loaded sucessfully**********")
print(Border)

print(df)

head = df.head()

print(Border)
print("First 5 records : ")
print(Border)
print(head)

tail = df.tail()

print(Border)
print("Last 5 records : ")
print(Border)

print(tail)

Column_Rows = df.shape

print(Border)
print(f"Total number of rows and columns : {Column_Rows}")
print(Border)

Col_List = df.columns

print(Border)
print(f"List of columns : {Col_List}")
print(Border)

Col_Datatype = df.dtypes

print(Border)
print("Columns data types are : ")
print(Border)

print(Col_Datatype)

#########################################################################################

# 2. Write a program to:

#     1.Display total number of students in the dataset

#     2.Count how many students Passed (FinalResult = 1)

#     3.Count how many students Failed (FinalResult = 0)

#########################################################################################

print(Border)
print(f"Total number of students in the dataset : {len(df)}")
print(Border)

print(Border)
print(f"Passed students : {(df["FinalResult"] == 1).sum()}")
print(Border)

print(Border)
print(f"Failed students : {(df["FinalResult"] == 0).sum()}")
print(Border)

#########################################################################################

# 3. Using pandas functions, calculate and display:

#     1.Average StudyHours

#     2.Average Attendance

#     3.Maximum PreviousScore

#     4.Minimum SleepHours

#########################################################################################

print(Border)
print(f"Average StudyHours : {df["StudyHours"].mean()}")
print(Border)

print(Border)
print(f"Average Attendance : {df["Attendance"].mean()}")
print(Border)

print(Border)
print(f"Maximum PreviousScore  : {df["PreviousScore"].max()}")
print(Border)

print(Border)   
print(f"Minimum SleepHours : {df["SleepHours"].min()}")
print(Border)

#########################################################################################

# 4. Use value_counts () to analyze the distribution of FinalResult. 
# Calculate the percentage of Pass and Fail students. Is the dataset balanced? Justify your answer.

#########################################################################################

passed = (df["FinalResult"] == 1).sum()
failed = (df["FinalResult"] == 0).sum()
total = len(df)

pass_percentage = (passed / total) * 100
fail_percentage = (failed / total) * 100

print(Border)
print(f"Passed Students : {passed}")
print(Border)

print(Border)
print(f"Failed Students : {failed}")
print(Border)

print(Border)
print(f"Pass Percentage : {(df["FinalResult"] == 1).mean() * 100}")
print(Border)

print(Border)
print(f"Fail Percentage : {(df["FinalResult"] == 0).mean() * 100}")
print(Border)

#########################################################################################

# 5. Based on the dataset values, analyze whether:

# Higher StudyHours increase the chance of passing.

# Higher Attendance improves FinalResult. Write your observations in 4-5 lines.

#########################################################################################

print(Border)
print(df.groupby("FinalResult")[["StudyHours", "Attendance"]].mean())
print(Border)


#########################################################################################

# 6. Plot a histogram of StudyHours. Explain what the distribution tells you.

#########################################################################################

plt.hist(df["StudyHours"], bins=10)
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.title("Distribution of Study Hours")
plt.show()


#########################################################################################

# 7. Create a scatter plot of: StudyHours vs PreviousScore

#########################################################################################

plt.scatter( df["StudyHours"], df["PreviousScore"], c=df["FinalResult"])

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("StudyHours vs PreviousScore")
plt.show()

#########################################################################################

# 8. Boxplot for Attendance

#########################################################################################

plt.boxplot(df["Attendance"])
plt.ylabel("Attendance")
plt.title("Attendance Distribution")
plt.show()

#########################################################################################

# 9. AssignmentsCompleted vs FinalResult

#########################################################################################

sns.boxplot(x="FinalResult", y="AssignmentsCompleted", data=df)

plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Assignments Completed")
plt.title("Assignments Completed vs Final Result")
plt.show()

#########################################################################################

# 10. SleepHours vs FinalResult

#########################################################################################

sns.boxplot(x="FinalResult", y="SleepHours", data=df)

plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Sleep Hours")
plt.title("Sleep Hours vs Final Result")
plt.show()



#*******************Assignment 39*************************** 

#########################################################################################

# 1. Import DecisionTreeClassifier from sklearn.
#     Create a model object and train it using fit()

#########################################################################################

X = df[["StudyHours", "Attendance", "PreviousScore"]]

Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

model = DecisionTreeClassifier()

model = model.fit(X_train,Y_train)

#########################################################################################

# 2. Use the trained model to predict results for X_test.
#     Display predicted values along with actual values.

#########################################################################################


Y_pred = model.predict(X_test)


#########################################################################################

# 3. Calculate model accuracy using accuracy_score.
#     Display the result in percentage format.

#########################################################################################


result = accuracy_score(Y_test,Y_pred)

print(Border)
print("Accuracy Score is  : ",result*100)
print(Border)

#########################################################################################

# 4. Generate confusion matrix using sklearn.
#     Display it using ConfusionMatrixDisplay.

#########################################################################################

# Create confusion matrix
cm = confusion_matrix(Y_test, Y_pred)

# Display confusion matrix
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)

display.plot()
plt.show()

#########################################################################################

# 5. Calculate:

#     Training accuracy
#     Testing accuracy

#     Compare both and comment whether the model is overfitting or underfitting.

#########################################################################################

# Training accuracy
Y_train_pred = model.predict(X_train)
train_accuracy = accuracy_score(Y_train, Y_train_pred)

# Testing accuracy
Y_test_pred = model.predict(X_test)
test_accuracy = accuracy_score(Y_test, Y_test_pred)

print(Border)
print("Training Accuracy:", train_accuracy * 100, "%")
print("Testing Accuracy:", test_accuracy * 100, "%")
print(Border)

#########################################################################################

# 6. Train Three Decision Tree Models

#     Train three Decision Tree models with:

#     max_depth = 1
#     max_depth = 3
#     max_depth = None

#     Compare their testing accuracies and write your observations.

#########################################################################################

# Features and target
X = df[["StudyHours", "Attendance", "PreviousScore",
        "AssignmentsCompleted", "SleepHours"]]

Y = df["FinalResult"]

# Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.5, random_state=42
)

# Model 1: max_depth = 1
model1 = DecisionTreeClassifier(max_depth=1, random_state=42)
model1.fit(X_train, Y_train)

# Model 2: max_depth = 3
model2 = DecisionTreeClassifier(max_depth=3, random_state=42)
model2.fit(X_train, Y_train)

# Model 3: max_depth = None
model3 = DecisionTreeClassifier(max_depth=None, random_state=42)
model3.fit(X_train, Y_train)

# Testing accuracy
acc1 = accuracy_score(Y_test, model1.predict(X_test))
acc2 = accuracy_score(Y_test, model2.predict(X_test))
acc3 = accuracy_score(Y_test, model3.predict(X_test))

print(Border)
print("Testing Accuracy (max_depth=1):", acc1 * 100, "%")
print("Testing Accuracy (max_depth=3):", acc2 * 100, "%")
print("Testing Accuracy (max_depth=None):", acc3 * 100, "%")
print(Border)


#########################################################################################

# 7. Predict Result for a New Student

#     Use the trained model to predict the result for a student with:

#     StudyHours = 6
#     Attendance = 85
#     PreviousScore = 66
#     AssignmentsCompleted = 7
#     SleepHours = 7

#     Will the student Pass or Fail?

#########################################################################################

student = [[6, 85, 66, 7, 7]]

prediction = model2.predict(student)

if prediction[0] == 1:
    print(Border)
    print("The student will Pass.")
    print(Border)
else:
    print(Border)
    print("The student will Fail.")
    print(Border)


#*******************Assignment 40***************************

#########################################################################################

# 1. Feature Importance

#     After training the Decision Tree model, use:

#     model.feature_importances_

#     Display importance score of each feature.
#     Which feature contributes the most in predicting FinalResult?
#     Which feature contributes the least?

#########################################################################################

importance = model.feature_importances_

for feature, score in zip(X.columns, importance):
    print(feature, ":", score)

print(Border)
print("Most important feature:", X.columns[importance.argmax()])
print("Least important feature:", X.columns[importance.argmin()])
print(Border)

#########################################################################################

# 2. Remove SleepHours

#     Remove the column SleepHours from the dataset.

#     Train the model again.
#     Compare new accuracy with previous accuracy.
#     Does removing this feature affect performance?

#########################################################################################

X_new = df[["StudyHours", "Attendance", "PreviousScore",
            "AssignmentsCompleted"]]

Y = df["FinalResult"]

X_train_new, X_test_new, Y_train_new, Y_test_new = train_test_split(
    X_new, Y, test_size=0.5, random_state=42
)

model_new = DecisionTreeClassifier(random_state=42)
model_new.fit(X_train_new, Y_train_new)

Y_pred_new = model_new.predict(X_test_new)

new_accuracy = accuracy_score(Y_test_new, Y_pred_new)

print(Border)
print("New Accuracy:", new_accuracy * 100, "%")

print("Previous Accuracy:", result * 100, "%")
print("New Accuracy:", new_accuracy * 100, "%")
print(Border)

#########################################################################################

# 3. Train Model Using Only Two Features

#     Train the model using only:

#     StudyHours
#     Attendance

#     Compare the accuracy with the full-feature model.

#     Is the model still performing well?

#########################################################################################

X_small = df[["StudyHours", "Attendance"]]

X_train_small, X_test_small, Y_train_small, Y_test_small = train_test_split(
    X_small, Y, test_size=0.5, random_state=42
)

model_small = DecisionTreeClassifier(random_state=42)
model_small.fit(X_train_small, Y_train_small)

Y_pred_small = model_small.predict(X_test_small)

small_accuracy = accuracy_score(Y_test_small, Y_pred_small)

print(Border)
print("Accuracy using StudyHours and Attendance:",
      small_accuracy * 100, "%")
print(Border)

#########################################################################################

# 4. Predict Results for 5 New Students

#     Create a new DataFrame with details of 5 new students.

#     Use the trained model to predict their results.

#     Display predictions clearly.

#########################################################################################

# Use all 5 features
X = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]]

Y = df["FinalResult"]

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.5, random_state=42
)

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

# New 5 students
new_students = pd.DataFrame({
    "StudyHours": [4, 6, 8, 3, 7],
    "Attendance": [70, 85, 90, 65, 80],
    "PreviousScore": [55, 66, 78, 50, 72],
    "AssignmentsCompleted": [4, 7, 9, 3, 8],
    "SleepHours": [6, 7, 8, 5, 7]
})

# Predict
predictions = model.predict(new_students)

# Display predictions
new_students["PredictedResult"] = predictions

new_students["PredictedResult"] = new_students["PredictedResult"].map({
    0: "Fail",
    1: "Pass"
})

print(Border)
print(new_students)
print(Border)

#########################################################################################

# 5. Manually Calculate Accuracy

#     Without using accuracy_score, manually calculate the accuracy.

#     Verify whether it matches the scikit-learn accuracy.

#########################################################################################

correct = 0

for actual, predicted in zip(Y_test, Y_pred):
    if actual == predicted:
        correct += 1

manual_accuracy = correct / len(Y_test)

print(Border)
print("Manual Accuracy:", manual_accuracy * 100, "%")
print("Sklearn Accuracy:", accuracy_score(Y_test, Y_pred) * 100, "%")
print(Border)

#########################################################################################

# 6. Identify Misclassified Students

#     Identify students where:

#     y_test != y_pred

#     Display those rows.
#     How many students were misclassified?
#     What common pattern do you observe?

#########################################################################################

comparison = pd.DataFrame({
    "Actual": Y_test,
    "Predicted": Y_pred
})

misclassified = comparison[comparison["Actual"] != comparison["Predicted"]]

print(Border)
print(misclassified)
print("Number of Misclassified Students:", len(misclassified))
print(Border)

#########################################################################################

# 7. Effect of random_state

#     Train the model using:

#     random_state = 0
#     random_state = 10
#     random_state = 42

#     Compare the testing accuracy.

#     Does the result change?

#########################################################################################



#########################################################################################

# 8. Decision Tree Visualization

#     Use:

#     from sklearn.tree import plot_tree

#     Visualize the trained Decision Tree.

#     Which feature appears at the root node?
#     Why do you think that feature was selected first?

#########################################################################################

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

plt.figure(figsize=(10, 6))

plot_tree(
    model,
    feature_names=X_train.columns,
    class_names=["Fail", "Pass"],
    filled=True
)

plt.show()

#########################################################################################

# 9. Create PerformanceIndex

#     Create a new column:

#     PerformanceIndex = (StudyHours * 2) + Attendance

#     Train the model including this new feature.

#     Does accuracy improve?

#########################################################################################

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

X_new = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "PerformanceIndex"
]]

Y = df["FinalResult"]

X_train_new, X_test_new, Y_train_new, Y_test_new = train_test_split(
    X_new, Y, test_size=0.5, random_state=42
)

model_new = DecisionTreeClassifier(random_state=42)
model_new.fit(X_train_new, Y_train_new)

Y_pred_new = model_new.predict(X_test_new)

accuracy_new = accuracy_score(Y_test_new, Y_pred_new)

print(Border)
print("New Testing Accuracy:", accuracy_new * 100, "%")

print("Old Accuracy:", result * 100, "%")
print("New Accuracy:", accuracy_new * 100, "%")
print(Border)

#########################################################################################

# 10. Training and Testing Accuracy

#     Train the model with:

#     max_depth = None

#     Calculate:

#     Training accuracy
#     Testing accuracy

#     If training accuracy is 100% but testing accuracy is lower, explain why this happens.

#########################################################################################

model_none = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)

model_none.fit(X_train, Y_train)

# Training prediction
Y_train_pred = model_none.predict(X_train)

# Testing prediction
Y_test_pred = model_none.predict(X_test)

# Accuracies
training_accuracy = accuracy_score(Y_train, Y_train_pred)
testing_accuracy = accuracy_score(Y_test, Y_test_pred)

print(Border)
print("Training Accuracy:", training_accuracy * 100, "%")
print("Testing Accuracy:", testing_accuracy * 100, "%")
print(Border)

