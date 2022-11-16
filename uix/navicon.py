from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior


Builder.load_string(
"""
<NavIcon>:

	adaptive_height: True
	icon: ''
	text: ''
	orientation: 'vertical'
	text_size: '14sp'
	icon_size: '34sp'

	screen: ''

	MDIcon:
		icon: root.icon
		font_size: root.icon_size
		pos_hint: {"center_x": .5}
		halign: 'center'
		size_hint_y: None
		padding: '1dp', '1dp'
		# md_bg_color: "black"

	MDLabel:
		text: root.text
		# font_style: 'TiktokIcons'
		height: self.texture_size[1]
		font_size: root.text_size
		bold: True
		halign: 'center'
		size_hint_y: None
"""
)



class NavIcon(ButtonBehavior, MDBoxLayout):
	def on_press(self):
		self.parent.parent.screen_manager.current = self.screen