import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20
        
        self.label = Label(
            text='VideoBot Studio\nby บ่าวภีม',
            font_size='24sp',
            halign='center',
            valign='middle'
        )
        self.add_widget(self.label)
        
        self.btn_start = Button(
            text='เริ่มทำงาน VideoBot',
            size_hint=(1, 0.2),
            font_size='18sp'
        )
        self.btn_start.bind(on_release=self.on_click_start)
        self.add_widget(self.btn_start)

    def on_click_start(self, instance):
        self.label.text = "VideoBot เริ่มทำงานแล้ว..."

class VideoBotApp(App):
    def build(self):
        return MainUI()

if __name__ == '__main__':
    VideoBotApp().run()
