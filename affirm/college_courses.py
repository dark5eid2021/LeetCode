"""
College Course Schedule
Time: O(V + E)
Space: O(V + E)
where V = number of courses, E = number of prerequisites
"""

def can_finish(num_courses, prerequisites):
    """
    Cycle detection in directed graph using DFS

    Strategy:
    - Build adjacency list from prerequisites
    - Use DFS to detect cycles in the graph
    - If cycle exists, courses cannot be completed
    - Track visiting state: 0 = unvisited, 1 = visiting, 2 = visited
    """

    # build adjacency list: course -> list of dependent courses
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 0 = unvisited, 1 = visiting (in current path), 2 = visited (completed)
    state = [0] * num_courses

    def has_cycle(course):
        """DFS to detect cycle starting from givenn course"""
        if state[course] == 1: # Found cycle (back edge)
            return True
        if state[course] == 2: # Already processed, no cycle
            return False
        
        # Mark as visiting
        state[course] = 1

        # Check for all dependent courses
        for next_course in graph[course]:
            if has_cycle(next_course):
                return True 
        
        # Check each course for cycles
        for course in range(num_courses):
            if state[course] == 0: # Not yet visited
                if has_cycle(course):
                    return False
        
        return True 


# Test cases
def test():
    print("Testing course schedule")

    print(f'2 courses, [[1,0]] -> {can_finish(2, [[1,0]])}')           # Expected: True
    print(f'2 courses, [[1,0],[0,1]] -> {can_finish(2, [[1,0],[0,1]])}')  # Expected: False
    print(f'4 courses, [[1,0],[2,0],[3,1],[3,2]] -> {can_finish(4, [[1,0],[2,0],[3,1],[3,2]])}')  # Expected: True
    print(f'3 courses, no prereqs -> {can_finish(3, [])}')             # Expected: True


if __name__ == "__main__":
    test()