import numpy as np
import copy
matrix = np.array([[10,-7,0,1],[-3,2.099999,6,2],[5,-1,5,-1],[2,1,0,2]])
b = np.array([8,5.900001,5,1])

def MainElement(matrix,b):
    rowchanged = {}
    norm_matrix = 0
    norm_inverse = 0
    det = 1
    (width,length) = matrix.shape
    x = []
    algebtaic_Cofactor = np.array([[None]*width]*width)
    for i in range(width):
        for j in range(width):
            rowlist = []
            columnlist = []
            for k in range(width):
                if k != i:
                    rowlist.append(k)
                if k != j:
                    columnlist.append(k)
            #algebtaic_Cofactor[i,j] = Det(augmentation[rowlist,columnlist])
    for i in range(width):
        c = 0
        for j in range(width):
            pass#c += augmentation[i,j]
        if norm_matrix < c:
            pass#norm_matrix = c
            
    augmentation = np.linspace(0,0,width*(length+1))
    augmentation = augmentation.reshape((width,length+1))
    for i in range(width):
        for j in range(width):
            augmentation[i,j] = matrix[i,j]
        augmentation[i,-1] = b[i]

    for i in range(width-1):
        row = i 
        a = augmentation[i,i]
        for j in range(i,width):
            if abs(a) < abs(augmentation[j,i]):
                row = j
                #print row
                a = augmentation[row,i]
        middle = copy.deepcopy(augmentation[i,:])
        augmentation[i,:] = augmentation[row,:]
        augmentation[row,:] = middle
        rowchanged[str(i)] = str(row)
        #print augmentation
        
        for j in range(i+1,width):
            augmentation[j,:] = augmentation[j,:]-\
                                augmentation[i,:]*augmentation[j,i]\
                                /augmentation[i,i]
    print augmentation
    for i in range(width):
        det *= augmentation[i,i]
    det *= ((-1)**len(rowchanged))
    for i in reversed(range(1,width)):
        augmentation[i,:] /= augmentation[i,i]
        for j in reversed(range(i)):
            augmentation[j,:] -= augmentation[i,:]\
                                 *augmentation[j,i]/augmentation[i,i]
        if i == 1:
            augmentation[0,:] /= augmentation[0,0]

    for i in range(width):
        x.append(augmentation[i,-1])

    for i in range(width):
        for j in range(width):
            pass#algebtaic_Cofactor[i,j] = algebtaic_Cofactor[i,j]/det
    
    for i in range(width):
        for j in range(width):
            pass#algebtaic_Cofactor[i,j] /= det

    for i in range(width):
        c = 0
        for j in range(width):
            pass#c += algebtaic_Cofactor[i,j]
        if norm_inverse < c:
            pass#norm_inverse = c
        
    return x
