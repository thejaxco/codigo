import matplotlib.pyplot as plt
import datetime as date
from random import randrange

def grafic(temperatura,humitat):   
    dades = temperatura # Valors de les variables
    dades2=humitat
    ind=range(10) # Coordenades x
    fig, (ax1,ax2) = plt.subplots(1,2) # Numero de grafiques que dibuixem a la figura. que passa si fem fig, (ax1,ax2) = plt.subplots(1,2)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=2, hspace=None)
    
    ############################ DIAGRAMA DE BARRES HORITZONTAL###################################################################################
    width = 0.75 # Amplada dels diagrames
    rects1 = ax1.bar(ind, dades, width, color='g') # Dades dels diagrames. Coordenades, Valors de les variables, Amplada i Color.
    ax1.set_ylabel('Temperatura') # Llegenda de eix Y.
    ax1.set_title('Temperatures') # Titol del grafic
    ax1.set_xticks(ind) # Marques sota de cada diagrama
    ax1.yaxis.set_major_locator(plt.NullLocator())
    ax1.set_xticklabels(('hora1')) # Text sota de cada diagrama en aquest cas 
    ax1.set_yticklabels([])
   
    for rect in rects1: # Dibuixem cadascun dels diagrames que son rectangles.
        height = rect.get_height() # De cada rectangle agafem la seva alcada.
        ax1.text(rect.get_x() + rect.get_width()/2., height,'%d' % int(height),ha='center', va='bottom') # Els valors quedaran damunt del diagrama
        
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.spines['top'].set_visible(False)  
    
    rects2 = ax2.bar(ind, dades2, width, color='r') # Dades dels diagrames. Coordenades, Valors de les variables, Amplada i Color.
    ax2.set_ylabel('Humitat') # Llegenda de eix Y.
    ax2.set_title('Humitats') # Titol del grafic
    ax2.set_xticks(ind) # Marques sota de cada diagrama
    ax2.yaxis.set_major_locator(plt.NullLocator())
    ax2.set_xticklabels(('hora2')) # Text sota de cada diagrama en aquest cas HOMES i DONES.
    ax2.set_yticklabels([])
   
    for rect in rects2: # Dibuixem cadascun dels diagrames que son rectangles.
        height = rect.get_height() # De cada rectangle agafem la seva alcada.
        ax2.text(rect.get_x() + rect.get_width()/2., height,'%d' % int(height),ha='center', va='bottom') # Els valors quedaran damunt del diagrama
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.spines['top'].set_visible(False)  
    

    ########################################## GUARDAR LA FIGURA #########################################################################
    nomdearxiu = str(date.datetime.now()) + '.png'
    nomdearxiu = nomdearxiu.replace(':','-')   
    plt.savefig(nomdearxiu, bbox_inches='tight')
    plt.close(fig)

def lectura():
    #codi del del sensor dht11 velleman temperatura i humitat
    temperatura = randrange(10,35)
    humitat = randrange(50,100)
    return temperatura,humitat