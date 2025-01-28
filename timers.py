from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scatterlayout import ScatterLayout

class WorkTimer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # Labels for each time in the ones and tens place
        # Should default to 25 minutes
        hours_tens = Label(text = "0", 
                           font_size = "200dp", 
                           size_hint = (None, None),
                           size = (100, 200))
        hours_ones = Label(text = "0", 
                           font_size = "200dp", 
                           size_hint = (None, None),
                           size = (100, 200))
        
        minutes_tens = Label(text = "2", 
                             font_size = "200dp", 
                             size_hint = (None, None),
                             size = (100, 200))
        minutes_ones = Label(text = "5", 
                             font_size = "200dp", 
                             size_hint = (None, None),
                             size = (100, 200))
        
        seconds_tens = Label(text = "0", 
                             font_size = "200dp", 
                             size_hint = (None, None),
                             size = (100, 200))
        seconds_ones = Label(text = "0", 
                             font_size = "200dp", 
                             size_hint = (None, None),
                             size = (100, 200))
        
        # Increment time 
        upper_arrows = BoxLayout(orientation = "horizontal", 
                                 size_hint_y = None, 
                                 height = 50)
        # Hour
        upper_arrows.add_widget(Button(text = "^", 
                                       font_size = "50dp", 
                                       size_hint_y = None, 
                                       on_press = lambda x: self.increment_time_label(hours_tens, hours_ones, "ones")))
        # Minutes
        upper_arrows.add_widget(Button(text = "^", 
                                       font_size = "50dp", 
                                       size_hint_y = None, 
                                       on_press = lambda x: self.increment_time_label(minutes_tens, minutes_ones, "tens")))
        upper_arrows.add_widget(Button(text = "^", 
                                       font_size = "50dp", 
                                       size_hint_y = None, 
                                       on_press = lambda x: self.increment_time_label(minutes_tens, minutes_ones, "ones")))
        # Seconds
        upper_arrows.add_widget(Button(text = "^", 
                                       font_size = "50dp", 
                                       size_hint_y = None, 
                                       on_press = lambda x: self.increment_time_label(seconds_tens, seconds_ones, "tens")))
        upper_arrows.add_widget(Button(text = "^", 
                                       font_size = "50dp", 
                                       size_hint_y = None, 
                                       on_press = lambda x: self.increment_time_label(seconds_tens, seconds_ones, "ones")))
        
        # Set time labels
        time_labels = BoxLayout(orientation = "horizontal", 
                                size_hint_y = None, 
                                height = 200,
                                pos_hint = {"x": 0.04},
                                spacing = 59)
        # Hour
        time_labels.add_widget(hours_ones)
        # Minutes
        time_labels.add_widget(minutes_tens)
        time_labels.add_widget(minutes_ones)
        # Seconds
        time_labels.add_widget(seconds_tens)
        time_labels.add_widget(seconds_ones)
        
        # Embed down arrows layout into a scatter layout to flip the arrows with the same characters used in up arrows
        # Could not find an identical symbol to the caret symbol that is flipped upside-down
        # Decrement time
        lower_arrows = ScatterLayout(rotation = 180, size_hint_y = None)
        flip = BoxLayout(orientation = "horizontal", 
                         size_hint_y = None,
                         height = 50)
        
        # Reverse order of buttons cause of rotation
        # Seconds
        flip.add_widget(Button(text = "^", 
                               font_size = "50dp", 
                               size_hint_y = None, 
                               on_press = lambda x: self.decrement_time_label(seconds_tens, seconds_ones, "ones")))
        flip.add_widget(Button(text = "^", 
                               font_size = "50dp", 
                               size_hint_y = None, 
                               on_press = lambda x: self.decrement_time_label(seconds_tens, seconds_ones, "tens")))
        # Minutes
        flip.add_widget(Button(text = "^", 
                               font_size = "50dp", 
                               size_hint_y = None, 
                               on_press = lambda x: self.decrement_time_label(minutes_tens, minutes_ones, "ones")))
        flip.add_widget(Button(text = "^", 
                               font_size = "50dp", 
                               size_hint_y = None, 
                               on_press = lambda x: self.decrement_time_label(minutes_tens, minutes_ones, "tens")))
        # Hour
        flip.add_widget(Button(text = "^", 
                               font_size = "50dp", 
                               size_hint_y = None, 
                               on_press = lambda x: self.decrement_time_label(hours_tens, hours_ones, "ones")))
        
        lower_arrows.add_widget(flip)
        
        self.add_widget(upper_arrows)
        self.add_widget(time_labels)
        self.add_widget(lower_arrows)
        
    def increment_time_label(self, label_tens, label_ones, place_str):
        str_as_int_tens = int(label_tens.text)
        str_as_int_ones = int(label_ones.text)
        
        if place_str == "tens":
            if str_as_int_tens == 5 and str_as_int_ones != 0:
                label_tens.text = str(str_as_int_tens + 1)
                label_ones.text = str(0)
            elif str_as_int_tens >= 6:
                label_tens.text = str(0)
            else:
                label_tens.text = str(str_as_int_tens + 1)
        elif place_str == "ones":
            if str_as_int_ones == 9 and str_as_int_tens != 5:
                label_tens.text = str(str_as_int_tens + 1)
                label_ones.text = str(0)
            elif str_as_int_ones == 9 and str_as_int_tens >= 5:
                label_tens.text = str(6)
                label_ones.text = str(0)
            elif str_as_int_tens == 6:
                pass
            else:
                label_ones.text = str(str_as_int_ones + 1)
        else:
            raise Exception("Digit place not specified.")
        

    def decrement_time_label(self, label_tens, label_ones, place_str):
        str_as_int_tens = int(label_tens.text)
        str_as_int_ones = int(label_ones.text)
        
        if place_str == "tens":
            if str_as_int_tens == 0:
                if str_as_int_ones > 0:
                    label_ones.text = str(0)
                else:
                    label_tens.text = str(6)
                    label_ones.text = str(0)
            else:
                label_tens.text = str(str_as_int_tens - 1)
        elif place_str == "ones":
            if str_as_int_ones == 0 and str_as_int_tens != 0:
                label_tens.text = str(str_as_int_tens - 1)
                label_ones.text = str(9)
            elif str_as_int_ones == 0 and str_as_int_tens == 0:
                label_tens.text = str(6)
                label_ones.text = str(0)
            else:
                label_ones.text = str(str_as_int_ones - 1)
        else:
            raise Exception("Digit place not specified.")

