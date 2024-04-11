def row_sums(my_matrix: list):

    sumsToBeAdded = []
    
    for i in range(len(my_matrix)):
        sum = 0
        for j in range(len(my_matrix[i])):
            sum += my_matrix[i][j]
        sumsToBeAdded.append(sum)

    for i in range(len(my_matrix)):
        my_matrix[i].append(sumsToBeAdded[i])

if __name__ == "__main__":
    my_matrix = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    row_sums(my_matrix)
    print(my_matrix)
