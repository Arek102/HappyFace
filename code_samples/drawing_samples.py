"""
this is line 1 of my comment
this is line 2 of my comment
"""
# import the arcade library
import arcade

arcade.open_window(600, 600, "drawing example")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 5, right of 35
# Top of 590, bottom of 570
arcade.draw_lrtb_rectangle_filled(5, 35, 590, 570, arcade.color.BITTER_LIME)

# Different way to draw a rectangle
# Center rectangle at (100, 520) with a width of 45 and height of 25
arcade.draw_rectangle_filled(100, 520, 45, 25, arcade.color.BLUSH)

# Rotate a rectangle
# Center rectangle at (200, 520) with a width of 45 and height of 25
# Also, rotate it 45 degrees.
arcade.draw_rectangle_filled(200, 520, 45, 25, arcade.color.BLUSH, 45)


# Draw a point at (50, 580) that is 5 pixels large
arcade.draw_point(50, 580, arcade.color.RED, 5)

# Draw a line
# Start point of (75, 590)
# End point of (95, 570)
arcade.draw_line(75, 590, 95, 570, arcade.color.BLACK, 2)

# Draw a circle outline centered at (140, 580) with a radius of 18 and a line
# width of 3.
arcade.draw_circle_outline(140, 580, 18, arcade.color.WISTERIA, 3)

# Draw a circle centered at (190, 580) with a radius of 18
arcade.draw_circle_filled(190, 580, 18, arcade.color.WISTERIA)

# Draw an ellipse. Center it at (240, 580) with a width of 30 and
# height of 15.
arcade.draw_ellipse_filled(240, 580, 30, 15, arcade.color.AMBER)

# Draw text starting at (10, 450) with a size of 20 points.
arcade.draw_text("Simpson College", 10, 450, arcade.color.BRICK_RED, 20)
arcade.finish_render()

# keep the window open until someone closes it
arcade.run()


