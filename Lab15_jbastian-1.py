"""
Program: Mapping Global Datasets from the Book
Author: Jonathan Bastian
The program maps positions to global positions taken from a data file, along with brightness for magnitude. Lists are created from the fields in each row.
Date: Sunday, August 10, 2025
"""

from pathlib import Path
import csv                                                      # standard; or json if json file

import pandas as pd
import plotly.express as px


# Read data as a string and convert to a Python object.
path = Path('eq_data/world_fires_1_day.csv')                    # (copying textbook) eq_data - any path look for it at, copy relative path, ex. eq_data/eq_data_1_day_m1.json
lines = path.read_text(encoding="utf-8").splitlines()           # ?splitlines?, jsons contents
reader = csv.reader(lines)                                      # all_eq_data = json.loads(contents)
header_row = next(reader)                                       # all_eq_dicts = all_eq_data["features"] # grab out of features
print(header_row)                                               # look at ex. all_eq_dicts

# latitude, longitude, brightness, scan, track, acq_date, acq_time, satellite, confidence, version, bright_t31, frp, daynight
brights, hover_texts, lons, lats, dates = [], [], [], [], []    # extract list of mags/magnitures, longitudes, latitudes out of list all data, and give coordinates
for row in reader:                                              # json eq_dict in all_eq_dicts
    hover_text = float(row[10])                                 # hover_text for date
    bright = float(row[2])                                      # json eq_dict['properties']['mag'], brights for magnitude
    lon = float(row[1])                                         # json eq_dict['geometry']['coordinates'][0]
    lat = float(row[0])                                         # json eq_dict['geometry']['coordinates'][1]
    date = str(row[5])
    hover_texts.append(hover_text)
    brights.append(bright)                                      # go through dictionaries, json mags
    lons.append(lon)
    lats.append(lat)
    dates.append(date)

def populate_and_show_plot_values():
    title = "Global Fires"                                      # Earthquakes, (°, °) 2018-09-22
    fig = px.scatter_geo(
        title=title,
        hover_name=hover_texts, lat=lats, lon=lons,
        color=brights, color_continuous_scale='Bluered_r', labels={'color':'Brightness'},
        )                                                       # pass in scatter geo so could put into earth automaically, size=mags

    fig.update_traces(
        marker=dict(size=15),
    )

    """
    fig.update_traces(
        hovertemplate="({lats}°"{lons}°)\n"
    )
    """

    fig.show()

populate_and_show_plot_values()

# ?try-except-else block avoid any invalid data?
# csv section book create lists, second section set up .html file to view the data with the global map
# use either simple method to set up form Scattergeo data = [Scattergeo(lon=lons, lat=lats)] or set up more complex model with colormap, using hover texts and a clormap


# looks similar but is different Lab 14
# (super simple spreadsheet comma separated values rows columns CSV data (tutorial video & textbook)
# trickier specified fields object with variables in it object, field names can have data, oriented notation like dictionary but each different, doesn't have large arrays more than a few objects each, doesn't go any deeper JSON/marketing Java Script Notation)
# about getting the data from the internet to use, two options 1 described 2 book suggestion (Try it Yourself 16.9) extra help advice
# downloading file a lot of data and passing to plotting, also plotly visualizations digital devices resizes (vs matplotlib charts/charting simple less flexible)
# also install plotly express
# $ python3 -m pip install --user plotly        difference using not very pronounced
# $ python3 -m pip install --user pandas
# pip freeze > requirements.txt
# can pull dataset to pull from blackboard - any kind of file, textbook; csv (comma separated value) files - might be easier to work with, json, right click save link

# short answers: difference CSV and JSON
# ME textbook:
# JSON (JavaScript Object Notation) module, allows to save user data so it isn't lost when your program stops running,
#   allows you to convert simple Python data structures into JSON-formatted strings, then load data from file next time program runs
#   can use json to share data between different PYthon programs
#   not specific to Python so can share data store in the JSON format people who work many other programming languages
#   useful portable format easy to learn
# CSV (Comma Separated Values) module, (simple way to store data in a text file), series of values separated by commas called comma-separated values
#   can be tedious to read but programs can process and extract information from them quickly and accurately

# ME: JSON, or JavaScript Object Notation and CSV, or Comma Separated Values, are both formats for storing data in text files; JSON despite having JavaScript in it's name is used by other languages. CSV is the simpler of the two, involving numbers and text stored in a table where a series of values are separated by commas, similar to a spreadsheet with rows and columns. While CSV is harder for humans to read, programs can quickly find and process the information, given that they are stored in plain text files which are more compact and can be opened in text editors. CSV files are also more secure than JSON files. JSON is more complicated, utilizing fields for storing objects as name-value pairs and small arrays, similar to a dictionary. JSON is also more readable than CSV, due to it's more organized formatting, involving nesting and hierarchies, this formatting also allows for scaling. JSON can be used to share data between different programs in many different languages including Python, making it widely portable, which is why it tends to be used for APIs and data configuration.