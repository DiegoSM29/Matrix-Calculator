from matrix_creator_function import create_matrix

def matrix_subtraction (matrix1 = 0, matrix2 = 0):
  A = create_matrix()
  B = create_matrix(len(A), len(A[0]))
  C = [[] for _ in range(len(A))]

  for i in range(len(A)):
    for j in range(len(A[0])):
      C[i].append(A[i][j] - B[i][j]);
  
  print(C);