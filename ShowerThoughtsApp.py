import kivy 
from kivy.app import App
# TODO: FLoatLayout or GridLayout ? 
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput




class Layout (GridLayout):
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    phone_number = ObjectProperty(None)
    def __init__(self, **kwargs): 
        super(Layout, self).__init__(**kwargs)

    def generate(self): 
        print("first name: ", self.first_name.text, "last name: ", self.last_name.text,
         "phone number: ",self.phone_number.text)
         #TODO: JSONify the above info 
         #TODO send the JSON to back end

class ShowerThoughtsApp(App):
   def build(self):
       return Layout()
if __name__ == '__main__':
     ShowerThoughtsApp().run()