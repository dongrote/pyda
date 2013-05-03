from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.listview import ListView
from kivy.uix.scrollview import ScrollView
from kivy.uix.splitter import Splitter

class MainViewApp(App):
    def build(self):
        splitter = Splitter()
        button = Button(text='button')
        functionlistscrollview = ScrollView()
        functionlistview = ListView(item_strings=[
            'line %d' % index for index in xrange(1000)])
        functionlistscrollview.add_widget(functionlistview)
        splitter.add_widget(functionlistscrollview)
        splitter.add_widget(button)
        return splitter

if '__main__' == __name__:
    MainViewApp().run()
