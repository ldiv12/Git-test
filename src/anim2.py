from pylab import *

ion() # mode interaction on

x = linspace(0, 3, 100)
k = 2*pi
w = 2*pi
dt = 0.01

# courbe initiale
t = 0
y = cos(k*x - w*t)
line, = plot(x, y) # une reference a la courbe est mise dans line

# courbe en mouvement
for i in range(50):
    t = t + dt
    y = cos(k*x - w*t)
    line.set_ydata(y) # modifie les valeurs de y
    draw() # force le dessin de la figure

ioff() # mode interaction off
show()
