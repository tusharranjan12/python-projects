import numpy as np

def input_matrix(prompt):
    print(prompt)
    rows = int(input('enter the number of rows: '))
    cols = int(input('Enter the number of columns: '))
    print('Enter the values of the matrix row by row')
    matrix = []
    for i in range(rows):
        row = list(map(float,input(f'Row{i+1}: ').split()))
        if len(row) != cols:
            print('Number of columns must match the input')
            return None
        matrix.append(row)
    return np.array(Matrix)
#Matrix operations
def operation():
    while True:
        print('1.Addition')
        print('2.Subtraction')
        print('3.Multiplication')
        print('4.exit')
        choice = input('Enter your operation(1-4): ')
        if choice == '4':
            break

        mat1 = input_matrix('Matrix1: ')
        mat2 = input_matrix('matrix2: ')
        if choice == '1':
            if mat1.shape == mat2.shape:
                print('result: \n', mat1+mat2)
            else:
                print('Matrix must have same number of dimension')

        elif choice == '2':
            if mat1.shape == mat2.shape:
                print('Result: \n', mat1-mat2)
            else:
                print('Matrix must have the same dimension')

        elif choice == '3':
            if mat1.shape[1] == mat2.shape[0]:
                print('result: \n', np.dot(mat1,mat2))
            else:
                print('matrix 1 columns must be same as number of rows in matrix 2 for multiplication')

        else:
            print('invalid')
#transpose of matrix
x = input_matrix("type a matrix: ")
result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

#determinant of a matrix
determinant = np.linalg.det(x)
print(int(determinant))

for r in result:
    print(r)
if __name__ == '__main__':
    operation()