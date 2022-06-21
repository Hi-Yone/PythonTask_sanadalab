# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def zeropad(imgdata, xmargin, ymargin):
    sz = np.shape(imgdata)      # (y, x)
    imgdata_zpad = np.zeros([ymargin*2 + sz[0], xmargin*2 + sz[1]])     # sz[0]:yの大きさ
    imgdata_zpad[ymargin:ymargin+sz[0],xmargin:xmargin+sz[1]] = imgdata # ゼロにするのではなく、ゼロになっているところに元データをはめこむ   
    return imgdata_zpad

def myfunc_conv2D(ZZ, kernel):
    # Compute convolution WITHOUT using built-in signal.convolve2D command
    # get size information from kernel and imagedata
    Ny, Nx = np.shape(ZZ)
    ZZ_filtered = np.zeros([Ny,Nx])             # imgと同じサイズの0埋め配列を用意
    sz_kernel = np.shape(kernel)                # カーネルの大きさを取得
    x_margin = int(np.floor(sz_kernel[1]/2))    # カーネルのx軸方向の大きさを2で割る -> サイズ外判定に使用
    y_margin = int(np.floor(sz_kernel[0]/2))    # カーネルのy軸方向の大きさを2で割る -> サイズ外判定に使用
    # enlarge image data, ZZ based on size of kernel
    ZZ_zpad = zeropad(ZZ, x_margin, y_margin)   # 範囲外を0埋め

    # convolve filter to data array.
    for ix in range(Nx):
        for iy in range(Ny):
            ix_centr = ix + x_margin
            iy_centr = iy + y_margin
            curr_ZZ = ZZ_zpad[ iy_centr - y_margin : iy_centr + y_margin + 1 , ix_centr - x_margin : ix_centr + x_margin + 1 ]
            ZZ_filtered[iy][ix] = np.sum(curr_ZZ*kernel)
    return ZZ_filtered

def Generate_Gauss_Kernel(xx, yy, posx, posy, sigma):
    XX, YY = np.meshgrid(xx, yy)
    eXX =((XX-posx)/sigma)**2/2
    eYY =((YY-posy)/sigma)**2/2
    # compute 2D gaussian
    ZZ = np.exp(-(eXX+eYY))
    # normalize ZZ
    kernel = ZZ/np.sum(ZZ)
    return kernel

# ガウス関数のカーネルを使用する方法
def myconv2D_2(ZZ, kernel):
    Ny,Nx = np.shape(ZZ)                            # 縦横のサイズを取得
    ZZ_filtered = np.copy(ZZ)                       # 元配列をコピー
    ZZ_ = np.copy(ZZ)
    filterable_limit = int(np.ceil(len(kernel)/2))  # kernelが配列内に収まるようにlimitを決めておく

    for ii in range(Ny):
        for jj in range(Nx):
            if (ii<filterable_limit) or (ii>Ny-filterable_limit):   # 上下端は0埋め
                ZZ_filtered[ii][jj] = ZZ_[ii][jj]
            elif (jj<filterable_limit) or (jj>Nx-filterable_limit): # 左右端は0埋め
                ZZ_filtered[ii][jj] = ZZ_[ii][jj]
            else:
                # フィルタリングする部分とその周辺を 5*5 の配列で切り出す -> 上下左右±2の範囲
                # きちんとndarrayに直しておく
                tmp_arr = np.array([[ZZ_[ii+mm][jj+ll] for ll in range(-10, 11)] for mm in range(-10, 11)])
                ZZ_filtered[ii][jj] = sum(sum(tmp_arr*kernel))          # 積和を取る

    return ZZ_filtered

plt.close("all")
# =============================================================================
# Load Image data
# =============================================================================
# filename = "wally_img"
# filename = "char_img"
filename = "text_img"
img_array=plt.imread("./images_forConv/" + filename + ".png")

ZZ = img_array[:,:,0]
Ny,Nx = np.shape(ZZ)
xx = np.linspace(-50,50,Nx)
incr_ = xx[1]-xx[0]
yy = np.arange(0,Ny,1)*incr_
yy = yy - max(yy)/2
xmax = max(np.abs(xx))

# =============================================================================
# Generate kernel
# =============================================================================
x = np.append(np.flip(-np.arange(incr_,5, incr_)), np.arange(0,5, incr_))
y = np.append(np.flip(-np.arange(incr_,5, incr_)), np.arange(0,5, incr_))
XX, YY = np.meshgrid(x, y)
sigma = 0.75
posx = 0 # set x position and y position independently
posy = 0
eXX =((XX-posx)/sigma)**2/2
eYY =((YY-posy)/sigma)**2/2
# compute 2D gaussian
ZZ = np.exp(-(eXX+eYY))
# normalize ZZ
kernel = ZZ/np.sum(ZZ)
kernel2 = np.tile(kernel,[3,1,1])

# =============================================================================
# convolution using spicy. 
# =============================================================================
temp = np.shape(img_array)
ZZ_filtered_signalconvolve2D = np.zeros(np.shape(img_array))
for ii in range(temp[2]):
    ZZ_filtered_signalconvolve2D[:,:,ii] = signal.convolve2d(img_array[:,:,ii], kernel, boundary='symm', mode='same')    # 各色チャネルにカーネルをかける必要あり

# =============================================================================
# convolution 2nd method
# =============================================================================
ZZ_filtered_2 = np.zeros(np.shape(img_array))
for ii in range(temp[2]):
    ZZ_filtered_2[:,:,ii] = myfunc_conv2D(img_array[:,:,ii], kernel)    # 各色チャネルにカーネルをかける必要あり



# =============================================================================
# Plot data
# =============================================================================
fig_ = plt.figure(figsize=(12,8))
plt.subplots_adjust(wspace=0.4, hspace=0.6)
# =============================================================================
# A: Plot kernel
# =============================================================================
plt.subplot(2,2,1)
plt.imshow(kernel, extent=[-5,5,-5,5])
plt.ylabel('y position'); plt.xlabel('x position'); plt.title('A:Gaussian Kernel')
# =============================================================================
# B: show original data 
# =============================================================================
plt.subplot(2,2,2)
plt.imshow(img_array, extent=[min(xx),max(xx),min(yy),max(yy)])
plt.ylabel('y position'); plt.xlabel('x position'); plt.title('B:2D image data')
# =============================================================================
# C: show convolution results, signal
# =============================================================================
plt.subplot(2,2,3)
plt.imshow(ZZ_filtered_signalconvolve2D, extent=[min(xx),max(xx),min(yy),max(yy)])
plt.ylabel('y position'); plt.xlabel('x position'); plt.title('C:2D convolution result \n using Signal')
# =============================================================================
# F: show your own convolution result, and G: difference from C
# =============================================================================
plt.subplot(2,2,4)
plt.imshow(ZZ_filtered_2, extent=[min(xx),max(xx),min(yy),max(yy)])
plt.ylabel('y position'); plt.xlabel('x position'); plt.title('D: 2D convolution result \n using myfunc_conv2D_2')



# =============================================================================
# 前回自分が作った関数が正常に動作しているか確認
# =============================================================================
# ZZ_filtered_3 = np.zeros(np.shape(img_array))
# for ii in range(temp[2]):
#     ZZ_filtered_3[:,:,ii] = myconv2D_2(img_array[:,:,ii], kernel) 

# plt.subplot(2,2,6)
# plt.imshow(ZZ_filtered_3, extent=[min(xx),max(xx),min(yy),max(yy)])
# plt.ylabel('y position'); plt.xlabel('x position'); plt.title('E: Neural Image \n using myfunc_conv2D_3')

plt.tight_layout()
plt.show()

# %%
