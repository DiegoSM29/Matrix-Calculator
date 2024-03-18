from matrix_creator_function import create_matrix
from print_matrix_function import print_matrix

def matrix_transpose():
  A = create_matrix();
  matrix_A_transposed = [[] for _ in range(len(A[0]))]

  for i in range(len(A)):
    for j in range(len(A[0])):
      matrix_A_transposed[j].append(A[i][j])
  
  print_matrix(matrix_A_transposed);
