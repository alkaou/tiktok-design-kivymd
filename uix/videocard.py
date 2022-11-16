from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivy.properties import DictProperty


Builder.load_string(
"""
<VideoCard>:
	md_bg_color: [0, 0, 0, 1]
	size_hint_y: None
	video_state: 'stop'
	MDFloatLayout:
		Video:
			source: root.data['source']
			state: root.video_state
			pos_hint: {'center_x': .5, 'top': 1}
		MDBoxLayout:
			orientation: 'vertical'
			pos_hint: {'x': 0, 'y': 0}
			size_hint_x: None
			width: root.width * 0.8 # ça  veut dire 80% du screen
			spacing: '5dp'
			padding: '5dp'
			MDLabel:
				text: root.data['name']
				height: self.texture_size[1]
				font_size: '14sp'
				size_hint_y: None
			MDLabel:
				text: root.data['caption']
				height: self.texture_size[1]
				font_size: '14sp'
				size_hint_y: None
			MDBoxLayout:
				size_hint_y: None
				height: self.minimum_height
				MDIcon:
					icon: 'music-note'
					size: self.texture_size
					size_hint: None, 1
					font_size: '14sp'
				MDLabel:
					text: root.data['song_name']
					height: self.texture_size[1]
					font_size: '14sp'
					size_hint_y: None

		MDBoxLayout:
			orientation: 'vertical'
			pos_hint: {'right': 1, 'y': 0}
			size_hint_x: None
			width: root.width * 0.2 # ça  veut dire 20% du screen
			spacing: '20dp'
			padding: '5dp'
			ProfileImg:
				img: root.data['profil_pic']
			NavIcon:
				icon: 'heart'
				text: root.data['likes']
				icon_size: '35sp'
			NavIcon:
				icon: 'comment'
				text: root.data['comments']
				icon_size: '30sp'
			NavIcon:
				icon: 'share'
				text: root.data['shares']
				icon_size: '25sp'
			AlbumImg:
				img: root.data['album_pic']
"""
)



class VideoCard(MDBoxLayout):
	data = DictProperty(defaultvalue={
		"name": "",
		"source": "",
		"caption": "",
		"song_name": "",
		"profil_pic": "",
		"likes": "",
		"comments": "",
		"shares": "",
		"album_pic": "",
	})