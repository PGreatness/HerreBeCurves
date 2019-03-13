import display as show
import draw as d
import parser as p
import matrix as m
import math

screen = show.new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = m.new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

p.parse_file( 'script', edges, transform, screen, color )
