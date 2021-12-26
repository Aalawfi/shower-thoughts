import kivy 
from kivy.app import App
# TODO: FLoatLayout or GridLayout ? 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput



class Layout (GridLayout):
    def __init__(self, **kwargs): 
        super(Layout, self).__init__(**kwargs)

class ShowerThoughtsApp(App):
   def build(self):
       return Layout()
if __name__ == '__main__':
     ShowerThoughtsApp().run()