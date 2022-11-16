from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty


Builder.load_string(
"""
<SnapScroll>:
	scroll_distance: 500 # Help prevent kivy detecting multiple scroll in drag.
	bar_width: 0
	scroll_wheel_distance: 0 # Disable mouse scrolling
"""
)

class SnapScroll(ScrollView):
	#Adapter layout à l'interieur de scrollview
	layout = ObjectProperty()

	def on_scroll_start(self, touch, check_children=True):
		# Sauvegarder la touch pos par click par user.
		touch.ud['pos'] = self.to_local(*touch.pos)
		# Looping through all widget to get the clicked widget
		for widget in self.layout.children:
			if widget != self:
				if widget.collide_point(*touch.ud['pos']):
					# saving the widget that received the touch
					touch.ud['widget'] = widget
					# And this index
					touch.ud['index'] = self.layout.children.index(widget)

		# Make sure to return that
		return super().on_scroll_start(touch, check_children=check_children)

	def on_scroll_stop(self, touch, check_children=True):
		self.touch = None # Cancel touch
		local_touch = self.to_local(*touch.pos)

		# Comparing current touch pos with the one we saved.
		# To know the direction the user is scrolling.
		if local_touch[1] > touch.ud['pos'][1]:

			# If widget is not the first, scroll up
			if touch.ud['index'] != 0:
				self.scroll_to(self.layout.children[touch.ud['index']-1], padding=0)

				self.layout.children[touch.ud['index']].video_state = 'pause' # Pause current video
				self.layout.children[touch.ud['index']-1].video_state = 'play' # Play next video
		
		elif local_touch[1] < touch.ud['pos'][1]:
			# If widget is not the last, scroll down
			if touch.ud['index'] < len(self.layout.children)-1:
				self.scroll_to(self.layout.children[touch.ud['index']+1], padding=0)

				self.layout.children[touch.ud['index']].video_state = 'pause' # Pause current video
				self.layout.children[touch.ud['index']+1].video_state = 'play' # Play prev video

		touch.ud.pop('pos') # We are done with the pos we save so we clear it

		return True # .......................