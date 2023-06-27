






# neuralnetwork-lightcurve-param-estimator

P. Hauff
Version 1.0

<div align="center">
    <img src="Screenshot 2023-06-28 085458.png" width="1200px"</img> 
</div>

<div align="center">
    <img src="Screenshot 2023-06-28 085727.png" width="1200px"</img> 
</div>
<div align="center">
    <img src="Screenshot 2023-06-28 085631.png" width="1200px"</img> 
</div>





# Namespace Index

## Namespace List

Here is a list of all namespaces with brief descriptions:

kepler-feature-counter  

lightcurve-parameter-estimator  

lightcurve-trainer  

lightcurve-trainer-start  



 

# Hierarchical Index

## Class Hierarchy

This inheritance list is sorted roughly, but not completely, alphabetically:

lightcurve-parameter-estimator.EllipseEquation

lightcurve-parameter-estimator.EllipticalDifferenceEquation



 

# Class Index

Class List

Here are the classes, structs, unions and interfaces with brief descriptions:

lightcurve-parameter-estimator.EllipseEquation  

lightcurve-parameter-estimator.EllipticalDifferenceEquation  



 

# File Index

File List

Here is a list of all files with brief descriptions:

kepler-feature-counter.py  

lightcurve-parameter-estimator.py  

lightcurve-trainer-start.py  

lightcurve-trainer.py  



 

# Namespace Documentation

kepler-feature-counter Namespace Reference

## Functions

•	calc_period (flux)

•	commandlinearguments ()

# Variables

•	argv = commandlinearguments()

•	int Smooth_factor = 20

•	int counter_id = 757000

•	str filename = "kplr{:09d}-2009131105131_llc.fits".format(counter_id)

•	mode

•	bjdrefi = hdulist[1].header['BJDREFI']

•	bjdreff = hdulist[1].header['BJDREFF']

•	times = hdulist[1].data['time']

•	sap_fluxes = hdulist[1].data['SAP_FLUX']

•	pdcsap_fluxes = hdulist[1].data['PDCSAP_FLUX']

•	N = len(sap_fluxes)

•	t = np.linspace(0,times[N-1]-times[0],N)

•	array_input = np.array(sap_fluxes)

•	max_array = np.max(array_input)

•	min_array = np.min(array_input)

•	amplitude = max_array-min_array

•	tuple offset = (max_array+min_array)/(2*(amplitude))

•	first_derivative = np.gradient(array_input)

•	maxima = argrelextrema(array_input,np.greater)

•	minima = argrelextrema(array_input,np.less)

•	maxima0 = argrelextrema(first_derivative,np.greater)

•	minima0 = argrelextrema(first_derivative,np.less)

•	int features = 2*len(maxima[0])+2*len(minima[0])+len(maxima0[0])+len(minima0[0])

•	Nperiod = calc_period(array_input)




 

 
 
