



# POWERLIFTING SYMMETRY AND PERFORMANCE PREDICTOR

PROJECT OVERVIEW
This project uses XGBoost Regression to analyze powerlifting performance data from the OpenPowerlifting dataset. The goal is to predict any one of the three primary lifts (Squat, Bench Press, or Deadlift) by using the other two lifts, Age, Sex, and Bodyweight as inputs. This allows for the identification of strength outliers and "Symmetry Gaps" in a lifter's profile. Note that the dataset uses Tested, Raw lifters in full meets.



## MODEL PERFORMANCE

1. DEADLIFT MODEL
Inputs: Age, Sex, Bodyweight, Squat, Bench
Accuracy: R2 Score 0.899 | RMSE 18.6 kg
2. SQUAT MODEL
Inputs: Age, Sex, Bodyweight, Bench, Deadlift
Accuracy: R2 Score 0.910 | RMSE 17.2 kg
3. BENCH MODEL
Inputs: Age, Sex, Bodyweight, Squat, Deadlift
Accuracy: R2 Score 0.884 | RMSE 14.2 kg


## KEY INSIGHTS

* AGE SENSITIVITY: Feature importance analysis shows that Age has a significantly higher impact on Bench Press predictions compared to the Squat or Deadlift..


## SETUP AND INSTALLATION

1. REQUIREMENTS: Python installed with pandas, xgboost, scikit-learn, and matplotlib.
2. DATA: Download the CSV from OpenPowerlifting.org. Save it in the same directory as the notebook and name it "openpowerlifting.csv".
3. EXECUTION: Run the Jupyter Notebook cells to clean the data and train the models. The final cell provides an interactive loop for personal strength predictions.

USAGE:
Input your Age, Sex (1 for Male, 0 for Female), Bodyweight, and two known lifts to receive a predicted value for your third lift.

PROJECT STRUCTURE:

Powerlifting_Analysis.ipynb: Main notebook for training and inference.
README.md: Project documentation.

LICENSE:
This project is open-source and available under the MIT License.

