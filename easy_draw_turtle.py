from turtle import Turtle

class EasyDrawTurtle(Turtle):
    ''' Class that extends the turtle class to have a "draw_stroke" function, that facilitates drawing.'''

    def __init__(self,parent,color,width,hide_turtle=True):
        Turtle.__init__(self)
        self.parent = parent
        self.width(width)
        if hide_turtle: self.hideturtle()
        self.color(color)

    def pick_draw_method(self, path_to_attribute):
        ''' Parse a string to get the right stroke method object and return it. This is necessary to get strokes from json.'''

        # Start from the parent object
        sub_object = self.parent

        # Recursively find the appropriate subattribute by splitting the name by periods
        for attr_name in path_to_attribute.split('.'):
            sub_object = getattr(sub_object,attr_name)

        return sub_object

    def draw_stroke(self, start, stroke_method_str, parameters):
        ''' 
        Use the stroke_method of choice to draw a stroke at the chosen start position with the parameters given.
        A stroke can consist of multiple steps. This is implemented as follows. Each step consists of a dictionary 
        having all the necessary parameters for the stroke method. If a list of these is passed then this method will
        loop through them in turn.
        '''

        # Go to the start position.
        self.penup()
        self.goto(start)

        # Ensure the parameters are in a list for the loop step and prepare to draw stroke
        parameters = [parameters] if not isinstance(parameters,list) else parameters
        self.pendown()

        # Draw each step of the stroke
        for parameter_dict in parameters:
            stroke_method = self.pick_draw_method(stroke_method_str)
            stroke_method(**parameter_dict)

    def draw_strokes(self,strokes):
        ''' Draw a list of strokes. Each stroke consists of dictionary containing the start, stroke method and parameters object.'''
        for stroke in strokes:
            self.draw_stroke(stroke['start'],stroke['stroke_method_str'],stroke['parameters'])