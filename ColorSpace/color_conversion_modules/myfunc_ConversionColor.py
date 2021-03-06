# %%
import numpy as np

# RGBとxyz間の変換
class RGB_and_xyz:
        def RGB2xyz(self, R, G, B):
                # ====================================
                # 任意のRGBの三刺激値(0~255)からxyz色度座標値を求める。
                # ====================================
                x, y, z = 0, 0, 0   # 求めるx,y,z

                R = R/255; G = G/255; B = B/255 # 0~1に正規化

                # RGBからCIE1931XYZ表色系への変換行列
                # -> 座標が変換後にXYZ軸に位置すること。白色点が全ての色から等距離(1/3)となること。Yが輝度値となること。
                Xrgb = [2.7689, 1.7517, 1.1302]
                Yrgb = [1.0, 4.5907, 0.0601]
                Zrgb = [0.0, 0.0565, 5.5943]

                to_XYZ_matrix = np.array([Xrgb, Yrgb, Zrgb])    # XYZへの変換行列
                RGB = np.array([R, G, B])                       # 変換元RGB値
                X, Y, Z = np.dot(to_XYZ_matrix, RGB.T)          # 内積をとる

                S = X+Y+Z       # X,Y,Zの総和

                x=X/S; y=Y/S; z=Z/S
                x = np.round(x, 6)
                y = np.round(y, 6)
                z = np.round(z, 6)

                return (x, y, z, Y)


        def xyL2RGB(self, x, y, L):   # 入力するx,yは高精度の値でないといけない。(少数6桁以上)
                # ====================================
                # 任意のxyの座標値と輝度値(cd/m^2)からRGB刺激値(0~255)を求める。
                # ====================================
                R, G, B = 0, 0, 0

                # 三刺激値XYZを求める
                X = (x/y)*L             # 
                Y = L                   # Yは輝度値
                Z = ((1-x-y)/y)*L       # Zはxとyから定まる

                to_RGB_matrix = np.array([[2.7689, 1.7517, 1.1302],     # RGBへの変換行列
                                        [1.0, 4.5907, 0.0601],
                                        [0.0, 0.0565, 5.5943]])
                to_RGB_matrix = np.linalg.inv(to_RGB_matrix)            # 逆行列を求める
                XYZ = np.array([X, Y, Z])                               # 変換元行列
                R, G, B = np.dot(to_RGB_matrix, XYZ.T)                  # 内積をとる

                R = int(R*255); G = int(G*255); B = int(B*255)         # 0~255の範囲に戻す
                
                return (R, G, B)


        def xyz_for_plot(self):     # xyzグラフ表示用関数
                x_arr=[]; y_arr=[]; z_arr=[]
                for i in range(1,256,16):
                        for j in range(1,256,16):
                                for k in range(1, 256, 16):
                                        x, y, z, Y = self.RGB2xyz(k, j, i)
                                        x_arr.append(x); y_arr.append(y); z_arr.append(z)
                return (x_arr, y_arr, z_arr)



# Luvとxyzの間の変換
class Luv_and_xyz:
        def RGB2Luv(self, R, G, B):     # 任意のRGB値からL*u*v*の座標値を求める
                # ====================================
                # RGBの三刺激値(0~255)からL*u*v*色度座標値を求める。
                # ====================================

                inst_RGB_and_xyz = RGB_and_xyz()        # インスタンス生成

                L=0; u=0; v=0       # 求めるL,u,v
                x, y, z, Y = inst_RGB_and_xyz.RGB2xyz(R, G, B)   # zは使わない。

                # Y, u', v'：試料物体の刺激値及び色度
                Y = 0               # Y : 輝度値
                ud = (4*x)/(-2*x + 12*y + 3)            # u'
                vd = (9*y)/(-2*x + 12*y + 3*z)            # v'

                '''
                Y0, u'0, v'0：基準白色面の刺激値及び色度（白色点における色度のこと。）
                u'0とv'0を定めるにはu'v'色度図を作成して白色点を調べる必要がある。
                (今回は2°標準観測者における標準光源Cの条件下で考える。 wikipedia)
                
                # 今回使用した(u'0,v'0)の値とY,Y0,L*の定義がきちんとなされていないので、
                # 方法が分かり次第、定義する。
                '''
                Y0 = 0              # Y0 : 輝度値
                ud0 = 0.2009        # ud0 : u'0
                vd0 = 0.4610        # vd0 : v'0

                # L*は物体色にのみ定義される.
                # L*のとる範囲は0~100
                # L_star = 116*(Y/Y0)**(-1/3) - 16  # L*を求める
                L_star = 50                         # よくわからなかったので、教科書のL*=50の場合でやってみる。
                u_star = 13*L_star*(ud - ud0)       # u*
                v_star = 13*L_star*(vd - vd0)       # v*

                return (L_star,u_star,v_star)



