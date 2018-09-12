from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

runTouchApp(Builder.load_string('''
StackLayout:
    #layout left to right, bottom to top
    #choose 'rl-bt' for right to left and 'tb-rl/lr' for top to bottom
    orientation: 'lr-bt'
    padding: 10
    spaceing: 5 #gap between buttons
    Button:
        text: 'S1'
        size_hint: .2,.1
    Button:
        text: 'S2'
        size_hint: .2,.1
    Button:
        text: 'S3'
        size_hint: .2,.1
    Button:
        text: 'S4'
        size_hint: .2, .1

'''))
