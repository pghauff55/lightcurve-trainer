# lightcurve-trainer
A tensorflow neural network Lightcurve parameter estimator.

Lightcurve-parameter-estimator


P. Hauff
Version 1.0
Table of Contents

Table of contents



Namespace Index
Namespace List
Here is a list of all namespaces with brief descriptions:
3dsphere  	pagenum
3dsphere2  	pagenum
animation  	pagenum
get-pip  	pagenum
image-cap  	pagenum
kepler-feature-counter  	pagenum
lightcurve-parameter-estimator  	pagenum
lightcurve-trainer  	pagenum
lightcurve-trainer-start  	pagenum
mouseclient  	pagenum
pygame-sphere  	pagenum
sphere3  	pagenum


Hierarchical Index
Class Hierarchy
This inheritance list is sorted roughly, but not completely, alphabetically:
lightcurve-parameter-estimator.EllipseEquation	pagenum
lightcurve-parameter-estimator.EllipticalDifferenceEquation	pagenum

sphere3.Sphere	pagenum

Class Index
Class List
Here are the classes, structs, unions and interfaces with brief descriptions:
lightcurve-parameter-estimator.EllipseEquation  	pagenum
lightcurve-parameter-estimator.EllipticalDifferenceEquation  	pagenum
sphere3.Sphere  	pagenum


File Index
File List
Here is a list of all files with brief descriptions:
3dsphere.py  	pagenum
3dsphere2.py  	pagenum
animation.py  	pagenum
get-pip.py  	pagenum
image-cap.py  	pagenum
image_cap.cpp  	pagenum
kepler-feature-counter.py  	pagenum
lightcurve-parameter-estimator.py  	pagenum
lightcurve-trainer-start.py  	pagenum
lightcurve-trainer.py  	pagenum
mouseclient.py  	pagenum
pygame-sphere.py  	pagenum
sphere3.py  	pagenum


Namespace Documentation
3dsphere Namespace Reference
AAAAAAAAAOAAAAAAAAAOVariables
0)	tuple display = (400, 300)
1)	tuple screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
2)	sphere = gluNewQuadric()
3)	viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
4)	bool run = True
5)	int counter_light = 0
6)	keypress = pygame.key.get_pressed()
7)	int theta = math.pi*counter_light/100

Variable Documentation
int 3dsphere.counter_light = 0
AAAAAAAAAPAAAAAAAAAPtuple 3dsphere.display = (400, 300)
AAAAAAAAAQAAAAAAAAAQ3dsphere.keypress = pygame.key.get_pressed()
AAAAAAAAARAAAAAAAAARbool 3dsphere.run = True
AAAAAAAAASAAAAAAAAAStuple 3dsphere.screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
AAAAAAAAATAAAAAAAAAT3dsphere.sphere = gluNewQuadric()
AAAAAAAAAUAAAAAAAAAUint 3dsphere.theta = math.pi*counter_light/100
AAAAAAAAAVAAAAAAAAAV3dsphere.viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
AAAAAAAAAWAAAAAAAAAW

3dsphere2 Namespace Reference
AAAAAAAAAXAAAAAAAAAXFunctions
0)	read_texture (filename)
1)	main ()

Function Documentation
3dsphere2.main ()
AAAAAAAAAYAAAAAAAAAYHere is the call graph for this function:
IMAGE
Here is the caller graph for this function:
IMAGE
3dsphere2.read_texture (  filename)
AAAAAAAAAZAAAAAAAAAZ
Reads an image file and converts to a OpenGL-readable textID format
 
Here is the caller graph for this function:
IMAGE


animation Namespace Reference
AAAAAAAABAAAAAAAAABAVariables
0)	tuple black = (0,0,0)
1)	tuple red = (255,0,0)
2)	tuple green = (0,255,0)
3)	tuple blue = (0,0,255)
4)	tuple white = (255,255,255)
5)	bool run_me = True
6)	int screen_size = 1080, 720
7)	screen = pygame.display.set_mode(screen_size)
8)	clock = pygame.time.Clock()
9)	int fps_limit = 60
10)	tuple colorcircle = (red)
11)	tuple colorcircle2 = (blue)
12)	int posx = 1080/2
13)	int posy = 720/2
14)	circle = pygame.draw.circle(screen, colorcircle, (posx, posy), 50)
15)	int r = posx*0.5
16)	int theta = 40/180*math.pi
17)	int time1 = 0
18)	int time2 = 0
19)	int angular_vel1 = 30/180*math.pi
20)	int angular_vel2 = 43/180*math.pi
21)	int angle2 = 40/180*math.pi
22)	float phi = 30.2/180*math.pi
23)	float delta_t = 0.9
24)	float delta_t1 = delta_t
25)	float delta_t2 = delta_t
26)	int counter = 0
27)	int dcounter = 1
28)	int x1 = -r*math.sin(angle2)*math.cos(angular_vel1*time1)
29)	int y1 = r*math.sin(angle2)*math.sin(angular_vel1*time1)
30)	int x2 = r*math.sin(angle2)*math.cos(angular_vel2*time2+phi)
31)	int y2 = r*math.sin(angle2)*math.sin(angular_vel2*time2+phi)
32)	width
33)	tuple distsquared = (x2-x1)*(x2-x1)
34)	dist = math.sqrt(distsquared)

Variable Documentation
int animation.angle2 = 40/180*math.pi
AAAAAAAABBAAAAAAAABBint animation.angular_vel1 = 30/180*math.pi
AAAAAAAABCAAAAAAAABCint animation.angular_vel2 = 43/180*math.pi
AAAAAAAABDAAAAAAAABDtuple animation.black = (0,0,0)
AAAAAAAABEAAAAAAAABEtuple animation.blue = (0,0,255)
AAAAAAAABFAAAAAAAABFanimation.circle = pygame.draw.circle(screen, colorcircle, (posx, posy), 50)
AAAAAAAABGAAAAAAAABGanimation.clock = pygame.time.Clock()
AAAAAAAABHAAAAAAAABHtuple animation.colorcircle = (red)
AAAAAAAABIAAAAAAAABItuple animation.colorcircle2 = (blue)
AAAAAAAABJAAAAAAAABJint animation.counter = 0
AAAAAAAABKAAAAAAAABKint animation.dcounter = 1
AAAAAAAABLAAAAAAAABLfloat animation.delta_t = 0.9
AAAAAAAABMAAAAAAAABMfloat animation.delta_t1 = delta_t
AAAAAAAABNAAAAAAAABNfloat animation.delta_t2 = delta_t
AAAAAAAABOAAAAAAAABOanimation.dist = math.sqrt(distsquared)
AAAAAAAABPAAAAAAAABPtuple animation.distsquared = (x2-x1)*(x2-x1)
AAAAAAAABQAAAAAAAABQint animation.fps_limit = 60
AAAAAAAABRAAAAAAAABRtuple animation.green = (0,255,0)
AAAAAAAABSAAAAAAAABSfloat animation.phi = 30.2/180*math.pi
AAAAAAAABTAAAAAAAABTint animation.posx = 1080/2
AAAAAAAABUAAAAAAAABUint animation.posy = 720/2
AAAAAAAABVAAAAAAAABVanimation.r = posx*0.5
AAAAAAAABWAAAAAAAABWtuple animation.red = (255,0,0)
AAAAAAAABXAAAAAAAABXbool animation.run_me = True
AAAAAAAABYAAAAAAAABYanimation.screen = pygame.display.set_mode(screen_size)
AAAAAAAABZAAAAAAAABZint animation.screen_size = 1080, 720
AAAAAAAACAAAAAAAAACAint animation.theta = 40/180*math.pi
AAAAAAAACBAAAAAAAACBint animation.time1 = 0
AAAAAAAACCAAAAAAAACCint animation.time2 = 0
AAAAAAAACDAAAAAAAACDtuple animation.white = (255,255,255)
AAAAAAAACEAAAAAAAACEanimation.width
AAAAAAAACFAAAAAAAACFint animation.x1 = -r*math.sin(angle2)*math.cos(angular_vel1*time1)
AAAAAAAACGAAAAAAAACGint animation.x2 = r*math.sin(angle2)*math.cos(angular_vel2*time2+phi)
AAAAAAAACHAAAAAAAACHint animation.y1 = r*math.sin(angle2)*math.sin(angular_vel1*time1)
AAAAAAAACIAAAAAAAACIint animation.y2 = r*math.sin(angle2)*math.sin(angular_vel2*time2+phi)
AAAAAAAACJAAAAAAAACJ

get-pip Namespace Reference
AAAAAAAACKAAAAAAAACKFunctions
0)	include_setuptools (args)
1)	include_wheel (args)
2)	determine_pip_install_arguments ()
3)	monkeypatch_for_cert (tmpdir)
4)	bootstrap (tmpdir)
5)	main ()
Variables
0)	this_python = sys.version_info[:2]
1)	tuple min_version = (3, 7)
2)	list message_parts
3)	str DATA

Function Documentation
get-pip.bootstrap (  tmpdir)
AAAAAAAACLAAAAAAAACLHere is the call graph for this function:
IMAGE
Here is the caller graph for this function:
IMAGE
get-pip.determine_pip_install_arguments ()
AAAAAAAACMAAAAAAAACMHere is the call graph for this function:
IMAGE
Here is the caller graph for this function:
IMAGE
get-pip.include_setuptools (  args)
AAAAAAAACNAAAAAAAACN
Install setuptools only if absent and not excluded.
 
Here is the caller graph for this function:
IMAGE
get-pip.include_wheel (  args)
AAAAAAAACOAAAAAAAACO
Install wheel only if absent and not excluded.
 
Here is the caller graph for this function:
IMAGE
get-pip.main ()
AAAAAAAACPAAAAAAAACPHere is the call graph for this function:
IMAGE
get-pip.monkeypatch_for_cert (  tmpdir)
AAAAAAAACQAAAAAAAACQ
Patches `pip install` to provide default certificate with the lowest priority.

This ensures that the bundled certificates are used unless the user specifies a
custom cert via any of pip's option passing mechanisms (config, env-var, CLI).

A monkeypatch is the easiest way to achieve this, without messing too much with
the rest of pip's internals.
 
Here is the caller graph for this function:
IMAGE

Variable Documentation
str get-pip.DATA
AAAAAAAACRAAAAAAAACRlist get-pip.message_parts
AAAAAAAACSAAAAAAAACSInitial value:1 =  [
2         "This script does not work on Python {}.{}".format(*this_python),
3         "The minimum supported Python version is {}.{}.".format(*min_version),
4         "Please use https://bootstrap.pypa.io/pip/{}.{}/get-pip.py instead.".format(*this_python),
5     ]
tuple get-pip.min_version = (3, 7)
AAAAAAAACTAAAAAAAACTget-pip.this_python = sys.version_info[:2]
AAAAAAAACUAAAAAAAACU

