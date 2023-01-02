import numpy as np

# Solve system of linear equations
#S1: {x-y-z=2, x+3y+2z=3, 2x-2y+z=1}
#S2: {x-y+2z=1,x+2y-z=4,4x-y+5z=1}
#S3: {x-y-2z=1,x+2y-z=4,4x-y-5z=1}


#S1
A1 = np.array([[1, -1, -1], [1, 3, 2], [2, -2, 1]])
b1 = np.array([2, 3, 1])
x1 = np.linalg.solve(A1, b1)
print("S1: ", x1)

#S2
A2 = np.array([[1, -1, 2], [1, 2, -1], [4, -1, 5]])
b2 = np.array([1, 4, 1])
x2 = np.linalg.solve(A2, b2)
print("S2: ", x2)

#S3
A3 = np.array([[1, -1, -2], [1, 2, -1], [4, -1, -5]])
b3 = np.array([1, 4, 1])
x3 = np.linalg.solve(A3, b3)
print("S3: ", x3)

# Exo 4 : Positivité & Décomposition de Cholesky
def is_positive(matrix):
    # Convertir la matrice en un objet NumPy array
    matrix = np.array(matrix)
    # Calculer la décomposition de Cholesky de la matrice
    try:
        L = np.linalg.cholesky(matrix)
    except np.linalg.LinAlgError:
        # Si la décomposition de Cholesky échoue, cela signifie que la matrice n'est pas positive
        return False
    # Si la décomposition de Cholesky réussit, cela signifie que la matrice est positive
    return True


A = np.array([[1, -1, -1], [-1, 2, 4], [-1, 4, 14]])
print("Verification de A: ",is_positive(A))


def is_positive_matrix(A):
  # Vérifiez si le déterminant de la matrice est strictement positif
  if np.linalg.det(A) <= 0:
    return False

  # Vérifiez si tous les éléments diagonaux de la matrice sont strictement positifs
  for i in range(A.shape[0]):
    if A[i, i] <= 0:
      return False

  # Si tous les tests ont été passés, la matrice est positive
  return True


# Exemple d'utilisation de la fonction
print("Redondance de verification de A: ",is_positive_matrix(A)) 


# Effectuez la décomposition de Choleski de la matrice A
L = np.linalg.cholesky(A)

# Affichez les matrices L et L.T
print(L)
print(L.T)
