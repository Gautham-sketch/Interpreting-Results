from turtle import distance
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import csv

whole = []
with open("Final_Project_Data.csv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        whole.append(row)

headers = whole[0]
data = whole[1: ]
star_name = data[1]
gravity = data[5]
mass = data[3]
radius = data[8]
distance = data[6]

Figure1 = px.scatter(x=star_name, y=mass)
Figure2 = px.scatter(x=star_name, y=radius)
Figure3 = px.scatter(x=star_name, y=gravity)
Figure4 = px.scatter(x=star_name, y=distance)
Figure1.show()
Figure2.show()
Figure3.show()
Figure4.show()