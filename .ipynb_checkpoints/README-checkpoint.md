# Project-1 

#Group Members: Moni Qiande, Elizabeth Webbe, Alex Pillai, Seth Robinson

# About

This project uses scripts in Jupyter to display images available through NASA's public API

# mais.py 

This script uses PIL and BytesIO to retrieve image data from NASA's Curiosity, Oppourtunity, and Spirit rovers on Mars. The script uses a for loop 


# Earth_Quaries.ipynb 

This scipt uses pip and opencage to ultimatley retrieve landsat imagery based on a supplied location and date. A for loop is used to first identify the intended city and then identify a date, of which the results are then printed. 

#Ex. 

while True:
    print('Enter the name of the city')
    city = input()
    print('Enter the name of the state or country where the city is located')
    state_country = input()
    query= city + ',' + state_country
    results = geocoder.geocode(query)    
    while results:
            while True:
                print('Enter the date (yyyy-mm-dd) you would like to see')
                date=input()
                try:
                    isinstance(datetime.datetime.strptime(date, '%Y-%m-%d'), datetime.datetime)
                    if  datetime.datetime.strptime(date, '%Y-%m-%d') <datetime.datetime(2013,2,11):
                        print("Landsat 8 launched February 11, 2013, please enter a date after Feb 2013."
                    else:
                        break
                        
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            getURL = base_earth + '?lon=' + str(lng) + '&lat=' + str(lat) + '&date='+date+'&dim=0.15&api_key=DEMO_KEY'
            response = requests.get(getURL,stream=True)
            if response:
                print("The link to your picture is " + getURL)
                
                img = Image.open(response.raw)
                plt.imshow(img)
                plt.axis('off')
                plt.show()
                
                urlretrieve(getURL, '.image1.png')
                break
            
