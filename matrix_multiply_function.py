from matrix_creator_function import create_matrix

def matrix_multiply():
  A = create_matrix();
  B = create_matrix(len(A[0]));
  C = [[] for _ in range(len(A))]
  print (f"A = {A} x B = {B} == C = {C}")
  currentResult = 0;
  for i in range(len(A)):
    for j in range(len(A[0])):
      for k in range(len(A[0])):
        currentResult += (A[i][k] * B[k][j]) 

      C[i].append(currentResult)
      currentResult = 0;
  print(C);

