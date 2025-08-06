# Task-2
Exploratory Data Analysis


1. **Data Loading**  
   The dataset 'titanic.csv' is loaded into a pandas DataFrame using `pd.read_csv`, making the data available for analysis.

2. **Summary Statistics**  
   - `df.describe()` outputs summary statistics for numerical columns, including count, mean, standard deviation (std), minimum, percentiles (25%, 50% [median], 75%), and maximum values[1][5][7][9].
   - `df.median(numeric_only=True)` prints the median values for all numeric columns, providing a measure of the central tendency that is less sensitive to outliers.

3. **Visualizations: Histograms and Boxplots**  
   - `sns.histplot(df['Age'].dropna(), bins=20)` creates a histogram to show the distribution of passenger ages, excluding missing values.
   - `sns.boxplot(x='Pclass', y='Fare', data=df)` produces a boxplot examining how fares vary across passenger classes, highlighting the median and spread within each class.

4. **Correlation Matrix**  
   - `sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')` computes and visualizes the correlation coefficients between numerical columns, helping you identify potential relationships between variables (like Age, Fare, etc.).

5. **Pairplot (Relationships)**  
   - `sns.pairplot(df, hue="Survived", vars=["Age", "Fare"])` plots pairwise relationships between Age and Fare, colored by the Survived column, to explore potential clustering or trends among survivors and non-survivors.

