Food Insecurity Forecasting Models

This repository contains the Jupyter notebooks and code for analysing and forecasting food insecurity using various machine learning and statistical models.

Project Overview:
This project analyses undernourishment rates from the FAO SDG 2.1.1 dataset for Nigeria, India, and Brazil, using five different forecasting models:

ARIMA
SARIMA
Prophet
Random Forest
LSTM

Setup Instructions:
Prerequisites:

Python 3.8 or higher
Jupyter Notebook or JupyterLab

Installation:

1. Clone or download this repository
2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install required packages:
pip install pandas numpy matplotlib sklearn tensorflow statsmodels prophet pmdarima
pip install jupyter


Running the Notebooks:

1. Start Jupyter:
jupyter notebook

2. Open the notebooks:

main_models.ipynb - Contains ARIMA, Random Forest, and LSTM models
additional_models.ipynb - Contains SARIMA and Prophet models


3. Run the cells in order

Make sure the data file FAO,DF_SDG_2_1_1,1.0+all.csv is in the same directory



Data Processing Flow:

Data Cleaning:

Load CSV data from the FAO dataset
Filter for target countries (Nigeria, India, Brazil)
Clean special values like "<2.5"


Train-Test Split:

Training data: 2001-2016
Testing data: 2017-2022


Model Training:

Five separate models trained for each country
Model-specific pre-processing (scaling for LSTM, etc.)


Evaluation:

MAE (Mean Absolute Error)
RMSE (Root Mean Square Error)
R² (R-squared)


Visualisation:

Comparison plots of actual vs predicted values
Forecast visualizations through 2025



Replicating Results
To replicate the analysis:

Run the main notebook first (main_models.ipynb)
This will generate a partial results CSV file
Run the second notebook (additional_models.ipynb)
This will combine all model results
Return to the main notebook to generate visualizations

Troubleshooting

Prophet installation issues: You may need to install Prophet separately with pip install prophet
TensorFlow errors: Make sure you have the appropriate version for your system
File not found errors: Ensure the CSV data file is in the correct location
Memory errors: LSTM models may require significant RAM; reduce batch size if needed