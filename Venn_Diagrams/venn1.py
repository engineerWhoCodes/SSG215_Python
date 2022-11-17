#Using python to create a venn diagram of two sets and intersections.
from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt
#Creating a set of authors available in the library
authorsLib = {
    'Fagunwa', 'Achebe', 'Shakespeare', 'Milton', 'Dante', 'Adichie', 'Soyinka', 'Clark', 'Saro Wiwa', 'Ngugi', 'Nwanko', 'Austen', 'Eliot', 'Hardy', 'Bunyan', 'Tutuola', 'Delano', 'Ulasi', 'Odunjo'}
#The sets of authors I wish to read
myList = {
    'Olabode', 'Yuppie', 'Adamu', 'Tho', 'Adichie', 'Achebe', 'Soyinka', 'Nwanko', 'Bronte', 'Rakumi', 'Yinka', 'Loto', 'Mu'
}
venn2([set(authorsLib), set(myList)],
set_labels= ('Available authors', 'My lists'),
set_colors= ('yellow', 'red'), alpha=0.4)

venn2_circles([set(authorsLib), set(myList)], linestyle=':', linewidth=1, color='green')

plt.title('Checking Book list against available ones')
plt.show()
listInt = authorsLib.intersection(myList)
