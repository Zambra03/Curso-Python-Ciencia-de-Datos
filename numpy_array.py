import numpy as np

escalar = np.array(42)
print(type(escalar))
print(escalar)

vector = np.array([30,29,42,35,37,24,31])
print(vector)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)

tensor = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(tensor)

array_arange = np.arange(10)
print(array_arange)

eye_matrix = np.eye(3)
print(eye_matrix)

diag = np.diag([1,2,3,4,5])
print(diag)

random = np.random.random((2,3))
print(random)

array = np.array([[1,2,3],[4,5,6]])
print(array.ndim)
print(array.shape)
print(array.dtype)

z = np.array(3, dtype=np.uint8)
print(z)

double_array = np.array([1,2,3], dtype='d')
print(double_array)