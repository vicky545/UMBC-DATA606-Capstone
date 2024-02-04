# Predict Droughts using Weather & Soil Data

- Author - Wihar Paladugula
- Semester - Spring'24
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- GitHub - <a href="https://github.com/vicky545" target="_blank"> wihar </a>
- LinkedIn - <a href="https://www.linkedin.com/in/wihar/" target="_blank"> Wihar Paladugula </a>

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
- **Source:** https://www.kaggle.com/datasets/cdminix/us-drought-meteorological-data
- **Size:** - 1.5 GB
- **Shape:** -
  - Rows - 79,47,156 
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


- **Target Variable(s)** - score and DRK_YN (2 different models will be developed)
- The remaining columns are predictors