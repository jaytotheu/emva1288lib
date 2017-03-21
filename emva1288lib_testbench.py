'''
Program:        emva1288lib_testbench.py - Testbench for emva1288lib.py.
Institut:       Max-Planck-Institut fuer Sonnensystemforschung
Adress:         Justus-von-Liebig-Weg 3, 37077 Goettingen, Germany
Author:         Julian Utehs
Maintainer:     Julian Utehs
E-mail:         utehs@mps.mpg.de

Description:    This program takes a document and removes the double empty lines. 

Copyricht:      Copyright (c) <2014> <Max-Planck-Institute for solar system research> 

Licence:        This software is licenced under the General Puplic Licence version 3 or later. For the original text see https://www.gnu.org/licenses/gpl.html or contact the program author. 
                The above copyright notice and the eventually given permission notice shall be included in all copies or substantial portions of the Software. 

Warranty:       THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

Version:        0.01 - Kick off
Date:           2017, 21. March
'''

import os
import sys as sys
import string as string
import numpy as np
import emva1288lib as emva

def getSamples(Nimages, inttime, bright):
    '''Returns images in 20x20 format with random noise and maximum value of 1023. (2^10)'''
    image = np.zeros((20, 20), np.int32)
    readout_noise = np.random.random_integers(0,10, (20,20))
    if (int(inttime/5) > 1000):
        dark_current_lower_limit = 1000
    else:
        dark_current_lower_limit = int(inttime/5)
    dark_current  = np.random.random_integers( dark_current_lower_limit, 2*int(inttime/5),  (20,20))
    if (bright):
        grey_value = np.random.poisson(int(inttime), (20,20))
    else: 
        grey_value = np.zeros((20, 20), np.int32)
    #print(image)
    #print(readout_noise)
    #print(dark_current)
    #print(grey_value)
    image = image + readout_noise + dark_current + grey_value
    image = np.clip(image, 0, 1023)
    return image

def startAnalysis():
    imageA = getSamples(1, 1000, False)
    imageB = getSamples(1, 1000, False)
    image_mean = emva.meanValueOf2Images(imageA, imageB, True)
    print(image_mean)
    image_var = emva.varianceValueOf2Images(imageA, imageB)
    print(image_var)
#    imageA = getSamples(1, 400, True)
#    imageB = getSamples(1, 400, True)
#    image_mean = emva.meanValueOf2Images(imageA, imageB, True)
#    print(image_mean)
#    imageA = getSamples(1, 200, True)
#    imageB = getSamples(1, 200, True)
#    image_mean = emva.meanValueOf2Images(imageA, imageB, True)
#    print(image_mean)

    return 0



def main(argv):
    '''Define all variables that are needed for the rest of the analysis. These might be handled in the future in a gui. Please do not apply of different image types. This won't lead to an error, but the data may not be valid. '''
    version = '0.1'
    src_path = ''
    work_path = ''
    lookup_path = ''
    grafic_format = 'png'
    details = False
    recursive = False
    search_source = True
    wait_search = False
    depth_analysis = False
    colours=['r*-','g<-','m+-','k>-','bo-','y*-','c*-','b<-','r>-','k<-','g<-','m<-','y<-','c>-','bo-','ro-']
    try:
        for i in range(len(argv)):
            if (search_source == True):
                if (os.path.isdir(argv[i]) == True):
                    if (wait_search == True):
                        wait_search = False
                    else:
                        src_path = argv[i]
                        search_source = False
#            if (argv[i] == '-r') or (argv[i] == '--recursive'):
#                recursive = True
            if (argv[i] == '--details'):
                details = True
            if (argv[i] == '-o') or (argv[i] == '--output'):
                try:
                    work_path = argv[i+1]
                    if (os.path.isdir(work_path) == True):
                        #print (('Working directory is: ' + work_path))
                        wait_search = True
                    else:
                        print ('Error: Working path does not exist.')
                        return False
                except:
                    print ('Error: No Working directory.')
                    # return False OR work_path = src_path
            if (argv[i] == '--help'):
                printHelp(version)
                return False
    except:
        print ('emva1288lib_testbench.py: Missing operands.')
        print ('Try: \'python3.5 emva1288lib_testbench.py --help \' for more information.')
        return False

    if (bool(src_path) == False):
        print ('Source path not found.')
#        return False
    if (bool(work_path) == False): # An empty string is False, if len(work_path) == 0
        work_path = src_path
    work_path = os.path.normpath(os.path.abspath(work_path)) + os.sep
    os.chdir(work_path)
#    print ('Details ?:')
#    print (details)
    
    startAnalysis()
    return 0

if __name__ == '__main__':
    main(sys.argv)

