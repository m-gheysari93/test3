import numpy as np

#initial definition
sigma-x=np.array([0,1.],[1.,0])
sigma-y=np.array([0,-j],[j,0])
sigma-z = ([[1.,0] , [0,-1.]])
I = np.array([1.,0],[0,1.])

#calculation Hamiltonian
H = (np.kron(.5*sigma-x,np.kron(.5*sigma-x,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I)))))))))+np.kron(.5*sigma-y,np.kron(.5*sigma-y,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I)))))))))+np.kron(.5*sigma-z,np.kron(.5*sigma-z,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I))))))))))
H = H + (np.kron(I,np.kron(.5*sigma-x,np.kron(.5*sigma-x,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I)))))))))+np.kron(I,np.kron(.5*sigma-y,np.kron(.5*sigma-y,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I)))))))))+np.kron(I,np.kron(.5*sigma-z,np.kron(.5*sigma-z,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I))))))))))
H = H + (np.kron(I,np.kron(I,np.kron(.5*sigma-x,np.kron(.5*sigma-x,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I)))))))))+np.kron(I,np.kron(I,np.kron(.5*sigma-y,np.kron(.5*sigma-y,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I)))))))))+np.kron(I,np.kron(I,np.kron(.5*sigma-z,np.kron(.5*sigma-z,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I))))))))))
H = H + (np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-x,np.kron(.5*sigma-x,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-y,np.kron(.5*sigma-y,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-z,np.kron(.5*sigma-z,np.kron(I,np.kron(I,np.kron(I,np.kron(I,I))))))))))
H = H + (np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-x,np.kron(.5*sigma-x,np.kron(I,np.kron(I,np.kron(I,I)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-y,np.kron(.5*sigma-y,np.kron(I,np.kron(I,np.kron(I,I)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-z,np.kron(.5*sigma-z,np.kron(I,np.kron(I,np.kron(I,I))))))))))
H = H + (np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-x,np.kron(.5*sigma-x,np.kron(I,np.kron(I,I)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-y,np.kron(.5*sigma-y,np.kron(I,np.kron(I,I)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-z,np.kron(.5*sigma-z,np.kron(I,np.kron(I,I))))))))))
H = H + (np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-x,np.kron(.5*sigma-x,np.kron(I,I)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-y,np.kron(.5*sigma-y,np.kron(I,I)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-z,np.kron(.5*sigma-z,np.kron(I,I))))))))))
H = H + (np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-x,np.kron(.5*sigma-x,I)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-y,np.kron(.5*sigma-y,I)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-z,np.kron(.5*sigma-z,I))))))))))
H = H + (np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-x,.5*sigma-x)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-y,.5*sigma-y)))))))))+np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-z,.5*sigma-z))))))))))
H = H + (np.kron(.5*sigma-x,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(.5*sigma-x,I)))))))))+np.kron(.5*sigma-y,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,.5*sigma-y)))))))))+np.kron(.5*sigma-z,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,np.kron(I,.5*sigma-z))))))))))

#defining s_1^z
s1z = np.kron(.5*sigma_x , identity)

#H diagnolization
e_values,e_vectors = np.linalg.eig(H)

#calculating expectation value for single state
ev_sz= np.dot(np.conj(e_vectors[:,1]),np.dot(s1z,e_vectors[:,1]))

#calculating e_values
for i in range(1,len10);
    e_value = np.array[H[i][i]]
print e_value
  
#calculating sz_betta
for j in range (0 , 5 , .05)
    sz_betta = np.dot(s1z , np.exp(-j*e_value))/np.trace(-j*e_value)

  print sz_betta
