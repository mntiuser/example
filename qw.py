from numpy import array
from numpy import tensordot
A=array ([ [[1,2,3], [4,5,6], [7,8,9]], [[11,12,13], [14,15,16], [17,18,19]], [[21,22,23], [24,25,26], [27,28,29]]])
print(A.shape)
print(" A Matrix is:\n")
print(A)
#B Array 
B=array ([ [[1,2,3], [4,5,6], [7,8,9]], [[11,12,13], [14,15,16], [17,18,19]], [[21,22,23], [24,25,26], [27,28,29]]])
print(B.shape) 
print("B Matrix is \n",B) 
print("Tensor addition is\n")
C=A+B
print(C.shape)
print("The Addition result C Matrix\n",C)
print("Tensor Subtraction is\n")
S=A-B
print(S.shape)
print("The difference S Matrix\n",S)
print("Tensor Multiplication is\n")
M=A*B
print(M.shape)
print("The Product of Scalar result matrix\n",M)
print("Tensor division is\n")
DI=A/B
print(DI.shape)
print("The Quotient DI Matix\n:",DI)
D=array([1,2])
E=array([3,4])
F=tensordot(D,E,axes=0)
print("Result wen axes=0\n",F)
F=tensordot(D,E,axes=1)
print("Result wen axes=1\n",F)