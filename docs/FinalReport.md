# Predicting Airline Passenger Satisfaction

- Author - Siddhidhatri Rohith Reddy Jaggari
- Semester - Spring'24
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- GitHub - <a href="https://github.com/SiddhiRohith29/" target="_blank"> Siddhi GitHub </a>
- LinkedIn - <a href="https://www.linkedin.com/in/siddhidhatri-rohith-reddy-jaggari-a4aa42183/" target="_blank"> Siddhidhatri Rohith LinkedIn </a>

## Background
### Problem Statement
The objective is to analyze this dataset and extract actionable insights to enhance customer satisfaction. The specific goals include:

1. Understanding the demographic distribution of customers and their travel preferences.
2. Identifying factors influencing customer satisfaction, such as onboard service quality, cleanliness, food and drink options, in-flight entertainment, and Wi-Fi service.
3. Investigating the impact of flight delays on customer satisfaction.
4. Assessing the relationship between satisfaction and factors like class, type of travel, and flight distance.

### Potential Real-world applications
1. **Airline Service Improvement:** Airlines can use the insights from this dataset to enhance various aspects of their services such as onboard service quality, cleanliness, food and drink options, in-flight entertainment, and Wi-Fi service to improve overall customer satisfaction.
2. **Customer Segmentation:** Airlines can segment their customers based on demographics and travel preferences to offer personalized services and targeted marketing campaigns.
3. **Operational Efficiency:** Understanding the impact of flight delays on customer satisfaction can help airlines optimize their flight schedules, improve punctuality, and minimize disruptions.
4. **Marketing and Pricing Strategies:** By assessing the relationship between satisfaction and factors like class, type of travel, and flight distance, airlines can refine their marketing strategies and pricing models to attract more customers and increase revenue.

### Research Questions
1. What are the key demographic factors influencing customer satisfaction in the airline industry?
2. How do different aspects of onboard services impact overall customer satisfaction?
3. What is the relationship between flight delays and customer satisfaction, and how can airlines mitigate the negative effects of delays?
   
## Data 
- **Source:** https://www.kaggle.com/datasets/ahmedelsharkaw/airline-passenger-satisfaction?select=airline_passenger_satisfaction.csv 
- **Size:** - 12.88 MB
- **Shape:** -
  - Rows - 129880 
  - Columns - 24
- **Each row describes** - Customer satisfaction rating for various criteria.
- **Data Dictionary**

| Column                                  | Data Type | Definition                                  | Potential Values                |
|-----------------------------------------|-----------|---------------------------------------------|--------------------------------|
| ID                                      | Integer   | Unique identifier for each observation     | Positive integers              |
| Gender                                  | String    | Gender of the passenger                     | Male, Female                   |
| Age                                     | Integer   | Age of the passenger                        | Positive integers              |
| Customer Type                           | String    | Type of customer                           | First-time, Returning          |
| Type of Travel                          | String    | Purpose of travel                           | Business, Personal             |
| Class                                   | String    | Class of travel                             | Business, Economy, Economy Plus|
| Flight Distance                         | Integer   | Distance of the flight in kilometers        | Positive integers              |
| Departure Delay                         | Integer   | Delay in minutes at departure               | Non-negative integers          |
| Arrival Delay                           | Float     | Delay in minutes at arrival                 | Non-negative floats            |
| Departure and Arrival Time Convenience  | Integer   | Rating of convenience regarding departure and arrival times | 1-5 (1 being lowest, 5 being highest) |
| Ease of Online Booking                  | Integer   | Rating of ease of online booking            | 1-5 (1 being lowest, 5 being highest) |
| Check-in Service                        | Integer   | Rating of check-in service                  | 1-5 (1 being lowest, 5 being highest) |
| Online Boarding                         | Integer   | Rating of online boarding experience        | 1-5 (1 being lowest, 5 being highest) |
| Gate Location                           | Integer   | Rating of gate location convenience         | 1-5 (1 being lowest, 5 being highest) |
| On-board Service                        | Integer   | Rating of on-board service                  | 1-5 (1 being lowest, 5 being highest) |
| Seat Comfort                            | Integer   | Rating of seat comfort                      | 1-5 (1 being lowest, 5 being highest) |
| Leg Room Service                        | Integer   | Rating of leg room service                  | 1-5 (1 being lowest, 5 being highest) |
| Cleanliness                             | Integer   | Rating of cleanliness                       | 1-5 (1 being lowest, 5 being highest) |
| Food and Drink                          | Integer   | Rating of food and drink                    | 1-5 (1 being lowest, 5 being highest) |
| In-flight Service                       | Integer   | Rating of in-flight service                 | 1-5 (1 being lowest, 5 being highest) |
| In-flight Wifi Service                  | Integer   | Rating of in-flight WiFi service            | 1-5 (1 being lowest, 5 being highest) |
| In-flight Entertainment                 | Integer   | Rating of in-flight entertainment           | 1-5 (1 being lowest, 5 being highest) |
| Baggage Handling                        | Integer   | Rating of baggage handling                  | 1-5 (1 being lowest, 5 being highest) |
| Satisfaction                            | String    | Passenger satisfaction with the flight      | Satisfied, Neutral or Dissatisfied |



