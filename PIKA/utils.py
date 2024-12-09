import numpy as np
import zipfile
import polars as pl
import matplotlib.pyplot as plt
from typing import Union

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
   x = (nDel * freqDel) / (mu * (freqAdd + 1))
   return np.log(x)


def deltaPoissonUp(
      nDel,
      freqAdd,
      freqDel,
      mu
   ):
   x = (mu * freqDel) / ((nDel + 1) * (freqAdd + 1))
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


def dataset_csv(
        path_data : str, 
        files : Union[list,None] = None,
        plot_traces : bool = False,
        SKIP : int = 1
    ):

    archive = zipfile.ZipFile(path_data, 'r')

    if files is None:
        files = archive.namelist()
    else:
        pass

    files = sorted(files)
    
    data = []
    for file_ in files:

        if len(file_) > 15:
            data_ =  pl.read_csv(
               archive.read(file_), 
               has_header = False, 
               separator = ","
            ).to_numpy().astype(dtype=np.float16)
            
            data.append((data_[:,::3] - data_[:,:10].mean())[::SKIP])

        else:
            pass

    data = np.concatenate(data, axis=0)
    data_train = data[::2]
    data_test = data[1::2]

    if plot_traces:
        with plt.style.context("seaborn-v0_8"):
            plt.figure(figsize=(10,4), dpi=100)
            plt.plot(data_train[::10].T,
                     alpha = 0.05,
                     linewidth = 1)
            plt.plot(data_test[::10].T,
                     alpha = 0.05,
                     linewidth = 1)
            plt.xlabel('Time (a.u.)')
            plt.ylabel('Voltage (a.u.)')
            plt.show()

    return data_train, data_test