# -*- coding: utf-8 -*-
# =============================================================================
# Example code of 2-D convolution using spicy/signals, and handmade function
# For excercise class 2021
# coded by Taka Sanada, 5/22/2021
# =============================================================================

#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def zeropad(imgdata, xmargin, ymargin):
    sz = np.shape(imgdata)
    imgdata_zpad = np.zeros([ymargin*2 + sz[0], xmargin*2 + sz[1]])
    imgdata_zpad[ymargin:ymargin+sz[0],xmargin:xmargin+sz[1]] = imgdata    
    return imgdata_zpad

#----------------------------------------------------------
def myfunc_conv2D(ZZ, kernel):
    # Compute convolution WITHOUT using built-in signal.convolve2D command
    # get size information from kernel and imagedata
    Ny, Nx = np.shape(ZZ)
    ZZ_filtered = np.zeros([Ny,Nx])
    sz_kernel = np.shape(kernel)
    x_margin = int(np.floor(sz_kernel[1]/2))
    y_margin = int(np.floor(sz_kernel[0]/2))
    # enlarge image data, ZZ based on size of kernel
    ZZ_zpad = zeropad(ZZ, x_margin, y_margin)     
    # convolve filter to data array.
    for ix in range(Nx):
        for iy in range(Ny):
            ix_centr = ix + x_margin
            iy_centr = iy + y_margin
            curr_ZZ = ZZ_zpad[ iy_centr - y_margin : iy_centr + y_margin + 1 , ix_centr - x_margin : ix_centr + x_margin + 1 ]
            ZZ_filtered[iy][ix] = np.sum(curr_ZZ*kernel)

    return ZZ_filtered

def Generate_Gauss_Kernel(XX, YY, posx, posy, sigma):
    eXX =((XX-posx)/sigma)**2/2
    eYY =((YY-posy)/sigma)**2/2
    # compute 2D gaussian
    ZZ = np.exp(-(eXX+eYY))
    # normalize ZZ
    kernel = ZZ/np.sum(ZZ)
    return kernel

# =============================================================================
# convert axis based on  frequency
# =============================================================================
sampling_freq = 0.5
sampling_interval = 1/ sampling_freq
x = np.arange(0, 5+sampling_freq, sampling_interval)
# print(x)

# =============================================================================
# convert axis based on sampling number and range
# =============================================================================
x_max = 5
x_min = -5
x_0 = np.arange(0, 5, 1)
sampling_interval = (x_max-x_min)/(len(x_0)-1)
x = np.arange(-5, 5+sampling_interval, sampling_interval)
# print(x)


# =============================================================================
# axis in 2-D
# =============================================================================
Xsize = 10
Ysize = 10
x_pixels = np.arange(0, Xsize, 1); n_x = len(x_pixels)
y_pixels = np.arange(0, Ysize, 1); n_y = len(y_pixels)
x_max = 5
x_min = -5
sampling_interval = (x_max-x_min)/(n_x-1)
x = np.arange(x_min, x_max+sampling_interval, sampling_interval)
y = np.arange(0, sampling_interval*n_y, sampling_interval)
y = y - max(y)/2
XX,YY = np.meshgrid(x, y)
posx, posy, sigma = 0, 0, 2

ZZ = Generate_Gauss_Kernel(XX, YY, posx, posy, sigma)

# plt.figure
# plt.pcolor(XX, YY, ZZ)  # 画像表示 imshowでも可
# plt.axis("equal")


# =============================================================================
# move kernel
# =============================================================================
plt.figure(figsize=(10, 10))
ifig = 1
for jj in range(len(y)):
    for ii in range(len(x)):
        temp_sigma = np.sqrt(x[ii]**2+y[jj]**2)/6 + 0.1
        plt.subplot(Xsize, Ysize, ifig); ifig+=1
        posx, posy , sigma = x[ii], y[jj], temp_sigma
        ZZ = Generate_Gauss_Kernel(XX, YY, posx, posy, sigma)
        plt.pcolor(XX, YY, ZZ)
        plt.axis("equal")


import __main__

if __name__ == '__main__':
    
    # plt.close("all")
    # # =============================================================================
    # # Generate kernel
    # # =============================================================================
    # x = np.linspace(-2,2, 5)
    # y = np.linspace(-2,2, 5)
    # XX, YY = np.meshgrid(x, y)
    # sigma = 0.75
    # posx = 0 # set x position and y position independently
    # posy = 0
    # eXX =((XX-posx)/sigma)**2/2
    # eYY =((YY-posy)/sigma)**2/2
    # # compute 2D gaussian
    # ZZ = np.exp(-(eXX+eYY))
    # # normalize ZZ
    # kernel = ZZ/np.sum(ZZ)
    # # =============================================================================
    # # Load Image data
    # # =============================================================================
    # img_array=plt.imread("./DetectSpike/ImageData.png")
    # ZZ = img_array[:,:,0]
    # Ny, Nx = np.shape(ZZ)
    # xx = np.arange(0,Nx,1)- np.floor(Nx/2)
    # yy = np.arange(0,Ny,1)- np.floor(Ny/2)
    # #------------------------
    # XX,YY = np.meshgrid(xx,yy)
    # # =============================================================================
    # # convolution using spicy. 
    # # =============================================================================
    # ZZ_filtered_signalconvolve2D = signal.convolve2d(ZZ, kernel, boundary='symm', mode='same')

    # # =============================================================================
    # # convolution using myfunc
    # # =============================================================================
    # ZZ_filtered = myfunc_conv2D(ZZ, kernel)

    # # =============================================================================
    # # Plot data
    # # =============================================================================
    # fig_ = plt.figure(figsize=(8,10))
    # plt.subplots_adjust(wspace=0.4, hspace=0.6)
    # # =============================================================================
    # # A: Plot kernel
    # # =============================================================================
    # plt.subplot(3,3,1)
    # plt.imshow(kernel)
    # plt.ylabel('y position'); plt.xlabel('x position'); plt.title('A:5x5 2D filter')
    # # =============================================================================
    # # B: show original data 
    # # =============================================================================
    # plt.subplot(3,3,2)
    # plt.imshow(ZZ)
    # plt.ylabel('y position'); plt.xlabel('x position'); plt.title('B:2D image data')
    # # =============================================================================
    # # C: show convolution results, signal
    # # =============================================================================
    # plt.subplot(3,3,3)
    # plt.imshow(ZZ_filtered_signalconvolve2D)
    # plt.ylabel('y position'); plt.xlabel('x position'); plt.title('C:2D convolution result \n using Signal')
    # # =============================================================================
    # # D: show your own convolution result, and E: difference from C
    # # =============================================================================
    # plt.subplot(3,2,3)
    # plt.imshow(ZZ_filtered)
    # plt.ylabel('y position'); plt.xlabel('x position'); plt.title('D:2D convolution result \n using myfunc_conv2D')
    # plt.subplot(3,2,4)
    # plt.plot(ZZ_filtered - ZZ_filtered_signalconvolve2D); plt.title('E:Difference (C-D)')
    # plt.ylim([-1,1]); plt.xlabel('x position');
    # # =============================================================================
    # # F: show your own convolution result, and G: difference from C
    # # =============================================================================
    # plt.subplot(3,2,5)
    # plt.ylabel('y position'); plt.xlabel('x position'); plt.title('F: 2D convolution result \n using myfunc_conv2D_2')
    # plt.subplot(3,2,6)
    # plt.ylim([-1,1]); plt.xlabel('x position');plt.title('G:Difference (C-F)')

    plt.show()
    

# %%
