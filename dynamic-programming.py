

def fib(n):

    memoize = {0: 0, 1: 1}

    def _fib(n):
        # print(n)
        if n not in memoize:
            memoize[n] = _fib(n-1) + _fib(n-2)
        return memoize[n]

    return _fib(n)

# x, y
# row, col
#
# (x, y)

# Can move right or down. No zig-zags. Returning how many 1s in graph.


def my_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total


def rec_my_sum(nums):
    def _rec_my_sum(i, running_total):
        # Exit Case
        if i > len(nums) - 1:
            return running_total
        # Action Logic
        # Recursive Call
        return _rec_my_sum(i + 1, running_total + nums[i])
    return _rec_my_sum(0, 0)


graph = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1]
]

graph = [
    [3, 3, 3, 1],
    [3, 3, 3, 1],
    [2, 2, 2, 1]
]

# [0, 1]
# [0, 1]
#
# 0+1+1
# 0+0+1
# float(-inf)
# O(n*m)


def traverse_graph(graph):

    def _traverse_graph(row, col, total):
        # Action logic
        total += graph[row][col]
        # Exit Case
        if row + 1 == len(graph) and col + 1 == len(graph[0]):
            return total
        # More Action logic
        if row + 1 < len(graph) and col + 1 < len(graph[0]):
            go_right = _traverse_graph(row, col + 1, total)
            go_down = _traverse_graph(row + 1, col, total)
            return max(go_right, go_down)
        elif row + 1 == len(graph):
            return _traverse_graph(row, col + 1, total)
        return _traverse_graph(row + 1, col, total)

        # Recursive Call
    return _traverse_graph(0, 0, 0)


graph = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1]
]


def traverse_graph_dynamic(graph):
    end_key = (len(graph) - 1, len(graph[0]) - 1)
    memoize = {end_key: graph[end_key[0]][end_key[1]]}

    def _traverse_graph(row, col):
        key = (row, col)
        # Exit Case
        if key in memoize:
            return memoize[key]

        # Action logic
        total = graph[row][col]
        # More Action logic
        if row + 1 < len(graph) and col + 1 < len(graph[0]):
            go_right = _traverse_graph(row, col + 1)
            go_down = _traverse_graph(row + 1, col)
            total += max(go_right, go_down)
        elif row + 1 == len(graph):
            total += _traverse_graph(row, col + 1)
        else:
            total += _traverse_graph(row + 1, col)

        memoize[key] = total
        return memoize[key]

        # Recursive Call
    return _traverse_graph(0, 0)


graph = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1]
]


def traverse_graph_dynamic2(graph):
    end_key = (len(graph) - 1, len(graph[0]) - 1)
    memoize = {"ob": 0, end_key: graph[end_key[0]][end_key[1]]}

    def _key_gen(row, col):
        if row >= len(graph) or col >= len(graph[0]):
            return "ob"
        return (row, col)

    def _traverse_graph(row, col):
        key = _key_gen(row, col)
        # Exit Case
        if key not in memoize:
            go_right = _traverse_graph(row, col + 1)
            go_down = _traverse_graph(row + 1, col)
            memoize[key] = max(go_right, go_down) + graph[row][col]
        return memoize[key]

        # Recursive Call
    return _traverse_graph(0, 0)


print(traverse_graph_dynamic2(graph))
'''










































'''


# def what_will_i_return():
#     number = 0
#
#     def _what_will_i_do(i):
#         number += i
#         if i < 5:
#             _what_will_i_do(i + 1)
#     return number
