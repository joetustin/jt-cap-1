import pyreadr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
%matplotlib inline
matplotlib.style.use("ggplot")
import time

result = pyreadr.read_r("data/point_by_point.RData")
df= result['point_by_point']

#given a list of strings for the server in a set which they won
#determine the win pt percentage by point for service games in the set
def point_by_sgame_perc(lst_of_str):
    """Input is a giant list of strings with each element representing
    a game in the set.  Sample Input: ["SSRSS","SRRSSS",....]

    Returns a list of point percentages such that each pt pecentage 
    represents the rate the server won that particular pt throughout
    the set.  Sample Return: [.68,.72,.60,....]
    """
    lst_of_pt_perc = []
    l=[len(element) for i,element in enumerate(lst_of_str)]
    l_idx = min(max(l),12) 
# I am only looking at first 12 pts as 80% of all games are decided in 8 or fewer points
    for i in range(l_idx):
        count, total = 0,0
        for j in range(len(lst_of_str)):
            if len(lst_of_str[j])-1 >= i:
                if lst_of_str[j][i]=="S":
                    count += 1
                    total += 1
                else:
                    total += 1
            else:
                pass
        lst_of_pt_perc.append(count/total)
    return lst_of_pt_perc

#given my giant string of pts in a match, split them up into a list of strings representing each game
def get_lst_of_strings_to_decode(x):
    """Input: A giant string representing the all the points in a set
    Sample Input: "SSRSS;SSRRSS;RRRR;...."
    Returm a list of strings representing each game
    Sample Output: ["SSRSS","SSRRSS","RRRR"...]
    """
    pt_hist_lst_games = x.split(";")
    return pt_hist_lst_games

if __name__ == "__main__":
    pass

