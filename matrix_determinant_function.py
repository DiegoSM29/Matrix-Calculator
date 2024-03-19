from matrix_creator_function import create_matrix
from upper_triangular_matrix_function import upper_triangular_matrix

def matrix_determinant ():
  orden = int(input("Ingrese el órden de la matriz: "))
  A = create_matrix(orden, orden);
  A = upper_triangular_matrix(A)
  determinant = 1
  for i in range(len(A)):
    determinant = determinant * A[i][i] 
  print(f"La determinante es: {determinant}")
  
