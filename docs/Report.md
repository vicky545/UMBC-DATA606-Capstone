# Predict Droughts using Weather & Soil Data

- Author - Wihar Paladugula
- Semester - Spring'24
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- GitHub - <a href="https://github.com/vicky545" target="_blank"> wihar </a>
- LinkedIn - <a href="https://www.linkedin.com/in/wihar/" target="_blank"> Wihar Paladugula </a>
- PowerPoint Presentation: <a href="https://umbc-my.sharepoint.com/:p:/g/personal/pwihar1_umbc_edu/EQM3hfIktmNJg95d0lKXAVIBb7rhuu4qa-uTziYhxIgqlg?e=qAijyW" target="_blank"> Powerpoint </a>
- YouTube Video: <a href="https://youtu.be/Nxnv7XoK0ZY" target="_blank"> YoutubeLink </a>

## Background
### Problem Statement
This project aims to predict drought conditions across the United States using only meteorological data. The provided dataset contains daily weather measurements from 2010-2016 for precipitation, temperature, humidity, wind speed, and other variables. By analyzing patterns in these meteorological indicators, the goal is to develop automated models that can accurately predict the emergence and severity of drought events.

### Potential Real-world applications
- Developing early warning systems for emerging droughts that allow for proactive water management and mitigation strategies by reservoirs, farms, municipalities, and other water users.
- Providing meteorological drought outlooks to government agencies, commodity markets, and insurance companies to factor into their planning and operations.
- Informing drought relief response by identifying the most severely impacted regions so resources can be mobilized.
- Improving climate model projections of drought risk and water resource availability under different climate change scenarios.
- Predicting impacts on crop yields, wildfire potential, reservoir levels, groundwater recharge rates, and other drought-sensitive systems.

### Research Questions
- What meteorological variables are most predictive of drought onset and severity? Precipitation and temperature are obvious candidates, but others like humidity, wind, and solar radiation may also be useful predictors.
- What are the optimal time lags and accumulation periods for meteorological indicators of drought? For example, accumulated precipitation over the past 3 months may be more predictive than just the past month.
- Can drought be accurately predicted based solely on meteorological data, or is incorporation of hydrological data like streamflow still necessary?
- How can meteorological drought predictions be made most relevant for agricultural and other sectoral impacts?

