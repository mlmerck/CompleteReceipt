from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from PIL import Image
import data as chartss

#Imports piechart saved by data.py


#Imports kv file (formatting) for use
Builder.load_file("layout.kv")
#Creates the main screen
class MainScreen(Screen):
    pass

#Creates the receipt screen
class ReceiptScreen(Screen):
    pass

#Creates the screen manager, to enable switching between receipt and main screens
sm = ScreenManager()
sm.add_widget(MainScreen(name = 'main'))
sm.add_widget(ReceiptScreen(name = 'receipts'))

#Defines the app, and names the window
class MyApp(App):
    def build(self):
        self.title = "Receipt Bag"
        return sm

#Starts the app
if __name__ == '__main__':
    MyApp().run()
