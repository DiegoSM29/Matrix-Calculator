from matrix_creator_function import create_matrix

def scalar_multiply_matrix ():
  scalar = int(input("Ingrese un escalar: "))
  A = create_matrix();
  RESULT = [[] for _ in range(len(A))]
  for i in range(len(A)):
    for j in range(len(A[0])):
      RESULT[i].append(A[i][j] * scalar)
  
  print(RESULT)
