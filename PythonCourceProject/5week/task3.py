"""
https://leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/bus-routes/
"""


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        bus_stops = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                bus_stops[stop].add(i)

        queue = deque([source])
        visited_stops = {source}
        visited_buses = set()
        buses = 0
        
        while queue:
            buses += 1
            for _ in range(len(queue)):
                stop = queue.popleft()
                for bus in bus_stops[stop]:
                    if bus in visited_buses:
                        continue
                    visited_buses.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop == target:
                            return buses
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append(next_stop)

        return -1