#abstact class
from abc import ABCMeta ,abstractmethod
import random
class salarie(metaclass = ABCMeta):
    #class attribut
    __counter=0
    #constructor
    def __init__(self, nom , nombre ,  etat ,  adresse ,  salaire ):
        self.__nom = nom 
        self.__nombre = nombre 
        self.__etat = etat 
        self.__adresse = adresse 
        self.__salaire = salaire
        salarie.__counter  =  salarie.__counter+1
    
    #getters
    def getnom(self):
        return self.__nom
        
    def getnombre(self):
        return self.__nombre
        
    def getetat(self):
        return self.__etat
    
    def getadresse(self):
        return self.__adresse
    
    def getsalaire(self):
        return self.__salaire
    def setsalaire(self, s):
        self.__salaire  = s
    
    def getcounter(self):
        return salarie.__counter
    
    #methods

    def matricule(self):
        mat=random.randint(0,999999)
        return mat

    def ToString(self):
        print("le salarie numero  {} de matricule : {} est :{} ,son numero de securite social est:{}, son etat civile est :{},son adresse est:{}  et son  salaire de base est :{}DH"
              .format(self.getcounter(),self.matricule(),self.getnom(),self.getnombre(), self.getetat(),self.getadresse(),self.getsalaire()))
        
    def Equal(self, S):
        if type(self)==type(S):
            if self.matricule() == S.matricule() and self.getsalaire()==S.getsalaire():
                print("les employes sont les memes")
            else:
                print("les employes ne sont pas les memes")

        else:
            print("les employes ne sont pas de meme type")

    

     #abstractmethod   
    @abstractmethod
    
    def salaire(self):
        pass

    
#first child class
class patron (salarie):
    #constructor
    def __init__(self,nom , nombre ,  etat ,  adresse ,  salaire ,prisque):
        #l'appel de la class mere
        super().__init__(nom , nombre ,  etat ,  adresse ,  salaire)
        self.__prisque= prisque

    #getter
    def getprisque(self):
        return self.__prisque
    
    #overridding dela method abstract
    def salaire(self):
        ps=self.getsalaire()+self.getprisque()
        return  ps
    
    def ToString(self):
        super().ToString()
        print("son salaire apres la prime de risque est: {}DH".format(self.salaire()))
      
    
#second child class
class vendeur(salarie):
    #constructor
    def __init__(self,nom , nombre ,  etat ,  adresse ,  salaire ,com , sup):
        #l'appel de la class mere
        super().__init__(nom , nombre ,  etat ,  adresse ,  salaire)
        self.__com= com
        self.__sup= sup


    #getter
    def getcom(self):
        return self.__com
    def getsup(self):
        return self.__sup
    
    #overridding dela method abstract
    def salaire(self):
        cm=self.getsalaire()+self.getcom()
        return  cm
    
    def ToString(self):
        super().ToString()
        print("son salaire apres la commision est: {}DH, son supérieur hiérarchique est :  {}".format(self.salaire(), self.getsup()))

 #third child class     
class caissier(salarie):
    #constructor
    def __init__(self,nom , nombre ,  etat ,  adresse ,  salaire , sup ):
        #l'appel de la class mere
        super().__init__(nom , nombre ,  etat ,  adresse ,  salaire)
        self.__sup= sup

    #getter
    def getsup(self):
        return self.__sup
    
    #overridding dela method abstract
    def salaire(self):
        return self.getsalaire()
    
    def ToString(self):
        super().ToString()
        print("son salaire est tjr fix: {}DH et son supérieur hiérarchique est :  {}".format(self.salaire(), self.getsup()))


 
    
    
p1=patron("farah",23456,  "celibataire"  , "marrakech 3457", 40000, 3000)
p2=patron("salma",9283,  "marie"  , "marrakech 56q1", 60000, 1000)
p1.ToString()
p2.ToString()
p1.Equal(p2)
v1=vendeur("meriem",45678  ,"divorce" , "cas45621", 7000  , 560,p1 )
v2=vendeur("wissal",65312  ,"fiance" , "cas4521", 5000  , 2560,v1 )
v1.ToString()
v2.ToString()
v1.Equal(v2)
p1.Equal(v2)
c1=caissier("hiba",21387  ,"marie" , "23rabat", 2000  , p1 )
c2=caissier("hanan",2319  ,"celibataire" , "fes612", 3000  , p1 )
c1.ToString()
c2.ToString()

