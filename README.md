# Competition 42039 - Assessment Invitation - Senior Applied Scientist, Data Science Program
Author: Brett Harvey  
Description: This repo contains the repository and the requested write-up for the skill assessment for the above competition. The write up for supplied questions is given below. There will be links supplied to supporting material.


## How to install dependencies

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

# Question 1 - Identify problem parts of the Winnipeg bus system. Consider location, time, and other factors as relevant. Explain your results clearly and concisely 
Detailed analysis can be found in the notebooks [here](https://github.com/bharvey125/SeniorAppliedScientist_assement/tree/main/busarrival-pred/notebooks)

## <u>Findings:</u>
-	It was found that the trend in performance is getting worse across the three months examined.  
-	Specific routes are performing worse than others.
-	Specific Neighborhoods perform drastically worse than others After cleaning some specific routes, the best and worst are..
  - Best: Westdale - Grace Hospital
  - Worst: South St. Anne's Express
-	17:00 is the worst performing time during the week and 15:00/16:00 is the worst performing during the weekend.
-	Mid-week performance worse than weekends.

  ## <u>Trend in Avg Times Across Days Of Week</u>
  ![Count Of Extreme Events By Day](https://github.com/bharvey125/SeniorAppliedScientist_assement/blob/main/Graphs/Count%20of%20extreme%20events%20by%20day.png)
- An extreme event is defined as deviations that are 1.5*middle 50% of the data away from the bottom 25%
- It was found that extreme events are more likely to occur from Tuesday to Friday. It was also found that Monday was only slightly worse in terms of extreme event occurrence than the weekend.

  ## <u>Trend in avg delay times by time of day - Weekday</u>
  ![Avg Deviation By Time Of Day - weekday](https://github.com/bharvey125/SeniorAppliedScientist_assement/blob/main/Graphs/mean%20deviation%20by%20Time%20of%20day%20-%20weekday.png)
- Not surprisingly the worst time of the day for avg deviation was found to be 17:00 on a weekday
- There is also an odd spike in mean performance around 2 am. I would hypothesize this is when the majority of routes shut down for the night or shifts change over. The same effect is not observed on weekends. In Fact there is a spike decrease in performance at 2 am on the weekend.


  ## <u>Trend in avg delay times by time of day - Weekend</u>
![Avg Deviation By Time Of Day - weekend](https://github.com/bharvey125/SeniorAppliedScientist_assement/blob/main/Graphs/mean%20deviation%20by%20Time%20of%20day%20-%20weekend.png)
- The worst time for deviation on the weekend is 15:00. There is also a reversal of the 2am spike. This would need further investigation to understand the cause.q
- These patterns hold for individual neighborhoods as well. The worst-performing neighborhoods all experience peak avg deviation around 17:00.
![Avg Deviation By Time Of Day - Neighborhoood](https://github.com/bharvey125/SeniorAppliedScientist_assement/blob/main/Graphs/mean%20deviation%20by%20Time%20of%20day%20and%20neighbourhood.png)

## weather effect
- Weather only had a minor effect on mean deviation, but this requires further investigation. 

## traffic effect
- Although we didn’t have a direct measure of traffic for the analysis. Time of day acts as a proxy. A good source of traffic data should be sourced in future iterations of this analysis. 
## area effect
- The Neighbourhood had a fairly strong impact on the mean deviation
- The 10 worst neighborhoods based on mean deviation are:
- Island Lakes, Victoria Cresent, Ridgewood South, North St. Boniface, East Elmwood, Grassie,   Archwood, Talbot-Grey, Weston, Vista, Normad Park.

# Question 2

** Assumption: we’ve estimated a model with adequate performance based on the mentioned accuracy measures.
** Assumption: we include 2 lags of the deviation in the model

## Non-Technical Audience:

Through rigorous analysis and modeling, we’ve identified a model that has adequate performance. We approach the problem by estimating a model for each bus route based on historic performance. For each route, the model takes as an input the previous 2 Deviations on the day and some other data like weather, traffic, and time of day to produce an estimate of the deviation for the next  stop. Since we know the scheduled arrival time we can combine the forecasted deviation with the scheduled time to provide the rider with an estimated arrival time.  This approach will allow us to estimate arrival times for each route one step ahead. Providing the rider with a better understanding of when their bus will arrive.

## Technical Audience:

There are a couple of approaches we could take. 
-	Estimating a single model and controlling for route information. This would cause issues with dimensions in the data set. 
-	Estimating a model by area of the city or by identifying route clusters and estimating a model per cluster.
-	Estimating a model per route. This will be the easiest from a modeling perspective, but would be computationally expensive and hard to implement an effective MLops strategy in production. I’m going to take those last two issues away for this assessment and proceed with the model-per-route approach.
To start I would want to establish a benchmark to compare against, for this, I would go with a simple autoregressive-exogenous variable model. After appropriate feature engineering is completed to ensure there is no leakage, the data will be split into train and test data and an AR-X model will be fit for each bus route. Next, I would move to more complex models and feature engineering. For example: a cumulative count of late stops…etc. Once the models are fit I would start exploring performance and model averaging procedures.  To test and compare models, I would calculate the MAPE, RMSE, and R^2 for each route on the test set,( note: these will be calculated in a one-step ahead fashion) and then average across the bus routes to obtain a single metric. This way we could also identify underperforming routes  and models that are underperforming in specific areas.  

# Question 3:
** Assumption: Linear Regression was the best-performing model. Ie: AR(2) model with exogenous variables. These variables are a one-hot encoded time of day and area of the city.  
** Assumption: Selected the 2nd best performing bus route and 2nd worst performing bus route based on average deviation across the period.  

After a model with the best performance has been identified, we would need to productionalize the code. To the point, most of the analysis has been done in a notebook. I recommend using Kedro for this portion of the project. It is an open-source framework for producing production-ready code.  After the notebook code has been refactored using the Kedro framework, unit testing should be done to ensure the system is behaving appropriately.
If the model is going to be deployed we would need to identify an adequate MLops strategy for monitoring and maintaining these roughly 85 models. Models will go stale and will need to be retrained. There are software packages out there for this, but it depends on how these individual models will be deployed (edge, cloud, on-prem).   Once it was decided on we would need to build systems to monitor for things like data drift, concept drift, and prediction drift. As well as monitor the performance and quality of incoming data.
