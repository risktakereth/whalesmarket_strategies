import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.colors import LinearSegmentedColormap



# ===================== User choices ==================

choix = 2 #1 donne affichage simple, 2 affichage complet
prix_eigen_maximale = 40
prix_eigen_wm_stable = 7.49
budget_init = 1000
prix_eth_init = 3500
prix_eigen_wm_eth = 8.48
prix_eth_min = prix_eth_init - 500
prix_eth_max = prix_eth_min + 100*prix_eigen_maximale



# ============ Creating matrice_stable and matrice_eth =============

# Définir la taille de la matrice
k = prix_eigen_maximale
rows, cols = k,k

matrice_stable = np.zeros((rows, cols))
matrice_eth = np.zeros((rows, cols))


# ==== matrice_stable ====


# Calcul préliminaires
budget_sept = 1000*1/1

nbr_eigen = budget_sept / prix_eigen_wm_stable

prix_max_eigen = 2*prix_eigen_wm_stable
protection = prix_max_eigen*nbr_eigen

for i in range(rows):
    for j in range(cols):
        valeur =  (i+1) * nbr_eigen
        if valeur > protection :
            valeur = protection
        matrice_stable[cols-1-i][j] = valeur


# ==== matrice_eth ====


# Calcul préliminaires

nbr_eigen = budget_init / prix_eigen_wm_eth


for i in range(rows):
    prix_eth_sept = prix_eth_min + i*100
    prix_max_eigen = 2*prix_eigen_wm_eth*prix_eth_sept/prix_eth_init
    
    protection = prix_max_eigen*nbr_eigen

    for j in range(cols):
        valeur =  (j+1) * nbr_eigen
        #print(valeur)
        if valeur > protection :
            valeur = protection
        else:
            a = 1
        matrice_eth[rows-1-j][i] = valeur



#print(matrice_eth)



# ==================== Calcul et affichage final =================

# Définir la taille de la matrice
rows, cols = k,k

# Créer une matrice de valeurs aléatoires pour illustration (vous pouvez remplir avec vos propres valeurs)
#matrix = np.random.rand(rows, cols)
matrix = matrice_eth - matrice_stable
#print(matrix)

# Définir les valeurs de l'axe vertical (de bas en haut)
vertical_axis = np.arange(1, rows + 1)[::-1]

# Définir les valeurs de l'axe horizontal (de gauche à droite)
horizontal_axis = np.linspace(3000, 6000, cols)




# Créer la heatmap
plt.figure(figsize=(10, 8))
vmin, vmax = matrix.min(), matrix.max()
if choix == 1 :
    norm = colors.TwoSlopeNorm(vmin=-1, vcenter=0, vmax=1)
    colors_list = [(1, 0, 0.1), (0, 0, 0), (0, 1, 0)]  # Vert, Blanc, Rouge
    cm = LinearSegmentedColormap.from_list('custom_cmap', colors_list, N=256)
elif choix == 2:
    norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=vmax)
    colors_list = [(1, 0, 0.1), (0, 0, 0), (0, 1, 0)]  # Vert, Blanc, Rouge
    cm = LinearSegmentedColormap.from_list('custom_cmap', colors_list, N=256)
plt.imshow(matrix, cmap=cm, aspect='auto', extent=[prix_eth_min, prix_eth_min+100*k, 1, k], norm=norm)
plt.colorbar(label='<= Stable meilleur                                              ETH meilleur =>')

# Ajouter les étiquettes des axes
plt.xlabel('Prix ETH')
plt.ylabel('Prix EIGEN')

# Afficher la heatmap
plt.title('Est-il préférable d acheter en ETH ou en stablecoin ?')
plt.show()