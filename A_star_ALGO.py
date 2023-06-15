import numpy as np
from PIL import Image, ImageDraw
import ast


file = open('H_table.txt', 'r')
contents = file.read()
H_table = ast.literal_eval(contents)
file.close()

map_image = Image.open("map.jpg")
file = open('my_image_points.txt', 'r')
contents = file.read()
dictPoint = ast.literal_eval(contents)
file.close()
def print_img(path):
    draw = ImageDraw.Draw(map_image)
    for i in range(len(path) - 1):
        for city, coord in dictPoint.items():
            # Draw a circle for the city
            draw.ellipse((coord[0] - 5, coord[1] - 5, coord[0] + 5, coord[1] + 5), fill="red", outline="black")
            # Draw the city name next to the circle
            draw.text((coord[0] + 10, coord[1] - 10), city, fill="black")

        # Draw a line between two cities
        draw.line((dictPoint[path[i]], dictPoint[path[i + 1]]), fill="blue", width=2)
    # show map with city markers
    map_image.show()
def get_heuristic(node, H_table):

    for nested_dict in H_table.values():
        if isinstance(nested_dict, dict) and node in nested_dict:
            return nested_dict[node]

    return None

def path_f_cost(path):

    g_cost=0
    for (node,cost) in path:
        g_cost+=cost
    last_node=path[-1][0]
    h_cost=get_heuristic(last_node,H_table)
    f_cost = g_cost + h_cost
    return f_cost,last_node

def A_star( start, goal):
    file = open('real_dist.txt', 'r')
    contents = file.read()
    graph = ast.literal_eval(contents)
    file.close()

    visited = []
    queue = [[(start,0)]]
    while queue:
        queue.sort(key=path_f_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            path_only = [node for node, cost in path]
            print_img(path_only)
            return path_only

        else:
            adjacent_noses = graph.get(node, [])
            for (node2,cost) in adjacent_noses:
                new_path = path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)