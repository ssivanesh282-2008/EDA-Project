import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# LOAD DATA
# ----------------------------
df = pd.read_csv("student_data.csv")

print("Dataset:\n")
print(df)

# ----------------------------
# BASIC STATISTICS
# ----------------------------
print("\nStatistical Summary:\n")
print(df.describe())

# ----------------------------
# CORRELATION
# ----------------------------
correlation = df.corr()

print("\nCorrelation Matrix:\n")
print(correlation)

# ----------------------------
# VISUALIZATION 1
# ----------------------------

# Study Hours vs Marks
plt.figure()
sns.scatterplot(x=df['StudyHours'], y=df['Marks'])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("study_vs_marks.png")
plt.show()

# ----------------------------
# VISUALIZATION 2
# ----------------------------

# Correlation Heatmap
plt.figure()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

print("\n✅ EDA Project Completed!")