from kivy.app import App
from kivy.lang import Builder  # concecta o arquivo .py com o .kv
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from PyPDF2 import PdfFileReader

import os

class TelaInicial(Screen):
    pass


class AbrirArquivo(Screen):
    """def arquivo_selecionado(self, filename):
        try:
            self.ids.my_image.source = filename[0]
        except:"""
    pass


GUI = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        return GUI

MainApp().run()
