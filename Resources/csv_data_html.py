from prettytable import PrettyTable
from IPython.display import HTML
from pandas import *
import pandas as pd
import numpy as np

df = pd.read_csv("cities.csv")

df.to_html('Data.html')