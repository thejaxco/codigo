from random import randint
from time import sleep
import matplotlib.pyplot as plt



#import cuentaPersonas.py
def grafic(datos):
    dades = datos # Valors de les variables

    ind=range(10) # Coordenades x
    fig, (ax1) = plt.subplots(1) # Numero de grafiques que dibuixem a la figura. que passa si fem fig, (ax1,ax2) = plt.subplots(1,2)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=1, hspace=None)

    ############################ DIAGRAMA DE BARRES HORITZONTAL###################################################################################
    width = 0.5 # Amplada dels diagrames
    rects1 = ax1.bar(ind, dades, width, color='r') # Dades dels diagrames. Coordenades, Valors de les variables, Amplada i Color.
    ax1.set_ylabel('Persones') # Llegenda de eix Y.
    ax1.set_title('Mostra de 10 minust') # Titol del grafic
    ax1.set_xticks(ind) # Marques sota de cada diagrama
    ax1.yaxis.set_major_locator(plt.NullLocator())
    ax1.set_xticklabels(('0123456789')) # Text sota de cada diagrama en aquest cas HOMES i DONES.
    ax1.set_yticklabels([])

    for rect in rects1: # Dibuixem cadascun dels diagrames que son rectangles.
        height = rect.get_height() # De cada rectangle agafem la seva alcada.
        ax1.text(rect.get_x() + rect.get_width()/2., height,'%d' % int(height),ha='center', va='bottom') # Els valors quedaran damunt del diagrama
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.spines['top'].set_visible(False)




    ########################################## GUARDAR LA FIGURA #########################################################################
    plt.savefig('prova1.png', bbox_inches='tight')
    #plt.show()
    plt.close(fig)




def lectura():
    binario = randint(0,1)
    return binario #0 o 1 en funcion que pase una persona o no
