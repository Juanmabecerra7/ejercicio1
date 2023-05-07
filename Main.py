from Email import Email
from ManejadorEmail import ManejadorEmail


if __name__ == '__main__':
    m = ManejadorEmail()
    nombre = input("ingrese el nombre de la persona")
    idcuenta = input("ingrese el id de su email")
    dominio = input("ingrese el dominio de su email")
    tipodominio = input("ingrese el tipo de dominio")
    contraseña = input("ingrese la contraseña")
    unEmail = Email(idcuenta, dominio, tipodominio, contraseña)
    print (f"estimado {nombre} te enviamos tus mensajes a la direccion {Email.retornaEmail(unEmail)}")
    Email.VerificarContraseña(unEmail)
    m.testEmail()
    print(str(m))
    dom = input("ingrese un dominio a buscar")
    print(f"la cantidad de mail con ese dominio son{m.IdentificarDominio(dom)}")
