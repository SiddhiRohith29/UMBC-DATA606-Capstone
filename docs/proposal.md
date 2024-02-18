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
5. Developing recommendations for improving overall customer satisfaction based on the analysis.

By addressing these objectives, the airline aims to tailor its services to better meet customer expectations and enhance their overall flying experience.

### Potential Real-world applications
1. **Airline Service Improvement:** Airlines can use the insights from this dataset to enhance various aspects of their services such as onboard service quality, cleanliness, food and drink options, in-flight entertainment, and Wi-Fi service to improve overall customer satisfaction.
2. **Customer Segmentation:** Airlines can segment their customers based on demographics and travel preferences to offer personalized services and targeted marketing campaigns.
3. **Operational Efficiency:** Understanding the impact of flight delays on customer satisfaction can help airlines optimize their flight schedules, improve punctuality, and minimize disruptions.
4. **Marketing and Pricing Strategies:** By assessing the relationship between satisfaction and factors like class, type of travel, and flight distance, airlines can refine their marketing strategies and pricing models to attract more customers and increase revenue.
5. **Competitive Analysis:** Airlines can benchmark their performance against competitors in terms of customer satisfaction and service quality to identify areas for improvement and maintain a competitive edge in the market.

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
- The remaining columns are predictors

### Checking Target Variable is Balanced or not
<img src="https://github.com/SiddhiRohith29/UMBC-DATA606-Capstone/blob/main/docs/newplot.png" alt="Headshot" width="150" height="150">

- I want to implement SMOTE Technique for balancing target variable.