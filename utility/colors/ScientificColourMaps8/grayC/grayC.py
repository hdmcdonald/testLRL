# 
#         grayC
#                   www.fabiocrameri.ch/colourmaps
from matplotlib.colors import LinearSegmentedColormap      
      
cm_data = [[0, 0, 0],      
           [0.0067245, 0.0067245, 0.0067245],      
           [0.014136, 0.014136, 0.014136],      
           [0.021325, 0.021325, 0.021325],      
           [0.028493, 0.028493, 0.028493],      
           [0.03585, 0.03585, 0.03585],      
           [0.042788, 0.042788, 0.042788],      
           [0.049375, 0.049376, 0.049376],      
           [0.055232, 0.055233, 0.055233],      
           [0.060739, 0.060739, 0.060739],      
           [0.065886, 0.065887, 0.065887],      
           [0.070724, 0.070725, 0.070725],      
           [0.075266, 0.075268, 0.075267],      
           [0.079586, 0.079588, 0.079588],      
           [0.083764, 0.083767, 0.083766],      
           [0.087719, 0.087721, 0.087721],      
           [0.09151, 0.091513, 0.091513],      
           [0.095184, 0.095187, 0.095186],      
           [0.098827, 0.098829, 0.098828],      
           [0.10251, 0.10251, 0.10251],      
           [0.10622, 0.10622, 0.10622],      
           [0.10991, 0.10991, 0.10991],      
           [0.11357, 0.11357, 0.11357],      
           [0.11721, 0.11721, 0.11721],      
           [0.12088, 0.12088, 0.12088],      
           [0.12457, 0.12457, 0.12457],      
           [0.12827, 0.12827, 0.12827],      
           [0.13195, 0.13195, 0.13195],      
           [0.13559, 0.13559, 0.13559],      
           [0.13926, 0.13926, 0.13926],      
           [0.14296, 0.14296, 0.14296],      
           [0.1466, 0.1466, 0.1466],      
           [0.15029, 0.15029, 0.15029],      
           [0.15393, 0.15393, 0.15393],      
           [0.15758, 0.15758, 0.15758],      
           [0.16127, 0.16127, 0.16127],      
           [0.16488, 0.16488, 0.16488],      
           [0.16854, 0.16854, 0.16854],      
           [0.17217, 0.17217, 0.17217],      
           [0.17579, 0.17579, 0.17579],      
           [0.17944, 0.17944, 0.17944],      
           [0.18305, 0.18305, 0.18305],      
           [0.18669, 0.18669, 0.18669],      
           [0.1903, 0.1903, 0.1903],      
           [0.19393, 0.19393, 0.19393],      
           [0.19752, 0.19752, 0.19752],      
           [0.20109, 0.20109, 0.20109],      
           [0.20472, 0.20472, 0.20472],      
           [0.20829, 0.20829, 0.20829],      
           [0.21189, 0.21189, 0.21189],      
           [0.21544, 0.21544, 0.21544],      
           [0.21902, 0.21902, 0.21902],      
           [0.22258, 0.22258, 0.22258],      
           [0.22614, 0.22614, 0.22614],      
           [0.22966, 0.22966, 0.22966],      
           [0.2332, 0.2332, 0.2332],      
           [0.23676, 0.23676, 0.23676],      
           [0.24025, 0.24025, 0.24025],      
           [0.24377, 0.24377, 0.24377],      
           [0.2473, 0.2473, 0.2473],      
           [0.2508, 0.2508, 0.2508],      
           [0.2543, 0.2543, 0.2543],      
           [0.25777, 0.25777, 0.25777],      
           [0.26126, 0.26126, 0.26126],      
           [0.26472, 0.26472, 0.26472],      
           [0.26818, 0.26818, 0.26818],      
           [0.27163, 0.27163, 0.27163],      
           [0.27509, 0.27509, 0.27509],      
           [0.27853, 0.27853, 0.27853],      
           [0.28196, 0.28196, 0.28196],      
           [0.28536, 0.28536, 0.28536],      
           [0.28879, 0.28879, 0.28879],      
           [0.29219, 0.29219, 0.29219],      
           [0.29558, 0.29558, 0.29558],      
           [0.29897, 0.29897, 0.29897],      
           [0.30233, 0.30233, 0.30233],      
           [0.30573, 0.30573, 0.30573],      
           [0.30909, 0.30909, 0.30909],      
           [0.31241, 0.31241, 0.31241],      
           [0.31577, 0.31577, 0.31577],      
           [0.31909, 0.31909, 0.31909],      
           [0.32242, 0.32242, 0.32242],      
           [0.32571, 0.32571, 0.32571],      
           [0.32904, 0.32904, 0.32904],      
           [0.33233, 0.33233, 0.33233],      
           [0.33561, 0.33561, 0.33561],      
           [0.33888, 0.33888, 0.33888],      
           [0.34215, 0.34215, 0.34215],      
           [0.3454, 0.3454, 0.3454],      
           [0.34864, 0.34864, 0.34864],      
           [0.35187, 0.35187, 0.35187],      
           [0.35511, 0.35511, 0.35511],      
           [0.35831, 0.35831, 0.35831],      
           [0.36152, 0.36152, 0.36152],      
           [0.36471, 0.36471, 0.36471],      
           [0.3679, 0.3679, 0.3679],      
           [0.37107, 0.37107, 0.37107],      
           [0.37425, 0.37425, 0.37425],      
           [0.37739, 0.37739, 0.37739],      
           [0.38054, 0.38054, 0.38054],      
           [0.38367, 0.38367, 0.38367],      
           [0.38679, 0.38679, 0.38679],      
           [0.3899, 0.3899, 0.3899],      
           [0.39301, 0.39301, 0.39301],      
           [0.3961, 0.3961, 0.3961],      
           [0.39917, 0.39917, 0.39917],      
           [0.40225, 0.40225, 0.40225],      
           [0.40532, 0.40532, 0.40532],      
           [0.40837, 0.40837, 0.40837],      
           [0.4114, 0.4114, 0.4114],      
           [0.41444, 0.41444, 0.41444],      
           [0.41747, 0.41747, 0.41747],      
           [0.42047, 0.42047, 0.42047],      
           [0.42347, 0.42347, 0.42347],      
           [0.42647, 0.42647, 0.42647],      
           [0.42946, 0.42946, 0.42946],      
           [0.43244, 0.43244, 0.43244],      
           [0.43541, 0.43541, 0.43541],      
           [0.43837, 0.43837, 0.43837],      
           [0.44132, 0.44132, 0.44132],      
           [0.44428, 0.44428, 0.44428],      
           [0.44722, 0.44722, 0.44722],      
           [0.45017, 0.45017, 0.45017],      
           [0.45311, 0.45311, 0.45311],      
           [0.45605, 0.45605, 0.45605],      
           [0.45899, 0.45899, 0.45899],      
           [0.46193, 0.46193, 0.46193],      
           [0.46487, 0.46487, 0.46487],      
           [0.46781, 0.46781, 0.46781],      
           [0.47076, 0.47076, 0.47076],      
           [0.4737, 0.4737, 0.4737],      
           [0.47667, 0.47667, 0.47667],      
           [0.47964, 0.47964, 0.47964],      
           [0.48261, 0.48261, 0.48261],      
           [0.48559, 0.48559, 0.48559],      
           [0.48859, 0.48859, 0.48859],      
           [0.4916, 0.4916, 0.4916],      
           [0.49462, 0.49462, 0.49462],      
           [0.49765, 0.49765, 0.49765],      
           [0.50069, 0.50069, 0.50069],      
           [0.50375, 0.50375, 0.50375],      
           [0.50682, 0.50682, 0.50682],      
           [0.50992, 0.50992, 0.50992],      
           [0.51303, 0.51303, 0.51303],      
           [0.51614, 0.51614, 0.51614],      
           [0.5193, 0.5193, 0.5193],      
           [0.52245, 0.52245, 0.52245],      
           [0.52563, 0.52563, 0.52563],      
           [0.52883, 0.52883, 0.52883],      
           [0.53204, 0.53204, 0.53204],      
           [0.53527, 0.53527, 0.53527],      
           [0.53853, 0.53853, 0.53853],      
           [0.54179, 0.54179, 0.54179],      
           [0.54509, 0.54509, 0.54509],      
           [0.5484, 0.5484, 0.5484],      
           [0.55173, 0.55173, 0.55173],      
           [0.55507, 0.55507, 0.55507],      
           [0.55843, 0.55843, 0.55843],      
           [0.56183, 0.56183, 0.56183],      
           [0.56523, 0.56523, 0.56523],      
           [0.56866, 0.56866, 0.56866],      
           [0.57211, 0.57211, 0.57211],      
           [0.57558, 0.57558, 0.57558],      
           [0.57906, 0.57906, 0.57906],      
           [0.58256, 0.58256, 0.58256],      
           [0.5861, 0.5861, 0.5861],      
           [0.58964, 0.58964, 0.58964],      
           [0.59321, 0.59321, 0.59321],      
           [0.5968, 0.5968, 0.5968],      
           [0.60041, 0.60041, 0.60041],      
           [0.60404, 0.60404, 0.60404],      
           [0.60769, 0.60769, 0.60769],      
           [0.61136, 0.61136, 0.61136],      
           [0.61505, 0.61505, 0.61505],      
           [0.61877, 0.61877, 0.61877],      
           [0.6225, 0.6225, 0.6225],      
           [0.62626, 0.62626, 0.62626],      
           [0.63004, 0.63004, 0.63004],      
           [0.63384, 0.63384, 0.63384],      
           [0.63766, 0.63766, 0.63766],      
           [0.6415, 0.6415, 0.6415],      
           [0.64536, 0.64536, 0.64536],      
           [0.64926, 0.64926, 0.64926],      
           [0.65315, 0.65315, 0.65315],      
           [0.65709, 0.65709, 0.65709],      
           [0.66104, 0.66104, 0.66104],      
           [0.66501, 0.66501, 0.66501],      
           [0.66902, 0.66902, 0.66902],      
           [0.67304, 0.67304, 0.67304],      
           [0.67708, 0.67708, 0.67708],      
           [0.68114, 0.68114, 0.68114],      
           [0.68523, 0.68523, 0.68523],      
           [0.68935, 0.68935, 0.68935],      
           [0.69348, 0.69348, 0.69348],      
           [0.69763, 0.69763, 0.69763],      
           [0.70181, 0.70181, 0.70181],      
           [0.70603, 0.70603, 0.70603],      
           [0.71025, 0.71025, 0.71025],      
           [0.7145, 0.7145, 0.7145],      
           [0.71878, 0.71878, 0.71878],      
           [0.72308, 0.72308, 0.72308],      
           [0.7274, 0.7274, 0.7274],      
           [0.73175, 0.73175, 0.73175],      
           [0.73612, 0.73612, 0.73612],      
           [0.74052, 0.74052, 0.74052],      
           [0.74495, 0.74495, 0.74495],      
           [0.74939, 0.74939, 0.74939],      
           [0.75387, 0.75387, 0.75387],      
           [0.75837, 0.75837, 0.75837],      
           [0.76288, 0.76288, 0.76288],      
           [0.76743, 0.76743, 0.76743],      
           [0.77201, 0.77201, 0.77201],      
           [0.77661, 0.77661, 0.77661],      
           [0.78123, 0.78123, 0.78123],      
           [0.78588, 0.78588, 0.78588],      
           [0.79055, 0.79055, 0.79055],      
           [0.79526, 0.79526, 0.79526],      
           [0.79999, 0.79999, 0.79999],      
           [0.80474, 0.80474, 0.80474],      
           [0.80952, 0.80952, 0.80952],      
           [0.81433, 0.81433, 0.81433],      
           [0.81916, 0.81916, 0.81916],      
           [0.82402, 0.82402, 0.82402],      
           [0.82892, 0.82892, 0.82892],      
           [0.83383, 0.83383, 0.83383],      
           [0.83877, 0.83877, 0.83877],      
           [0.84374, 0.84374, 0.84374],      
           [0.84875, 0.84875, 0.84875],      
           [0.85377, 0.85377, 0.85377],      
           [0.85883, 0.85883, 0.85883],      
           [0.86392, 0.86392, 0.86392],      
           [0.86903, 0.86903, 0.86903],      
           [0.87416, 0.87416, 0.87416],      
           [0.87933, 0.87933, 0.87933],      
           [0.88453, 0.88453, 0.88453],      
           [0.88976, 0.88976, 0.88976],      
           [0.89502, 0.89502, 0.89502],      
           [0.9003, 0.9003, 0.9003],      
           [0.90562, 0.90562, 0.90562],      
           [0.91096, 0.91096, 0.91096],      
           [0.91633, 0.91633, 0.91633],      
           [0.92173, 0.92173, 0.92173],      
           [0.92716, 0.92716, 0.92716],      
           [0.93262, 0.93262, 0.93262],      
           [0.93811, 0.93811, 0.93811],      
           [0.94363, 0.94363, 0.94363],      
           [0.94918, 0.94918, 0.94918],      
           [0.95476, 0.95476, 0.95476],      
           [0.96036, 0.96036, 0.96036],      
           [0.96599, 0.96599, 0.96599],      
           [0.97165, 0.97165, 0.97165],      
           [0.97733, 0.97733, 0.97733],      
           [0.98303, 0.98303, 0.98303],      
           [0.98876, 0.98876, 0.98876],      
           [0.9945, 0.9945, 0.9945],      
           [1, 1, 1]]      
      
grayC_map = LinearSegmentedColormap.from_list('grayC', cm_data)      
# For use of "viscm view"      
test_cm = grayC_map      
      
if __name__ == "__main__":      
    import matplotlib.pyplot as plt      
    import numpy as np      
      
    try:      
        from viscm import viscm      
        viscm(grayC_map)      
    except ImportError:      
        print("viscm not found, falling back on simple display")      
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',      
                   cmap=grayC_map)      
    plt.show()      
