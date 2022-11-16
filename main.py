import os
os.environ['KIVY_VIDEO'] = 'ffpyplayer'
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition, ScreenManager
from kivymd.font_definitions import theme_font_styles
from screens.screens import *
from uix.uix import *
from kivy.core.text import LabelBase


Window.size = (310, 600)

class windowManager(ScreenManager):
	pass

class Tiktok(MDApp):
	def build(self):
		self.wm = windowManager(transition=FadeTransition()) #transition entre les screen
		self.theme_cls.theme_style="Dark"

		# Avant de créer l'écran, on charge le fonts
		LabelBase.register(name="TiktokIcons", fn_regular="fonts/2.ttf")
		theme_font_styles.append("TiktokIcons")
		self.theme_cls.font_styles["TiktokIcons"] = ["TiktokIcons", 16, False, 0.15]

		screens = [
			Home(name='home')
		]
		for screen in screens:
			self.wm.add_widget(screen)

		return self.wm



if __name__ == '__main__':
	Tiktok().run()