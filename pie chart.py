# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 06:50:33 2023

@author: ACER
"""

import pandas as pd
import matplotlib.pyplot as plt

def pieplot():
    population.groupby(['Continent']).sum().plot.pie(
        y='Pop2022', autopct='%1.0f%%', figsize=(10, 10))
    
    # Adding titles and labels
    plt.title("World Continent Populations in 2022")
    plt.legend(loc="upper right")
    # save as png
    plt.savefig("piechart.png")

# read file into dataframe and print
population = pd.read_csv("World Populations 2022.csv")

# calling pieplot
pieplot()
