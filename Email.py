class Email:
    __idcuenta = ""
    __dominio = ""
    __tipodominio = ""
    __contraseña = 0
    
    def __init__ (self, idcuenta, dominio, tipodominio, contraseña):
        self.__idcuenta = idcuenta
        self.__dominio = dominio 
        self.__tipodominio = tipodominio
        self.__contraseña = contraseña
        
    def crearCuenta (self):
        a = False
        if len (self.__idcuenta) == 0:
            print ("error de idcuenta")
        elif not str (self.__dominio) == "gmail" or str (self.__dominio) == "hotmail":
            print ("error de dominio")
        elif len (self.__tipodominio) > 3 and len (self.__tipodominio) <= 1:
            print ("error de tipo de dominio")
        else:
            a = True
        return a
    
    def VerificarContraseña (self):
        contra = input ("ingrese la contraseña actual")
        if contra == self.__contraseña:
           nuevacontra = input ("ingrese la nueva contraseña")
           self.__contraseña = nuevacontra
        else:
            print ("contraseña incorrecta")
        
    def getDominio (Self):
        return str(Self.__dominio)
    
    def retornaEmail (Self):
        return str(Self.__idcuenta +"@"+ Self.__dominio+"."+Self.__tipodominio)
    
    def __str__(self):
        return str(self.__idcuenta+"@"+self.__dominio+"."+self.__tipodominio+" "+self.__contraseña+" ")
