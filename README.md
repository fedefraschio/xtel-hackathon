# XTEL CPG Hackathon – Sales Forecasting Project

## 📌 Objective

The goal of this project is to forecast weekly product sales for a set of Consumer Packaged Goods (CPG) products using historical data.

The target variable is:

    TOTAL_SALES

Predictions are required for the test year where sales values are not available.

Evaluation metric:
    Mean Absolute Percentage Error (MAPE)

---

## 📂 Dataset Description

Two datasets are provided:

- weekly_train → Historical weekly data including TOTAL_SALES
- weekly_test → Same structure but without TOTAL_SALES (to be predicted)

Main feature categories:

- Price information
- Promotional flags (IS_PROMO, IS_COUPON, IS_DISPLAY, IS_FEATURE)
- Special events (Christmas, Thanksgiving, Super Bowl, etc.)
- Product identifiers

---

## 🧠 Modeling Strategy

### 1. Data Preparation
- Date feature engineering (year extraction)
- Time-based train/validation split
- Feature cleaning and selection
- Removal of non-numeric fields when required

### 2. Model

Model used:
    XGBoost Regressor

Hyperparameters optimized using GridSearchCV.

Best parameters found:
    - learning_rate: 0.03
    - max_depth: 6
    - n_estimators: 300
    - subsample: 0.8
    - colsample_bytree: 0.8
    - reg_lambda: 5

Validation MAPE:
    0.0136

---

## 🚀 Pipeline Overview

1. Load dataset
2. Preprocess features
3. Train model on historical data
4. Validate on most recent year
5. Generate predictions for test set
6. Export submission file

---

## 📊 Bonus Objective (Baseline Sales)

The project structure allows future extension to:
- Separate promotional uplift
- Predict baseline (non-promotional) demand

---

## 📁 Repository Structure

├── data/
| ├── raw/
│ | ├── weekly_train.csv
│ | └── weekly_test.csv
| └── processed/
|  └── test_predictions.csv
├── notebooks/
│ └── sales_forecasting.ipynb
├── requirements.txt
└── README.md

## 🛠 Requirements

See 'requirements.txt' file


Install dependencies:
``pip install -r requirements.txt``

## 👥 Authors

Federico Faccioli, Sara Casadio, Arash Foroozanfar





