'''
Program:        emva1288lib.py - Librabry for the emva1288 v3.1 standard. 
Institut:       Max-Planck-Institut fuer Sonnensystemforschung
Adress:         Justus-von-Liebig-Weg 3, 37077 Goettingen, Germany
Author:         Julian Utehs
Maintainer:     Julian Utehs
E-mail:         utehs@mps.mpg.de

Description:    This librabry can be used for 

Copyricht:      Copyright (c) <2017> <Julian Utehs> 

Licence:        This software is licenced under the General Puplic Licence version 3 or later. For the original text see https://www.gnu.org/licenses/gpl.html or contact the program author. 
                The above copyright notice and the eventually given permission notice shall be included in all copies or substantial portions of the Software. 

Warranty:       THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

Version:        0.01 - Kick off
Date:           2017, 20. March

'''

import os as os
import sys as sys
import numpy as numpy

def meanValueOf2Images(imageA, imageB, verbose=False):
    '''Calculates the mean values of 2 images. Both images shall be given as numpy arrays.'''
    imageA_size = imageA.shape
    imageB_size = imageB.shape
    if (verbose):
        print("Image A dimensions:")
        print(imageA_size)
        print("Image B dimensions:")
        print(imageB_size)
    if ( (len(imageA_size) != len(imageB_size)) or (imageA_size[0] != imageB_size[0]) or (imageA_size[1] != imageB_size[1]) ):
        raise Exception("Dimensions of the images in meanValueOf2Images are not equal.")
        return 0
    else:
        image = imageA + imageB
    return (numpy.mean(image, dtype=numpy.float64)/2)

def meanImageOfNImages(imageN, verbose=False):
    '''Calculates the mean image of N images. Input shall be given as 3 dimensional numpy array. '''
    imageN_size = imageN.shape
    if (len(imageN_size) > 3):
        raise Exception("ImageN in meanImageOfNImages is not 3 dimensional.")
        return imageN
    elif (len(imageN_size) == 3): # Not secure here, a depth analysis is senseless if the image just have one frame
        image_x = imageN_size[2]
        image_y = imageN_size[1]
        image_z = imageN_size[0]
    else:
        return imageN
    meanImage  = numpy.zeros((image_y, image_x))
    for i in range(len(n)):
        pass
    return meanImage

def varianceValueOf2Images(imageA, imageB, verbose=False):
    '''Calculates the variance values of 2 images. Both images shall be given as numpy arrays.'''
    imageA_size = imageA.shape
    imageB_size = imageB.shape
    if (verbose):
        print("Image A dimensions:")
        print(imageA_size)
        print("Image B dimensions:")
        print(imageB_size)
    if ( (len(imageA_size) != len(imageB_size)) or (imageA_size[0] != imageB_size[0]) or (imageA_size[1] != imageB_size[1]) ):
        raise Exception("Dimensions of the images in meanValueOf2Images are not equal.")
        return 0
    else:
        image = imageA - imageB
        square = numpy.square(image)
        print(square)
        variance = numpy.mean(square, dtype=numpy.float64)
        print(variance)
        variance = variance/2
        print(variance)
        print("Variance alternative:")
        varinace = (     (  numpy.mean(  (numpy.square(image))  , dtype=numpy.float64)  )     /2     )
        print(variance)
    return (     (  numpy.mean(  (numpy.square(image))  , dtype=numpy.float64)  )     /2     )

    
def varianceValueOfNImages():
    pass
