Project Overview: This project uses XGBoost Regression to analyze powerlifting performance data from the OpenPowerlifting dataset. The goal is to predict any one of the three primary lifts (Squat, Bench Press, or Deadlift) by using the other two lifts, Age, Sex, and Bodyweight as inputs. This allows for the identification of strength outliers and "Symmetry Gaps" in a lifter's profile.

Model Performance:
Deadlift Model: Predicts Deadlift using Age, Sex, Bodyweight, Squat, and Bench. Result: R2 Score 0.899 | RMSE 18.6 kg
Squat Model: Predicts Squat using Age, Sex, Bodyweight, Bench, and Deadlift. Result: R2 Score 0.910 | RMSE 17.2 kg
Bench Model: Predicts Bench using Age, Sex, Bodyweight, Squat, and Deadlift. Result: R2 Score 0.884 | RMSE 14.2 kg

Key Insights:
Feature importance analysis shows that Age has a significantly higher impact on Bench Press predictions compared to the Squat or Deadlift.
The models successfully identify specialists. For example, a lifter with an elite deadlift relative to their squat will show a high "Symmetry Gap," marking them as a specialized outlier rather than a balanced lifter.
Setup and Installation:

Requirements: You must have Python installed with the following libraries: pandas, xgboost, scikit-learn, and matplotlib.
Data: Download the CSV from Kaggle OpenPowerlifting.org. Save it in the same directory as the notebook and name it "openpowerlifting.csv".
Execution: Run the Jupyter Notebook cells to clean the data and train the models. The final cell provides an interactive loop for personal strength predictions.
Usage: Input your Age, Sex (1 for Male, 0 for Female), Bodyweight, and two known lifts to receive a predicted value for your third lift.
Project Structure:
Powerlifting_Analysis.ipynb: Main notebook for training and inference.
README.txt: Project documentation.
License: This project is open-source and available under the MIT License.
