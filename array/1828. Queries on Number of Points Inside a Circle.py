'''
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.
'''
import math

class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        return [sum(math.sqrt((x0-x1)**2 + (y0-y1)**2) <= r for x1, y1 in points) for x0, y0, r in queries]

if __name__ == "__main__":
    points = [[1,3],[3,3],[5,3],[2,2]]
    queries = [[2,3,1],[4,3,1],[1,1,2]]
