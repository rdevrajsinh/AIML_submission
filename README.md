# University Admission Prediction

## 1. Exploring the Dataset
The dataset consists of various data fields, including:
- Serial No.
- GRE Score
- TOEFL Score
- University Rating
- SOP (Statement of Purpose)
- LOR (Letter of Recommendation)
- CGPA (Cumulative Grade Point Average)
- Research (Binary: 0 for no, 1 for yes)
- Chance of Admit (Probability of admission)

The data types vary from integers to floats, indicating numerical features. Initial exploration includes checking the shape of the dataset, displaying the first few rows, and examining column names, data types, and basic statistics.

## 2. Data Visualization
Histograms were created to visualize the distribution of key features such as GRE Scores, TOEFL Scores, University Ratings, SOP Ratings, LOR Ratings, and CGPA. Histograms provide insights into the distribution of scores and ratings, which are essential for understanding the dataset's characteristics.

## 3. Data Cleaning
Data cleaning involved handling missing values by replacing 0 values in specific columns with NaN. The 'Serial No.' column, which serves as an identifier, was dropped to avoid unnecessary processing.

## 4. Model Building
Two regression models were employed for predicting admission probability:
- Linear Regression
- Decision Tree Regression

The dataset was split into features (X) and labels (y), followed by further division into training and testing sets. Each model was trained using the training data and evaluated using the R-squared metric to assess its performance.

## 5. Model Evaluation
Linear Regression achieved the highest R-squared score of 0.819, indicating its superior predictive capability. Decision Tree Regression attained R-squared scores of 0.563.

## 6. Conclusion
Based on R-squared scores, Linear Regression emerged as the most effective model for predicting university admission probability. The trained Linear Regression model was saved for future use, offering a reliable solution for admission prediction.