image-cap Namespace Reference
AAAAAAAACVAAAAAAAACVVariables
0)	int cams_test = 10
1)	cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
2)	test = cap.isOpened()
3)	cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
4)	ret
5)	frame = cv2.GaussianBlur(frame,(35,35),0)
6)	frame_still = cv2.GaussianBlur(frame_still,(35,35),0)
7)	int img_counter = 0
8)	bins = np.array([0,51,102,153,204,255])
9)	right
10)	greyscale2 = cv2.cvtColor(frame_still, cv2.COLOR_BGR2GRAY)
11)	int Thresh = 100
12)	greyscale1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
13)	background
14)	k = cv2.waitKey(1)

Variable Documentation
image-cap.background
AAAAAAAACWAAAAAAAACWimage-cap.bins = np.array([0,51,102,153,204,255])
AAAAAAAACXAAAAAAAACXimage-cap.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
AAAAAAAACYAAAAAAAACYint image-cap.cams_test = 10
AAAAAAAACZAAAAAAAACZimage-cap.cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
AAAAAAAADAAAAAAAAADAimage-cap.frame = cv2.GaussianBlur(frame,(35,35),0)
AAAAAAAADBAAAAAAAADBimage-cap.frame_still = cv2.GaussianBlur(frame_still,(35,35),0)
AAAAAAAADCAAAAAAAADCimage-cap.greyscale1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
AAAAAAAADDAAAAAAAADDimage-cap.greyscale2 = cv2.cvtColor(frame_still, cv2.COLOR_BGR2GRAY)
AAAAAAAADEAAAAAAAADEint image-cap.img_counter = 0
AAAAAAAADFAAAAAAAADFimage-cap.k = cv2.waitKey(1)
AAAAAAAADGAAAAAAAADGimage-cap.ret
AAAAAAAADHAAAAAAAADHimage-cap.right
AAAAAAAADIAAAAAAAADIimage-cap.test = cap.isOpened()
AAAAAAAADJAAAAAAAADJint image-cap.Thresh = 100
AAAAAAAADKAAAAAAAADK

kepler-feature-counter Namespace Reference
AAAAAAAADLAAAAAAAADLFunctions
0)	calc_period (flux)
1)	commandlinearguments ()
Variables
0)	argv = commandlinearguments()
1)	int Smooth_factor = 20
2)	int counter_id = 757000
3)	str filename = "kplr{:09d}-2009131105131_llc.fits".format(counter_id)
4)	mode
5)	bjdrefi = hdulist[1].header['BJDREFI']
6)	bjdreff = hdulist[1].header['BJDREFF']
7)	times = hdulist[1].data['time']
8)	sap_fluxes = hdulist[1].data['SAP_FLUX']
9)	pdcsap_fluxes = hdulist[1].data['PDCSAP_FLUX']
10)	N = len(sap_fluxes)
11)	t = np.linspace(0,times[N-1]-times[0],N)
12)	array_input = np.array(sap_fluxes)
13)	max_array = np.max(array_input)
14)	min_array = np.min(array_input)
15)	amplitude = max_array-min_array
16)	tuple offset = (max_array+min_array)/(2*(amplitude))
17)	first_derivative = np.gradient(array_input)
18)	maxima = argrelextrema(array_input,np.greater)
19)	minima = argrelextrema(array_input,np.less)
20)	maxima0 = argrelextrema(first_derivative,np.greater)
21)	minima0 = argrelextrema(first_derivative,np.less)
22)	int features = 2*len(maxima[0])+2*len(minima[0])+len(maxima0[0])+len(minima0[0])
23)	Nperiod = calc_period(array_input)

Function Documentation
kepler-feature-counter.calc_period (  flux)
AAAAAAAADMAAAAAAAADMkepler-feature-counter.commandlinearguments ()
AAAAAAAADNAAAAAAAADN
Variable Documentation
kepler-feature-counter.amplitude = max_array-min_array
AAAAAAAADOAAAAAAAADOkepler-feature-counter.argv = commandlinearguments()
AAAAAAAADPAAAAAAAADPtuple kepler-feature-counter.array_input = np.array(sap_fluxes)
AAAAAAAADQAAAAAAAADQkepler-feature-counter.bjdreff = hdulist[1].header['BJDREFF']
AAAAAAAADRAAAAAAAADRkepler-feature-counter.bjdrefi = hdulist[1].header['BJDREFI']
AAAAAAAADSAAAAAAAADSint kepler-feature-counter.counter_id = 757000
AAAAAAAADTAAAAAAAADTint kepler-feature-counter.features = 2*len(maxima[0])+2*len(minima[0])+len(maxima0[0])+len(minima0[0])
AAAAAAAADUAAAAAAAADUkepler-feature-counter.filename = "kplr{:09d}-2009131105131_llc.fits".format(counter_id)
AAAAAAAADVAAAAAAAADVkepler-feature-counter.first_derivative = np.gradient(array_input)
AAAAAAAADWAAAAAAAADWkepler-feature-counter.max_array = np.max(array_input)
AAAAAAAADXAAAAAAAADXkepler-feature-counter.maxima = argrelextrema(array_input,np.greater)
AAAAAAAADYAAAAAAAADYkepler-feature-counter.maxima0 = argrelextrema(first_derivative,np.greater)
AAAAAAAADZAAAAAAAADZkepler-feature-counter.min_array = np.min(array_input)
AAAAAAAAEAAAAAAAAAEAkepler-feature-counter.minima = argrelextrema(array_input,np.less)
AAAAAAAAEBAAAAAAAAEBkepler-feature-counter.minima0 = argrelextrema(first_derivative,np.less)
AAAAAAAAECAAAAAAAAECkepler-feature-counter.mode
AAAAAAAAEDAAAAAAAAEDkepler-feature-counter.N = len(sap_fluxes)
AAAAAAAAEEAAAAAAAAEEkepler-feature-counter.Nperiod = calc_period(array_input)
AAAAAAAAEFAAAAAAAAEFtuple kepler-feature-counter.offset = (max_array+min_array)/(2*(amplitude))
AAAAAAAAEGAAAAAAAAEGkepler-feature-counter.pdcsap_fluxes = hdulist[1].data['PDCSAP_FLUX']
AAAAAAAAEHAAAAAAAAEHkepler-feature-counter.sap_fluxes = hdulist[1].data['SAP_FLUX']
AAAAAAAAEIAAAAAAAAEIkepler-feature-counter.Smooth_factor = 20
AAAAAAAAEJAAAAAAAAEJkepler-feature-counter.t = np.linspace(0,times[N-1]-times[0],N)
AAAAAAAAEKAAAAAAAAEKkepler-feature-counter.times = hdulist[1].data['time']
AAAAAAAAELAAAAAAAAEL

lightcurve-parameter-estimator Namespace Reference
AAAAAAAAEMAAAAAAAAEMClasses
0)	class EllipseEquationclass EllipticalDifferenceEquation
Functions
0)	extend_signal (signal, K)
1)	signal_weight (signal)
2)	shuffle (inputs_train, labels_train, N_counter)
Variables
0)	tuple rel_flux = (0.516874,0.514718,0.513875,0.51701,0.515947,0.516506,0.514698,0.514998,0.51023,0.507271,0.509727,0.511362,0.506488,0.508958,0.507097,0.506385,0.502653,0.508093,0.503255,0.504292,0.506062,0.501479,0.504612,0.503892,0.509819,0.502666,0.50247,0.506035,0.506205,0.504486,0.505797,0.506178,0.510974,0.508446,0.508027,0.506151,0.514618,0.516266,0.517662,0.522371,0.524497,0.526994,0.530796,0.536497,0.544171,0.549154,0.551763,0.55893,0.570134,0.575073,0.583214,0.596239,0.603371,0.61613,0.627472,0.644398,0.652329,0.671484,0.691639,0.702505,0.723772,0.743772,0.760631,0.775118,0.785617,0.79526,0.803752,0.794038,0.786258,0.78557,0.777623,0.774241,0.769259,0.762497,0.757905,0.751677,0.742528,0.74069,0.733236,0.728572,0.724491,0.719929,0.713713,0.709665,0.703484,0.701474,0.692684,0.690999,0.684574,0.677643,0.675762,0.670914,0.665341,0.662756,0.656312,0.654239,0.64872,0.647028,0.644872,0.640277,0.636528,0.632404,0.626704,0.622936,0.623371,0.618118,0.616468,0.609824,0.606578,0.603021,0.602043,0.598819,0.595745,0.591926,0.592143,0.587627,0.586611,0.580896,0.579149,0.57916,0.575455,0.572138,0.571212,0.569107,0.567314,0.56236,0.559392,0.560168,0.555153,0.559972,0.554559,0.554885,0.551798,0.551857,0.546404,0.546068,0.546875,0.542806,0.540206,0.539358,0.5379,0.53581,0.534171,0.532926,0.530805,0.526911,0.528021,0.525736,0.521182,0.523219,0.519413,0.518268,0.519494,0.517206,0.516313,0.515425,0.514182,0.513064,0.512183,0.512074,0.509471,0.510413,0.511378,0.508993,0.508499,0.509499,0.507778,0.506582,0.507644,0.506492,0.508728,0.506722,0.508668,0.511519,0.510983,0.50951,0.511776,0.513629,0.515124,0.51429,0.518482,0.519538,0.522113,0.524569,0.529436,0.532123,0.536144,0.537676,0.545072,0.551342,0.557408,0.562603,0.568011,0.579297,0.586273,0.595202,0.60494,0.617419,0.625935,0.638816,0.656777,0.668723,0.684399,0.702941,0.721203,0.740341,0.757633,0.774475,0.788345,0.801681,0.8066,0.813014,0.816262,0.821714,0.821885,0.823638,0.818231,0.817136,0.812044,0.811869,0.809314,0.802038,0.797923,0.791057,0.7838,0.782822,0.775374,0.771899,0.762528,0.759973,0.754587,0.747702,0.742875,0.73873,0.73184,0.726124,0.721643,0.715755,0.71217,0.706259,0.701883,0.69765,0.692345,0.688974,0.683167,0.678736)
1)	tuple time_base = (0,0.000569,0.00114,0.001709,0.002279,0.002849,0.003418,0.003989,0.004559,0.005128,0.005698,0.006268,0.006837,0.007407,0.007977,0.008546,0.009116,0.009686,0.010255,0.010825,0.011395,0.011964,0.012534,0.013104,0.013673,0.014242,0.014812,0.015381,0.015951,0.016521,0.01709,0.01766,0.01823,0.018799,0.019369,0.019938,0.020508,0.021077,0.021647,0.022217,0.022786,0.023356,0.023925,0.024495,0.025064,0.025634,0.026204,0.026773,0.027343,0.027912,0.028482,0.029052,0.029621,0.030191,0.03076,0.03133,0.0319,0.032469,0.033039,0.033608,0.034178,0.034747,0.035317,0.035886,0.036456,0.037026,0.037595,0.0439,0.04447,0.045039,0.045608,0.046178,0.046747,0.047317,0.047886,0.048456,0.049026,0.049595,0.050165,0.050734,0.051304,0.051873,0.052443,0.053013,0.053583,0.054152,0.054722,0.055291,0.055861,0.05643,0.057,0.057569,0.058139,0.058708,0.059278,0.059847,0.060417,0.060987,0.061556,0.062126,0.062696,0.063265,0.063835,0.064404,0.064974,0.065543,0.066113,0.066682,0.067252,0.067821,0.068391,0.068961,0.06953,0.0701,0.070669,0.071239,0.071809,0.072379,0.072949,0.073518,0.074088,0.074657,0.075227,0.075797,0.076366,0.076935,0.077505,0.078075,0.078644,0.079214,0.079783,0.080353,0.080923,0.081492,0.082062,0.082632,0.083201,0.083771,0.08434,0.08491,0.085479,0.086049,0.086618,0.087188,0.087757,0.088327,0.088897,0.089466,0.090036,0.090605,0.091175,0.091744,0.092314,0.092884,0.093453,0.094023,0.094593,0.095162,0.095732,0.096302,0.096872,0.097441,0.09801,0.09858,0.099149,0.099719,0.100289,0.101241,0.10181,0.10238,0.102949,0.103519,0.104089,0.104658,0.105228,0.105797,0.106367,0.106937,0.107506,0.108075,0.108645,0.109215,0.109784,0.110354,0.110923,0.111493,0.112062,0.112632,0.113201,0.113771,0.114341,0.11491,0.11548,0.116049,0.116619,0.117189,0.117758,0.118328,0.118897,0.119467,0.120036,0.120606,0.121176,0.121745,0.122315,0.122885,0.123454,0.124024,0.124593,0.125163,0.125732,0.126302,0.126871,0.127441,0.128011,0.12858,0.12915,0.129719,0.130289,0.130858,0.131428,0.131998,0.132567,0.133137,0.133706,0.134276,0.134845,0.135415,0.135984,0.136554,0.137124,0.137693,0.138263,0.138832,0.139402,0.139972,0.140541,0.141111,0.141681,0.14225,0.14282,0.14339,0.143959,0.144529,0.145098,0.145668)
2)	spline_data = CubicSpline(time_base,rel_flux)
3)	int O = 2000
4)	t = np.linspace(0, 0.145668, num=int(O))
5)	signal = spline_data(t)
6)	float M = 1.9891E30
7)	float e1 = 0.70
8)	float e2 = 0.30
9)	float e3 = 0.30
10)	EDE_main = EllipticalDifferenceEquation(t,signal,M,e1,e2,e3)
11)	int N = 100
12)	list inputs_train = []
13)	list labels_train = []
14)	list features_train = []
15)	int max_features = 0
16)	int l = 0
17)	int delta_step = 15
18)	int m = 0
19)	int i = 1
20)	int j = 1
21)	float dist_main = EDE_main.dist+0.5
22)	first_derivative = np.gradient(dist_main)
23)	maxima = argrelextrema(dist_main,np.greater)
24)	minima = argrelextrema(dist_main,np.less)
25)	maxima0 = argrelextrema(first_derivative,np.greater)
26)	minima0 = argrelextrema(first_derivative,np.less)
27)	int features = 2*len(maxima[0])+2*len(minima[0])+len(maxima0[0])+len(minima0[0])
28)	list labels_out = [i/N,j/N,0.1+l*0.008,0.1+m*0.008]

