from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string(
"""
<NavBar>:
	md_bg_color: [0, 0, 0, 1]
	orientation: 'vertical'
	height: dp(50)
	size_hint_y: None
	MDBoxLayout:
		padding: '10dp', '5dp'
		spacing: '5dp'

		NavIcon:
			icon: 'home'
			text: 'Home'
			icon_size: '28sp'
			text_size: '12sp'
			screen: 'feed'
		NavIcon:
			icon: 'magnify'
			text: 'Discover'
			icon_size: '28sp'
			text_size: '12sp'
			screen: 'discover'
		Image:
			source: 'assets/images/plus.png'
			size_hint_x: None
			width: '35dp'
			# radius: [36, 36, 36, 36]
			# screen: 'home'
		NavIcon:
			icon: 'inbox'
			text: 'Inbox'
			icon_size: '28sp'
			text_size: '12sp'
			screen: 'inbox'
		NavIcon:
			icon: 'face-man-profile'
			text: 'Me'
			icon_size: '28sp'
			text_size: '12sp'
			screen: 'profile'

	MDBoxLayout:
		size_hint_y: None
		height: '5dp'
		
"""
)

class NavBar(MDBoxLayout):
	pass