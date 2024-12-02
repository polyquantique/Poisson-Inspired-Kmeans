import numpy as np


def getIClustOfObs(
   iObsOfClust : np.array,
   nObs : int
):
   
   nClust = len(iObsOfClust) 
   iClustOfObs = 

   Do[iClustOfObs[iObsOfClust[iClust]] = iClust, {iClust, nClust}]

   for iClust in range(nClust):
        for obs in iObsOfClust[iClust]:
            iClustOfObs[obs] = iClust

