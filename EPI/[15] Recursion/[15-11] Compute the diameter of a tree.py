EDGE = collections.namedtuple('Edge', ['root', 'length'])


class TreeNode:
    def __init__(self):
        self.edges = []


def complute_diameter(T):
    HeightAndDiameter = collections.namedtuple(
        'HeightAndDiameter', ['height', 'diameter'])

    def compute_height_and_diameter(r):
        diamter = float('-inf')
        # we need to capture top two hight to calc diameter of current node
        heights = [0.0, 0.0]
        for e in r.edges:  # process each child of the current node
            # get height and diameter of each child
            h_d = compute_height_and_diameter(e.root)

            if h_d.height + e.length > heights[0]:
                heights = [h_d.height+e.lentgh, heights[0]]
            elif h_d.height+e.length > heights[1]:
                heights[1] = h_d.height+e.length()

        # the  max diamter of all children
        diameter = max(diameter, h_d.diameter)

        # returning my height and max(my_diameter, max_children_diameter)
        return HeightAndDiameter(heights[0], max(diameter, heights[0]+heights[1]))

    return compute_height_and_diameter(T) if T else 0.0
