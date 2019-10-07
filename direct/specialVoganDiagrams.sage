'''
   This algorithm allows to determine special Vogan diagrams
   for real semisimple Lie algebras.
   For the details, see https://arxiv.org/abs/1811.06958.

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

[lieType,rank]=[raw_input('Type: '),input('Rank: ')]
print DynkinDiagram([lieType,rank])
W=WeylGroup([lieType,rank],implementation='permutation')
positiveRoots=W.positive_roots()	# Positive roots
C=CartanMatrix([lieType,rank])	# Cartan matrix of the Lie algebra   
print "Dimension:",2*len(positiveRoots)+rank
print '  '
for P in [q for q in Combinations(range(rank)) if q!=[]]:
		compactroots=[root for root in positiveRoots if sum(root[k] for k in P)%2==0]	
		noncompactroots=[root for root in positiveRoots if sum(root[k] for k in P)%2!=0]	
		epsilon={root: (1 if root in noncompactroots else -1) for root in positiveRoots}	
		eta=-2*sum(epsilon[alpha]*alpha for alpha in positiveRoots)	# Eta vector
		phiP=(C)*(eta-2*sum(root for root in positiveRoots if all(root[k]==0 for k in P)))	
		if all(phiP[k]==0 for k in range(len(phiP))):	
			print "phiP:",[var('v'+str(k)) if k in P else 0 for k in range(len(phiP))],' for all vi>0     P:',P,'  ','symplectic Calabi-Yau'
		elif [sgn(phiP[k]) for k in range(len(phiP))]==[-1 if k in P else 0 for k in range(len(phiP))]:	
			print "phiP:",-phiP/(gcd(phiP))	,'   ','P:',P,'   ','symplectic general type'
		elif [sgn(phiP[k]) for k in range(len(phiP))]==[1 if k in P else 0 for k in range(len(phiP))]:	
			print "phiP:",phiP/(gcd(phiP))	,'   ','P:',P,'   ','symplectic Fano'

