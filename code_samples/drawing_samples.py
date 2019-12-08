"""
this is line 1 of my comment
this is line 2 of my comment
"""
# import the arcade library
import arcade

arcade.open_window(600, 600, "drawing example")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

# draw a rectangle
# order is: left, right, top, bottom
arcade.draw_lrtb_rectangle_filled(200, 520, 45, 25, arcade.color.BITTER_LIME)
arcade.draw_rectangle_filled(200, 520, 45, 25, arcade.color.BITTER_LEMON, 45)

arcade.finish_render()

# keep the window open until someone closes it
arcade.run()


