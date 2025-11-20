
""" Ques:- A wire is the form of Arc at an angle of 60 degrees and the radius of the arc is 42.The wire is converted into a square. 
Find the area of the square.   """
# given :-
centre_angle = 60
radius = 42

arc_length = (centre_angle/360)*2*3.14*radius
print("Length of arc is {} ".format(arc_length))

sq_side = arc_length/4

area = sq_side*sq_side
print("Area is {}".format(area))