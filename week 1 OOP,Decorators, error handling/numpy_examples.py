#numpy examples
import numpy as np
a = np.arange(15).reshape(3, 5)

print(a)

print(f"shape {a.shape}")

print(f" no. of dims {a.ndim}")

#a.dtype.name

print(f"size {a.size} ")

#a.dtype.name


import numpy as np
a = np.array([2, 3, 4])
print(f"array= {a}")

b = np.array([(1.5, 2, 3), (4, 5, 6)])


print(f"\n B = {b}")


print(f"\n The function zeros creates an array full of zeros, the function ones creates an array full of ones, and the function empty creates an array whose initial content is random and depends on the state of the memory.\n")

print(f"Array of zeros")
print(f"\n {np.zeros((3, 4))}")

print(f"Array of ones")
print(f"\n {np.ones((3, 4))}")

print(f"\nTo create sequences of numbers, NumPy provides the arange function which is analogous to the Python built-in range, but returns an array.")

print(f" {np.arange(10, 30, 5)}\n")



print(f" {np.arange(0, 2, 0.3)}\n")


from numpy import pi

print(" linespace use the function linspace that receives as an argument the number of elements that we want\n np.linspace(0, 2, 9) here np.linspace(start, end, no. of elements)  ")
print(f" numpy array = {np.linspace(0, 2, 9)}")

x = np.linspace(0, 2 * pi, 100) 
f = np.sin(x)



print(f" special sine function={f}")


a = np.arange(6)

print(f"a = {a}")
b = np.arange(12).reshape(4, 3)  
print(f"b = {b}")


c = np.arange(24).reshape(2, 3, 4) 


print(f"c = {c}")

print("\n")
print(np.arange(10000))

print("\n")
print(np.arange(10000).reshape(100, 100))



a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(f"b={b}\n")
c = a - b
print(f"c= {c}")
print(f"b**2={b**2}")
print(f"10 * np.sin(a) ={10 * np.sin(a)}")
print(f"a < 35{a < 35}")


A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(f"A * B={A * B}")     # elementwise product
print(f"A @ B={A @ B}")     # matrix product
print(f"A.dot(B)={A.dot(B)}")  # another matrix product



print("Universal functions\n")
print("NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called “universal functions” (ufunc). Within NumPy, these functions operate elementwise on an array, producing an array as output.\n")



B = np.arange(3)
print(f"B={B}\n")
print(f"np.exp(B) -> {np.exp(B)}\n")
print(f"np.sqrt(B) -> {np.sqrt(B)}\n")

C = np.array([2., -1., 4.])

print(f"np.add(B, C)-> {np.add(B, C)}\n")


print("Indexing, slicing and iterating\n")
print("One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences.\n")


a = np.arange(10)**3
print(f"a={a}\n")
print(f"a={a[2]}\n")
print(f"a={a[2:5]}\n")


# equivalent to a[0:6:2] = 1000;
# from start to position 6, exclusive, set every 2nd element to 1000
a[:6:2] = 1000
print(f"a={a}\n")
a=a[::-1]  # reversed a
print(f"a[::-1]={a}\n")
for i in a:
    print(i**(1 / 3.))

print("Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas:\n")


def f(x, y):
    return 10 * x + y
b = np.fromfunction(f, (5, 4), dtype=int)
print(f"b={b}\n")
print(f"b[2, 3]={b[2, 3]}\n")

# each row in the second column of b
print(f"b[0:5, 1]={b[0:5, 1]}\n")

    # equivalent to the previous example
print(f"b[:, 1]={b[:, 1]}\n")

 # each column in the second and third row of b
print(f"b[1:3, :] ={b[1:3, :] }\n")

print("When fewer indices are provided than the number of axes, the missing indices are considered complete slices:\n")
print(f"b[-1]  ={b[-1]  }\n")



c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [ 10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])


print(f"c.shape{c.shape}\n")

#c[1, ...] 


for row in b:
    print(row)

print("\n\n")


for element in b.flat:
    print(element)