Function Documentation
lightcurve-parameter-estimator.extend_signal (  signal,   K)
AAAAAAAAENAAAAAAAAENHere is the caller graph for this function:
IMAGE
lightcurve-parameter-estimator.shuffle (  inputs_train,   labels_train,   N_counter)
AAAAAAAAEOAAAAAAAAEOlightcurve-parameter-estimator.signal_weight (  signal)
AAAAAAAAEPAAAAAAAAEPHere is the caller graph for this function:
IMAGE

Variable Documentation
int lightcurve-parameter-estimator.delta_step = 15
AAAAAAAAEQAAAAAAAAEQfloat lightcurve-parameter-estimator.dist_main = EDE_main.dist+0.5
AAAAAAAAERAAAAAAAAERfloat lightcurve-parameter-estimator.e1 = 0.70
AAAAAAAAESAAAAAAAAESfloat lightcurve-parameter-estimator.e2 = 0.30
AAAAAAAAETAAAAAAAAETfloat lightcurve-parameter-estimator.e3 = 0.30
AAAAAAAAEUAAAAAAAAEUlightcurve-parameter-estimator.EDE_main = EllipticalDifferenceEquation(t,signal,M,e1,e2,e3)
AAAAAAAAEVAAAAAAAAEVint lightcurve-parameter-estimator.features = 2*len(maxima[0])+2*len(minima[0])+len(maxima0[0])+len(minima0[0])
AAAAAAAAEWAAAAAAAAEWlightcurve-parameter-estimator.features_train = []
AAAAAAAAEXAAAAAAAAEXlightcurve-parameter-estimator.first_derivative = np.gradient(dist_main)
AAAAAAAAEYAAAAAAAAEYint lightcurve-parameter-estimator.i = 1
AAAAAAAAEZAAAAAAAAEZlightcurve-parameter-estimator.inputs_train = []
AAAAAAAAFAAAAAAAAAFAint lightcurve-parameter-estimator.j = 1
AAAAAAAAFBAAAAAAAAFBint lightcurve-parameter-estimator.l = 0
AAAAAAAAFCAAAAAAAAFClist lightcurve-parameter-estimator.labels_out = [i/N,j/N,0.1+l*0.008,0.1+m*0.008]
AAAAAAAAFDAAAAAAAAFDlightcurve-parameter-estimator.labels_train = []
AAAAAAAAFEAAAAAAAAFEfloat lightcurve-parameter-estimator.M = 1.9891E30
AAAAAAAAFFAAAAAAAAFFint lightcurve-parameter-estimator.m = 0
AAAAAAAAFGAAAAAAAAFGint lightcurve-parameter-estimator.max_features = 0
AAAAAAAAFHAAAAAAAAFHlightcurve-parameter-estimator.maxima = argrelextrema(dist_main,np.greater)
AAAAAAAAFIAAAAAAAAFIlightcurve-parameter-estimator.maxima0 = argrelextrema(first_derivative,np.greater)
AAAAAAAAFJAAAAAAAAFJlightcurve-parameter-estimator.minima = argrelextrema(dist_main,np.less)
AAAAAAAAFKAAAAAAAAFKlightcurve-parameter-estimator.minima0 = argrelextrema(first_derivative,np.less)
AAAAAAAAFLAAAAAAAAFLint lightcurve-parameter-estimator.N = 100
AAAAAAAAFMAAAAAAAAFMint lightcurve-parameter-estimator.O = 2000
AAAAAAAAFNAAAAAAAAFNtuple lightcurve-parameter-estimator.rel_flux = (0.516874,0.514718,0.513875,0.51701,0.515947,0.516506,0.514698,0.514998,0.51023,0.507271,0.509727,0.511362,0.506488,0.508958,0.507097,0.506385,0.502653,0.508093,0.503255,0.504292,0.506062,0.501479,0.504612,0.503892,0.509819,0.502666,0.50247,0.506035,0.506205,0.504486,0.505797,0.506178,0.510974,0.508446,0.508027,0.506151,0.514618,0.516266,0.517662,0.522371,0.524497,0.526994,0.530796,0.536497,0.544171,0.549154,0.551763,0.55893,0.570134,0.575073,0.583214,0.596239,0.603371,0.61613,0.627472,0.644398,0.652329,0.671484,0.691639,0.702505,0.723772,0.743772,0.760631,0.775118,0.785617,0.79526,0.803752,0.794038,0.786258,0.78557,0.777623,0.774241,0.769259,0.762497,0.757905,0.751677,0.742528,0.74069,0.733236,0.728572,0.724491,0.719929,0.713713,0.709665,0.703484,0.701474,0.692684,0.690999,0.684574,0.677643,0.675762,0.670914,0.665341,0.662756,0.656312,0.654239,0.64872,0.647028,0.644872,0.640277,0.636528,0.632404,0.626704,0.622936,0.623371,0.618118,0.616468,0.609824,0.606578,0.603021,0.602043,0.598819,0.595745,0.591926,0.592143,0.587627,0.586611,0.580896,0.579149,0.57916,0.575455,0.572138,0.571212,0.569107,0.567314,0.56236,0.559392,0.560168,0.555153,0.559972,0.554559,0.554885,0.551798,0.551857,0.546404,0.546068,0.546875,0.542806,0.540206,0.539358,0.5379,0.53581,0.534171,0.532926,0.530805,0.526911,0.528021,0.525736,0.521182,0.523219,0.519413,0.518268,0.519494,0.517206,0.516313,0.515425,0.514182,0.513064,0.512183,0.512074,0.509471,0.510413,0.511378,0.508993,0.508499,0.509499,0.507778,0.506582,0.507644,0.506492,0.508728,0.506722,0.508668,0.511519,0.510983,0.50951,0.511776,0.513629,0.515124,0.51429,0.518482,0.519538,0.522113,0.524569,0.529436,0.532123,0.536144,0.537676,0.545072,0.551342,0.557408,0.562603,0.568011,0.579297,0.586273,0.595202,0.60494,0.617419,0.625935,0.638816,0.656777,0.668723,0.684399,0.702941,0.721203,0.740341,0.757633,0.774475,0.788345,0.801681,0.8066,0.813014,0.816262,0.821714,0.821885,0.823638,0.818231,0.817136,0.812044,0.811869,0.809314,0.802038,0.797923,0.791057,0.7838,0.782822,0.775374,0.771899,0.762528,0.759973,0.754587,0.747702,0.742875,0.73873,0.73184,0.726124,0.721643,0.715755,0.71217,0.706259,0.701883,0.69765,0.692345,0.688974,0.683167,0.678736)
AAAAAAAAFOAAAAAAAAFOlightcurve-parameter-estimator.signal = spline_data(t)
AAAAAAAAFPAAAAAAAAFPlightcurve-parameter-estimator.spline_data = CubicSpline(time_base,rel_flux)
AAAAAAAAFQAAAAAAAAFQlightcurve-parameter-estimator.t = np.linspace(0, 0.145668, num=int(O))
AAAAAAAAFRAAAAAAAAFRtuple lightcurve-parameter-estimator.time_base = (0,0.000569,0.00114,0.001709,0.002279,0.002849,0.003418,0.003989,0.004559,0.005128,0.005698,0.006268,0.006837,0.007407,0.007977,0.008546,0.009116,0.009686,0.010255,0.010825,0.011395,0.011964,0.012534,0.013104,0.013673,0.014242,0.014812,0.015381,0.015951,0.016521,0.01709,0.01766,0.01823,0.018799,0.019369,0.019938,0.020508,0.021077,0.021647,0.022217,0.022786,0.023356,0.023925,0.024495,0.025064,0.025634,0.026204,0.026773,0.027343,0.027912,0.028482,0.029052,0.029621,0.030191,0.03076,0.03133,0.0319,0.032469,0.033039,0.033608,0.034178,0.034747,0.035317,0.035886,0.036456,0.037026,0.037595,0.0439,0.04447,0.045039,0.045608,0.046178,0.046747,0.047317,0.047886,0.048456,0.049026,0.049595,0.050165,0.050734,0.051304,0.051873,0.052443,0.053013,0.053583,0.054152,0.054722,0.055291,0.055861,0.05643,0.057,0.057569,0.058139,0.058708,0.059278,0.059847,0.060417,0.060987,0.061556,0.062126,0.062696,0.063265,0.063835,0.064404,0.064974,0.065543,0.066113,0.066682,0.067252,0.067821,0.068391,0.068961,0.06953,0.0701,0.070669,0.071239,0.071809,0.072379,0.072949,0.073518,0.074088,0.074657,0.075227,0.075797,0.076366,0.076935,0.077505,0.078075,0.078644,0.079214,0.079783,0.080353,0.080923,0.081492,0.082062,0.082632,0.083201,0.083771,0.08434,0.08491,0.085479,0.086049,0.086618,0.087188,0.087757,0.088327,0.088897,0.089466,0.090036,0.090605,0.091175,0.091744,0.092314,0.092884,0.093453,0.094023,0.094593,0.095162,0.095732,0.096302,0.096872,0.097441,0.09801,0.09858,0.099149,0.099719,0.100289,0.101241,0.10181,0.10238,0.102949,0.103519,0.104089,0.104658,0.105228,0.105797,0.106367,0.106937,0.107506,0.108075,0.108645,0.109215,0.109784,0.110354,0.110923,0.111493,0.112062,0.112632,0.113201,0.113771,0.114341,0.11491,0.11548,0.116049,0.116619,0.117189,0.117758,0.118328,0.118897,0.119467,0.120036,0.120606,0.121176,0.121745,0.122315,0.122885,0.123454,0.124024,0.124593,0.125163,0.125732,0.126302,0.126871,0.127441,0.128011,0.12858,0.12915,0.129719,0.130289,0.130858,0.131428,0.131998,0.132567,0.133137,0.133706,0.134276,0.134845,0.135415,0.135984,0.136554,0.137124,0.137693,0.138263,0.138832,0.139402,0.139972,0.140541,0.141111,0.141681,0.14225,0.14282,0.14339,0.143959,0.144529,0.145098,0.145668)
AAAAAAAAFSAAAAAAAAFS

