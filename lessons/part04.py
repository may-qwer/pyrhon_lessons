import random

MAT1 = [[1, 2, 1],
        [4, 2, 2],
        [0, 1, 7]]

MAT2 =  [[7, 5, 1],
        [2, 1, 2],
        [4, 3, 4]]

MAT1_1 = [[5, 3, 7, 0],
          [7, 1, 9, 2],
          [3, 4, 7, 6]]

MAT2_1 =  [[20.3, 1.6],
           [18.6, 1.3],
           [12.1, 1],
           [23, 1.8]]

random.seed(2024)

def random_mat(n, m):
    mat = []
    for i in range(n):
        mat.append([random.randint(0, 9) for j in range(m)])
    return mat

def identity_mat(n):
    mat = []
    one_index = 0
    for i in range(n):
        mat.append([0 for j in range(n)])
    for el in mat:
        el[one_index] = 1
        one_index += 1
    return mat

def product_of_mat(mat1, mat2):
    res_mat = []
    for i in range(len(mat1)):
        res_mat.append([0 for j in range(len(mat2[0]))])
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                res_mat[i][j] += mat1[i][k] * mat2[k][j]
    return res_mat


def show_matrix(mat):
    for i in mat:
        print(i)


if __name__ == "__main__":
    show_matrix(random_mat(3,4))
    print("")
    show_matrix(identity_mat(5))
    print("")
    show_matrix(product_of_mat(MAT1_1, MAT2_1))
    print("")
    show_matrix((product_of_mat(MAT1, MAT2)))
    print("")
    show_matrix((product_of_mat(random_mat(3,4), random_mat(4,5))))
