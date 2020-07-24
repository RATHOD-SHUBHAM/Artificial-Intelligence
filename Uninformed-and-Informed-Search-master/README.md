# Artificial Intelligence 
# Uninformed-and-Informed-Search

![](t1_p1.gif)

Implement a search algorithm that can find a route between any two cities. 
The program will be called find_route, and will take exactly commandline arguments as follows:

find_route input_filename origin_city destination_city heuristic_filename

# An example command line is:

python find_route input1.txt Bremen Kassel (For doing Uninformed search)

or

python find_route input1.txt Bremen Kassel h_kassel.txt (For doing Informed search)


# If heuristic is not provided then program must do uninformed search. 
Argument input_filename is the name of a text file such as input1.txt, that describes road connections between cities in some part of the world. For example, the road system described by file input1.txt can be visualized in Figure shown above. You can assume that the input file is formatted in the same way as input1.txt: each line contains three items. The last line contains the items "END OF INPUT", and that is how the program can detect that it has reached the end of the file. The other lines of the file contain, in this order, a source city, a destination city, and the length in kilometers of the road connecting directly those two cities. Each city name will be a single word (for example, we will use New_York instead of New York), consisting of upper and lowercase letters and possibly underscores.

The program will compute a route between the origin city and the destination city, and will print out both the length of the route and the list of all cities that lie on that route. It should also display the number of nodes expanded, nodes generated and max number of nodes in the fringe. 
# For example,

python find_route input1.txt Bremen Kassel

should have the following output:

nodes expanded: 12

nodes generated: 19

max nodes in memory: 11

distance: 297.0 km

route:

Bremen to Hannover, 132.0 km

Hannover to Kassel, 165.0 km

and

find_route input1.txt London Kassel

should have the following output:

nodes expanded: 7

nodes generated: 6

max nodes in memory: 3

distance: infinity

route:

none


# If a heuristic file is provided then program must perform Informed search. 
The heuristic file gives the estimate of what the cost could be to get to the given destination from any start state (note this is just an estimate). In this case the command line would look like

python find_route inf input1.txt Munich Kassel h_kassel.txt

Here the last argument contains a text file what has the heuristic values for every state wrt the given destination city (note different destinations will need different heuristic values). For example, you have been provided a sample file h_kassel.txt which gives the heuristic value for every state (assuming kassel is the goal). The program should use this information to reduce the number of nodes it ends up expanding. Other than that, the solution returned by the program should be the same as the uninformed version. 
# For example,

python find_route input1.txt Bremen Kassel h_kassel.txt

should have the following output:

nodes expanded: 3

nodes generated: 7

max nodes in memory: 6

distance: 297.0 km

route:

Bremen to Hannover, 132.0 km

Hannover to Kassel, 165.0 km 
