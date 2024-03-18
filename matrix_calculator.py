from matrix_sum_function import matrix_sum
from matrix_subtraction_function import matrix_subtraction;
from scalar_multiply_matrix_function import scalar_multiply_matrix
from matrix_multiply_function import matrix_multiply
from matrix_transpose_function import matrix_transpose
from inverse_matrix_function import inverse_matrix

def matrix_calculator ():
  print("1) Suma \n2) Resta \n3) Multiplicación por un escalar \n4) Multiplicación de matrices \n5) Matriz transpuesta \n6) Matriz inversa")
  userOption = int(input("Ingrese la operación que desee realizar: "))
  match userOption:
    case 1:
      matrix_sum() 
    case 2:
      matrix_subtraction()
    case 3:
      scalar_multiply_matrix()
    case 4:
      matrix_multiply()
    case 5:
      matrix_transpose()
    case 6:
      inverse_matrix()
      
matrix_calculator()
