# ガウス関数を使う(step3)
# ガウス関数を使用したフィルタリング先の画像と同じ大きさの画像(kernel)をいちいち作って内積
# ↑ generate_gauss_kernelという関数を作ってn*mのサイズのカーネルを作成する。


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
# ガウス関数を使ったカーネルを使用する方法
def myfunc_conv2D(ZZ, kernel):  # ZZ:ガウシアンを計算する関数（x,yを持つ）
    Ny,Nx = np.shape(ZZ)
    ZZ_filtered = []

    for ii in range(Ny):
        for jj in range(Nx):
            if (ii == 0 | ii == Ny):
                ZZ_filtered.append(0)
            elif (jj == 0 | jj == Nx):
                ZZ_filtered.append(0)
            else:
                ZZ_filtered.append(kernel * ZZ[ii][jj])
    return ZZ_filtered

#----------------------------------------------------------
# カーネルそのものをガウス関数とする方法
# def myfunc_conv2D_2(xx, yy, ZZ, sigma):

#     return ZZ_filtered_2


plt.close("all")
# =============================================================================
# Generate kernel
# =============================================================================
x = np.linspace(-2,2, 5)
y = np.linspace(-2,2, 5)
XX, YY = np.meshgrid(x, y)
sigma = 0.75
posx = 0 # set x position and y position independentlyO
posy = 0
eXX =((XX-posx)/sigma)**2/2
eYY =((YY-posy)/sigma)**2/2
# compute 2D gaussian
gauss_func = np.exp(-(eXX+eYY))
# normalize gauss_func
kernel = gauss_func/np.sum(gauss_func)

# =============================================================================
# Load Image data
# =============================================================================
img_array=plt.imread("ImageData.png")
ZZ = img_array[:,:,0]
Ny,Nx = np.shape(ZZ)
xx = np.arange(0,Nx,1)- np.floor(Nx/2)      # x,y軸を定義する、
yy = np.arange(0,Ny,1)- np.floor(Ny/2)

# =============================================================================
# convolution using spicy. 
# =============================================================================
ZZ_filtered_signalconvolve2D = signal.convolve2d(ZZ, kernel, boundary='symm', mode='same')

# =============================================================================
# convolution using myfunc
# =============================================================================
ZZ_filtered = myfunc_conv2D(ZZ, kernel)
print(len(ZZ_filtered[0]), len(ZZ_filtered[1]), len(ZZ_filtered[2]), len(ZZ_filtered[3]))
print(len(ZZ_filtered))

# =============================================================================
# convolution 2nd method
# =============================================================================
# ZZ_filtered_2 = myfunc_conv2D_2(xx, yy, ZZ, sigma):

    
# =============================================================================
# Plot data
# =============================================================================
fig_ = plt.figure(figsize=(8,10))
plt.subplots_adjust(wspace=0.4, hspace=0.6)
# =============================================================================
# A: Plot kernel
# =============================================================================
plt.subplot(3,3,1)
plt.imshow(kernel)
plt.ylabel('y position'); plt.xlabel('x position'); plt.title('A:5x5 2D filter')
# =============================================================================
# B: show original data 
# =============================================================================
plt.subplot(3,3,2)
plt.imshow(ZZ)
plt.ylabel('y position'); plt.xlabel('x position'); plt.title('B:2D image data')
# =============================================================================
# C: show convolution results, signal
# =============================================================================
plt.subplot(3,3,3)
plt.imshow(ZZ_filtered_signalconvolve2D)
plt.ylabel('y position'); plt.xlabel('x position'); plt.title('C:2D convolution result \n using Signal')
# =============================================================================
# D: show your own convolution result, and E: difference from C
# =============================================================================
plt.subplot(3,2,3)
# plt.imshow(ZZ_filtered)
plt.ylabel('y position'); plt.xlabel('x position'); plt.title('D:2D convolution result \n using myfunc_conv2D')
plt.subplot(3,2,4)
# plt.plot(ZZ_filtered - ZZ_filtered_signalconvolve2D); 
plt.ylim([-1,1]); plt.xlabel('x position');plt.title('E:Difference (C-D)')
# =============================================================================
# F: show your own convolution result, and G: difference from C
# =============================================================================
plt.subplot(3,2,5)
# plt.imshow(ZZ_filtered_2)
plt.ylabel('y position'); plt.xlabel('x position'); plt.title('F: 2D convolution result \n using myfunc_conv2D_2')
plt.subplot(3,2,6)
# plt.plot(ZZ_filtered_2 - ZZ_filtered_signalconvolve2D);
plt.ylim([-1,1]); plt.xlabel('x position');plt.title('G:Difference (C-F)')

plt.show()
# save data
# plt.savefig("Task_CONV-1_012345_Yourname_Convolution2D.pdf")
# %%
