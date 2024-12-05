# Name: Adekeye Opemipo Ayokunle
# Matric-No: RUN/IFT/22/13158

import matplotlib.pyplot as pl

with_music = [304, 257, 174, 214, 69, 317, 387, 47, 157, 0, 332, 308, 317, 286, 236, 299, 206, 278, 188, 43, 0, 0, 0, 0, 0]
without_music = [292, 270, 47, 288, 324, 292, 364, 316, 287, 75, 282, 149, 274, 319, 213, 3, 324, 2, 128, 219, 94, 164, 0, 0, 0]

# Dot Plot: With Music
pl.figure(figsize=(8, 5))
pl.scatter(range(len(with_music)), with_music, color='blue', label='With Music')
pl.title("Dot Plot: With Music")
pl.xlabel("Plant Index")
pl.ylabel("Growth (mm)")
pl.legend()
pl.show()

# Dot Plot: Without Music
pl.figure(figsize=(8, 5))
pl.scatter(range(len(without_music)), without_music, color='green', label='Without Music')
pl.title("Dot Plot: Without Music")
pl.xlabel("Plant Index")
pl.ylabel("Growth (mm)")
pl.legend()
pl.show()

# Histogram: With Music
pl.figure(figsize=(8, 5))
pl.hist(with_music, bins=10, color='blue', alpha=0.7, label='With Music')
pl.title("Histogram: With Music")
pl.xlabel("Growth (mm)")
pl.ylabel("Frequency")
pl.legend()
pl.show()

# Histogram: Without Music
pl.figure(figsize=(8, 5))
pl.hist(without_music, bins=10, color='green', alpha=0.7, label='Without Music')
pl.title("Histogram: Without Music")
pl.xlabel("Growth (mm)")
pl.ylabel("Frequency")
pl.legend()
pl.show()
