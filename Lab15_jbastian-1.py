"""
Program: Mapping Global Datasets from the Book
Author: Jonathan Bastian
The program maps positions to global positions taken from a data file, along with brightness for magnitude. Lists are created from the fields in each row.
Date: Sunday, August 10, 2025
"""

from pathlib import Path
import json                     # standard

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_1_day_m1.json')             # (copying textbook) eq_data - any path look for it at, copy relative path
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)
all_eq_dicts = all_eq_data["features"] # grab out of features
print(all_eq_dicts) # look at

mags, lons, lats = [], [], [] # extract list of magnitures, longitudes, latitudes out of list all data, and give coordinates
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag) # go through dictionaries
    lons.append(lon)
    lats.append(lat)


def populate_and_show_plot_values():
    title = "Global Earthquakes"
    fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title) # pass in scatter geo so could put into earth automaically
    fig.show()



populate_and_show_plot_values()

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