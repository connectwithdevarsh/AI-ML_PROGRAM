# Assignment 10: Loan Eligibility Classification

This project uses Random Forest Classifiers to predict general loan and vehicle loan eligibility based on applicant details.

## Python Version
- Python 3.x (tested on Python 3.9+)

## Libraries Used
- pandas
- scikit-learn
- openpyxl (to read Excel files)

## Dataset Used
- `loan_data.xlsx` (for general loan prediction)
- `vehicle loan.xlsx` (for vehicle loan prediction)

## How to Run
First, make sure the required packages are installed:
```bash
pip install pandas scikit-learn openpyxl
```

Then run the scripts:
```bash
python loan_prediction.py
python vehicle_prediction.py
```
Each script will output the accuracy score and prompt you to input details for prediction.

## Project Files
- **loan_prediction.py**: General loan eligibility classification model and user prediction interface.
- **vehicle_prediction.py**: Vehicle loan eligibility classification model and user prediction interface.
