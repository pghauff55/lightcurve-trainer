import os.path
import numpy as np
from astropy.io import fits
from astropy.table import Table 
from scipy.signal import argrelextrema
import sys
import time
import statistics
from statistics import mode, StatisticsError

def calc_period(flux):
             ##################################### PERIOD CALCULATION #########################################
            #use adaptive smoothing to find optimal maxima for period calculation
            use_maxima=True #False untested
            #print('Calculating Period...')
            Smooth_factor=20
         
            N_list=[]
            Index0_list=[]
            Index1_list=[]
            N_fluxmax=len(flux)
            if(N_fluxmax>1000): # cut short due to errors with np.max
                 N_fluxmax=1000
            #to avoid local maxima choose maxima with flux above %90 maximum
            fluxmax=0.95*np.max(flux[range(N_fluxmax)])
            fluxmin=0.95*np.min(flux[range(N_fluxmax)])
            #print('Flux Maximum:  '+repr(fluxmax)+' Flux Minimum:  '+repr(fluxmin))
            while Smooth_factor<60:
                test_flux=np.convolve(flux,np.ones(Smooth_factor)/Smooth_factor,mode='same')
                maxima=argrelextrema(test_flux,np.greater)
                minima=argrelextrema(test_flux,np.less)
                maxima=maxima[0]
                minima=minima[0]
                temp_maxima=[]
                for maxima_index in maxima:
                    if(flux[maxima_index]>fluxmax):
                        temp_maxima.append(maxima_index)
                maxima=temp_maxima
                temp_minima=[]
                for minima_index in maxima:
                    if(flux[minima_index]<fluxmin):
                        temp_minima.append(minima_index)
                minima=temp_minima
                #print(maxima)
                i=1
                N=0
                while N<1000: #period cutoff 
                    if use_maxima:
                        if(i+1>len(maxima)):
                            break
                        N=maxima[i]-maxima[i-1]
                    else:
                        if(i+1>len(minima)):
                            break
                        N=minima[i]-minima[i-1]
                    i=i+1
                i=i-1
                if(N>10): # use values that represent a proper period
                    N_list.append(N)
                    if use_maxima:
                        Index0_list.append(maxima[i])
                        Index1_list.append(maxima[i-1])
                    else:
                        Index0_list.append(minima[i])
                        Index1_list.append(minima[i-1])
                        
                #print(N)
                Smooth_factor=Smooth_factor+1
                
            
            #choose most frequent from (N_list)
            try:
                 N=mode(N_list)
            except StatisticsError:
                 #print ("No unique mode found")
                 return -1
                  
            
            #print('N:'+repr(N))
            
            #search N_list for index of N
            i=0
            for j in range(len(N_list)):
                if(N_list[j]==N):
                    i=j
                    break
            index0=Index0_list[i]
            index1=Index1_list[i]
            return N
            #####################################################################################################

def commandlinearguments():
     if __name__ == "__main__":
          print(f"Arguments count: {len(sys.argv)}")
          for i, arg in enumerate(sys.argv):
               print(f"Argument {i:>6}: {arg}")
     return sys.argv



argv=commandlinearguments()
Smooth_factor=20
if(len(argv)==2):
    Smooth_factor=int(argv[1])

counter_id=757000
while True:
     filename = "kplr{:09d}-2009131105131_llc.fits".format(counter_id)
     if(os.path.isfile(filename)):
         #
         with fits.open(filename, mode="readonly") as hdulist:
             # Read in the "BJDREF" which is the time offset of the time array.
             bjdrefi = hdulist[1].header['BJDREFI'] 
             bjdreff = hdulist[1].header['BJDREFF']

             # Read in the columns of data.
             times = hdulist[1].data['time'] 
             sap_fluxes = hdulist[1].data['SAP_FLUX']
             pdcsap_fluxes = hdulist[1].data['PDCSAP_FLUX']

    

         N=len(sap_fluxes)
         t=np.linspace(0,times[N-1]-times[0],N)
     
         array_input=np.array(sap_fluxes)
         array_input = array_input[~np.isnan(array_input)]
         array_input=np.convolve(array_input,np.ones(Smooth_factor)/Smooth_factor,mode='same')
         max_array=np.max(array_input)
         min_array=np.min(array_input)
         amplitude=max_array-min_array
         
         #print("Max:"+format(max_array,".2f")+"Min:"+format(min_array,".2f"))
         offset=(max_array+min_array)/(2*(amplitude))
         array_input=array_input/amplitude-offset
         first_derivative=np.gradient(array_input)
         maxima=argrelextrema(array_input,np.greater)
         minima=argrelextrema(array_input,np.less)
         maxima0=argrelextrema(first_derivative,np.greater)
         minima0=argrelextrema(first_derivative,np.less)
         features=2*len(maxima[0])+2*len(minima[0])+len(maxima0[0])+len(minima0[0])
         Nperiod=calc_period(array_input)
        
         print("Period ratio %: "+repr(N/Nperiod)+" features:"+repr(Nperiod*features/N))
         #fits.info(filename)
          #     break
         #fits.close()
         if(features>100):
             os.remove(filename)
         if(Nperiod==-1):
             os.remove(filename)
     counter_id+=1
     #print(counter_id)