## Data 
- **Source:** [kaggle](https://www.kaggle.com/datasets/cdminix/us-drought-meteorological-data){:target="_blank"}
- **Size:** - 1.5 GB
- **Shape:** -
  - Rows - 7,947,156 
  - Columns - 22
- **Time period** - 2010-2016
- **Each row describes** - Meteorological data for each day of the timeperiod.
- **Data Dictionary**

| Column | Data Type | Definition | Potential Values |
|-|-|-|-|  
| WS10M_MIN | Float | Minimum Wind Speed at 10 Meters | Continuous values |
| QV2M | Float | Specific Humidity at 2 Meters | Continuous positive values |  
| T2M_RANGE | Float | Temperature Range at 2 Meters | Continuous values |
| WS10M | Float | Wind Speed at 10 Meters | Continuous positive values |
| T2M | Float | Temperature at 2 Meters | Continuous values |
| WS50M_MIN | Float | Minimum Wind Speed at 50 Meters | Continuous values |
| T2M_MAX | Float | Maximum Temperature at 2 Meters | Continuous values |
| WS50M | Float | Wind Speed at 50 Meters | Continuous positive values |
| TS | Float | Earth Skin Temperature | Continuous values |
| WS50M_RANGE | Float | Wind Speed Range at 50 Meters | Continuous values |
| WS50M_MAX | Float | Maximum Wind Speed at 50 Meters | Continuous values |
| WS10M_MAX | Float | Maximum Wind Speed at 10 Meters | Continuous values |
| WS10M_RANGE | Float | Wind Speed Range at 10 Meters | Continuous values |
| PS | Float | Surface Pressure | Continuous positive values |  
| T2MDEW | Float | Dew/Frost Point at 2 Meters | Continuous values |
| T2M_MIN | Float | Minimum Temperature at 2 Meters | Continuous values |
| T2MWET | Float | Wet Bulb Temperature at 2 Meters | Continuous values |
| PRECTOT | Float | Precipitation | Continuous values |
| fips | Integer | FIPS county code | Positive integers |
| date | Date | Date of observation | Dates in YYYY-MM-DD format |
| score | Float | Drought indicator (target variable) | Continuous values from 0 to 1 |


- **Target Variable(s)** - score
- The remaining columns are predictors

## Exploratory Data Analysis
From this visualization, we observed that the majority of the data points were non-drought conditions. To handle this I used Upsampling and Class weights during  modeling.<br/>

![vis1](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis1.png)

Below Visualsations shows the distribution of all the columns in the dataset.<br/>

![vis2](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis2.png)
![vis3](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis3.png)
![vis4](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis4.png)
![vis5](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis5.png)

From below we can observe number of rows for all years, months, and days are uniformly distributed.<br/>

![vis6](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis6.png)
![vis7](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis7.jpg)
![vis8](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis8.png)

Below Stacked barchart shows distribution of Day, Month, and day for various drought scores.<br/>

![vis9](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis9.png)

Checking skewness in data, as we handled outliers the skewness, it was reduced.<br/>

![vis10](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis10.png)

A correlation analysis showed columns like QV2M, T2M, and others show strong correlations.<br/>

![vis11](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis11.png)

Despite these strong positive correlations, from these scatter plots below, we can observe a significant variance between these variables. Based on this, I decided to explore other feature selection methods.<br/>

![vis12](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis12.png)
![vis13](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis13.png)
![vis14](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/vis14.png)

## Class Imbalance and Feature Selection
A key challenge with this dataset was the class imbalance, with non-drought conditions being over-represented. To address this, we employed two techniques: SMOTE (Synthetic Minority Over-sampling Technique) and class weights.

As we have many features I used RFE(Recursive  Feature Elimination) I got the top 8 features for better modeling. The top 8 features are: 'PS', 'QV2M', 'T2M', 'T2M_MIN', 'T2M_RANGE', 'WS50M', 'WS50M_MAX', 'day'

## Model Training
1. Models for Predictive Analytics:
Models used are  Decision trees, Random forest, KNN,  Adaboost, . I have applied grid search with Hyperparameter tuning to get the best model to recieve ideal results.

2. Training Procedure:
The dataset has around 7M training records and around 2M testing records. Which was provided by diving first itself.

3. Python Packages:
I have primarily used python packages in project. They are Numpy, Pandas, matplotlib, plotly, seaborn and scikit-learn

4. Development Environments:
The development environments are
- Local machine: Jupyter Notebook 
- Online platforms: Google Colab, GitHub

5. Performance Measures of the models:
I have evaluated performance of the model using Accuracy, Recall, Precision, F1 Score, AUC Score, ROC curve.

The performance metrics of models trained and evaluated with upsampling and class weights are as below:

![mdl1](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/mdl1.png)
![mdl2](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/mdl2.png)
![mdl3](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/mdl3.png)
![mdl4](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/mdl4.png)
![mdl5](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/mdl5.png)

The performance metrics of models trained and evaluated with including Hyperparameter tuning are:

![mdl6](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/mdl6.png)
![mdl7](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/mdl7.png)
![mdl8](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/mdl8.png)
![mdl9](https://github.com/vicky545/UMBC-DATA606-Capstone/blob/main/Images/mdl9.png)

## Web App Development:
Developed a web application using Streamlit for users to interact with weather conditions.
- **Streamliapp:** <a href="https://drought-prediction.streamlit.app/" target="_blank"> WebAppLink </a>

## Conclusion:
- This study successfully developed machine learning models to predict droughts using weather and soil data. The Adaboost model with class weights, upsampling, and hyperparameter tuning achieved the highest accuracy of 85.64%. The results demonstrate the potential of leveraging data-driven approaches to forecast droughts effectively.
- Limitation: Data is till 2016 only and users has to manully enter weather conditions.
- Future Research Direction: As soon as a user grants location permissions we can add the ability to locate the user and get required conditions for past few months and predict drought level.