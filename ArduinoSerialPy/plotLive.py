import matplotlib.pyplot as plt
import matplotlib.animation as animation
# Deixar o grafico mais bonitinho
from matplotlib import style

# Um tipo de grafico
style.use('fivethirtyeight')

fig = plt.figure()

# Um plot 1x1 e o plot eh o numero 1
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    # i eh o intervalo
    graph_data = open('example.txt' , 'r').read()
    lines = graph_data.split('\n')

    xs = []
    ys = []

    for line in lines:
        # Corta as linhas vazias
        if len(line)>1:
            # , pois o arquivo eh separado por virgula
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    # Limpa tudo antes de plotar
    ax1.clear()
    ax1.plot(xs,ys)

# qual figura queremos animar, qual funcao eo intervalo em ms que o grafico vai dar update
animt = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()