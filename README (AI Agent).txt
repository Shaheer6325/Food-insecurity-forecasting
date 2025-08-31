Food Insecurity Forecasting Assistant
This repository contains a simple AI assistant that can answer questions about food insecurity forecasting models built as part of a final year project.

Setup Instructions:

Prerequisites:

Python 3.8 or higher
Ollama (for running local LLMs)

Installation:
1. Clone or download this repository
2. Install required packages

pip install streamlit langchain langchain_community ollama pandas matplotlib

Install and start Ollama, Download and install Ollama from https://ollama.ai/

After installation, start the Ollama service:
ollama serve

Pull the required model

In a new terminal window, run:
ollama pull mistral


Running the Application:

1. Start Ollama service (if not already running):
ollama serve

2. Run the Streamlit app Navigate to the project directory and run:
cd path/to/food_insecurity_agent
streamlit run app.py

Access the web interface
The application should automatically open in your browser at http://localhost:8501

Usage

Type questions in the text input field about the food insecurity forecasting project
View model evaluation metrics on the right side of the interface
Select specific countries to see their performance charts

Example Questions

"Which model performed best for Nigeria?"
"What happened to undernourishment rates during COVID-19?"
"Why do the models have negative R² values?"
"Compare the performance of LSTM and Random Forest"
"Which country was most difficult to forecast?"
"What did the LSTM model predict for Nigeria in 2022?"

Troubleshooting

"Error connecting to Ollama" message: Ensure Ollama is running with ollama serve in a separate terminal
Slow responses: If responses are too slow, you can try a smaller model by changing model="mistral" to model="tinyllama" in app.py
Model not found: Run ollama pull mistral to download the required model