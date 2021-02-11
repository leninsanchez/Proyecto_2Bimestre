# Python Code for factory method  
# it comes under the creational  
# Design Pattern
# Su solución es reemplazar las llamadas directas de construcción de objetos con llamadas 
# al método de fábrica especial. En realidad, no habrá diferencia en la creación de objetos, 
# pero se llaman dentro del método de fábrica . 
  
class FrenchLocalizer: 
  
    """ Simplemente devuelve la version Franses """
  
    def __init__(self): 
  
        self.translations = {"car": "voiture", "bike": "bicyclette", 
                             "cycle":"cyclette"} 
  
    def localize(self, message): 
  
        """cambiar el mensaje usando la traducción"""
        return self.translations.get(msg, msg) 
  
class SpanishLocalizer: 
    """Simplemente devuelve la version Español"""
  
    def __init__(self): 
        self.translations = {"car": "coche", "bike": "bicicleta", 
                             "cycle":"ciclo"} 
  
    def localize(self, msg): 
  
        """cambiar el mensaje usando la traducción"""
        return self.translations.get(msg, msg) 
  
class EnglishLocalizer: 
    """Simplemente devuelva el mismo mensaje"""
  
    def localize(self, msg): 
        return msg 
  
def Factory(language ="English"): 
  
    """Factory Method"""
    localizers = { 
        "French": FrenchLocalizer, 
        "English": EnglishLocalizer, 
        "Spanish": SpanishLocalizer, 
    } 
  
    return localizers[language]() 
#iniciliazador del programa.. 
if __name__ == "__main__": 
  
    f = Factory("French") 
    e = Factory("English") 
    s = Factory("Spanish") 
  
    message = ["car", "bike", "cycle"] 
  
    for msg in message: 
        print(f.localize(msg)) 
        print(e.localize(msg)) 
        print(s.localize(msg)) 