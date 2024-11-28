import numpy as np

EPS = 1e-12

def deltaKMeansDel(
      freq : int,
      meanSquareDiff : float
   ):
   return (freq / (freq - 1)) * meanSquareDiff

def deltaKMeansAdd(
      freq : int,
      meanSquareDiff : float
   ):
   return (freq / (freq + 1)) * meanSquareDiff


def deltaPoissonDn(
      nDel,
      freqAdd,
      freqDel,
      mu
   ):
   x = (nDel * freqDel) / (mu * (freqAdd + 1)) + EPS
   return np.log(x)


def deltaPoissonUp(
      nDel,
      freqAdd,
      freqDel,
      mu
   ):
   x = (mu * freqDel) / ((nDel + 1) * (freqAdd + 1)) + EPS
   return np.log(x)


def meanSquare(x):
   return np.dot(x,x) / x.shape[0]


def newMeanTraceDel(
      freq,
      oldMeanTrace,
      transferTrace
   ):

   return (freq * oldMeanTrace - transferTrace) / (freq - 1)


def newMeanTraceAdd(
      freq,
      oldMeanTrace,
      transferTrace
   ):

   return (freq * oldMeanTrace + transferTrace) / (freq + 1)
