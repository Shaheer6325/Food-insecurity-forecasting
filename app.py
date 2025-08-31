import streamlit as st
import pandas as pd
import langchain
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import matplotlib.pyplot as plt
import os
from project_data import *

# Set page config
st.set_page_config(
    page_title="Food Insecurity Forecasting Assistant",
    page_icon="🌍",
    layout="wide"
)

# Setup the LLM with Ollama
@st.cache_resource
def get_llm():
    try:
        # Using a smaller model like mistral is good for local use
        return Ollama(model="mistral")
    except Exception as e:
        st.error(f"Error connecting to Ollama: {str(e)}")
        st.error("Make sure Ollama is installed and running (https://ollama.ai/)")
        return None

# Create a pandas DataFrame for visualization
def get_evaluation_df():
    df = pd.DataFrame(EVALUATION_DATA, columns=["Country", "Model", "MAE", "RMSE", "R²"])
    return df

# Format yearly predictions for prompt
def format_yearly_predictions(yearly_predictions):
    formatted = []
    
    for country, models in yearly_predictions.items():
        formatted.append(f"\n{country}:")
        
        # First print actuals in a clean format
        if 'Actual' in models:
            actual_values = [f"{year}: {value}%" for year, value in models['Actual'].items()]
            formatted.append(f"  Actual values: {', '.join(actual_values)}")
        
        # Then print model predictions
        for model_name, predictions in models.items():
            if model_name != 'Actual':
                pred_values = [f"{year}: {value:.2f}%" for year, value in predictions.items()]
                formatted.append(f"  {model_name} predictions: {', '.join(pred_values)}")
    
    return "\n".join(formatted)

# Prepare the LLM prompt template
prompt_template = PromptTemplate(
    input_variables=["question", "project_info", "eval_data", "best_models", 
                     "country_insights", "model_descriptions", "yearly_predictions"],
    template="""
    You are an AI assistant for a food insecurity forecasting project. Answer the user's question based ONLY on the following project information.
    
    PROJECT INFORMATION:
    {project_info}
    
    EVALUATION DATA:
    {eval_data}
    
    BEST MODELS:
    {best_models}
    
    COUNTRY INSIGHTS:
    {country_insights}
    
    MODEL DESCRIPTIONS:
    {model_descriptions}
    
    YEARLY PREDICTIONS:
    {yearly_predictions}
    
    User question: {question}
    
    Your answer (keep it clear, concise and factual - if you don't know, just say so):
    """
)

# Application UI
st.title("Food Insecurity Forecasting Assistant")

st.markdown("""
This assistant can answer questions about the food insecurity forecasting project 
that used machine learning models to predict undernourishment percentages in India, Nigeria, and Brazil.
""")

# Two columns layout
col1, col2 = st.columns([2, 1])

with col1:
    # Question input
    user_question = st.text_input("Ask a question about the project:", 
                                 placeholder="e.g., What did LSTM predict for Nigeria in 2022?")
    
    # Initialize LLM and create chain
    llm = get_llm()
    if llm and user_question:
        # Prepare the evaluation data as a formatted string
        eval_df = get_evaluation_df()
        eval_data_str = eval_df.to_string()
        
        best_models_str = "\n".join([f"{country}: {info['model']} (MAE: {info['MAE']})" 
                                   for country, info in BEST_MODELS.items()])
        
        country_insights_str = "\n".join([f"{country}: {insight}" 
                                        for country, insight in COUNTRY_INSIGHTS.items()])
        
        model_descriptions_str = "\n".join([f"{model}: {description}" 
                                          for model, description in MODEL_DESCRIPTIONS.items()])
                                          
        yearly_predictions_str = format_yearly_predictions(YEARLY_PREDICTIONS)
        
        # Create the chain
        chain = LLMChain(llm=llm, prompt=prompt_template)
        
        try:
            # Run the chain with all data including yearly predictions
            with st.spinner("Generating answer..."):
                response = chain.run(
                    question=user_question,
                    project_info=PROJECT_INFO,
                    eval_data=eval_data_str,
                    best_models=best_models_str,
                    country_insights=country_insights_str,
                    model_descriptions=model_descriptions_str,
                    yearly_predictions=yearly_predictions_str
                )
            
            # Display the answer
            st.markdown("### Answer:")
            st.markdown(response)
        except Exception as e:
            st.error(f"Error generating answer: {str(e)}")
            st.error("Make sure Ollama is running properly and the selected model is available.")

