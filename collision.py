def check_collision(a, b):
    for b1 in a.bboxes:
        for b2 in b.bboxes:
            if b1.xmax < b2.xmin or b1.xmin > b2.xmax or b1.ymax < b2.ymin or b1.ymin > b2.ymax:
                continue
            else:
                return True
        