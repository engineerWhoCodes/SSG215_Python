from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt
jetClub = {'Musa', 'Lade', 'Joseph', 'Timi', 'Yetunde', 'Kola'}
mathClub = {'Okoro', 'David', 'Joseph', 'Musa', 'Yetunde', 'Lade'}
#The venn2 function is used to plot the venn diagram
#The function takes as argument a list of two sets and plots the required diagram
venn2([jetClub, mathClub],
set_labels = ('JETCLUB', 'MATHSCLUB'),
set_colors = ('green', 'red'), alpha=0.8) #This is to set colors and opacity
venn2_circles([set(jetClub), set(mathClub)], linestyle='-.', linewidth=2, color='purple') #To change and style circles
plt.title('A venn diagram showing people who are in two different clubs')
plt.show()
intList = jetClub.intersection(mathClub)

