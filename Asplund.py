import numpy as np
import os
__author__ = 'Jens-Kristian Krogager'

if 'VFITDATA' in os.environ.keys():
    datafile = os.environ['VFITDATA']+'/Asplund2009.dat'

else:
    source_dir = os.path.dirname(__file__)
    if source_dir != '':
        atomfile = source_dir + '/static/Asplund2009.dat'
    else:
        atomfile = 'static/Asplund2009.dat'

dt = [('element', 'S2'), ('N', 'f4'), ('N_err', 'f4'), ('N_m', 'f4'), ('N_m_err', 'f4')]
data = np.loadtxt(datafile, dtype=dt)

photosphere = dict()
meteorite = dict()

for element, N_phot, N_phot_err, N_met, N_met_err in data:
    photosphere[element] = [N_phot, N_phot_err]
    meteorite[element] = [N_met, N_met_err]

print "\n Loaded Solar abundances from Asplund et al. 2009  (photospheric)"
# print bold+"    The Chemical Composition of the Sun"+reset
# print " Annual Review of Astronomy and Astrophysics"
# print "             Vol. 47: 481-522"
# print ""
# print " Data available:  photosphere,  meteorite"
print ""
