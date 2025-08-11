"""
Program: Mapping Global Datasets from the Book
Author: Jonathan Bastian
The program maps the positions of world fires to global positions taken from a data file, along with brightness. The map includes text if hovered over and a color gradiant.
Date: Sunday, August 10, 2025
"""

from pathlib import Path
import csv                                                      # standard; or json if json file

import pandas as pd
import plotly.express as px


# Read data as a string and convert to a Python object.
path = Path('eq_data/world_fires_1_day.csv')                    # (copying textbook) eq_data - any path look for it at, copy relative path, ex. eq_data/eq_data_1_day_m1.json
lines = path.read_text(encoding="utf-8").splitlines()           # csv added splitlines, jsons contents
reader = csv.reader(lines)                                      # all_eq_data = json.loads(contents)
header_row = next(reader)                                       # all_eq_dicts = all_eq_data["features"] # grab out of features
print(header_row)                                               # look at ex. all_eq_dicts

# latitude, longitude, brightness, scan, track, acq_date, acq_time, satellite, confidence, version, bright_t31, frp, daynight
brights, hover_texts, lons, lats, dates = [], [], [], [], []    # extract list of mags/magnitures, longitudes, latitudes out of list all data, and give coordinates
for row in reader:                                              # json eq_dict in all_eq_dicts
    bright = float(row[2])                                      # json eq_dict['properties']['mag'], brights for magnitude
    lon = float(row[1])                                         # json eq_dict['geometry']['coordinates'][0]
    lat = float(row[0])                                         # json eq_dict['geometry']['coordinates'][1]
    date = str(row[5])
    hover_text = f"{row[5]}"                                    # hover_text for date, f"({row[0]}°, {row[1]}°)<br>{row[5]}" unnecessary since hovertemplate=None automatic
    hover_texts.append(hover_text)
    brights.append(bright)                                      # go through dictionaries, json mags
    lons.append(lon)
    lats.append(lat)
    dates.append(date)

def populate_and_show_plot_values():
    title = "Global Fires"                                      # Earthquakes
    fig = px.scatter_geo(
        title=title,
        hover_name=hover_texts, lat=lats, lon=lons,
        color=brights, color_continuous_scale='Bluered_r', labels={'color':'Brightness'},
        )                                                       # pass in scatter geo so could put into earth automaically, size=mags

    fig.update_traces(
        marker=dict(size=15),
        hovertemplate=None,
    )

    fig.show()

populate_and_show_plot_values()

# ?try-except-else block avoid any invalid data?
