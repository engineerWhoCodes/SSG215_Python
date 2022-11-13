import matplotlib_venn as venn
import matplotlib.pyplot as plt
jetClub = {'Musa', 'Lade', 'Joseph', 'Timi', 'Yetunde', 'Kola'}
mathClub = {'Okoro', 'David', 'Joseph', 'Musa', 'Yetunde', 'Lade'}
#The venn2 function is used to plot the venn diagram
#The function takes as argument a list of two sets and plots the required diagram
venn.venn2([jetClub, mathClub],
set_labels = ('JETCLUB', 'MATHSCLUB'),
set_colors = ('green', 'red'))
plt.title('A venn diagram showing people who are in two different clubs')
plt.show()
