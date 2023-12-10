# Competition 42039 - Assessment - Senior Applied Scientist, Data Science Program
Author: Brett Harvey  
Description: This repo contains the repository and the requested write-up for the skill assessment for the above competition. The write up for supplied questions is given below. There will be links supplied to supporting material.


## How to install dependencies

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run the project

Once installed navigate to the root of the project:
```
cd /path/to/root/SeniorAppliedScientist_assement/busarrival-pred
```
From the root directory you can run your Kedro project with:

```
kedro run
```

# Expected Output:
After a successful run, the pipeline will report  and store several objects:<br>
- the versioned models will be stored in the model folder
- the predictions and the actuals for the test set will be stored in the model output folder.
- The performance for each model will be reported to stdout
![stdout](https://github.com/bharvey125/SeniorAppliedScientist_assement/blob/main/Graphs/kedro%20output.png)

# Question 1 - Identify problem parts of the Winnipeg bus system. Consider location, time, and other factors as relevant. Explain your results clearly and concisely 
Detailed analysis can be found in the notebooks [here](https://github.com/bharvey125/SeniorAppliedScientist_assement/tree/main/busarrival-pred/notebooks)

## <u>Findings:</u>
-	It was found that the trend in performance is getting worse across the three months examined.  
-	Specific routes are performing worse than others.
-	Specific Neighborhoods perform drastically worse than others after cleaning some specific routes, the best and worst are..
    - Best: Westdale - Grace Hospital
    - Worst: South St. Anne's Express
-	17:00 is the worst performing time during the week and 15:00/16:00 is the worst performing during the weekend.
-	Mid-week performance worse than weekends.

  ## <u>Trend in Avg Times Across Days Of Week</u>
  ![Count Of Extreme Events By Day](https://github.com/bharvey125/SeniorAppliedScientist_assement/blob/main/Graphs/Count%20of%20extreme%20events%20by%20day.png)
-	It was found that extreme events are more likely to occur from Tuesday to Friday. It was also found that Monday was only slightly worse in terms of extreme event occurrence then the weekend.

  ## <u>Trend in avg delay times by time of day - Weekday</u>
  ![Avg Deviation By Time Of Day - weekday](https://github.com/bharvey125/SeniorAppliedScientist_assement/blob/main/Graphs/mean%20deviation%20by%20Time%20of%20day%20-%20weekday.png)
-	The worst time of the day for avg deviation was found to be 17:00 on a weekday
-	There is also an odd spike in mean performance around 2am. I would hypothesize this is when the majority of routes shut down for the night or shift change over. The same effect is not observed on weekends. In Fact, there is a spike decrease in performance at 2am on the weekend. 



  ## <u>Trend in avg delay times by time of day - Weekend</u>
![Avg Deviation By Time Of Day - weekend](https://github.com/bharvey125/SeniorAppliedScientist_assement/blob/main/Graphs/mean%20deviation%20by%20Time%20of%20day%20-%20weekend.png)
-	These patterns hold true for individual neighborhoods as well. 
![Avg Deviation By Time Of Day - Neighborhoood](https://github.com/bharvey125/SeniorAppliedScientist_assement/blob/main/Graphs/mean%20deviation%20by%20Time%20of%20day%20and%20neighbourhood.png)

## Weather effect
- Weather only had a minor effect on mean deviation, but this requires further investigation. 

## Traffic effect
- Although we didn’t have a direct measure of traffic for the analysis. Time of day acts as a proxy. A good source of traffic data should be sourced in future iterations of this analysis. 
## area effect
- Neighbourhood had a fairly strong impact on the mean deviation
- Best performing Neighborhood is Westdale - Grace Hospital.
- The 10 worst neighbourhoods based on mean deviation are:  
        - Island Lakes, Victoria Cresent, Ridgewood South, North St. Boniface, East Elmwood, Grassie,   Archwood, Talbot-Grey, Weston, Vista, Normad Park.

  ![Best and Worst Neighborhood by Avg Deviation](https://github.com/bharvey125/SeniorAppliedScientist_assement/blob/main/Graphs/best%20and%20worst%20neighborhood%20by%20mean%20deviation.png)


# Question 2: Provide an overview of how you would approach the problem of modeling late arrivals in real-time.

*Assumption:* we’ve estimated a model with adequate performance based on the mentioned accuracy measures.<br>
*Assumption:* we include 2 lags of the deviation in the model.<br>

## Non-Technical Audience:

Through rigorous analysis and modeling, we’ve identified a model that has adequate performance to predict arrival time deviations in real-time. We approach the problem by estimating a model for each bus route based on historic performance. For each route, the model takes as an input the previous 2 Deviations on the day and some other data like weather, traffic, and time of day to produce an estimate of the deviation for the next  stop. Since we know the scheduled arrival time we can combine the forecasted deviation with the scheduled time to provide the rider with an estimated arrival time.  This approach will allow us to estimate arrival times for each route one step ahead. Providing the rider with a better understanding of when their bus will arrive.<br>

## Technical Audience:
*Assumption:*  I’m assuming you want this question to focus on the modeling and not the technical aspects of real-time deployment. Due to the maximum word requirement on the question I won’t address the deployment options here, but I have experience in designing real-time systems using technologies like Kafka (confluent is the cloud-hosted version), HiveMQ (MQTT brokers) and High-performance Time series databases (Influxdb, TimescaleDB). I’ve included a brief High-level description of a request-response type of deployment in the appendix.<br> 


There are a couple of approaches we could take. 
-	Estimating a single model and controlling for route information. This would cause issues with dimensions in the data set. 
-	Estimating a model by area of the city or by identifying route clusters and estimating a model per cluster.
-	Estimating a model per route. This will be the easiest from a modeling perspective, but would be computationally expensive and hard to implement an effective MLops strategy in production. I’m going to assume those last two issues away for this assessment and proceed with the model-per-route approach.

To start I would want to establish a benchmark to compare against, for this, I would go with a simple autoregressive-exogenous variable model. After appropriate feature engineering is completed, to ensure there is information leakage into the model the data will be split into train and test sets. From there AR-X model will be fit for each bus route. To establish a baseline I would calculate standard performance metrics on the test set. After this, I would move to more complex models, feature engineering, and hyperparameter tuning. For example: a cumulative count of late stops on the day, identifying networks in the bus data and using the deviation from the bus ahead in the network as a proxy for traffic..etc. By Iterating in this systematic way we can be sure we deliver the best-performing model.  

  To test and compare models, I would calculate the MAPE, RMSE, and R^2 for each route on the test set, then average across the bus routes to obtain a single metric[^1]. This  approach would allow us to identify underperforming routes and models, we could then focus on the edge cases and tune the models and features to increase the performance of the system overall.

# Question 3:<br>

### [Link to Repo](https://github.com/bharvey125/SeniorAppliedScientist_assement/tree/main/busarrival-pred)<br>

*Assumption:* Linear Regression was the best-performing model. This will not be true in practice, but for simplicity we will move ahead with it. Ie: AR(2) model with exogenous variables. These variables are one-hot encoded time of day and area of city.<br>
*Assumption:* Two random routes were selected to be included. Broadway-Williams and South St. Anne's Express. <br>
*Assumption:* The model is going to be put into production. <br>
*Assumption:* Focus on the Machine process and not the technology required for edge data transmission and model deployment. <br> 

After a model with the best performance has been identified, we would need to productionalize the code. To the point, most of the analysis has been done in a notebook. I recommend using Kedro for this portion of the project. It is an open-source framework for producing production-ready code.  After the notebook code has been refactored using the Kedro framework, unit testing should be done to ensure the system is behaving appropriately[^2].<br>

  ![Kedro Pipeline](https://github.com/bharvey125/SeniorAppliedScientist_assement/blob/main/Graphs/pipeline%20vizualization.png)

If the model is going to be deployed we would need to identify an adequate MLops strategy for monitoring and maintaining these roughly 85 models. Models will go stale and will need to be retrained. There are software packages out there for this, but it depends on how these individual models will be deployed (edge, cloud, on-prem).   Once it was decided on we would need to build systems to monitor for things like data drift, concept drift, and prediction drift. As well as monitor the performance and quality of incoming data[^3].<br>


# Appendix:
Brief deployment description:  

I believe the best option here would be a request-response type of model deployment.  Each bus would be streaming live data to a central (assuming cloud hosted) database. Since it’s cloud base we could leverage a cloud service provider to host live end points for the models. When a user wants an estimated arrival time, the app would make a request to the end point passing through the required data from the DB, the live prediction would then be add or subtracted from the scheduled arrival time to provide the end user with the new predicted arrival time. Technical specifications are outside the scope of this document.
	




[^1]: These metrics will be calculated in a one-step-ahead fashion.<br>
[^2]: Unit testing is outside of the scope of this assessment but should be done rigorously.<br> 
[^3]: The project toy model is implemented using the Kedro framework. A production-ready Python framework that makes bridging the gap between prod and POC easier, because of this there are extra boilerplate files. The majority of the work is being done in the pipeline files in src folder.<br>


