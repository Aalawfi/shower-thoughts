import kivy 
from kivy.app import App
# TODO: FLoatLayout or GridLayout ? 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class Layout(Widget):
    pass


class ShowerThoughtsApp(App):
   def build(self):
       return FloatLayout()
if __name__ == '__main__':
     ShowerThoughtsApp().run()