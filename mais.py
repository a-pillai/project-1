try:
    from PIL import Image
except:
    print("Pillow module not installed. Please run this command: 'python3 -m pip install Pillow'.")
    quit()

try:
    import requests
except:
    print("Requests module not installed. Please run this command: 'python3 -m pip install requests'.")
    quit()

try:
    from io import BytesIO
    from datetime import date, timedelta
    import re
except:
    print('ERROR IN DEFAULT MODULES')
    quit()

def writePrint(text):
    print(text)
    print(text, file = f)

def setDates():
  today = date.today()
  today = today.strftime('%Y-%m-%d')

  yesterday = date.today() - timedelta(1)
  yesterday = yesterday.strftime('%Y-%m-%d')

  return(today, yesterday)

def defineURLs():
  curiosity_base_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
  insight_url = 'https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0'

  api_key = 'DEMO_KEY'
  api_url = 'api_key=' + api_key
  date_url = 'earth_date=' + usr_date
  camera_url =  'camera=' + camera

  curiosity_url = curiosity_base_url + '?' + date_url + '&' + camera_url + '&' + api_url

  return(curiosity_url, insight_url)

def accessURLs():
  insight = requests.get(insight_url)
  insight_resp = insight.json()

  curiosity = requests.get(curiosity_url)
  curiosity_resp = curiosity.json()

  insight_keys = []
  for i in list(insight_resp.keys()):
    try:
      cut = re.findall("\d+", i)[0]
      if len(cut) > 0:
        insight_keys.append(cut)
    except:
      pass

  for k in insight_keys:
    if yesterday in insight_resp[k]['First_UTC']:
      insight_resp_yesterday = insight_resp[k]
    elif today in insight_resp[k]['First_UTC']:
      insight_resp_today = insight_resp[k]
    else:
      insight_resp_today = 'No weather data for ' + today + '.'
      insight_resp_yesterday = 'No weather data for ' + yesterday + '.'
  
  return(curiosity_resp, insight_resp_today, insight_resp_yesterday)

def processImage():
    try:
        img_url = curiosity_resp['photos'][0]['img_src']
        img = requests.get(img_url)
        img = Image.open(BytesIO(img.content))

        rover_name = str(curiosity_resp['photos'][0]['rover']['name'])
        camera_name = str(curiosity_resp['photos'][0]['camera']['full_name'])
        img_sol = str(curiosity_resp['photos'][0]['sol'])
  
        caption = 'This image was taken by ' + rover_name + ' using its ' + camera_name + ' on Sol ' + img_sol + '.'

        return(img, caption)
    except:
        img = 0
        caption = 'NO IMAGE FOUND'
        return(img, caption)

def getWeatherData(data, date):
  if type(data) == dict:
    try:
      avg_temp = data['AT']['av']
      writePrint(f'Average reported temperature on {date} was {avg_temp} degrees Fahrenheit.')
    except:
      avg_temp = 'No reported average temperature.'

    try:
      avg_ws = data['HWS']['av']
      writePrint(f'Average reported wind speed on {date} was {avg_ws} meters per second.')
    except:
      avg_ws = 'No reported average wind speed.'

    try:
      avg_pres = data['PRE']['av']
      writePrint(f'Average reported pressure on {date} was {avg_pres} Pascals.')
    except:
      avg_pres = 'No reported average pressure.'
    
  elif type(data) == str:
    writePrint(data)

line_brk = "---------------------------------------------------------------------------------------------"
new_line = "\n"

camera_dict = {'fhaz' : 'Front Hazard Avoidance Camera',
               'rhaz' : 'Rear Hazard Avoidance Camera',
               'mast' : 'Mast Camera',
               'chemcam' : 'Chemistry and Camera Complex',
               'mahli' : 'Mars Hand Lens Imager',
               'mardi' : 'Mars Descent Imager',
               'navcam' : 'Navigation Camera'}

f = open('output/output_text.txt', 'w')

today, yesterday = setDates()
writePrint('WELCOME TO M.A.I.S. --- MARS API INFORMATION SERIVCE')
writePrint("This program is built using NASA's Open APIs.")
writePrint(line_brk)
writePrint(f"Today's Date: {today}")
writePrint(f"Yesterday's Date: {yesterday}")
writePrint(new_line)

writePrint('SEARCH MARS ROVER IMAGES BY DATE AND CAMERA')
writePrint('The following cameras can be selected:')
for cam in camera_dict:
  writePrint(f'Camera code: {cam} --- {camera_dict[cam]}')
writePrint(line_brk)
usr_date = input('Enter date as YYYY-MM-DD: ')
camera = input('Enter camera code: ')
print(f'Enter date as YYYY-MM-DD: {usr_date}', file = f)
print(f'Enter camera code: {camera}', file = f)
writePrint(new_line)

curiosity_url, insight_url = defineURLs()
writePrint('QUERYING APIs')
writePrint(line_brk)
writePrint(f'Accessing {curiosity_url}...')
writePrint(f'Accessing {insight_url}...')
writePrint(new_line)

curiosity_resp, insight_resp_today, insight_resp_yesterday = accessURLs()

img, caption = processImage()

writePrint('WEATHER DATA FROM INSIGHT MARS LANDER')
writePrint(line_brk)
getWeatherData(insight_resp_today, today)
writePrint(new_line)
getWeatherData(insight_resp_yesterday, yesterday)
writePrint(new_line)

# use img.show() for script version
writePrint('IMAGES FROM CURIOSITY MARS ROVER')
writePrint(line_brk)
writePrint(caption)
if img != 0:
    img.show()
    img.save('output/output_image.png')
elif img == 0:
    quit()