lightcurve-trainer Namespace Reference
AAAAAAAAIYAAAAAAAAIYFunctions
0)	prompt (timeout)
1)	commandlinearguments ()
2)	shuffle (inputs_train, labels_train, N_counter)
3)	shuffle2 (inputs_train, labels_train)
4)	shuffle3 (inputs_train, labels_train)
Variables
0)	argv = commandlinearguments()
1)	inputs = tf.keras.Input(shape=(98,))
2)	dense = tf.keras.layers.Dense(128,activation="relu")
3)	x = dense(inputs)
4)	outputs = tf.keras.layers.Dense(7,activation="sigmoid")(x)
5)	model = tf.keras.Model(inputs=inputs, outputs=outputs)
6)	loss
7)	optimizer
8)	metrics
9)	int counter = 0
10)	inputs_train = np.load("inputs_train_data.npy")
11)	labels_train = np.load("labels_train_data.npy")
12)	checkpoint = tf.train.Checkpoint(model)
13)	load_status = model.load_weights("./checkpoint"+argv[1])
14)	status = checkpoint.restore("./checkpoint"+argv[1])
15)	int counter_shuffle = 0
16)	hist = model.fit(inputs_train, labels_train, epochs=2)

Function Documentation
lightcurve-trainer.commandlinearguments ()
AAAAAAAAIZAAAAAAAAIZlightcurve-trainer.prompt (  timeout)
AAAAAAAAJAAAAAAAAAJAlightcurve-trainer.shuffle (  inputs_train,   labels_train,   N_counter)
AAAAAAAAJBAAAAAAAAJBlightcurve-trainer.shuffle2 (  inputs_train,   labels_train)
AAAAAAAAJCAAAAAAAAJClightcurve-trainer.shuffle3 (  inputs_train,   labels_train)
AAAAAAAAJDAAAAAAAAJD
Variable Documentation
lightcurve-trainer.argv = commandlinearguments()
AAAAAAAAJEAAAAAAAAJElightcurve-trainer.checkpoint = tf.train.Checkpoint(model)
AAAAAAAAJFAAAAAAAAJFint lightcurve-trainer.counter = 0
AAAAAAAAJGAAAAAAAAJGint lightcurve-trainer.counter_shuffle = 0
AAAAAAAAJHAAAAAAAAJHlightcurve-trainer.dense = tf.keras.layers.Dense(128,activation="relu")
AAAAAAAAJIAAAAAAAAJIlightcurve-trainer.hist = model.fit(inputs_train, labels_train, epochs=2)
AAAAAAAAJJAAAAAAAAJJlightcurve-trainer.inputs = tf.keras.Input(shape=(98,))
AAAAAAAAJKAAAAAAAAJKlightcurve-trainer.inputs_train = np.load("inputs_train_data.npy")
AAAAAAAAJLAAAAAAAAJLlightcurve-trainer.labels_train = np.load("labels_train_data.npy")
AAAAAAAAJMAAAAAAAAJMlightcurve-trainer.load_status = model.load_weights("./checkpoint"+argv[1])
AAAAAAAAJNAAAAAAAAJNlightcurve-trainer.loss
AAAAAAAAJOAAAAAAAAJOlightcurve-trainer.metrics
AAAAAAAAJPAAAAAAAAJPlightcurve-trainer.model = tf.keras.Model(inputs=inputs, outputs=outputs)
AAAAAAAAJQAAAAAAAAJQlightcurve-trainer.optimizer
AAAAAAAAJRAAAAAAAAJRlightcurve-trainer.outputs = tf.keras.layers.Dense(7,activation="sigmoid")(x)
AAAAAAAAJSAAAAAAAAJSlightcurve-trainer.status = checkpoint.restore("./checkpoint"+argv[1])
AAAAAAAAJTAAAAAAAAJTlightcurve-trainer.x = dense(inputs)
AAAAAAAAJUAAAAAAAAJU

lightcurve-trainer-start Namespace Reference
AAAAAAAAJVAAAAAAAAJVFunctions
0)	shuffle (inputs_train, labels_train, N_counter)
Variables
0)	inputs = tf.keras.Input(shape=(99,))
1)	dense = tf.keras.layers.Dense(128,activation="relu")
2)	x = dense(inputs)
3)	outputs = tf.keras.layers.Dense(5,activation="sigmoid")(x)
4)	model = tf.keras.Model(inputs=inputs, outputs=outputs)
5)	loss
6)	optimizer
7)	metrics
8)	inputs_train = np.load("inputs_train_data.npy")
9)	labels_train = np.load("labels_train_data.npy")
10)	N = len(inputs_train)
11)	int K = 128000
12)	int counter = 0
13)	hist = model.fit(inputs_train, labels_train, epochs=2)

Function Documentation
lightcurve-trainer-start.shuffle (  inputs_train,   labels_train,   N_counter)
AAAAAAAAJWAAAAAAAAJW
Variable Documentation
int lightcurve-trainer-start.counter = 0
AAAAAAAAJXAAAAAAAAJXlightcurve-trainer-start.dense = tf.keras.layers.Dense(128,activation="relu")
AAAAAAAAJYAAAAAAAAJYlightcurve-trainer-start.hist = model.fit(inputs_train, labels_train, epochs=2)
AAAAAAAAJZAAAAAAAAJZlightcurve-trainer-start.inputs = tf.keras.Input(shape=(99,))
AAAAAAAAKAAAAAAAAAKAlightcurve-trainer-start.inputs_train = np.load("inputs_train_data.npy")
AAAAAAAAKBAAAAAAAAKBint lightcurve-trainer-start.K = 128000
AAAAAAAAKCAAAAAAAAKClightcurve-trainer-start.labels_train = np.load("labels_train_data.npy")
AAAAAAAAKDAAAAAAAAKDlightcurve-trainer-start.loss
AAAAAAAAKEAAAAAAAAKElightcurve-trainer-start.metrics
AAAAAAAAKFAAAAAAAAKFlightcurve-trainer-start.model = tf.keras.Model(inputs=inputs, outputs=outputs)
AAAAAAAAKGAAAAAAAAKGlightcurve-trainer-start.N = len(inputs_train)
AAAAAAAAKHAAAAAAAAKHlightcurve-trainer-start.optimizer
AAAAAAAAKIAAAAAAAAKIlightcurve-trainer-start.outputs = tf.keras.layers.Dense(5,activation="sigmoid")(x)
AAAAAAAAKJAAAAAAAAKJlightcurve-trainer-start.x = dense(inputs)
AAAAAAAAKKAAAAAAAAKK

mouseclient Namespace Reference
AAAAAAAAKLAAAAAAAAKLFunctions
0)	Cube ()
1)	main ()
Variables
0)	tuple verticies
1)	tuple edges

Function Documentation
mouseclient.Cube ()
AAAAAAAAKMAAAAAAAAKMHere is the caller graph for this function:
IMAGE
mouseclient.main ()
AAAAAAAAKNAAAAAAAAKNHere is the call graph for this function:
IMAGE
Here is the caller graph for this function:
IMAGE

Variable Documentation
tuple mouseclient.edges
AAAAAAAAKOAAAAAAAAKOInitial value:1 =  (
2     (0,1),
3     (0,3),
4     (0,4),
5     (2,1),
6     (2,3),
7     (2,7),
8     (6,3),
9     (6,4),
10     (6,7),
11     (5,1),
12     (5,4),
13     (5,7)
14     )
tuple mouseclient.verticies
AAAAAAAAKPAAAAAAAAKPInitial value:1 =  (
2     (1, -1, -1),
3     (1, 1, -1),
4     (-1, 1, -1),
5     (-1, -1, -1),
6     (1, -1, 1),
7     (1, 1, 1),
8     (-1, -1, 1),
9     (-1, 1, 1)
10     )


