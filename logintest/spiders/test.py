def maxPoints(points):
    max = 0
    for idx,po in enumerate(points):
        if points.count(po)>1:
            points.pop(idx)
    for i in range(len(points)):
        line = []
        line.append(points[i])
        for j in range(i + 1, len(points)):
            line = line[:1]
            line.append(points[j])
            for k in range(j + 1, len(points)):
                p1 = points[i]
                p2 = points[j]
                p3 = points[k]
                if (p2[1] - p1[1]) * (p3[0] - p2[0]) == (p2[0] - p1[0]) * (p3[1] - p2[1]):
                    line.append(p3)
            if len(line) > max:
                max = len(line)
    return max

li = [[0,9],[138,429],[115,359],[115,359],[-30,-102],[230,709],[-150,-686],[-135,-613],[-60,-248],[-161,-481],[207,639],[23,79],[-230,-691],[-115,-341],[92,289],[60,336],[-105,-467],[135,701],[-90,-394],[-184,-551],[150,774]]
print(maxPoints(li))
print(len(li))