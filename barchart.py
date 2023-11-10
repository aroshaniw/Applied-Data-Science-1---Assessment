# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 07:40:58 2023

@author: ACER
"""


import pandas as pd
import matplotlib.pyplot as plt


def barchart():
    # Data
    city = df1['City']
    values1 = df1['Pop2022']
    values2 = df1['Pop2023']

    # Creating the stacked bar plot
    plt.bar(city, values1, label='Pop2022')
    plt.bar(city, values2, bottom=values1, label='Pop2023')

    # Adding titles and labels
    plt.title('City wise population of Oceania 2022 and 2023')
    plt.xlabel('City')
    plt.ylabel('Population(Mn)')
    
    plt.legend()
    plt.legend(loc="upper right")
    # save as png
    plt.savefig("barchart.png")

    # Display the chart
    plt.show()

# read file into dataframe and print
population = pd.read_csv("World Populations 2022.csv")

df1 = population[population['Continent'] == 'Oceania']

# calling barchart
barchart()
