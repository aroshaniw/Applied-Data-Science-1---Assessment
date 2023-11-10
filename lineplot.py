# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 07:07:19 2023

@author: ACER
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 03:14:51 2023

@author: ACER
"""


import pandas as pd
import matplotlib.pyplot as plt

def lineplot(head, headers):
    for head in headers:
        plt.plot(population["Year"], population[head], label=head)

    # Adding titles and labels
    plt.title('Worlds Top Five Populated Countries')
    plt.xlabel("Year")
    plt.ylabel("Popuation(Mn)")
    plt.legend()
    # save as png
    plt.savefig("lineplot.png")
    # Display the chart
    plt.show()


# read file into dataframe and print
population = pd.read_excel("Worlds Top Five Populated Countries.xlsx")
print(population)

# plot the line charts
plt.figure()

# calling lineplot with a list of the columns to be plotted.
lineplot(population, ["China", "India",
         "United States", "Indonesia", "Pakistan"])
