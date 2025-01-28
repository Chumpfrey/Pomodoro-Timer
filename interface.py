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
        scroll_view = ScrollView(size_hint = (1, 1))
        
        timers_layout = BoxLayout(orientation = "vertical", size_hint_y = None, 
                                  spacing = 50)
        timers_layout.bind(minimum_height = timers_layout.setter("height"))
        
        wrk = WorkTimer(size_hint = (1, None), height = 400)
        
        brk = BreakTimer(size_hint = (1, None), height = 400)

        timers_layout.add_widget(wrk)
        timers_layout.add_widget(brk)
        
        scroll_view.add_widget(timers_layout)
        
        self.add_widget(scroll_view)
        
class Timer(App):
    def build(self):
        return AppLayout()
    
# Launch the app
if __name__ == "__main__":
    Timer().run()