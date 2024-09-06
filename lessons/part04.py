import random

MAT1 = [[1, 2, 1],
        [4, 2, 2],
        [0, 1, 7]]
MAT2 =  [[7, 5, 1],
        [2, 1, 2],
        [4, 3, 4]]

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

def product_of_matrices(mat1, mat2):
    index_c = 0
    index_r = 0
    res_mat = []
    for i in range(len(mat1[0])):
        res_mat.append([0 for j in range(mat2)])
    for i in range(len(mat1[0])):
        for j in range(len(mat2)):
            
            index_c += 1
        index_r += 1


def show_matrix(mat):
    for i in mat:
        print(i)

if __name__ == "__main__":
    show_matrix(random_mat(3,4))
    print("")
    show_matrix(identity_mat(5))