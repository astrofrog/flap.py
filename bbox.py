class BBox(object):
    def __init__(self, x, y, dx, dy):
        self.xmin = x
        self.xmax = x + dx
        self.ymin = y
        self.ymax = y + dy