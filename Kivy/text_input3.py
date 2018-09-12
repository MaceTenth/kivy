from kivy.app import App
from kivy.lang import Builder

kv = """
AnchorLayout:
    TextInput:
        size_hint: None, None
        size: 600, 200
        text: "Shimon Moyal\\nShimon Moyal\\nShimon Moyal\\nShimon Moyal\\n"
        font_size: 50
        focus: True
        on_scroll_y: print(self.focus)
"""

class TextInput(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    TextInput().run()
