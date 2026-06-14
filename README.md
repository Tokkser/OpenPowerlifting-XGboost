# Powerlifting Performance Predictor

XGBoost-based regression models trained on the OpenPowerlifting dataset to predict any one of the three primary lifts — Squat, Bench Press, or Deadlift — from the other two, plus Age, Sex, and Bodyweight. Useful for identifying strength outliers and symmetry gaps in a lifter's profile.

> Dataset scope: Tested, Raw lifters in full meets (SBD).

---

## Model Performance

| Model     | Inputs                              | R² Score | RMSE     |
|-----------|-------------------------------------|----------|----------|
| Deadlift  | Age, Sex, Bodyweight, Squat, Bench  | 0.899    | 18.6 kg  |
| Squat     | Age, Sex, Bodyweight, Bench, Deadlift | 0.910  | 17.2 kg  |
| Bench     | Age, Sex, Bodyweight, Squat, Deadlift | 0.884  | 14.2 kg  |

---

## Key Insights

- **Age sensitivity:** Feature importance analysis shows Age has a significantly higher impact on Bench Press predictions relative to Squat or Deadlift.

---

## Setup

### Requirements

```bash
pip install pandas xgboost scikit-learn matplotlib
```

### Data

1. Download the dataset from Kaggle: [OpenPowerlifting · Aleksey Bilogur](https://www.kaggle.com/datasets/open-powerlifting/powerlifting-database)
2. Save the CSV in the same directory as the notebook and rename it `openpowerlifting.csv`

### Running

Open and run all cells in the Jupyter notebook. The final cell launches an interactive loop for personal lift predictions.

---

## Usage

```
Input:  Age, Sex (1 = Male, 0 = Female), Bodyweight (kg), and two known lifts (kg)
Output: Predicted value for your third lift (kg)
```

---

## Project Structure

```
├── OpenPowerlifting (Tested, Raw, SBD)-Copy1.ipynb   # Main notebook
└── README.md                                          # Documentation
```

---

## License

MIT License — open source, free to use and modify.