with col2:
    st.markdown("### Evaluation Metrics")
    
    # Add tab option to switch between metrics and predictions
    tab1, tab2 = st.tabs(["Model Metrics", "Yearly Predictions"])
    
    with tab1:
        # Show country selector and filter table
        selected_country = st.selectbox("Select Country:", ["All Countries", "Nigeria", "India", "Brazil"], key="country_select1")
        
        df = get_evaluation_df()
        if selected_country != "All Countries":
            df = df[df["Country"] == selected_country]
        
        # Sort by MAE to show best models first
        df = df.sort_values(by=["Country", "MAE"])
        
        # Display the table
        st.dataframe(df, hide_index=True)
        
        # Display a simple bar chart of MAE by model
        if selected_country != "All Countries":
            st.markdown(f"### MAE by Model for {selected_country}")
            fig, ax = plt.subplots(figsize=(5, 3))
            country_df = df[df["Country"] == selected_country].sort_values(by="MAE")
            ax.bar(country_df["Model"], country_df["MAE"], color='skyblue')
            ax.set_ylabel("MAE (lower is better)")
            ax.set_title(f"Model Performance for {selected_country}")
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)
    
    with tab2:
        # Yearly predictions explorer
        pred_country = st.selectbox("Select Country:", ["Nigeria", "India", "Brazil"], key="country_select2")
        pred_year = st.slider("Select Year:", min_value=2016, max_value=2025, value=2022)
        pred_model = st.selectbox("Select Model:", ["All Models", "ARIMA", "SARIMA", "Prophet", "RF", "LSTM"])
        
        # Create prediction data table
        if pred_model == "All Models":
            # Show all models for the selected year
            data = {
                "Model": ["Actual"] + ["ARIMA", "SARIMA", "Prophet", "RF", "LSTM"],
                f"Value ({pred_year})": [
                    YEARLY_PREDICTIONS[pred_country]["Actual"].get(pred_year, "N/A"),
                    YEARLY_PREDICTIONS[pred_country]["ARIMA"][pred_year],
                    YEARLY_PREDICTIONS[pred_country]["SARIMA"][pred_year],
                    YEARLY_PREDICTIONS[pred_country]["Prophet"][pred_year],
                    YEARLY_PREDICTIONS[pred_country]["RF"][pred_year],
                    YEARLY_PREDICTIONS[pred_country]["LSTM"][pred_year]
                ]
            }
            pred_df = pd.DataFrame(data)
        else:
            # Show selected model for all years
            years = range(2016, 2026)
            data = {"Year": list(years)}
            
            # Add actual values where available
            actual_values = []
            for year in years:
                actual_values.append(YEARLY_PREDICTIONS[pred_country]["Actual"].get(year, "N/A"))
            data["Actual"] = actual_values
            
            # Add selected model predictions
            data[pred_model] = [YEARLY_PREDICTIONS[pred_country][pred_model][year] for year in years]
            
            pred_df = pd.DataFrame(data)
        
        st.dataframe(pred_df, hide_index=True)
        
        # Plot the data
        if pred_model == "All Models":
            # Bar chart for all models in selected year
            st.markdown(f"### {pred_country} Predictions for {pred_year}")
            fig, ax = plt.subplots(figsize=(5, 3))
            
            # Filter out Actual if it's N/A
            plot_df = pred_df.copy()
            if plot_df.iloc[0, 1] == "N/A":
                plot_df = plot_df.iloc[1:].reset_index(drop=True)
                
            ax.bar(plot_df["Model"], plot_df[f"Value ({pred_year})"], color='lightgreen')
            ax.set_ylabel("Undernourishment (%)")
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            # Line chart for selected model across years
            st.markdown(f"### {pred_model} Predictions for {pred_country}")
            fig, ax = plt.subplots(figsize=(5, 3))
            
            # Plot actual values where available
            actual_years = [year for year in range(2016, 2023)]
            actual_values = [YEARLY_PREDICTIONS[pred_country]["Actual"].get(year, None) for year in actual_years]
            actual_values = [val for val in actual_values if val is not None]
            ax.plot(actual_years[:len(actual_values)], actual_values, 'o-', label="Actual", color="black")
            
            # Plot model prediction for all years
            model_years = list(range(2016, 2026))
            model_values = [YEARLY_PREDICTIONS[pred_country][pred_model][year] for year in model_years]
            ax.plot(model_years, model_values, 's--', label=pred_model, color="blue")
            
            ax.set_ylabel("Undernourishment (%)")
            ax.set_xlabel("Year")
            ax.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Food Insecurity Forecasting Project - Final Year Project")