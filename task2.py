
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('titanic.csv')

# 1. Summary statistics
print(df.describe())
print(df.median(numeric_only=True))

# 2. Histograms and boxplots
sns.histplot(df['Age'].dropna(), bins=20)
plt.show()
sns.boxplot(x='Pclass', y='Fare', data=df)
plt.show()

# 3. Correlation matrix
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()

# 4. Pairplot (relationships)
sns.pairplot(df, hue="Survived", vars=["Age", "Fare"])
plt.show()


