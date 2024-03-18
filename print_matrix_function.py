def print_matrix (matrix_param):
  matrix = "\n";

  for i in range(len(matrix_param)):
    for j in range(len(matrix_param[0])):
      matrix += f"{str(matrix_param[i][j])} "
    matrix += "\n"
  print(matrix)