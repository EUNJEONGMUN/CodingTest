def solution(commands):
    LENGTH = 50*50
    matrix = ["EMPTY"]*LENGTH
    index = list(range(LENGTH))
    answer = []

    def convert_xy(a, b):
        return (int(a)-1)*50+(int(b)-1)

    def update(xy, s):
        for idx in range(LENGTH):
            if index[idx] == index[xy]:
                matrix[idx] = s

    def replace(s1, s2):
        for i in range(LENGTH):
            if matrix[i] == s1:
                matrix[i] = s2

    def merge(a, b):
        val = "EMPTY"
        if matrix[a] != "EMPTY":
            val = matrix[a]
        elif matrix[b] != "EMPTY":
            val = matrix[b]

        merge_idx = index[a]
        old_idx = index[b]

        for i in range(LENGTH):
            if index[i] == old_idx:
                index[i] = merge_idx
        if val != "EMPTY":
            for i in range(LENGTH):
                if index[i] == merge_idx:
                    matrix[i] = val

    def unmerge(xy):
        val = matrix[xy]
        position = index[xy]
        for i in range(LENGTH):
            if index[i] == position:
                matrix[i] = "EMPTY"
                index[i] = i
        matrix[xy] = val

    def print_matrix(xy):
        answer.append(matrix[xy])

    for command in commands:
        c = command.split()
        if c[0] == "UPDATE":
            if len(c) > 3:
                update(convert_xy(c[1], c[2]), c[3])
            else:
                replace(c[1], c[2])
        elif c[0] == "MERGE":
            merge(convert_xy(c[1], c[2]), convert_xy(c[3], c[4]))
        elif c[0] == "UNMERGE":
            unmerge(convert_xy(c[1], c[2]))
        elif c[0] == "PRINT":
            print_matrix(convert_xy(c[1], c[2]))

    return answer


print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant",
      "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d",
      "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