pygame-sphere Namespace Reference
AAAAAAAAKQAAAAAAAAKQVariables
0)	tuple display = (400, 300)
1)	tuple scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
2)	sphere = gluNewQuadric()
3)	viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
4)	bool run = True
5)	keypress = pygame.key.get_pressed()

Variable Documentation
tuple pygame-sphere.display = (400, 300)
AAAAAAAAKRAAAAAAAAKRpygame-sphere.keypress = pygame.key.get_pressed()
AAAAAAAAKSAAAAAAAAKSbool pygame-sphere.run = True
AAAAAAAAKTAAAAAAAAKTtuple pygame-sphere.scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
AAAAAAAAKUAAAAAAAAKUpygame-sphere.sphere = gluNewQuadric()
AAAAAAAAKVAAAAAAAAKVpygame-sphere.viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
AAAAAAAAKWAAAAAAAAKW

sphere3 Namespace Reference
AAAAAAAAKXAAAAAAAAKXClasses
class SphereFunctions
0)	read_texture (filename)
1)	read_3dtexture ()
2)	update_point (coords, seed, MAP_SIZE)
3)	generate_heightmap (map_size)
4)	main ()
Variables
0)	int last_time = 0
1)	int SCALE = 10

Function Documentation
sphere3.generate_heightmap (  map_size)
AAAAAAAAKYAAAAAAAAKYHere is the call graph for this function:
IMAGE
sphere3.main ()
AAAAAAAAKZAAAAAAAAKZHere is the call graph for this function:
IMAGE
Here is the caller graph for this function:
IMAGE
sphere3.read_3dtexture ()
AAAAAAAALAAAAAAAAALAHere is the caller graph for this function:
IMAGE
sphere3.read_texture (  filename)
AAAAAAAALBAAAAAAAALB
Reads an image file and converts to a OpenGL-readable textID format
 
sphere3.update_point (  coords,   seed,   MAP_SIZE)
AAAAAAAALCAAAAAAAALCHere is the caller graph for this function:
IMAGE

Variable Documentation
int sphere3.last_time = 0
AAAAAAAALDAAAAAAAALDint sphere3.SCALE = 10
AAAAAAAALEAAAAAAAALE
Class Documentation
lightcurve-parameter-estimator.EllipseEquation Class Reference
AAAAAAAAFTAAAAAAAAFTInheritance diagram for lightcurve-parameter-estimator.EllipseEquation:
IMAGE

Public Member Functions
0)	__init__ (self)
1)	__init__ (self, a, e, M)
2)	calc_r (self, theta)
3)	calc_v (self, r)
4)	calc (self, N, x_offset=0)
Public Attributes
0)	ea
1)	b
2)	M
3)	P
4)	x_offset
5)	t
6)	dist
7)	accel
8)	Theta
9)	vel
10)	vel_x
11)	dist_x
12)	x_coords
13)	y_coords
14)	dt
Static Public Attributes
0)	list t = []
1)	list dist = []
2)	list accel = []
3)	list vel = []
4)	list Theta = []
5)	list vel_x = []
6)	list dist_x = []
7)	list x_coords = []
8)	list y_coords = []
9)	int x_offset = 0
10)	float G = 6.673e-11
11)	int dt = 0

Constructor & Destructor Documentation
lightcurve-parameter-estimator.EllipseEquation.__init__ (  self)
AAAAAAAAFUAAAAAAAAFU
Reimplemented in lightcurve-parameter-estimator.EllipticalDifferenceEquation (p.pagenum).
lightcurve-parameter-estimator.EllipseEquation.__init__ (  self,   a,   e,   M)
AAAAAAAAFWAAAAAAAAFW
Reimplemented in lightcurve-parameter-estimator.EllipticalDifferenceEquation (p.pagenum).

Member Function Documentation
lightcurve-parameter-estimator.EllipseEquation.calc (  self,   N,   x_offset = 0)
AAAAAAAAFXAAAAAAAAFX
Reimplemented in lightcurve-parameter-estimator.EllipticalDifferenceEquation (p.pagenum).
lightcurve-parameter-estimator.EllipseEquation.calc_r (  self,   theta)
AAAAAAAAFZAAAAAAAAFZlightcurve-parameter-estimator.EllipseEquation.calc_v (  self,   r)
AAAAAAAAGAAAAAAAAAGA
Member Data Documentation
lightcurve-parameter-estimator.EllipseEquation.a
AAAAAAAAGBAAAAAAAAGBlist lightcurve-parameter-estimator.EllipseEquation.accel = [][static]
AAAAAAAAGCAAAAAAAAGClightcurve-parameter-estimator.EllipseEquation.accel
AAAAAAAAGDAAAAAAAAGDlightcurve-parameter-estimator.EllipseEquation.b
AAAAAAAAGEAAAAAAAAGElist lightcurve-parameter-estimator.EllipseEquation.dist = [][static]
AAAAAAAAGFAAAAAAAAGFlightcurve-parameter-estimator.EllipseEquation.dist
AAAAAAAAGGAAAAAAAAGGlist lightcurve-parameter-estimator.EllipseEquation.dist_x = [][static]
AAAAAAAAGHAAAAAAAAGHlightcurve-parameter-estimator.EllipseEquation.dist_x
AAAAAAAAGIAAAAAAAAGIint lightcurve-parameter-estimator.EllipseEquation.dt = 0[static]
AAAAAAAAGJAAAAAAAAGJlightcurve-parameter-estimator.EllipseEquation.dt
AAAAAAAAGKAAAAAAAAGKlightcurve-parameter-estimator.EllipseEquation.e
AAAAAAAAGLAAAAAAAAGLfloat lightcurve-parameter-estimator.EllipseEquation.G = 6.673e-11[static]
AAAAAAAAGMAAAAAAAAGMlightcurve-parameter-estimator.EllipseEquation.M
AAAAAAAAGNAAAAAAAAGNlightcurve-parameter-estimator.EllipseEquation.P
AAAAAAAAGOAAAAAAAAGOlist lightcurve-parameter-estimator.EllipseEquation.t = [][static]
AAAAAAAAGPAAAAAAAAGPlightcurve-parameter-estimator.EllipseEquation.t
AAAAAAAAGQAAAAAAAAGQlist lightcurve-parameter-estimator.EllipseEquation.Theta = [][static]
AAAAAAAAGRAAAAAAAAGRlightcurve-parameter-estimator.EllipseEquation.Theta
AAAAAAAAGSAAAAAAAAGSlist lightcurve-parameter-estimator.EllipseEquation.vel = [][static]
AAAAAAAAGTAAAAAAAAGTlightcurve-parameter-estimator.EllipseEquation.vel
AAAAAAAAGUAAAAAAAAGUlist lightcurve-parameter-estimator.EllipseEquation.vel_x = [][static]
AAAAAAAAGVAAAAAAAAGVlightcurve-parameter-estimator.EllipseEquation.vel_x
AAAAAAAAGWAAAAAAAAGWlist lightcurve-parameter-estimator.EllipseEquation.x_coords = [][static]
AAAAAAAAGXAAAAAAAAGXlightcurve-parameter-estimator.EllipseEquation.x_coords
AAAAAAAAGYAAAAAAAAGYint lightcurve-parameter-estimator.EllipseEquation.x_offset = 0[static]
AAAAAAAAGZAAAAAAAAGZlightcurve-parameter-estimator.EllipseEquation.x_offset
AAAAAAAAHAAAAAAAAAHAlist lightcurve-parameter-estimator.EllipseEquation.y_coords = [][static]
AAAAAAAAHBAAAAAAAAHBlightcurve-parameter-estimator.EllipseEquation.y_coords
AAAAAAAAHCAAAAAAAAHC
The documentation for this class was generated from the following file:
lightcurve-parameter-estimator.py

lightcurve-parameter-estimator.EllipticalDifferenceEquation Class Reference
AAAAAAAAHDAAAAAAAAHDInheritance diagram for lightcurve-parameter-estimator.EllipticalDifferenceEquation:
IMAGE

Collaboration diagram for lightcurve-parameter-estimator.EllipticalDifferenceEquation:
IMAGE

Public Member Functions
0)	__init__ (self, time, flux, Mass, e1, e2, e3)
1)	normalise (self, array_input)
2)	apply_phase (self, array_input, phase)
3)	calc_arrays (self, array1, array2, amplitude, phase)
4)	calc_weights (self, list_array, delta_phase)
5)	calc (self)
6)	calc_main (self, ARGS=[], E1=2, E2=7, deltaN=1)
7)	printout (self)
8)	optimise_e (self, e=1, count_max=5, phase_max1=0.1, phase_max2=0.05, phase_min=0.02, delta_phase1=1, delta_phase2=1)
9)	calc_period (self)
Public Member Functions inherited from lightcurve-parameter-estimator.EllipseEquation
0)	__init__ (self)
1)	__init__ (self, a, e, M)
2)	calc_r (self, theta)
3)	calc_v (self, r)
4)	calc (self, N, x_offset=0)
Public Attributes
0)	e1e2
1)	e3
2)	Mass
3)	time
4)	flux
5)	list_EE
6)	index1
7)	index0
8)	obs_period
9)	N
10)	semimajoraxis
11)	dist
12)	resultant
13)	N_phase1
14)	N_phase2
Public Attributes inherited from lightcurve-parameter-estimator.EllipseEquation
0)	e
1)	a
2)	b
3)	M
4)	P
5)	x_offset
6)	t
7)	dist
8)	accel
9)	Theta
10)	vel
11)	vel_x
12)	dist_x
13)	x_coords
14)	y_coords
15)	dt
Static Public Attributes
0)	list list_EE = []
1)	int Mass = 0
2)	int semimajoraxis = 0
3)	float amplitude = 1.0
4)	int offset = 0
5)	float obs_amplitude = 1.0
6)	int obs_offset = 0
7)	int obs_period = 0
8)	list time = []
9)	list flux = []
10)	list resultant = []
11)	list dist = []
12)	int e1 = 0
13)	int e2 = 0
14)	int e3 = 0
15)	float G = 6.673e-11
16)	int phase = 0
17)	int N = 1000
18)	int N_phase1 = 0
19)	int N_phase2 = 0
20)	int index0 = 0
21)	int index1 = 0
Static Public Attributes inherited from lightcurve-parameter-estimator.EllipseEquation
0)	list t = []
1)	list dist = []
2)	list accel = []
3)	list vel = []
4)	list Theta = []
5)	list vel_x = []
6)	list dist_x = []
7)	list x_coords = []
8)	list y_coords = []
9)	int x_offset = 0
10)	float G = 6.673e-11
11)	int dt = 0

Constructor & Destructor Documentation
lightcurve-parameter-estimator.EllipticalDifferenceEquation.__init__ (  self,   time,   flux,   Mass,   e1,   e2,   e3)
AAAAAAAAFVAAAAAAAAFV
Reimplemented from lightcurve-parameter-estimator.EllipseEquation (p.pagenum).

