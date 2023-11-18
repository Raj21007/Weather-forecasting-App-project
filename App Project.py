from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import requests

class WeatherApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10,)

        # Widgets
        layout.add_widget(Label(text="ARic Weather App", font_size=30))

        list_statename = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat",
                         "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala",
                         "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
                         "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
                         "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh",
                         "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
                         "National Capital Territory of Delhi", "Puducherry"]

        self.state_spinner = Spinner(text="Select State", values=list_statename, size_hint=(1, None), height=40)
        layout.add_widget(self.state_spinner)

        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=50)
        button_layout.add_widget(Label())  # Empty widget for spacing
        button_layout.add_widget(Button(text="Get Weather", on_press=self.data_get, size_hint=(None, None), size=(200, 50)))
        button_layout.add_widget(Label())  # Empty widget for spacing
        layout.add_widget(button_layout)

        self.weather_label = Label(text="Tomorrow's Climate", font_size=20)
        layout.add_widget(self.weather_label)

        self.weather_description_label = Label(text="Tomorrow's Weather Description", font_size=20)
        layout.add_widget(self.weather_description_label)

        self.temperature_label = Label(text="Tomorrow's Temperature", font_size=20)
        layout.add_widget(self.temperature_label)

        self.pressure_label = Label(text="Tomorrow's Pressure", font_size=20)
        layout.add_widget(self.pressure_label)

        return layout

    def data_get(self, instance):
        state = self.state_spinner.text
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={state}&appid=016ef45ff991dacc00e360223085b321").json()

        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = str(int(data["main"]["temp"] - 273.15))
        pressure = data["main"]["pressure"]

        self.weather_label.text = f"Tomorrow's Climate: {weather}"
        self.weather_description_label.text = f"Tomorrow's Weather Description: {description}"
        self.temperature_label.text = f"Tomorrow's Temperature: {temperature}°C"
        self.pressure_label.text = f"Tomorrow's Pressure: {pressure}"

if __name__ == '__main__':
    WeatherApp().run()
