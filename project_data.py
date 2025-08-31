# project_data.py

# Model evaluation results
EVALUATION_DATA = [
    # Nigeria
    ["Nigeria", "ARIMA", 4.4426, 5.1197, -3.2284],
    ["Nigeria", "RF", 3.3127, 4.2408, -1.5508],
    ["Nigeria", "LSTM", 4.6967, 5.5363, -3.3472],
    ["Nigeria", "SARIMA", 5.5973, 6.6062, -5.1898],
    ["Nigeria", "Prophet", 4.2607, 5.5027, -3.2946],
    # India
    ["India", "ARIMA", 2.5421, 3.4190, -5.0256],
    ["India", "RF", 1.3403, 1.4322, -0.0574],
    ["India", "LSTM", 1.3469, 1.4572, -0.0945],
    ["India", "SARIMA", 2.5421, 3.4190, -5.0256],
    ["India", "Prophet", 3.7629, 4.6150, -9.9787],
    # Brazil
    ["Brazil", "ARIMA", 0.5714, 0.8992, -0.6774],
    ["Brazil", "RF", 0.5932, 0.8127, -0.3701],
    ["Brazil", "LSTM", 0.5755, 0.8811, -0.6105],
    ["Brazil", "SARIMA", 0.5714, 0.8992, -0.6774],
    ["Brazil", "Prophet", 0.5714, 0.8992, -0.6774],
]

# Project information
PROJECT_INFO = """
Project Title: Machine Learning Prediction based model for food insecurity forecasting
Dataset: FAO SDG 2.1.1 dataset tracking % of population undernourished from 2001 to 2022
Countries: India, Nigeria, and Brazil
Models Implemented: ARIMA, SARIMA, Prophet, Random Forest, LSTM
Training Period: 2001-2016
Testing Period: 2017-2022
Key Findings:
- Random Forest performed best for Nigeria (MAE: 3.31)
- Random Forest performed best for India (MAE: 1.34)
- ARIMA, SARIMA and Prophet models performed equally well for Brazil (MAE: 0.57)
- Most models failed to predict the COVID-19 related rise in undernourishment
- All models had negative R² values showing the difficulty in forecasting during unprecedented events
"""

# Best models per country
BEST_MODELS = {
    "Nigeria": {"model": "RF", "MAE": 3.31, "RMSE": 4.24},
    "India": {"model": "RF", "MAE": 1.34, "RMSE": 1.43},
    "Brazil": {"model": "ARIMA/SARIMA/Prophet", "MAE": 0.57, "RMSE": 0.90}
}

# Country specific insights
COUNTRY_INSIGHTS = {
    "Nigeria": "Nigeria showed the most dramatic increase in undernourishment during 2019-2022, rising from 11.8% to 18.0%. None of the models successfully predicted this sharp increase.",
    "India": "India's undernourishment levels rose from 10.3% in 2018 to 14.0% in 2021, with Random Forest and LSTM models performing best.",
    "Brazil": "Brazil had historically low undernourishment (2.5%) which suddenly increased to 4.2% in 2021. All models predicted the same constant value of 2.5%, leading to identical performance metrics for some models."
}

# Model descriptions
MODEL_DESCRIPTIONS = {
    "ARIMA": "AutoRegressive Integrated Moving Average - A statistical model that uses its own lags and lagged forecast errors for prediction.",
    "SARIMA": "Seasonal ARIMA - Extends ARIMA by including seasonal components.",
    "Prophet": "Facebook Prophet - A decomposable additive model with trend, seasonality, and holiday components.",
    "RF": "Random Forest - An ensemble of decision trees with predictions made by averaging the outputs of individual trees.",
    "LSTM": "Long Short-Term Memory - A recurrent neural network architecture designed to model temporal sequences and time series."
}

