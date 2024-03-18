from print_matrix_function import print_matrix
def upper_triangular_matrix (matrix_param):
  pivot = 0;
  for i in range(len(matrix_param) - 1):
    for extra in range (i + 1, len(matrix_param)):
      print(f"extra: {extra}")
      pivot = -(matrix_param[extra][i] / matrix_param[i][i]);
      print(f"soy el pivot {pivot} resultado de esto: {matrix_param[extra][i]} / {matrix_param[i][i]} ")      
      for j in range(len(matrix_param[0])):
        matrix_param[extra][j] = pivot * matrix_param[i][j] + matrix_param[extra][j]
      
  print_matrix(matrix_param)