# Project-1 

#Group Members: Moni Qiande, Elizabeth Webbe, Alex Pillai, Seth Robinson

# About

This project uses scripts in Jupyter to display images available through NASA's public API

# mais.py 

This script retrieves image data from NASA's Curiosity, Oppourtunity, and Spirit rovers on Mars. The script selects images using date and rover camera mount location.

#Ex. 

WELCOME TO M.A.I.S. --- MARS API INFORMATION SERIVCE

This program is built using NASA's Open APIs.

Today's Date: 2020-11-05
Yesterday's Date: 2020-11-04


SEARCH MARS ROVER IMAGES BY DATE AND CAMERA

The following cameras can be selected:

Camera code: fhaz --- Front Hazard Avoidance Camera

Camera code: rhaz --- Rear Hazard Avoidance Camera

Camera code: mast --- Mast Camera

Camera code: chemcam --- Chemistry and Camera Complex

Camera code: mahli --- Mars Hand Lens Imager

Camera code: mardi --- Mars Descent Imager
Camera code: navcam --- Navigation Camera

Enter date as YYYY-MM-DD:  2019-07-07
Enter camera code:  mahli


QUERYING APIs

Accessing https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2019-07-07&camera=mahli&api_key=DEMO_KEY...
Accessing https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0...


WEATHER DATA FROM INSIGHT MARS LANDER

No weather data for 2020-11-05.


Average reported temperature on 2020-11-04 was -66.652 degrees Fahrenheit.

Average reported wind speed on 2020-11-04 was 7.459 meters per second.

Average reported pressure on 2020-11-04 was 741.526 Pascals.


IMAGES FROM CURIOSITY MARS ROVER

This image was taken by Curiosity using its Mars Hand Lens Imager on Sol 2459.



# Earth_Quaries.ipynb 

This scipt uses opencage to ultimatley retrieve landsat imagery based on a supplied location and date. A for loop is used to first identify the intended city and then identify a date, of which the results are then printed. 

#Ex. 

Enter the name of the city

 Tbilisi
 
Enter the name of the state or country where the city is located

 Georgia
 
Enter the date (yyyy-mm-dd) you would like to see

 2017-07-07
 
The link to your picture is https://api.nasa.gov/planetary/earth/imagery?lon=44.8014495&lat=41.6934591&date=2017-07-07&dim=0.15&api_key=DEMO_KEY

            