# Year-by-year predictions (2016-2025)
YEARLY_PREDICTIONS = {
    "Nigeria": {
        "Actual": {2016: 10.7, 2017: 11.3, 2018: 11.8, 2019: 13.6, 2020: 15.1, 2021: 17.0, 2022: 18.0},
        "ARIMA": {2016: 10.28, 2017: 10.14, 2018: 10.05, 2019: 9.99, 2020: 9.96, 2021: 9.93, 2022: 9.92, 2023: 9.91, 2024: 9.90, 2025: 9.89},
        "SARIMA": {2016: 9.99, 2017: 9.30, 2018: 8.58, 2019: 7.97, 2020: 7.57, 2021: 7.41, 2022: 7.50, 2023: 7.82, 2024: 7.95, 2025: 8.18},
        "Prophet": {2016: 10.60, 2017: 10.47, 2018: 10.34, 2019: 10.20, 2020: 8.82, 2021: 8.69, 2022: 8.56, 2023: 8.43, 2024: 6.57, 2025: 5.28},
        "RF": {2016: 10.77, 2017: 10.66, 2018: 10.57, 2019: 10.60, 2020: 10.58, 2021: 10.60, 2022: 10.58, 2023: 10.58, 2024: 10.58, 2025: 10.58},
        "LSTM": {2016: 9.70, 2017: 9.56, 2018: 9.36, 2019: 9.13, 2020: 9.04, 2021: 8.95, 2022: 8.88, 2023: 8.85, 2024: 8.86, 2025: 8.86}
    },
    "India": {
        "Actual": {2016: 11.5, 2017: 10.5, 2018: 10.3, 2019: 11.6, 2020: 13.1, 2021: 14.0, 2022: 13.7},
        "ARIMA": {2016: 11.85, 2017: 11.61, 2018: 11.46, 2019: 11.35, 2020: 11.29, 2021: 11.24, 2022: 11.21, 2023: 11.20, 2024: 11.18, 2025: 11.17},
        "SARIMA": {2016: 11.64, 2017: 10.95, 2018: 10.23, 2019: 9.57, 2020: 9.02, 2021: 8.56, 2022: 8.11, 2023: 7.67, 2024: 7.22, 2025: 6.47},
        "Prophet": {2016: 10.42, 2017: 9.73, 2018: 9.03, 2019: 8.34, 2020: 7.64, 2021: 6.94, 2022: 6.25, 2023: 5.55, 2024: 4.86, 2025: 4.86},
        "RF": {2016: 12.44, 2017: 12.40, 2018: 12.36, 2019: 12.36, 2020: 12.36, 2021: 12.36, 2022: 12.36, 2023: 12.36, 2024: 12.36, 2025: 12.36},
        "LSTM": {2016: 12.53, 2017: 12.53, 2018: 12.53, 2019: 12.53, 2020: 12.53, 2021: 12.53, 2022: 12.53, 2023: 12.53, 2024: 12.53, 2025: 12.53}
    },
    "Brazil": {
        "Actual": {2016: 2.5, 2017: 2.5, 2018: 2.5, 2019: 2.5, 2020: 3.4, 2021: 4.2, 2022: 3.9},
        "ARIMA": {2016: 2.52, 2017: 2.53, 2018: 2.55, 2019: 2.56, 2020: 2.58, 2021: 2.59, 2022: 2.60, 2023: 2.61, 2024: 2.62, 2025: 2.63},
        "SARIMA": {2016: 2.50, 2017: 2.50, 2018: 2.50, 2019: 2.50, 2020: 2.50, 2021: 2.50, 2022: 2.50, 2023: 2.50, 2024: 2.50, 2025: 2.50},
        "Prophet": {2016: 2.50, 2017: 2.50, 2018: 2.50, 2019: 2.50, 2020: 2.50, 2021: 2.50, 2022: 2.50, 2023: 2.50, 2024: 2.50, 2025: 2.50},
        "RF": {2016: 2.65, 2017: 2.65, 2018: 2.65, 2019: 2.65, 2020: 2.65, 2021: 2.65, 2022: 2.65, 2023: 2.65, 2024: 2.65, 2025: 2.65},
        "LSTM": {2016: 2.53, 2017: 2.53, 2018: 2.53, 2019: 2.53, 2020: 2.53, 2021: 2.53, 2022: 2.53, 2023: 2.53, 2024: 2.53, 2025: 2.53}
    }
}