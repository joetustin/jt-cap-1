# Not All Points Are Created Equal!
A point by point statistical analysis from over 70,000 documented ATP tour matches.

## Dataset: point_by_point.RData
Last updated ?, [updated dataset](https://github.com/joetustin/jt-cap-1/blob/master/data/point_by_point.RData)

## Tennis Analysis
Tennis is a game of statistics.  What is your first serve percentage?  What is your winner / error ratio.  Did you know a good winner to error ratio is 1:2?  Why does that work?  Does it make sense?  Using data science,  one can deduce significant events which affect match outcomes.  This area has become big business as evidenced by sports gambling on tennis as well as players purchasing data science materials to aid in opponent game planning.   For more information on this topic, check out The Brain Game by Craig O”Shaughnessy.  He writes for the NY Times as well as provides Data Science reports to players.

### My Question / Questions:
Not all points are created equally.  Some points have more value(Big Points).  In a 6-3, 6-3 match, the match outcome can often be swayed by winning four to six key points.  Can I use statistical analysis to find out the most important point to win in a game to have a positive set outcome.  My suspicion is that the first point as well as the fifth point(30-all) have the biggest influence, but we will see.

Also, what is the most important game in a set to win to have more statistical certainty of winning the set.  In tennis forums, we have always talked about the importance of winning the seventh game(ie - 3-3 or 4-2 game).  Is it true?

### Data Analysis
I downloaded my data set from Stephanie Kovalchik who works for Victoria University as well as Tennis Australia.  She has a repo of varied tennis data called Deuce which is in R format. I have been able to look at the data using Jupyter Notebooks.  In particular, there is a column with point outcomes for players in string format.  My plan is to create a list of lists and replace the letters indicating point outcomes with numbers(0,1).  From these numbers, I will calculate my (win point/ win set) probabilities.  The sample string of point results is shown below.

'SSSS;RRRR;SSRRSS;SSRRSS;RSRSRSRR;SSRSS;RSRRSR;SSRSS;RSRSSS;SSRSRRRSSS'



|Percentile|         Pts won    |
|     ----:|:---                   |
|min       |        0              |
|25%       |        10             |
|50%       |        50             |
|75%       |        30             |
|max       |        10             |


### Minimal Viable product:
1. Download data showing point/game/set/match results in a useable table.
2. Plot the % of the time you win a game vs the number of a particular point which must be won to get the game averaging over approximately 10,000 matches.
3. Plot the differential of the previous graph to show the maximum slope.  This maximal slope should indicate the statistically most important point to win.
4. Plot of % chance of winning a set vs the number of the game in the set which you won.

### References:
1. Stephanie Kovalchik
2. Craig O'Shaughnessy

## Exploratory Data Analysis
### Sub-Heading


![Serve Point Percentage by Game][Serve_Pt]
![Return Point Percentage by Game][Return_Pt]
![Win Game Percentage by Set][Win_Game]


[Serve_Pt]: Serve_Pt%.png
[Return_Pt]: Return_Pt%.png
[Win_Game]: Win_Game%.png