Member Function Documentation
lightcurve-parameter-estimator.EllipticalDifferenceEquation.apply_phase (  self,   array_input,   phase)
AAAAAAAAHEAAAAAAAAHEHere is the call graph for this function:
IMAGE
lightcurve-parameter-estimator.EllipticalDifferenceEquation.calc (  self)
AAAAAAAAFYAAAAAAAAFY
Reimplemented from lightcurve-parameter-estimator.EllipseEquation (p.pagenum).
Here is the caller graph for this function:
IMAGE
lightcurve-parameter-estimator.EllipticalDifferenceEquation.calc_arrays (  self,   array1,   array2,   amplitude,   phase)
AAAAAAAAHFAAAAAAAAHFHere is the caller graph for this function:
IMAGE
lightcurve-parameter-estimator.EllipticalDifferenceEquation.calc_main (  self,   ARGS = [],   E1 = 2,   E2 = 7,   deltaN = 1)
AAAAAAAAHGAAAAAAAAHGHere is the call graph for this function:
IMAGE
lightcurve-parameter-estimator.EllipticalDifferenceEquation.calc_period (  self)
AAAAAAAAHHAAAAAAAAHHlightcurve-parameter-estimator.EllipticalDifferenceEquation.calc_weights (  self,   list_array,   delta_phase)
AAAAAAAAHIAAAAAAAAHIHere is the call graph for this function:
IMAGE
Here is the caller graph for this function:
IMAGE
lightcurve-parameter-estimator.EllipticalDifferenceEquation.normalise (  self,   array_input)
AAAAAAAAHJAAAAAAAAHJHere is the caller graph for this function:
IMAGE
lightcurve-parameter-estimator.EllipticalDifferenceEquation.optimise_e (  self,   e = 1,   count_max = 5,   phase_max1 = 0.1,   phase_max2 = 0.05,   phase_min = 0.02,   delta_phase1 = 1,   delta_phase2 = 1)
AAAAAAAAHKAAAAAAAAHKHere is the call graph for this function:
IMAGE
lightcurve-parameter-estimator.EllipticalDifferenceEquation.printout (  self)
AAAAAAAAHLAAAAAAAAHLHere is the call graph for this function:
IMAGE

Member Data Documentation
float lightcurve-parameter-estimator.EllipticalDifferenceEquation.amplitude = 1.0[static]
AAAAAAAAHMAAAAAAAAHMlist lightcurve-parameter-estimator.EllipticalDifferenceEquation.dist = [][static]
AAAAAAAAHNAAAAAAAAHNlightcurve-parameter-estimator.EllipticalDifferenceEquation.dist
AAAAAAAAHOAAAAAAAAHOint lightcurve-parameter-estimator.EllipticalDifferenceEquation.e1 = 0[static]
AAAAAAAAHPAAAAAAAAHPlightcurve-parameter-estimator.EllipticalDifferenceEquation.e1
AAAAAAAAHQAAAAAAAAHQint lightcurve-parameter-estimator.EllipticalDifferenceEquation.e2 = 0[static]
AAAAAAAAHRAAAAAAAAHRlightcurve-parameter-estimator.EllipticalDifferenceEquation.e2
AAAAAAAAHSAAAAAAAAHSint lightcurve-parameter-estimator.EllipticalDifferenceEquation.e3 = 0[static]
AAAAAAAAHTAAAAAAAAHTlightcurve-parameter-estimator.EllipticalDifferenceEquation.e3
AAAAAAAAHUAAAAAAAAHUlist lightcurve-parameter-estimator.EllipticalDifferenceEquation.flux = [][static]
AAAAAAAAHVAAAAAAAAHVlightcurve-parameter-estimator.EllipticalDifferenceEquation.flux
AAAAAAAAHWAAAAAAAAHWfloat lightcurve-parameter-estimator.EllipticalDifferenceEquation.G = 6.673e-11[static]
AAAAAAAAHXAAAAAAAAHXint lightcurve-parameter-estimator.EllipticalDifferenceEquation.index0 = 0[static]
AAAAAAAAHYAAAAAAAAHYlightcurve-parameter-estimator.EllipticalDifferenceEquation.index0
AAAAAAAAHZAAAAAAAAHZint lightcurve-parameter-estimator.EllipticalDifferenceEquation.index1 = 0[static]
AAAAAAAAIAAAAAAAAAIAlightcurve-parameter-estimator.EllipticalDifferenceEquation.index1
AAAAAAAAIBAAAAAAAAIBlist lightcurve-parameter-estimator.EllipticalDifferenceEquation.list_EE = [][static]
AAAAAAAAICAAAAAAAAIClightcurve-parameter-estimator.EllipticalDifferenceEquation.list_EE
AAAAAAAAIDAAAAAAAAIDint lightcurve-parameter-estimator.EllipticalDifferenceEquation.Mass = 0[static]
AAAAAAAAIEAAAAAAAAIElightcurve-parameter-estimator.EllipticalDifferenceEquation.Mass
AAAAAAAAIFAAAAAAAAIFint lightcurve-parameter-estimator.EllipticalDifferenceEquation.N = 1000[static]
AAAAAAAAIGAAAAAAAAIGlightcurve-parameter-estimator.EllipticalDifferenceEquation.N
AAAAAAAAIHAAAAAAAAIHint lightcurve-parameter-estimator.EllipticalDifferenceEquation.N_phase1 = 0[static]
AAAAAAAAIIAAAAAAAAIIlightcurve-parameter-estimator.EllipticalDifferenceEquation.N_phase1
AAAAAAAAIJAAAAAAAAIJint lightcurve-parameter-estimator.EllipticalDifferenceEquation.N_phase2 = 0[static]
AAAAAAAAIKAAAAAAAAIKlightcurve-parameter-estimator.EllipticalDifferenceEquation.N_phase2
AAAAAAAAILAAAAAAAAILfloat lightcurve-parameter-estimator.EllipticalDifferenceEquation.obs_amplitude = 1.0[static]
AAAAAAAAIMAAAAAAAAIMint lightcurve-parameter-estimator.EllipticalDifferenceEquation.obs_offset = 0[static]
AAAAAAAAINAAAAAAAAINint lightcurve-parameter-estimator.EllipticalDifferenceEquation.obs_period = 0[static]
AAAAAAAAIOAAAAAAAAIOlightcurve-parameter-estimator.EllipticalDifferenceEquation.obs_period
AAAAAAAAIPAAAAAAAAIPint lightcurve-parameter-estimator.EllipticalDifferenceEquation.offset = 0[static]
AAAAAAAAIQAAAAAAAAIQint lightcurve-parameter-estimator.EllipticalDifferenceEquation.phase = 0[static]
AAAAAAAAIRAAAAAAAAIRlist lightcurve-parameter-estimator.EllipticalDifferenceEquation.resultant = [][static]
AAAAAAAAISAAAAAAAAISlightcurve-parameter-estimator.EllipticalDifferenceEquation.resultant
AAAAAAAAITAAAAAAAAITint lightcurve-parameter-estimator.EllipticalDifferenceEquation.semimajoraxis = 0[static]
AAAAAAAAIUAAAAAAAAIUlightcurve-parameter-estimator.EllipticalDifferenceEquation.semimajoraxis
AAAAAAAAIVAAAAAAAAIVlist lightcurve-parameter-estimator.EllipticalDifferenceEquation.time = [][static]
AAAAAAAAIWAAAAAAAAIWlightcurve-parameter-estimator.EllipticalDifferenceEquation.time
AAAAAAAAIXAAAAAAAAIX
The documentation for this class was generated from the following file:
lightcurve-parameter-estimator.py

sphere3.Sphere Class Reference
AAAAAAAALFAAAAAAAALFPublic Member Functions
0)	__init__ (self, radius)
1)	calc_display_list (self)
2)	init (self)
3)	compute_location (self)
4)	display (self)
5)	calc_vertex (self)
6)	special (self, key, x, y)
7)	idle (self)
8)	visible (self, vis)
Public Attributes
0)	radiuslats
1)	longs
2)	user_theta
3)	user_height
4)	direction
5)	intensity
6)	ambient_intensity
7)	surface
8)	N
9)	list_vertex
10)	list_normals
11)	list_random_maps
12)	counter_random
13)	index
14)	idle
Static Public Attributes
0)	vn4 = np.cross(vf1,vf2)
vf1=v2-v1 vf2=v3-v1 vn2=np.cross(vf1,vf2) v1=self.list_vertex[k][i-1,j-1] v2=self.list_vertex[k][i-1,j] v3=self.list_vertex[k][i-2,j-1] vf1=v2-v1 vf2=v3-v1 vn3=np.cross(vf1,vf2) v1=self.list_vertex[k][i-1,j-1] v2=self.list_vertex[k][i-1,j-2] v3=self.list_vertex[k][i-2,j-1] vf1=v2-v1 vf2=v3-v1 

0)	vn_avg = np.linalg.norm(vn4)

