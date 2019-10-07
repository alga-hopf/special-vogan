'''
   This script allows to choose proportion for training and test.

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
import random
import os, math
proportion=float(input("Choose percentage of training: "))
print(type(proportion))
finalData=np.load(os.path.expanduser('~/special-vogan/deep-learning/data/finalData.npy'))
specialityIndex=np.load(os.path.expanduser('~/special-vogan/deep-learning/data/specialityIndex.npy'))
trainTest=random.sample(range(1, len(finalData)), int(math.ceil(len(finalData)*proportion/100)))
trainData=[]
testData=[]
trainLabels=[]
testLabels=[]
for i in range(len(finalData)):
	if i in trainTest:
		testData.append(finalData[i])
		testLabels.append(specialityIndex[i])
	else:
		trainData.append(finalData[i])
		trainLabels.append(specialityIndex[i])
np.save(os.path.expanduser('~/special-vogan/deep-learning/data/dataProportion/trainOrbits'),trainData)
np.save(os.path.expanduser('~/special-vogan/deep-learning/data/dataProportion/trainLabels'),trainLabels)
np.save(os.path.expanduser('~/special-vogan/deep-learning/data/dataProportion/testOrbits'),testData)
np.save(os.path.expanduser('~/special-vogan/deep-learning/data/dataProportion/testLabels'),testLabels)

