import matplotlib.pyplot as plt
import numpy as np
from typing import Union


def defaultPlot(
   config : dict,
   title : str,
   yInput : np.array,
   xInput : Union[np.array, None] = None,
   ylabel : str = 'Voltage (a.u.)',
   xlabel : str = 'Time (a.u.)',
):
      
   with plt.style.context(config['styleName']):
      plt.figure(figsize = config['outputImageSize'], dpi=config['dpi'])
      if xInput is None:
          plt.plot(yInput, alpha=0.8)
      else:
         plt.plot(xInput, yInput, alpha=0.8)
      plt.ylabel(ylabel)
      plt.xlabel(xlabel)
      plt.title(title)
      plt.tight_layout()
      plt.show()


def defaultHist(
   config : dict,
   title : str,
   input_ : np.array,
   ylabel : str = 'Voltage (a.u.)',
   xlabel : str = 'Time (a.u.)',
):
      
   with plt.style.context(config['styleName']):
      plt.figure(figsize = config['outputImageSize'], dpi=config['dpi'])
      plt.hist(input_, alpha=0.8, bins=config['binFract'])
      plt.ylabel(ylabel)
      plt.xlabel(xlabel)
      plt.title(title)
      plt.tight_layout()
      plt.show()


def graphMeanTraceFtn(
   config : dict,
   meanTrace_ : np.array
):
   
   defaultPlot(
      config = config,
      title = 'Mean trace of first cluster',
      yInput = meanTrace_,
      xInput  = None
   )

   
def graphFindDotProductEffectivePhotonNumbers(
   config : dict,
   nPhotonEff : np.array
):
   
   defaultHist(
      config = config,
      title = '`findDotProductEffectivePhotonNumbers`',
      input_ = nPhotonEff,
      xlabel = 'n_eff',
      ylabel = 'Count'
   )


def graphCreateInitialClusters(
   config : dict,
   clustMeanTrace : np.array
):
   
   defaultPlot(
      config = config,
      title = '`createInitialClust`',
      yInput = clustMeanTrace.T,
      xInput = None
   )


def graphClusterDeviationFromMean(
   config : dict,
   sqDevOfClust : np.array,
   nPhotonOfClust : np.array
):

   defaultPlot(
      config = config,
      title = '`findInitialObjectiveFunction`',
      yInput = sqDevOfClust,
      xInput = nPhotonOfClust,
      ylabel = 'RMS deviation (Voltage input units)',
      xlabel = 'Number of photons n'
   )











def graphFinal(
   config : dict,
   objFtn : np.array,
   clustMeanTrace : np.array
):
   
   defaultPlot(
      config = config,
      title = '`Final`',
      yInput =  objFtn,
      ylabel = 'Objective Function',
      xlabel = 'Iteration'
   )

   defaultPlot(
      config = config,
      title = '`Final`',
      yInput = clustMeanTrace.T,
   )