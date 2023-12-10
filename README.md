# Competition 42039 - Assessment Invitation - Senior Applied Scientist, Data Science Program
Author: Brett Harvey
Description: This repo contains the repository and the requested write-up for the skill assessment about the above competition. The write up for supplied questions is given below. There will be links supplied to supporting material.

# Question 1 - Identify problem parts of the Winnipeg bus system. Consider location, time, and other factors as relevant. Explain your results clearly and concisely 

- It was found that the trend in performance is getting worse across the three months examined.  
- Specific routes are performing worse then others.
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
