MODEL PERFORMANCE

Deadlift Model

Features: Age, Sex, Bodyweight, Squat, Bench

Result: R2 Score 0.899 | RMSE 18.6 kg

Squat Model

Features: Age, Sex, Bodyweight, Bench, Deadlift

Result: R2 Score 0.910 | RMSE 17.2 kg

Bench Model

Features: Age, Sex, Bodyweight, Squat, Deadlift

Result: R2 Score 0.884 | RMSE 14.2 kg

KEY INSIGHTS

Feature importance analysis shows that Age has a significantly higher impact on Bench Press predictions compared to the Squat or Deadlift.

The models successfully identify specialists. For example, a lifter with an elite deadlift relative to their squat will show a high "Symmetry Gap," marking them as a specialized outlier rather than a balanced lifter.

SETUP AND INSTALLATION

Requirements: Python (pandas, xgboost, scikit-learn, matplotlib).

Data: Download the CSV from OpenPowerlifting.org. Save it in the same directory as the notebook and name it "openpowerlifting.csv".

Execution: Run the Jupyter Notebook cells to clean the data and train the models.

USAGE Use the interactive loop in the final cell of the notebook. Input your Age, Sex (1 for Male, 0 for Female), Bodyweight, and two known lifts to receive a predicted value for your third lift.

PROJECT STRUCTURE

Powerlifting_Analysis.ipynb: Main notebook for training and inference.

README.txt: Project documentation.

LICENSE This project is open-source and available under the MIT License.
