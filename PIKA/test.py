import numpy as np

from .utils import *

def test_deltaKMeans():

   freqAddA = 9
   freqDelA = 14
   meanTraceAdd = np.array([1.1, 2.9, 8.9, 9.0, 6.1, 4.3])
   meanTraceDel = np.array([0.9, 1.7, 4.0, 8.8, 5.2, 3.3])
   transferTrace = np.array([1.2, 3.1, 8.9, 9.5, 8.1, 5.2])

   out1 = deltaKMeansAdd(
      freq = freqAddA,
      meanSquareDiff = meanSquare(meanTraceAdd - transferTrace)
   )

   out2 = deltaKMeansDel(
      freq = freqDelA,
      meanSquareDiff = meanSquare(meanTraceDel - transferTrace)
   )

   output = out1 - out2

   assert np.isclose(
      a = output, 
      b = -6.15632, 
      rtol = 1e-5)
   

def test_newMeanTraceAdd():

   freqAddA = 9
   freqDelA = 14
   meanTraceAdd = np.array([1.1, 2.9, 8.9, 9.0, 6.1, 4.3])
   meanTraceDel = np.array([0.9, 1.7, 4.0, 8.8, 5.2, 3.3])
   transferTrace = np.array([1.2, 3.1, 8.9, 9.5, 8.1, 5.2])

   output = newMeanTraceAdd(
      freq = freqAddA,
      oldMeanTrace = meanTraceAdd,
      transferTrace = transferTrace
   )

   assert np.allclose(
      a = output, 
      b = np.array([1.11, 2.92, 8.90, 9.05, 6.3, 4.39]), 
      rtol = 1e-2)
   
def test_newMeanTraceDel():

   freqAddA = 9
   freqDelA = 14
   meanTraceAdd = np.array([1.1, 2.9, 8.9, 9.0, 6.1, 4.3])
   meanTraceDel = np.array([0.9, 1.7, 4.0, 8.8, 5.2, 3.3])
   transferTrace = np.array([1.2, 3.1, 8.9, 9.5, 8.1, 5.2])

   output = newMeanTraceDel(
      freq = freqDelA,
      oldMeanTrace = meanTraceDel,
      transferTrace = transferTrace
   )

   assert np.allclose(
      a = output, 
      b = np.array([0.876923, 1.59231, 3.62308, 8.74615, 4.97692, 3.15385]), 
      rtol = 1e-5)



def test_delatPoissonUp():

   output = deltaPoissonUp(
      mu = 4.4,
      nDel = 2,
      freqAdd = 7,
      freqDel = 5
   )

   assert np.isclose(
      a = output, 
      b = -0.0870114, 
      rtol = 1e-6)