Constructor & Destructor Documentation
sphere3.Sphere.__init__ (  self,   radius)
AAAAAAAALGAAAAAAAALG
Member Function Documentation
sphere3.Sphere.calc_display_list (  self)
AAAAAAAALHAAAAAAAALHHere is the call graph for this function:
IMAGE
sphere3.Sphere.calc_vertex (  self)
AAAAAAAALIAAAAAAAALIHere is the caller graph for this function:
IMAGE
sphere3.Sphere.compute_location (  self)
AAAAAAAALJAAAAAAAALJHere is the caller graph for this function:
IMAGE
sphere3.Sphere.display (  self)
AAAAAAAALKAAAAAAAALKsphere3.Sphere.idle (  self)
AAAAAAAALLAAAAAAAALLsphere3.Sphere.init (  self)
AAAAAAAALMAAAAAAAALMHere is the call graph for this function:
IMAGE
sphere3.Sphere.special (  self,   key,   x,   y)
AAAAAAAALNAAAAAAAALNHere is the call graph for this function:
IMAGE
sphere3.Sphere.visible (  self,   vis)
AAAAAAAALOAAAAAAAALO
Member Data Documentation
sphere3.Sphere.ambient_intensity
AAAAAAAALPAAAAAAAALPsphere3.Sphere.counter_random
AAAAAAAALQAAAAAAAALQsphere3.Sphere.direction
AAAAAAAALRAAAAAAAALRsphere3.Sphere.idle
AAAAAAAALSAAAAAAAALSsphere3.Sphere.index
AAAAAAAALTAAAAAAAALTsphere3.Sphere.intensity
AAAAAAAALUAAAAAAAALUsphere3.Sphere.lats
AAAAAAAALVAAAAAAAALVsphere3.Sphere.list_normals
AAAAAAAALWAAAAAAAALWsphere3.Sphere.list_random_maps
AAAAAAAALXAAAAAAAALXsphere3.Sphere.list_vertex
AAAAAAAALYAAAAAAAALYsphere3.Sphere.longs
AAAAAAAALZAAAAAAAALZsphere3.Sphere.N
AAAAAAAAMAAAAAAAAAMAsphere3.Sphere.radius
AAAAAAAAMBAAAAAAAAMBsphere3.Sphere.surface
AAAAAAAAMCAAAAAAAAMCsphere3.Sphere.user_height
AAAAAAAAMDAAAAAAAAMDsphere3.Sphere.user_theta
AAAAAAAAMEAAAAAAAAMEsphere3.Sphere.vn4 = np.cross(vf1,vf2)[static]
AAAAAAAAMFAAAAAAAAMF
vf1=v2-v1 vf2=v3-v1 vn2=np.cross(vf1,vf2) v1=self.list_vertex[k][i-1,j-1] v2=self.list_vertex[k][i-1,j] v3=self.list_vertex[k][i-2,j-1] vf1=v2-v1 vf2=v3-v1 vn3=np.cross(vf1,vf2) v1=self.list_vertex[k][i-1,j-1] v2=self.list_vertex[k][i-1,j-2] v3=self.list_vertex[k][i-2,j-1] vf1=v2-v1 vf2=v3-v1 
sphere3.Sphere.vn_avg = np.linalg.norm(vn4)[static]
AAAAAAAAMGAAAAAAAAMG
The documentation for this class was generated from the following file:
sphere3.py
File Documentation
3dsphere.py File Reference
AAAAAAAAAAAAAAAAAAAANamespaces
0)	namespace 3dsphere
Variables
0)	tuple 3dsphere.display = (400, 300)
1)	tuple 3dsphere.screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
2)	3dsphere.sphere = gluNewQuadric()
3)	3dsphere.viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
4)	bool 3dsphere.run = True
5)	int 3dsphere.counter_light = 0
6)	3dsphere.keypress = pygame.key.get_pressed()
7)	int 3dsphere.theta = math.pi*counter_light/100


3dsphere2.py File Reference
AAAAAAAAABAAAAAAAAABNamespaces
0)	namespace 3dsphere2
Functions
0)	3dsphere2.read_texture (filename)
1)	3dsphere2.main ()


animation.py File Reference
AAAAAAAAACAAAAAAAAACNamespaces
0)	namespace animation
Variables
0)	tuple animation.black = (0,0,0)
1)	tuple animation.red = (255,0,0)
2)	tuple animation.green = (0,255,0)
3)	tuple animation.blue = (0,0,255)
4)	tuple animation.white = (255,255,255)
5)	bool animation.run_me = True
6)	int animation.screen_size = 1080, 720
7)	animation.screen = pygame.display.set_mode(screen_size)
8)	animation.clock = pygame.time.Clock()
9)	int animation.fps_limit = 60
10)	tuple animation.colorcircle = (red)
11)	tuple animation.colorcircle2 = (blue)
12)	int animation.posx = 1080/2
13)	int animation.posy = 720/2
14)	animation.circle = pygame.draw.circle(screen, colorcircle, (posx, posy), 50)
15)	int animation.r = posx*0.5
16)	int animation.theta = 40/180*math.pi
17)	int animation.time1 = 0
18)	int animation.time2 = 0
19)	int animation.angular_vel1 = 30/180*math.pi
20)	int animation.angular_vel2 = 43/180*math.pi
21)	int animation.angle2 = 40/180*math.pi
22)	float animation.phi = 30.2/180*math.pi
23)	float animation.delta_t = 0.9
24)	float animation.delta_t1 = delta_t
25)	float animation.delta_t2 = delta_t
26)	int animation.counter = 0
27)	int animation.dcounter = 1
28)	int animation.x1 = -r*math.sin(angle2)*math.cos(angular_vel1*time1)
29)	int animation.y1 = r*math.sin(angle2)*math.sin(angular_vel1*time1)
30)	int animation.x2 = r*math.sin(angle2)*math.cos(angular_vel2*time2+phi)
31)	int animation.y2 = r*math.sin(angle2)*math.sin(angular_vel2*time2+phi)
32)	animation.width
33)	tuple animation.distsquared = (x2-x1)*(x2-x1)
34)	animation.dist = math.sqrt(distsquared)


get-pip.py File Reference
AAAAAAAAADAAAAAAAAADNamespaces
0)	namespace get-pip
Functions
0)	get-pip.include_setuptools (args)
1)	get-pip.include_wheel (args)
2)	get-pip.determine_pip_install_arguments ()
3)	get-pip.monkeypatch_for_cert (tmpdir)
4)	get-pip.bootstrap (tmpdir)
5)	get-pip.main ()
Variables
0)	get-pip.this_python = sys.version_info[:2]
1)	tuple get-pip.min_version = (3, 7)
2)	list get-pip.message_parts
3)	str get-pip.DATA


image-cap.py File Reference
AAAAAAAAAEAAAAAAAAAENamespaces
0)	namespace image-cap
Variables
0)	int image-cap.cams_test = 10
1)	image-cap.cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
2)	image-cap.test = cap.isOpened()
3)	image-cap.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
4)	image-cap.ret
5)	image-cap.frame = cv2.GaussianBlur(frame,(35,35),0)
6)	image-cap.frame_still = cv2.GaussianBlur(frame_still,(35,35),0)
7)	int image-cap.img_counter = 0
8)	image-cap.bins = np.array([0,51,102,153,204,255])
9)	image-cap.right
10)	image-cap.greyscale2 = cv2.cvtColor(frame_still, cv2.COLOR_BGR2GRAY)
11)	int image-cap.Thresh = 100
12)	image-cap.greyscale1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
13)	image-cap.background
14)	image-cap.k = cv2.waitKey(1)


image_cap.cpp File Reference
AAAAAAAAAFAAAAAAAAAF#include <opencv2/opencv.hpp>
#include <iostream>
Include dependency graph for image_cap.cpp:
IMAGE

Functions
0)	int main ()

Function Documentation
int main ()
AAAAAAAAAGAAAAAAAAAG

kepler-feature-counter.py File Reference
AAAAAAAAAHAAAAAAAAAHNamespaces
0)	namespace kepler-feature-counter
Functions
0)	kepler-feature-counter.calc_period (flux)
1)	kepler-feature-counter.commandlinearguments ()
Variables
0)	kepler-feature-counter.argv = commandlinearguments()
1)	int kepler-feature-counter.Smooth_factor = 20
2)	int kepler-feature-counter.counter_id = 757000
3)	str kepler-feature-counter.filename = "kplr{:09d}-2009131105131_llc.fits".format(counter_id)
4)	kepler-feature-counter.mode
5)	kepler-feature-counter.bjdrefi = hdulist[1].header['BJDREFI']
6)	kepler-feature-counter.bjdreff = hdulist[1].header['BJDREFF']
7)	kepler-feature-counter.times = hdulist[1].data['time']
8)	kepler-feature-counter.sap_fluxes = hdulist[1].data['SAP_FLUX']
9)	kepler-feature-counter.pdcsap_fluxes = hdulist[1].data['PDCSAP_FLUX']
10)	kepler-feature-counter.N = len(sap_fluxes)
11)	kepler-feature-counter.t = np.linspace(0,times[N-1]-times[0],N)
12)	kepler-feature-counter.array_input = np.array(sap_fluxes)
13)	kepler-feature-counter.max_array = np.max(array_input)
14)	kepler-feature-counter.min_array = np.min(array_input)
15)	kepler-feature-counter.amplitude = max_array-min_array
16)	tuple kepler-feature-counter.offset = (max_array+min_array)/(2*(amplitude))
17)	kepler-feature-counter.first_derivative = np.gradient(array_input)
18)	kepler-feature-counter.maxima = argrelextrema(array_input,np.greater)
19)	kepler-feature-counter.minima = argrelextrema(array_input,np.less)
20)	kepler-feature-counter.maxima0 = argrelextrema(first_derivative,np.greater)
21)	kepler-feature-counter.minima0 = argrelextrema(first_derivative,np.less)
22)	int kepler-feature-counter.features = 2*len(maxima[0])+2*len(minima[0])+len(maxima0[0])+len(minima0[0])
23)	kepler-feature-counter.Nperiod = calc_period(array_input)