# Nearly identical to the work timer
# Only difference is there is no hour setter
# Break should not last longer than an hour
class BreakTimer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
        self.spacing = 20
        
        # Labels for each time in the ones and tens place
        # Should default to 5 minutes
        
        minutes_tens = Label(text = "0", 
                             font_size = "200dp", 
                             size_hint = (None, None),
                             size = (100, 200))
        minutes_ones = Label(text = "5", 
                             font_size = "200dp", 
                             size_hint = (None, None),
                             size = (100, 200))
        
        seconds_tens = Label(text = "0", 
                             font_size = "200dp", 
                             size_hint = (None, None),
                             size = (100, 200))
        seconds_ones = Label(text = "0", 
                             font_size = "200dp", 
                             size_hint = (None, None),
                             size = (100, 200))
        
        # Increment time 
        upper_arrows = BoxLayout(orientation = "horizontal", 
                                 size_hint_y = None, 
                                 height = 50)
        # Minutes
        upper_arrows.add_widget(Button(text = "^", 
                                       font_size = "50dp", 
                                       size_hint_y = None, 
                                       on_press = lambda x: self.increment_time_label(minutes_tens, minutes_ones, "tens")))
        upper_arrows.add_widget(Button(text = "^", 
                                       font_size = "50dp", 
                                       size_hint_y = None, 
                                       on_press = lambda x: self.increment_time_label(minutes_tens, minutes_ones, "ones")))
        # Seconds
        upper_arrows.add_widget(Button(text = "^", 
                                       font_size = "50dp", 
                                       size_hint_y = None, 
                                       on_press = lambda x: self.increment_time_label(seconds_tens, seconds_ones, "tens")))
        upper_arrows.add_widget(Button(text = "^", 
                                       font_size = "50dp", 
                                       size_hint_y = None, 
                                       on_press = lambda x: self.increment_time_label(seconds_tens, seconds_ones, "ones")))
        
        # Set time labels
        time_labels = BoxLayout(orientation = "horizontal", 
                                size_hint_y = None, 
                                height = 200,
                                pos_hint = {"x": 0.063},
                                spacing = 100)
        # Minutes
        time_labels.add_widget(minutes_tens)
        time_labels.add_widget(minutes_ones)
        # Seconds
        time_labels.add_widget(seconds_tens)
        time_labels.add_widget(seconds_ones)
        
        # Embed down arrows layout into a scatter layout to flip the arrows with the same characters used in up arrows
        # Could not find an identical symbol to the caret symbol that is flipped upside-down
        # Decrement time
        lower_arrows = ScatterLayout(rotation = 180, size_hint_y = None)
        flip = BoxLayout(orientation = "horizontal", 
                         size_hint_y = None,
                         height = 50)
        
        # Reverse order of buttons cause of rotation
        # Seconds
        flip.add_widget(Button(text = "^", 
                               font_size = "50dp", 
                               size_hint_y = None, 
                               on_press = lambda x: self.decrement_time_label(seconds_tens, seconds_ones, "ones")))
        flip.add_widget(Button(text = "^", 
                               font_size = "50dp", 
                               size_hint_y = None, 
                               on_press = lambda x: self.decrement_time_label(seconds_tens, seconds_ones, "tens")))
        # Minutes
        flip.add_widget(Button(text = "^", 
                               font_size = "50dp", 
                               size_hint_y = None, 
                               on_press = lambda x: self.decrement_time_label(minutes_tens, minutes_ones, "ones")))
        flip.add_widget(Button(text = "^", 
                               font_size = "50dp", 
                               size_hint_y = None, 
                               on_press = lambda x: self.decrement_time_label(minutes_tens, minutes_ones, "tens")))
        
        lower_arrows.add_widget(flip)
        
        self.add_widget(upper_arrows)
        self.add_widget(time_labels)
        self.add_widget(lower_arrows)
        
    def increment_time_label(self, label_tens, label_ones, place_str):
        str_as_int_tens = int(label_tens.text)
        str_as_int_ones = int(label_ones.text)
        
        if place_str == "tens":
            if str_as_int_tens == 5 and str_as_int_ones != 0:
                label_tens.text = str(str_as_int_tens + 1)
                label_ones.text = str(0)
            elif str_as_int_tens >= 6:
                label_tens.text = str(0)
            else:
                label_tens.text = str(str_as_int_tens + 1)
        elif place_str == "ones":
            if str_as_int_ones == 9 and str_as_int_tens != 5:
                label_tens.text = str(str_as_int_tens + 1)
                label_ones.text = str(0)
            elif str_as_int_ones == 9 and str_as_int_tens >= 5:
                label_tens.text = str(6)
                label_ones.text = str(0)
            elif str_as_int_tens == 6:
                pass
            else:
                label_ones.text = str(str_as_int_ones + 1)
        else:
            raise Exception("Digit place not specified.")
        

    def decrement_time_label(self, label_tens, label_ones, place_str):
        str_as_int_tens = int(label_tens.text)
        str_as_int_ones = int(label_ones.text)
        
        if place_str == "tens":
            if str_as_int_tens == 0:
                if str_as_int_ones > 0:
                    label_ones.text = str(0)
                else:
                    label_tens.text = str(6)
                    label_ones.text = str(0)
            else:
                label_tens.text = str(str_as_int_tens - 1)
        elif place_str == "ones":
            if str_as_int_ones == 0 and str_as_int_tens != 0:
                label_tens.text = str(str_as_int_tens - 1)
                label_ones.text = str(9)
            elif str_as_int_ones == 0 and str_as_int_tens == 0:
                label_tens.text = str(6)
                label_ones.text = str(0)
            else:
                label_ones.text = str(str_as_int_ones - 1)
        else:
            raise Exception("Digit place not specified.")