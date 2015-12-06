#codind: utf-8

import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.core.audio import *
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.listview import ListItemButton, ListView
from kivy.adapters.listadapter import ListAdapter

class LoadDialog(BoxLayout):

    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Root(BoxLayout):

    list_of_songs = []

#_____Функция, открывающая окно с диалогом выбора файлов

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))

        self._popup.open()

#_____Функция, закрывающая всплывающее окно

    def dismiss_popup(self):
        self._popup.dismiss()

#_____Функция вывода предупреждений

    def warnings(self, warning_text):
        content = Label(text = '%s'%(warning_text))
        _popup = Popup(title = 'Test', content=content, auto_dismiss=True, size_hint=(None, None), size=(300, 200))
        _popup.open()

#____Функция выбора файлов и добавления их в плейлист

    def load(self, path, filename):

        try:

            if str(filename[0]).endswith('mp3'):                   # добавление в плейлист только мр3 файлов
                self.list_of_songs.append(os.path.join(path, filename[0]))                  
            else:
                self.warnings('This is not .mp3 file')
        
            # ___ создание плейлиста в виде ListItemButton
            item_strings = ["{0}".format(index) for index in self.list_of_songs]
    
            list_adapter = ListAdapter( 
                                        data=self.list_of_songs,
                                        selection_mode='single',
                                        allow_empty_selection=False,
                                        cls=ListItemButton
                                        )
    
            list_view = ListView(adapter=list_adapter)
    
            list_adapter.bind(on_selection_change=self.sound_load)
    
            global list_view
            print(self.list_of_songs[0])

        except  IndexError:
            
            self.warnings('Choose a song')

#_____Функция, выводящая на экран плейлист

    def show_playlist(self):
        try:
            content = list_view
            _popup = Popup(title = 'Test', content=content, auto_dismiss=True, size_hint=(None, None), size=(400, 400))
            _popup.open()
            global list_view
            
        except NameError:     #предотвращение вылета из-за того, что плейлист пустой

            self.warnings('There is no song in playlist')


#_____Фуннкция выбора песни в плейлисте

    def sound_load(self, list_adapter):
        
        global song
        song = SoundLoader.load(list_adapter.selection[0].text)
        return song

#_____Функция play/stop для выбранной песни

    def play_song(self):
        try:
            if song.state == 'stop':
                song.play()
            else:
                song.stop()

        except NameError:              #предотвращение вылета, если не выбрана ни одна песня в плейлисте.
        
            self.warnings('Choose song in playlist')

#_____Функция перемотки на начало песни

    def rewinds(self):
        try: song.seek(0.0)
        except NameError: pass

#_____Функция play/pause

    def play_pause(self):
        try:

            if song.state == "play":
    
                song.current_length = song.length     
                song.current_pos = song.get_pos()
                song.stop()
    
            else: 
    
                song.play()
                if song.current_length > 1.0:
                    while song.length < song.current_length:
                        pass
                song.seek(song.current_pos)

        except NameError:
            pass


class Editor(App):
    pass

if __name__ == '__main__':
    Editor().run()