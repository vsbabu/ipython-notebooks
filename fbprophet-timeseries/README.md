# Jupyter Lab Notebook using Facebook Prophet

1. Model and predict a timeseries data
1. Find out anomalies
1. Use Pandas styler to highlight anomalies
1. Transpose timeseries data frame to a weekly values dataframe AND stylize it.

Sample data is a function of time taken to execute a script that I run daily;
and is in the [CSV file](prophet_example_weekly.csv). It is referred to
in the [notebook](prophet_example_weekly.ipynb).

Note that the github preview of the notebook does not show styled tables with
colors. If you run the notebook on your own, you can see it - or here are the
screenshots.

![Anomaly Altair Chart](prophet_example_weekly_ss01.png?raw=true "Altair Chart")
![Anomaly Weekly Dataframe](prophet_example_weekly_ss02.png?raw=true "Weekly Table")

The python code here would work just as well in a headless mode from scripts
with `html.render()` function as well - you can use it to write to a file or
send as email.
