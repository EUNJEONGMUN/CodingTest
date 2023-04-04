def solution(arr):
    def div(size, x, y):
        if size == 2:
            sum_arr = arr[x][y]+arr[x+1][y]+arr[x][y+1]+arr[x+1][y+1]
            if sum_arr == 4:
                return (0, 1)
            elif sum_arr == 0:
                return (1, 0)
            else:
                return (4-sum_arr, sum_arr)
        left_up = div(size//2, x, y)
        left_down = div(size//2, x+size//2, y)
        right_up = div(size//2, x, y+size//2)
        right_down = div(size//2, x+size//2, y+size//2)

        if left_up[0]+left_down[0]+right_up[0]+right_down[0] == 4 and left_up[1]+left_down[1]+right_up[1]+right_down[1] == 0:
            return (1, 0)
        elif left_up[0]+left_down[0]+right_up[0]+right_down[0] == 0 and left_up[1]+left_down[1]+right_up[1]+right_down[1] == 4:
            return (0, 1)
        else:
            return (left_up[0]+left_down[0]+right_up[0]+right_down[0], left_up[1]+left_down[1]+right_up[1]+right_down[1])
    return list(div(len(arr), 0, 0))


print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [
      0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