lightcurve-parameter-estimator.py File Reference
AAAAAAAAAIAAAAAAAAAIClasses
0)	class lightcurve-parameter-estimator.EllipseEquationclass lightcurve-parameter-estimator.EllipticalDifferenceEquation
Namespaces
0)	namespace lightcurve-parameter-estimator
Functions
0)	lightcurve-parameter-estimator.extend_signal (signal, K)
1)	lightcurve-parameter-estimator.signal_weight (signal)
2)	lightcurve-parameter-estimator.shuffle (inputs_train, labels_train, N_counter)
Variables
0)	tuple lightcurve-parameter-estimator.rel_flux = (0.516874,0.514718,0.513875,0.51701,0.515947,0.516506,0.514698,0.514998,0.51023,0.507271,0.509727,0.511362,0.506488,0.508958,0.507097,0.506385,0.502653,0.508093,0.503255,0.504292,0.506062,0.501479,0.504612,0.503892,0.509819,0.502666,0.50247,0.506035,0.506205,0.504486,0.505797,0.506178,0.510974,0.508446,0.508027,0.506151,0.514618,0.516266,0.517662,0.522371,0.524497,0.526994,0.530796,0.536497,0.544171,0.549154,0.551763,0.55893,0.570134,0.575073,0.583214,0.596239,0.603371,0.61613,0.627472,0.644398,0.652329,0.671484,0.691639,0.702505,0.723772,0.743772,0.760631,0.775118,0.785617,0.79526,0.803752,0.794038,0.786258,0.78557,0.777623,0.774241,0.769259,0.762497,0.757905,0.751677,0.742528,0.74069,0.733236,0.728572,0.724491,0.719929,0.713713,0.709665,0.703484,0.701474,0.692684,0.690999,0.684574,0.677643,0.675762,0.670914,0.665341,0.662756,0.656312,0.654239,0.64872,0.647028,0.644872,0.640277,0.636528,0.632404,0.626704,0.622936,0.623371,0.618118,0.616468,0.609824,0.606578,0.603021,0.602043,0.598819,0.595745,0.591926,0.592143,0.587627,0.586611,0.580896,0.579149,0.57916,0.575455,0.572138,0.571212,0.569107,0.567314,0.56236,0.559392,0.560168,0.555153,0.559972,0.554559,0.554885,0.551798,0.551857,0.546404,0.546068,0.546875,0.542806,0.540206,0.539358,0.5379,0.53581,0.534171,0.532926,0.530805,0.526911,0.528021,0.525736,0.521182,0.523219,0.519413,0.518268,0.519494,0.517206,0.516313,0.515425,0.514182,0.513064,0.512183,0.512074,0.509471,0.510413,0.511378,0.508993,0.508499,0.509499,0.507778,0.506582,0.507644,0.506492,0.508728,0.506722,0.508668,0.511519,0.510983,0.50951,0.511776,0.513629,0.515124,0.51429,0.518482,0.519538,0.522113,0.524569,0.529436,0.532123,0.536144,0.537676,0.545072,0.551342,0.557408,0.562603,0.568011,0.579297,0.586273,0.595202,0.60494,0.617419,0.625935,0.638816,0.656777,0.668723,0.684399,0.702941,0.721203,0.740341,0.757633,0.774475,0.788345,0.801681,0.8066,0.813014,0.816262,0.821714,0.821885,0.823638,0.818231,0.817136,0.812044,0.811869,0.809314,0.802038,0.797923,0.791057,0.7838,0.782822,0.775374,0.771899,0.762528,0.759973,0.754587,0.747702,0.742875,0.73873,0.73184,0.726124,0.721643,0.715755,0.71217,0.706259,0.701883,0.69765,0.692345,0.688974,0.683167,0.678736)
1)	tuple lightcurve-parameter-estimator.time_base = (0,0.000569,0.00114,0.001709,0.002279,0.002849,0.003418,0.003989,0.004559,0.005128,0.005698,0.006268,0.006837,0.007407,0.007977,0.008546,0.009116,0.009686,0.010255,0.010825,0.011395,0.011964,0.012534,0.013104,0.013673,0.014242,0.014812,0.015381,0.015951,0.016521,0.01709,0.01766,0.01823,0.018799,0.019369,0.019938,0.020508,0.021077,0.021647,0.022217,0.022786,0.023356,0.023925,0.024495,0.025064,0.025634,0.026204,0.026773,0.027343,0.027912,0.028482,0.029052,0.029621,0.030191,0.03076,0.03133,0.0319,0.032469,0.033039,0.033608,0.034178,0.034747,0.035317,0.035886,0.036456,0.037026,0.037595,0.0439,0.04447,0.045039,0.045608,0.046178,0.046747,0.047317,0.047886,0.048456,0.049026,0.049595,0.050165,0.050734,0.051304,0.051873,0.052443,0.053013,0.053583,0.054152,0.054722,0.055291,0.055861,0.05643,0.057,0.057569,0.058139,0.058708,0.059278,0.059847,0.060417,0.060987,0.061556,0.062126,0.062696,0.063265,0.063835,0.064404,0.064974,0.065543,0.066113,0.066682,0.067252,0.067821,0.068391,0.068961,0.06953,0.0701,0.070669,0.071239,0.071809,0.072379,0.072949,0.073518,0.074088,0.074657,0.075227,0.075797,0.076366,0.076935,0.077505,0.078075,0.078644,0.079214,0.079783,0.080353,0.080923,0.081492,0.082062,0.082632,0.083201,0.083771,0.08434,0.08491,0.085479,0.086049,0.086618,0.087188,0.087757,0.088327,0.088897,0.089466,0.090036,0.090605,0.091175,0.091744,0.092314,0.092884,0.093453,0.094023,0.094593,0.095162,0.095732,0.096302,0.096872,0.097441,0.09801,0.09858,0.099149,0.099719,0.100289,0.101241,0.10181,0.10238,0.102949,0.103519,0.104089,0.104658,0.105228,0.105797,0.106367,0.106937,0.107506,0.108075,0.108645,0.109215,0.109784,0.110354,0.110923,0.111493,0.112062,0.112632,0.113201,0.113771,0.114341,0.11491,0.11548,0.116049,0.116619,0.117189,0.117758,0.118328,0.118897,0.119467,0.120036,0.120606,0.121176,0.121745,0.122315,0.122885,0.123454,0.124024,0.124593,0.125163,0.125732,0.126302,0.126871,0.127441,0.128011,0.12858,0.12915,0.129719,0.130289,0.130858,0.131428,0.131998,0.132567,0.133137,0.133706,0.134276,0.134845,0.135415,0.135984,0.136554,0.137124,0.137693,0.138263,0.138832,0.139402,0.139972,0.140541,0.141111,0.141681,0.14225,0.14282,0.14339,0.143959,0.144529,0.145098,0.145668)
2)	lightcurve-parameter-estimator.spline_data = CubicSpline(time_base,rel_flux)
3)	int lightcurve-parameter-estimator.O = 2000
4)	lightcurve-parameter-estimator.t = np.linspace(0, 0.145668, num=int(O))
5)	lightcurve-parameter-estimator.signal = spline_data(t)
6)	float lightcurve-parameter-estimator.M = 1.9891E30
7)	float lightcurve-parameter-estimator.e1 = 0.70
8)	float lightcurve-parameter-estimator.e2 = 0.30
9)	float lightcurve-parameter-estimator.e3 = 0.30
10)	lightcurve-parameter-estimator.EDE_main = EllipticalDifferenceEquation(t,signal,M,e1,e2,e3)
11)	int lightcurve-parameter-estimator.N = 100
12)	list lightcurve-parameter-estimator.inputs_train = []
13)	list lightcurve-parameter-estimator.labels_train = []
14)	list lightcurve-parameter-estimator.features_train = []
15)	int lightcurve-parameter-estimator.max_features = 0
16)	int lightcurve-parameter-estimator.l = 0
17)	int lightcurve-parameter-estimator.delta_step = 15
18)	int lightcurve-parameter-estimator.m = 0
19)	int lightcurve-parameter-estimator.i = 1
20)	int lightcurve-parameter-estimator.j = 1
21)	float lightcurve-parameter-estimator.dist_main = EDE_main.dist+0.5
22)	lightcurve-parameter-estimator.first_derivative = np.gradient(dist_main)
23)	lightcurve-parameter-estimator.maxima = argrelextrema(dist_main,np.greater)
24)	lightcurve-parameter-estimator.minima = argrelextrema(dist_main,np.less)
25)	lightcurve-parameter-estimator.maxima0 = argrelextrema(first_derivative,np.greater)
26)	lightcurve-parameter-estimator.minima0 = argrelextrema(first_derivative,np.less)
27)	int lightcurve-parameter-estimator.features = 2*len(maxima[0])+2*len(minima[0])+len(maxima0[0])+len(minima0[0])
28)	list lightcurve-parameter-estimator.labels_out = [i/N,j/N,0.1+l*0.008,0.1+m*0.008]


lightcurve-trainer-start.py File Reference
AAAAAAAAAJAAAAAAAAAJNamespaces
0)	namespace lightcurve-trainer-start
Functions
0)	lightcurve-trainer-start.shuffle (inputs_train, labels_train, N_counter)
Variables
0)	lightcurve-trainer-start.inputs = tf.keras.Input(shape=(99,))
1)	lightcurve-trainer-start.dense = tf.keras.layers.Dense(128,activation="relu")
2)	lightcurve-trainer-start.x = dense(inputs)
3)	lightcurve-trainer-start.outputs = tf.keras.layers.Dense(5,activation="sigmoid")(x)
4)	lightcurve-trainer-start.model = tf.keras.Model(inputs=inputs, outputs=outputs)
5)	lightcurve-trainer-start.loss
6)	lightcurve-trainer-start.optimizer
7)	lightcurve-trainer-start.metrics
8)	lightcurve-trainer-start.inputs_train = np.load("inputs_train_data.npy")
9)	lightcurve-trainer-start.labels_train = np.load("labels_train_data.npy")
10)	lightcurve-trainer-start.N = len(inputs_train)
11)	int lightcurve-trainer-start.K = 128000
12)	int lightcurve-trainer-start.counter = 0
13)	lightcurve-trainer-start.hist = model.fit(inputs_train, labels_train, epochs=2)


lightcurve-trainer.py File Reference
AAAAAAAAAKAAAAAAAAAKNamespaces
0)	namespace lightcurve-trainer
Functions
0)	lightcurve-trainer.prompt (timeout)
1)	lightcurve-trainer.commandlinearguments ()
2)	lightcurve-trainer.shuffle (inputs_train, labels_train, N_counter)
3)	lightcurve-trainer.shuffle2 (inputs_train, labels_train)
4)	lightcurve-trainer.shuffle3 (inputs_train, labels_train)
Variables
0)	lightcurve-trainer.argv = commandlinearguments()
1)	lightcurve-trainer.inputs = tf.keras.Input(shape=(98,))
2)	lightcurve-trainer.dense = tf.keras.layers.Dense(128,activation="relu")
3)	lightcurve-trainer.x = dense(inputs)
4)	lightcurve-trainer.outputs = tf.keras.layers.Dense(7,activation="sigmoid")(x)
5)	lightcurve-trainer.model = tf.keras.Model(inputs=inputs, outputs=outputs)
6)	lightcurve-trainer.loss
7)	lightcurve-trainer.optimizer
8)	lightcurve-trainer.metrics
9)	int lightcurve-trainer.counter = 0
10)	lightcurve-trainer.inputs_train = np.load("inputs_train_data.npy")
11)	lightcurve-trainer.labels_train = np.load("labels_train_data.npy")
12)	lightcurve-trainer.checkpoint = tf.train.Checkpoint(model)
13)	lightcurve-trainer.load_status = model.load_weights("./checkpoint"+argv[1])
14)	lightcurve-trainer.status = checkpoint.restore("./checkpoint"+argv[1])
15)	int lightcurve-trainer.counter_shuffle = 0
16)	lightcurve-trainer.hist = model.fit(inputs_train, labels_train, epochs=2)


mouseclient.py File Reference
AAAAAAAAALAAAAAAAAALNamespaces
0)	namespace mouseclient
Functions
0)	mouseclient.Cube ()
1)	mouseclient.main ()
Variables
0)	tuple mouseclient.verticies
1)	tuple mouseclient.edges


pygame-sphere.py File Reference
AAAAAAAAAMAAAAAAAAAMNamespaces
0)	namespace pygame-sphere
Variables
0)	tuple pygame-sphere.display = (400, 300)
1)	tuple pygame-sphere.scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
2)	pygame-sphere.sphere = gluNewQuadric()
3)	pygame-sphere.viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
4)	bool pygame-sphere.run = True
5)	pygame-sphere.keypress = pygame.key.get_pressed()


sphere3.py File Reference
AAAAAAAAANAAAAAAAAANClasses
class sphere3.SphereNamespaces
0)	namespace sphere3
Functions
0)	sphere3.read_texture (filename)
1)	sphere3.read_3dtexture ()
2)	sphere3.update_point (coords, seed, MAP_SIZE)
3)	sphere3.generate_heightmap (map_size)
4)	sphere3.main ()
Variables
0)	int sphere3.last_time = 0
1)	int sphere3.SCALE = 10

Index
INDEX