- **Target Variable(s)** - Satisfaction
- The remaining columns are predictors.

### Checking Target Variable is Balanced or not
<img src="https://github.com/SiddhiRohith29/UMBC-DATA606-Capstone/blob/main/docs/newplot.png" alt="Headshot" width="250" height="250">.
- The Target Variable is Balanced.

### Model Training
1. Models for Predictive Analytics:
Models used are Logistic regression, KNN, Gradient Boost, Random forest and XGboost. I have applied grid search on the best model to receive idea results.

2. Training Procedure:
I have performed the Train vs test split for 70/30 to ensure the model learns effectively and generalizes well to new data.

3. Python Packages:
I have primarily used python packages in project. They are Numpy, Pandas, missingno, matplotlib, plotly, seaborn and scikit-learn

4. Development Environments:
The development environments are
- Local machine: Jupyter Notebook 
- Online platforms: Google Colab, GitHub

5.Performance Measures of the models
I have evaluated performance of the model using Accuracy, Classification Report and ROC curve.

### Airline Satisfaction Prediction Web App Development:
1. **User Interface for Ratings:** The app provides a simple and intuitive interface for users to rate various aspects of an airline's service, such as cleanliness, food and drink, online boarding, in-flight WiFi service, and seat comfort on a scale from 1 to 5.
2. **Prediction Button:** After ratings are input, there is a "Predict Satisfaction" button suggesting the app uses the given ratings to predict the level of satisfaction of a user with the airline services.
3. **Satisfaction Output:** The app displays the prediction output below the button, in this case indicating that the service is "Neutral or Dissatisfied" based on the low ratings provided, which demonstrates the app's capability to process user input and deliver real-time feedback.

## Conclusion: Airline Satisfaction System

This project successfully developed an Airline Satisfaction Prediction System under the guidance of Dr. Chaojie (Jay) Wang, with the diligent effort of Jaggari Siddhidhatri Rohith Reddy. This capstone project aimed to distill actionable insights from customer feedback, enhancing the airline service experience.

### Achievements:
- **Comprehensive Analysis:** We mapped the demographic distribution and travel preferences of customers, uncovering essential insights into the factors that drive customer satisfaction, such as onboard services, cleanliness, and in-flight entertainment.
- **Data-Driven Insights:** Through meticulous data cleaning and visualization, we revealed key influences on customer satisfaction, such as the significant impact of flight delays and the varying satisfaction levels among different demographic groups.
- **Robust Modeling:** Our exploration of various classification models, from Random Forest to XGBoost, allowed us to predict customer satisfaction with high accuracy, as demonstrated by our ROC AUC scores and cross-validation results.

### Implications:
- The project holds the potential to revolutionize how airlines understand and improve customer satisfaction, with direct applications in service quality enhancement, customer segmentation, and operational efficiency.
- Future directions include refining the models for greater precision and exploring the nuanced preferences of diverse customer segments.



