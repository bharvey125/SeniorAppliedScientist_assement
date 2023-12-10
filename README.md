# Competition 42039 - Assessment Invitation - Senior Applied Scientist, Data Science Program
Author: Brett Harvey
Description: This repo contains the repository and the requested write-up for the skill assessment about the above competition. The write up for supplied questions is given below. There will be links supplied to supporting material.

# Question 1 - Identify problem parts of the Winnipeg bus system. Consider location, time, and other factors as relevant. Explain your results clearly and concisely 
Detailed analysis can be found in the notebooks![here](https://github.com/bharvey125/SeniorAppliedScientist_assement/tree/main/busarrival-pred/notebooks)

## <u>Findings:</u>
- It was found that the trend in performance is getting worse across the three months examined.  
- Specific routes are performing worse than others.
- Specific Neighborhoods perform drastically worse than others.
- 17:00 is the worst performing time during the week and 15:00/16:00 is the worst performing during the weekend.
- Mid-week performance worse then weekends.
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
- The 10 worst neighbourhoods based on mean deviation are:
- Island Lakes, Victoria Cresent, Ridgewood South, North St. Boniface, East Elmwood, Grassie,   Archwood, Talbot-Grey, Weston, Vista, Normad Park.

# Question 2
