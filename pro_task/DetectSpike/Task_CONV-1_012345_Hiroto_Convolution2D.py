#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import __main__

def zeropad(imgdata, xmargin, ymargin):
    sz = np.shape(imgdata)
    imgdata_zpad = np.zeros([ymargin*2 + sz[0], xmargin*2 + sz[1]])
    imgdata_zpad[ymargin:ymargin+sz[0],xmargin:xmargin+sz[1]] = imgdata    
    return imgdata_zpad

#----------------------------------------------------------
# ガウス関数のカーネルを使用する方法
def myfunc_conv2D(ZZ, kernel):
    Ny,Nx = np.shape(ZZ)                            # 縦横のサイズを取得
    ZZ_filtered = np.copy(ZZ)                       # 元配列をコピー
    ZZ_ = np.copy(ZZ)
    filterable_limit = int(np.ceil(len(kernel)/2))  # kernelが配列内に収まるようにlimitを決めておく

    for ii in range(Ny):
        for jj in range(Nx):
            if (ii<filterable_limit) or (ii>Ny-filterable_limit):   # 上下端は0埋め
                ZZ_filtered[ii][jj] = 0
            elif (jj<filterable_limit) or (jj>Nx-filterable_limit): # 左右端は0埋め
                ZZ_filtered[ii][jj] = 0
            else:
                # フィルタリングする部分とその周辺を 5*5 の配列で切り出す -> 上下左右±2の範囲
                # きちんとndarrayに直しておく
                tmp_arr = np.array([[ZZ_[ii+mm][jj+ll] for ll in range(-2, 3)] for mm in range(-2, 3)])
                ZZ_filtered[ii][jj] = sum(sum(tmp_arr*kernel))          # 積和を取る

    return ZZ_filtered

#----------------------------------------------------------
# カーネルそのものをガウス関数とする方法
def myfunc_conv2D_2(xx, yy, ZZ, sigma):
    Nyy, Nxx = np.shape(ZZ)                         # 縦横の長さを取得
    ZZ_ = np.copy(ZZ)                               # 一応コピー
    XX2, YY2 = np.meshgrid(xx, yy)
    ZZ_filtered_2 = np.zeros([Nyy, Nxx])            # 結果の二次元配列を初期化

    for ii in range(Nyy):
        for jj in range(Nxx):
            posxx = xx[jj]                          # μを決める
            posyy = yy[ii]                          # μを決める
            eXX2 = ((XX2-posxx)/sigma)**2/2         # 指数部分のx
            eYY2 = ((YY2-posyy)/sigma)**2/2         # 指数部分のy
            gauss_func2 = 1/ (2*np.pi*sigma**2) * np.exp(-(eXX2 + eYY2))    # ガウス関数を定義
            norm_gauss_func2 = np.array(ZZ_[ii][jj] * gauss_func2/np.sum(gauss_func2))  # ガウス関数との積を取る
            ZZ_filtered_2 += norm_gauss_func2       # 全て足し合わせる

    return ZZ_filtered_2

#-----------------------------------------------------------



if  __name__ == "__main__": 
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
    kernel = np.array(gauss_func/np.sum(gauss_func))

    # =============================================================================
    # Load Image data
    # =============================================================================
    # img_array=plt.imread("ImageData.png")
    img_array=plt.imread("Dekachu.png")
    ZZ = img_array[:,:,0]
    Ny,Nx = np.shape(ZZ)
    xx = np.arange(0,Nx,1) - np.floor(Nx/2)      # x,y軸を定義する、
    yy = np.arange(0,Ny,1) - np.floor(Ny/2)

    # =============================================================================
    # convolution using spicy. 
    # =============================================================================
    ZZ_filtered_signalconvolve2D = signal.convolve2d(ZZ, kernel, boundary='symm', mode='same')

    # =============================================================================
    # convolution using myfunc
    # =============================================================================
    ZZ_filtered = myfunc_conv2D(ZZ, kernel)

    # =============================================================================
    # convolution 2nd method
    # =============================================================================
    ZZ_filtered_2 = myfunc_conv2D_2(xx, yy, ZZ, sigma)
        
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
    plt.imshow(ZZ_filtered)
    plt.ylabel('y position'); plt.xlabel('x position'); plt.title('D:2D convolution result \n using myfunc_conv2D')
    plt.subplot(3,2,4)
    plt.plot(ZZ_filtered - ZZ_filtered_signalconvolve2D); 
    plt.ylim([-1,1]); plt.xlabel('x position');plt.title('E:Difference (C-D)')
    # =============================================================================
    # F: show your own convolution result, and G: difference from C
    # =============================================================================
    plt.subplot(3,2,5)
    plt.imshow(ZZ_filtered_2)
    plt.ylabel('y position'); plt.xlabel('x position'); plt.title('F: 2D convolution result \n using myfunc_conv2D_2')
    plt.subplot(3,2,6)
    plt.plot(ZZ_filtered_2 - ZZ_filtered_signalconvolve2D)
    plt.ylim([-1,1]); plt.xlabel('x position');plt.title('G:Difference (C-F)')
    plt.show()
    # %%
