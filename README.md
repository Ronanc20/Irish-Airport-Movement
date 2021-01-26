# Irish-Airport-Movement

> A data visualisation dashboard of passenger movement through irish airports

> check it out here: https://ronanc20.pythonanywhere.com

## Intro

The aim for this project was to build a dashboard illustrating passenger movement through Irish airports.
This is done using Dash by plotly. Dash is a Open Source Python library for creating reactive, Web-based applications. 
The data is illustrated using 2 plots, a scatter mapbox and a bar plot. The user has control over various filters 
they want to apply to obtain specific results.

## Filter Features

The following filter features are included to control the dashboard:
 - Irish airport(Donegal, Dublin, Kerry, Knock, Cork, Shannon)
 - flexible time range from 2006 to 2020
 - choice of passenger direction(Inward or Outward)
 - bar chart scale (Linear or Log)
 - map style (Street, Dark or Satellite)
 - Country

![alt text](https://github.com/Ronanc20/Irish-Airport-Movement/blob/main/settings.PNG?raw=true)


## Dataset

The dataset used in the main app.py file is formed by merging 2 separate datasets:

(1) Passenger Movement - available at https://statbank.cso.ie/px/pxeirestat/Statire/SelectVarVal/Define.asp?maintable=ctm01
- they have recently updated their database management system. At the time the API was not working so I just downloaded the 
pc axis file and used a package called pyaxis to read in into a jupyter notebook. Too large to upload to Git.

(2) GlobalAirportDatabase - available at https://www.partow.net/miscellaneous/airportdatabase
-  a database of 9300 airports big and small from all around the world.


The 2 datasets were merged based off the common IATA(International Air Transport Association).
The Data_Prep.ipynb file takes care of this merging process and exports Airport_Traffic_Data.csv used for the dashboard.
Please take a look at that notebook for a detailed explanation: https://github.com/Ronanc20/Irish-Airport-Movement/blob/main/Data_Prep.ipynb

## Layout 

I used a base css layout for the front end of this project available at: https://codepen.io/chriddyp/pen/bWLwgP. 
Adding my own functions to the base file I was able to create the containers for each component in the layout. Using css 
grid I said i'd have a go at making it responsive which seems to work quite well(just dont open it from a phone). The css for the 
dashboard can be found in the assets folder.