#%%

        # RGB->xyzの変換について、、

        # # 原刺激XYZのrgb系における色度座標（教科書のものを使用）
        # # Xrgb = (1.2750, -0.2778, 0.0028)
        # # Yrgb = (-1.7392, 2.761, -0.0279)
        # # Zrgb = (-0.7431, 0.1409, 1.6022)

        # CIE表色系の変換行列
        # # Xrgb=(2.7689, 1.7517, 1.1302)
        # # Yrgb=(1, 4.5907, 0.0601)
        # # Zrgb=(0, 0.0565, 5.5943)

        # 同じにならなかった。CIE_RGB（白色点E）      英語版wikiも見たらこれがCIE-standard
        # # X = 0.4898*R + 0.3101*G + 0.2001*B
        # # Y = 0.1769*R + 0.8124*G + 0.0107*B
        # # Z = 0.0000*R + 0.0100*G + 0.9903*B

        # sRGB（白色点 D65 (0.333, 0.333)）
        # # X = 0.4224*R 0.3576*G 0.1805*B
        # # Y = 0.2326*R 0.7152*G 0.0722*B
        # # Z = 0.0193*R 0.1192*G 0.9505*B

        # sRGB (白色点 C)
        # # X = 0.5778*R 0.1825*G 0.1902*B
        # # Y = 0.3070*R 0.6170*G 0.0761*B
        # # Z = 0.0181*R 0.0695*G 1.0015*B

# %%
# def rgb2xyz(R, G, B):
#         # ====================================
#         # 任意のRGBの三刺激値(0~255)からxyz色度座標値を求める。
#         # ====================================
#         x, y, z = 0, 0, 0   # 求めるx,y,z

#         R = R/255; G = G/255; B = B/255 # 0~1に正規化

#         # 原刺激XYZのrgb系における色度座標の初期化
#         Xr, Xg, Xb = (0, 0, 0)
#         Yr, Yg, Yb = (0, 0, 0)
#         Zr, Zg, Zb = (0, 0, 0)

#         # 原刺激XYZのrgb系における色度座標（教科書のものを使用）
#         Xrgb = (1.2750, -0.2778, 0.0028)
#         Yrgb = (-1.7392, 2.761, -0.0279)
#         Zrgb = (-0.7431, 0.1409, 1.6022)

#         # 色光CがX,Y,Zのいずれかの軸に一致している場合 + 色光Cが基礎刺激である場合を考える
#         # Xを求める(係数行列)
#         valX = [[Yrgb[0], Yrgb[1], Yrgb[2]],\
#                 [Zrgb[0], Zrgb[1], Zrgb[2]],\
#                 [1, 1, 1]]
#         ansX = [0, 0, 1]

#         # # Yを求める(係数行列)
#         valY = [[Xrgb[0], Xrgb[1], Xrgb[2]],\
#                 [Zrgb[0], Zrgb[1], Zrgb[2]],\
#                 [1, 1, 1]]
#         ansY = [0, 0, 1]

#         # # Zを求める(係数行列)
#         valZ = [[Xrgb[0], Xrgb[1], Xrgb[2]],\
#                 [Yrgb[0], Yrgb[1], Yrgb[2]],\
#                 [1, 1, 1]]
#         ansZ = [0, 0, 1]

#         # # 連立方程式を解いて、XYZそれぞれの係数を算出する
#         Xr, Xg, Xb = np.round(solve(valX, ansX), 5)
#         Yr, Yg, Yb = np.round(solve(valY, ansY), 5)
#         Zr, Zg, Zb = np.round(solve(valZ, ansZ), 5)

#         # # 色光Cの三刺激値RGBが与えられた時のXYZの刺激値
#         X = (Xr*R + Xg*G + Xb*B)
#         Y = (Yr*R + Yg*G + Yb*B)
#         Z = (Zr*R + Zg*G + Zb*B)

#         # X,Y,Zの総和
#         S = X+Y+Z

#         x=X/S; y=Y/S; z=Z/S

#         return x, y, z, Y

# %%
