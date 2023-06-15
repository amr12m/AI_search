import numpy as np
from PIL import Image, ImageDraw
import ast

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
def BFS(start, goal):
    file = open('my_graph.txt', 'r')
    contents = file.read()
    graph = ast.literal_eval(contents)
    file.close()

    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            print_img(path)
            return path

        else:
            adjacent_noses = graph.get(node, [])
            for node2 in adjacent_noses:
                new_path = path.copy()
                new_path.append(node2)
                queue.append(new_path)