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
        # determine the number of columns of the layout
        self.cols = 1
        # Header widget (maybe use an image instead ??  )
        self.add_widget( Label(text="Shower Thoughts") )
        # Inputs 
        self.add_widget( Label(text="First name") )
        self.add_widget( TextInput(multiline =False,size_hint = (0.2,  None) ) )

        self.add_widget( Label(text="Last name") )
        self.add_widget( TextInput(multiline =False,size_hint = (0.2,  None) ) )

        self.add_widget( Label(text="Phone number ") )
        self.add_widget( TextInput(text="+1",multiline =False,size_hint = (0.2,  None) ) )

class ShowerThoughtsApp(App):
   def build(self):
       return Layout()
if __name__ == '__main__':
     ShowerThoughtsApp().run()