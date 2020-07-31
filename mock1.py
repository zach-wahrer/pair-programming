def comboSum(candidates: list, target: int) -> list:

    def backtrack(result, current, candidates, target, index):
        if target < 0:
            return
        if target == 0:
            result.append(current)
            return
        for i in range(index, len(candidates)):
            backtrack(result, current+[candidates[i]], candidates, target - candidates[i], i)

    result = []
    backtrack(result, [], candidates, target, 0)
    return result


print(comboSum([1, 2], 2))  # [[1, 1], [2]]
assert comboSum([1, 2], 2) == [[1, 1], [2]]

print(comboSum([2, 3, 6, 7], 7))
assert comboSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]

print(comboSum([2, 3, 5], 8))
assert comboSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


# Found 2, can be component of 7, t

# [2] 5
# [2, 2] 3
# [2, 2, 2] 1
# [2, 2] 3
# [2] 5
# [2, 3] 2
#
# 7 6  3 2
# [7]
# [3 2 2]
# # Copy temp lists
#
# def dan(candidates, target):
#     res = []
