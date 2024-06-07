# Forecasting Dispatch Processing Times

This project aims to predict the processing times for non-stock shipments at a logistics center using various machine learning models. We explore different approaches including LSTM (Long Short-Term Memory) and hybrid LSTM-Attention models to handle the time-dependent nature of the data.

## Table of Contents
- [Overview](#overview)
- [Data Description](#data-description)
- [Data Preparation](#data-preparation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Feature Engineering](#feature-engineering)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributors](#contributors)

## Overview
The accurate prediction of dispatch processing times is crucial for logistics centers to ensure efficient operations and timely deliveries. This project involves:
1. Data loading and merging from multiple Excel files.
2. Data cleaning and preprocessing.
3. Exploratory Data Analysis (EDA) to identify trends and patterns.
4. Developing and evaluating machine learning models for time series. (Not yet implemented)

## Data Description
The datasets used in this project include:
- **Export_LIPS.xlsx**: Sales document delivery item data.
- **Export_Packstuecke_MVA.xlsx**: Package details such as dimensions and weight.
- **Export_TBL_MVA.xlsx**: Main table with shipment processing details.
- **Export_Traffic_Tracking.xlsx**: Tracking data for shipment searches.
- **EXPORT_VBAK.xlsx**: Sales document header data.
- **Export_VTTP.xlsx**: Delivery item data.

## Data Preparation
1. **Loading Data**: Load the datasets using pandas.
2. **Merging Data**: Merge the datasets on common keys to create a unified DataFrame.
3. **Data Cleaning**: Handle missing values, correct data types, and remove duplicates.

## Exploratory Data Analysis (EDA)
1. **Summary Statistics**: Provide a summary of the numerical data.
2. **Distribution Analysis**: Visualize the distribution of processing times.
3. **Correlation Analysis**: Identify correlations between numeric features using a heatmap.

## Requirements
To run this project, you need the following libraries:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/forecasting-dispatch-processing-times.git
   cd forecasting-dispatch-processing-times
