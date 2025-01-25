import time

from kivy.app import App

from kivy.uix.behaviors.focus import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button    
from kivy.uix.floatlayout import FloatLayout  
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from timers import WorkTimer, BreakTimer

class AppLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        timers_layout = BoxLayout(orientation = "vertical", size_hint_y = None)
        
        wrk = WorkTimer(size_hint_y = None)
        
        brk = BreakTimer()

        timers_layout.add_widget(wrk)
        #timers_layout.add_widget(brk)
        
        self.add_widget(timers_layout)
        
class Timer(App):
    def build(self):
        return AppLayout()
    
# Launch the app
if __name__ == "__main__":
    Timer().run()