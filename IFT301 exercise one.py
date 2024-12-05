# Name : Adekeye Opemipo Ayokunle
# Matic-Number : RUN/IFT/22/13158

import matplotlib.pyplot as pltt

items = ['Spinach', 'Sausage', 'Prawns', 'Pineapple', 'Mushroom']
proportions = [0.27, 0.20, 0.12, 0.27, 0.15]
pltt.barh(items, proportions, color='purple')
pltt.xlabel('Proportion of Total')
pltt.ylabel('Items')
pltt.title('Proportions of Items')
pltt.show()
