# import random

# maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#         [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
#         [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

# #  Goal states specified
# Goal_node_1 = [18,23]
# Goal_node_2 = [21,2]

# #  Function to check if the new postion in path meets the required constraints
# #  Constraints are that the cordinates does not lie out of bounds Or they do not meet the last traveled position Or they are not blocked
# def check_next_node(node, last_node):
#     x = node[0]
#     y = node[1]
    
        
#     if (x < 0 or x > 24 ):
#             return 0

#     elif (y < 0 or y > 24):
#             return 0

#     elif (maze[x][y] == 1):
#             return 0

#     elif (node == last_node):
#             return 0
#     else:
#         return 1


# #  Intial cost is set to one as the postion that the robot/person starts from also counted as 1
# cost = 1

# # Last_node is basically the postion that the person/robot just travelled
# Last_node = [0,0]

# # current_node is the postion that the person is currently on
# Current_node = [11,2]

# # Loop till the goal postion is not found
# while((Current_node != Goal_node_1) or (Current_node != Goal_node_2) ):
    
#     x = Current_node[0]
#     y = Current_node[1]
    
# # in order to travel, a person/robot can move in 4 different direction
# #  up, down, left, right
#     x_up = x+1
#     x_down = x-1
#     y_left = y-1
#     y_right = y+1

# # list of 4 different postions that the person can travel to without taking into considaration the edge cases
#     Next_nodes_total = [[x_up,y], [x_down,y], [x,y_left], [x,y_right]]

# # Updated list of 4 different postions that the person can travel to considering the edge cases as well
#     Next_nodes_checked = []

# # loop to create the updated list  
#     for node in Next_nodes_total:
#         node_checked_for_constraints = node

#         # Tru_False basically stores the value of 1 or 0, 1 = node meets the constraints, 0 = node doesnt meet the constraints
#         Tru_false = check_next_node(node, Last_node)
#         if(Tru_false != 0):
#             Next_nodes_checked.append(node_checked_for_constraints)

#    # print(Next_nodes_checked)

# # if the updated list is completely empty then it means the person has moved to a postion from where it cannot travel to any other
# # place, keeping in mind that the constraints are met
#     if(len(Next_nodes_checked) == 0):
#         print("the random search will enter into infinite loop, terminate the code")
#         break;

# #  Just updating the postions
#     Last_node = Current_node
#     Current_node = random.choice(Next_nodes_checked)
#     # print(Current_node)
    
#     cost = cost+1 
    
#     if((Current_node == Goal_node_1) or (Current_node == Goal_node_2)):
#         print("the program has successfully run and total cost is ")
#         print(cost)
#         break

    
#     # simply edit cost == 1000 OR 10K OR 100K OR 1000K
#     if cost == 10000: 
#         print("the search has exceeded the steps")
#         break



a = (1,2)

print(a[0])

# lista = listb + lista

# print(lista)