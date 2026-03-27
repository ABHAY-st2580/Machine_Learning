import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

df = pd.read_csv('Kohli.csv')

report = ProfileReport(df)
report.to_file('KOHLI_REPORT.html')