'''
   This script allows to collect Cartan matrices of a special Vogan diagram together with the speciality index: 0 if the diagram is special, 1 otherwise.

   Copyright (C) 2019  Alice Gatti

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import numpy as np
def toMatrix(M):
	mat=[]
	for i in range(len(M[0])):
		mat.append([])
		for j in range(len(M[0])):
			mat[i].append(M[i,j])
	return matrix(mat)
data=[]   # data will become the array of Cartan matrices. We fill data with all Cartan matrices in range maxRange 
specialityIndex=[]   # specialityIndex will become the array of Cartan matrices  
maxRange=11
maxSizeRow=20
for lieType in ['A','B','C','D','E','F','G']:
	for rank in range(2,maxRange):
		if (lieType=='C' and rank<=2) or (lieType=='D' and rank<=3) or (lieType=='G' and rank!=2) or (lieType=='F' and rank!=4) or (lieType=='E' and (rank not in [6,7,8])):
			continue
		W=WeylGroup([lieType,rank],implementation='permutation')
		positiveRoots=W.positive_roots()	# Positive roots
		C=CartanMatrix([lieType,rank])	# Cartan matrix of the Lie algebra   
		for y in [q for q in Combinations(range(rank)) if q!=[]]:
			compactroots=[root for root in positiveRoots if sum(root[k] for k in y)%2==0]	# Compact roots
			noncompactroots=[root for root in positiveRoots if sum(root[k] for k in y)%2!=0]	# Non-compact roots
			epsilon={root: (1 if root in noncompactroots else -1) for root in positiveRoots}	# Compactness coefficient
			eta=-2*(sum(-compactroots[i] for i in range(len(compactroots)))+sum(noncompactroots[i] for i in range(len(noncompactroots))))	# Eta vector
			phi0=(C)*(eta-2*sum(root for root in positiveRoots if all(root[k]==0 for k in y)))	# phi0 vector
			res_left=int((maxSizeRow-rank)/2)	# Pads for the Cartan matrix augmented with the Vogan diagram
			res_right=maxSizeRow-rank-res_left
			if all(phi0[k]==0 for k in range(len(phi0))):
				cartanEn=np.pad(np.array((toMatrix(C)).insert_row(rank,[1 if i in y else 0 for i in range(rank)])),((res_left,res_right),(res_left,res_right)),'constant')
				data.append(cartanEn)
				specialityIndex.append(0)
			elif [sgn(phi0[k]) for k in range(len(phi0))]==[-1 if k in y else 0 for k in range(len(phi0))]:	
				cartanEn=np.pad(np.array((toMatrix(C)).insert_row(rank,[1 if i in y else 0 for i in range(rank)])),((res_left,res_right),(res_left,res_right)),'constant')
				data.append(cartanEn)
				specialityIndex.append(0)
			elif [sgn(phi0[k]) for k in range(len(phi0))]==[1 if k in y else 0 for k in range(len(phi0))]:	
				cartanEn=np.pad(np.array((toMatrix(C)).insert_row(rank,[1 if i in y else 0 for i in range(rank)])),((res_left,res_right),(res_left,res_right)),'constant')
				data.append(cartanEn)
				specialityIndex.append(0)
			else:
				cartanEn=np.pad(np.array((toMatrix(C)).insert_row(rank,[1 if i in y else 0 for i in range(rank)])),((res_left,res_right),(res_left,res_right)),'constant')
				data.append(cartanEn)
				specialityIndex.append(1)
finalData=np.stack(data)
np.save(os.path.expanduser('~/special-vogan/deep-learning/data/finalData'),finalData)
np.save(os.path.expanduser('~/special-vogan/deep-learning/data/specialityIndex'),specialityIndex)
print(cputime())
