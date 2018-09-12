from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout


Builder.load_string('''
<Demo>:
    cols: 1
    BoxLayout:
        orientation: 'horizontal'
        Button:
            text: 'Demo'
            pos_hint: {'x': 0}
        Button:
            text: 'Demo'
            pos_hint:{'x': 0}

''')
class Demo(GridLayout):
    pass

class DemoApp(App):
    def build(self):
        return Demo()

if __name__ == '__main__':
    DemoApp().run()

"""
button demo with size control
runTouchApp(Builder.load_string('''

StackLayout:
    Button:
        text: 'kivy'
        size_hint: .2,.2


'''))"""
