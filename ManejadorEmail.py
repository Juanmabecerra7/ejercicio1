from Email import Email
import csv

class ManejadorEmail:
    def __init__(self):
        self.__lista = []
        
    def IdentificarDominio (self, dom):
        indice = 0
        contador = 0
        while indice < len (self.__lista):
            if str (self.__lista[indice].getDominio())==str(dom):
                contador = contador + 1
            indice = indice + 1
            return contador
        
    def agregarEmail (Self, unEmial):
        Self.__lista.append(unEmial)
    
    def testEmail (self):
        archivo = open ("email.csv")
        reader = csv.reader (archivo, delimiter=",")
        for fila in reader: 
            idcuenta =fila[0]
            dominio = fila [1]
            tipodominio = fila [2]
            contraseña = fila [3]
            unEmail = Email(idcuenta, dominio, tipodominio ,contraseña)
            bandera = Email.crearCuenta(unEmail)
            if bandera:
                self.agregarEmail(unEmail)
        archivo.close()
        
    def __str__(self):
        s = ""
        for Email in self.__lista:
            s = s+ str(Email) + "\n"
            return s     
