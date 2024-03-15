def create_matrix (rows_param = 0, colums_param = 0):
  matrix = []
  rows = int(input("Ingrese el número de filas de la matriz: ")) if rows_param == 0 else rows_param;
  colums = int(input("Ingrese el número de columnas de la matriz: ")) if colums_param == 0 else colums_param;
  print("soy otra matriz") if colums_param != 0 else print("soy la primera matriz") 
  for i in range(0, rows):
    matrix.append([])
    for k in range (0, colums):
      num = int(input(f"Ingrese un valor para A{i+1}{k+1}: "))
      matrix[i].append(num)
      print("gaaaa")
  return matrix