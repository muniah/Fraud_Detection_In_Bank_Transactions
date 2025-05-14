```markdown
# Fraud Detection System

A modular machine learning pipeline for detecting fraudulent financial transactions.

## Features

- **10+ Classifiers**: Random Forest, XGBoost, LightGBM, CatBoost, SVM, etc.
- **Hyperparameter Tuning**: GridSearchCV with custom parameter grids
- **Class Imbalance Handling**: SMOTE oversampling + automatic class weights
- **Comprehensive Metrics**: ROC-AUC, accuracy, precision/recall reports
- **Production-Ready**: Modular design with error handling

## Installation

```bash
git clone https://github.com/yourusername/fraud-detection.git
cd fraud-detection
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Quick Start

```python
from model_evaluator import ModelEvaluator
from sklearn.ensemble import RandomForestClassifier

# 1. Initialize with your models
evaluator = ModelEvaluator(
    models={'Random Forest': RandomForestClassifier()},
    param_grids={'Random Forest': {'n_estimators': [100, 200]}}
)

# 2. Run evaluation
results = evaluator.run_evaluation(X_train, y_train, X_test, y_test)

# 3. Get best model
best_name, best_model = evaluator.get_best_model()
```

## Configuration

### Custom Models
```python
models = {
    'XGBoost': xgb.XGBClassifier(),
    'SVM': SVC(probability=True)
}

param_grids = {
    'XGBoost': {'learning_rate': [0.01, 0.1]},
    'SVM': {'C': [0.1, 1], 'kernel': ['rbf']}
}
```

## Output Example
```
==============================
Evaluating Random Forest
==============================

Best params: {'n_estimators': 200}
Train Accuracy: 0.982 | Test Accuracy: 0.956
ROC AUC: 0.983

Classification Report:
              precision  recall  f1-score   support
           0       0.98      0.98      0.98      2099
           1       0.85      0.86      0.86       301
```

## Project Structure
```
fraud-detection/
├── data/                    # Sample datasets
├── models/                  # Saved model binaries
├── src/
│   ├── evaluation.py        # Main evaluation class
│   ├── preprocessing.py     # Data cleaning
│   └── visualization.py     # Plotting utils
└── requirements.txt
```

## Dependencies
- Python 3.8+
- scikit-learn>=1.0
- imbalanced-learn
- pandas
- numpy
- Optional: xgboost, lightgbm, catboost
