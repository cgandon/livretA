#!/usr/bin/env python
# coding: utf-8

# In[6]:


def validate(x,y):
    # x = valeur à tester
    # y = type de valeur (t pour taux, m pour montant, a pour années)
    try:
        float(x)
    except:
        print("Attention ceci n'est pas une valeur")
        return False
    else:
        if float(x) < 0:
            print("Entrez une valuer positive")
            return False
        if y == "t":
            if float(x) > 1:
                print("le taux doit être exprimé en décimal, par ex 0.1 pour 10%")
                return False
    return True
    
def interet():
    a = input("Entrez un capital à investir:")
    if validate(a,"m") == True:
        a = float(a)
        b = input("Entrez un taux d'intérêt:")
        if validate(b,"t") == True:
            b = float(b)
            c = input("Entre une durée de placement souhaitée:")
            if validate(c,"a") == True:
                c = int(c)
                k = a*(1+b)**c
                print("Le capital final sera de {:.2f} euro".format(k))
            else:
                interet()
        else:
            interet()
    else:
        interet()
            
interet()


# In[ ]:





# In[ ]:




