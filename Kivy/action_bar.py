from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint:{'top': 1}
    ActionView:
        ActionPrevious:
            title: 'Action Bar'
            with_previous: False
        ActionOverflow:
        ActionButton:
            text: 'Btn 1'
        ActionButton:
            text: 'Btn 2'
        ActionButton:
            text: 'Btn3'
        ActionButton:
            text: 'Btn 4'
        ActionButton:
            text: 'Btn 5'



'''))
