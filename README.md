# Weather-forecasting-App-project
The Project defines a simple weather application using the Kivy framework(Augmented Reality). The application displays weather information for selected Indian states. Here's a breakdown of the code:

Imports:

python
Copy code
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
The code imports the necessary modules, including requests for making HTTP requests and Kivy modules for building the graphical user interface.

WeatherApp Class:

python
Copy code
class WeatherApp(App):
Defines a class WeatherApp that inherits from the App class provided by Kivy. This class represents the main application.

build Method:

python
Copy code
def build(self):
This method is part of the WeatherApp class and is used to build the application's user interface. It creates various widgets and organizes them in a vertical box layout.

Widget Creation:

BoxLayout:

python
Copy code
layout = BoxLayout(orientation='vertical', spacing=10, padding=10,)
Creates a vertical box layout with specified spacing and padding.

Labels:

python
Copy code
layout.add_widget(Label(text="ARic Weather App", font_size=30))
Adds a label displaying the title of the weather app.

Spinner:

python
Copy code
self.state_spinner = Spinner(text="Select State", values=list_statename, size_hint=(1, None), height=40)
Creates a spinner (drop-down menu) with a list of Indian state names.

Button Layout:

python
Copy code
button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=50)
Creates a horizontal box layout for buttons.

Button:

python
Copy code
button_layout.add_widget(Button(text="Get Weather", on_press=self.data_get, size_hint=(None, None), size=(200, 50)))
Adds a button with the label "Get Weather" and associates it with the data_get method when pressed.

Empty Widgets for Spacing:

python
Copy code
button_layout.add_widget(Label())  # Empty widget for spacing
Adds empty widgets for spacing in the button layout.

Adding Widgets to Layout:

python
Copy code
layout.add_widget(self.state_spinner)
layout.add_widget(button_layout)
Adds the spinner and button layout to the main vertical layout.

Labels for Weather Information:

python
Copy code
self.weather_label = Label(text="Tomorrow's Climate", font_size=20)
layout.add_widget(self.weather_label)
Creates labels to display weather information such as climate, weather description, temperature, and pressure.

Return Layout:

python
Copy code
return layout
Returns the main layout to be displayed in the application.

data_get Method:

python
Copy code
def data_get(self, instance):
This method is triggered when the "Get Weather" button is pressed. It fetches weather data from the OpenWeatherMap API based on the selected state and updates the labels with the retrieved information.

python
Copy code
state = self.state_spinner.text
data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={state}&appid=016ef45ff991dacc00e360223085b321").json()
Fetches weather data using the OpenWeatherMap API.

python
Copy code
weather = data["weather"][0]["main"]
description = data["weather"][0]["description"]
temperature = str(int(data["main"]["temp"] - 273.15))
pressure = data["main"]["pressure"]
Extracts relevant weather information from the API response.

python
Copy code
self.weather_label.text = f"Tomorrow's Climate: {weather}"
self.weather_description_label.text = f"Tomorrow's Weather Description: {description}"
self.temperature_label.text = f"Tomorrow's Temperature: {temperature}°C"
self.pressure_label.text = f"Tomorrow's Pressure: {pressure}"
Updates the labels with the retrieved weather information.

Main Block:

python
Copy code
if __name__ == '__main__':
    WeatherApp().run()
Runs the application if the script is executed directly. Creates an instance of the WeatherApp class and starts the application.

This application uses Kivy for the graphical interface and the OpenWeatherMap API to fetch weather data based on the selected Indian state.
