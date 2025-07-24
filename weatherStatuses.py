import requests

'''try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Miami, FL, US&APPID=3e741f7aaaec99b9436a3c17bed74a32")
    print(response.json())
except:
    print("Information not accessible.")

response_json = response.json()

temp = response_json["main"]["temp"]
temp_min = response_json["main"]["temp_min"]
temp_max = response_json["main"]["temp_max"]

print(f"Today's high is {temp_max}. The low is {temp_min}.")
'''

#class to pull from any city

class City:
    def __init__ (self, name, lat, lon):
        self.name= name
        self.lat = lat
        self.lon = lon
        self.get_data()
        
    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.name}&lat={self.lat}&lon={self.lon}&APPID=3e741f7aaaec99b9436a3c17bed74a32")
            print(response.json())
        except:
            print("Information not accessible.")

        response_json = response.json()

        self.temp = response_json["main"]["temp"]
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]

    def temp_print(self):
        print(f"Today's high is {self.temp_max}. The low is {self.temp_min}.")
        
my_city = City("Miami", 40.7743, -70.1937)
my_city.temp_print()

vacation_city =  City("Miami", 40.7743, -70.1937)
vacation_city.temp_print()    
