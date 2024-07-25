from ast import If
import csv
from re import L
from configparser import ConfigParser
from datetime import date
import os


class Geografias:

    # CONSTRUCTOR
    def __init__(self, pComuna, pSeccion, pDivision):
        self.__Comuna = pComuna
        self.__Seccion = pSeccion
        self.__Division = pDivision

    # GETTERS
    @property
    def Comuna(self):
        return self.__Comuna

    @property
    def Seccion(self):
        return self.__Seccion

    @property
    def Division(self):
        return self.__Division

    # SETTERS
    @Comuna.setter
    def Comuna(self, pComuna):
        self.__Comuna = pComuna

    @Seccion.setter
    def Seccion(self, pSeccion):
        self.__Seccion = pSeccion

    @Division.setter
    def Division(self, pDivision):
        self.__Division = pDivision

    def GeoCompleta(self):
        return 'C'+self.__Comuna+'S'+self.__Seccion+'D'+self.__Division


# la info formularios es un archivo

class Personas(Geografias):

    # CONSTRUCTOR
    def __init__(self, pNombre, pApellido, pCargo, pLegajo, geografia):
        self.__Nombre = pNombre
        self.__Apellido = pApellido
        self.__Cargo = pCargo
        self.__Legajo = pLegajo
        self.geografia = geografia
        # super().__init__(pComuna, pSeccion, pDivision)

    # GETTERS
    @property
    def Nombre(self):
        return self.__Nombre
    # GETTERS
    @property
    def Apellido(self):
        return self.__Apellido
    # GETTERS
    @property
    def Cargo(self):
        return self.__Cargo
    # GETTERS
    @property
    def Legajo(self):
        return self.__Legajo

    # SETTERS
    @Nombre.setter
    def Nombre(self, pNombre):
        self.__Nombre = pNombre
    # SETTERS
    @Apellido.setter
    def Apellido(self, pApellido):
        self.__Apellido = pApellido
    # SETTERS
    @Cargo.setter
    def Cargo(self, pCargo):
        self.__Cargo = pCargo
    # SETTERS
    @Legajo.setter
    def Legajo(self, pLegajo):
        self.__Legajo = pLegajo


class Informes(Geografias):
    def cantEncuestados():
        encuestas=[]
        count=0
        encuestas=Encuestas.consultarEncuestas()
        for linea in encuestas:
            count+=1
        
        return count
    def porcentajesAumentaran():
        encuestas={}
        aumentaran=0
        lista=[0]*15
        encuestas=Encuestas.consultarEncuestas()
        for i in encuestas:
            if i["preg1"].lower()=='si':
                lista[int(i["comuna"])-1]=lista[int(i["comuna"])-1]+1
        
        for j in range(len(lista)):
            aumentaran=(lista[j]/len(encuestas))*100
            print(f"De la comuna {j+1} cree que aumentaran los preccios el {aumentaran}%")
            print(f"De la comuna {j+1} No cree que aumentaran los preccios el {100-aumentaran}%")        


    def productoEnAumento():
        encuestas = {}
        aumentaran = 0
        lista = [0] * 15
        encuestas = Encuestas.consultarEncuestas()
        for i in encuestas:
            if i["preg1"].lower() == 'si':
                lista[int(i["comuna"]) - 1] = lista[int(i["comuna"]) - 1] + 1

class Encuestas(Geografias):
    def __init__(self, preg1, preg2, preg3, preg4, geografia):
        self.pre1 = preg1
        self.pre2 = preg2
        self.pre3 = preg3
        self.pre4 = preg4
        self.geografia = geografia

#GETTERS
    @property
    def Preg1(self):
        return self.pre1
    @property
    def Preg2(self):
        return self.pre2
    @property
    def Preg3(self):
        return self.pre3
    @property
    def Preg4(self):
        return self.pre4
    @property
    def Geografia(self):
        return self.geografia

#SETTERS
    @Preg1.setter
    def Preg1(self, pre1):
        self.pre1 = pre1
    @Preg2.setter
    def Preg2(self, pre2):
        self.pre2 = pre2
    @Preg3.setter
    def Preg3(self, pre3):
        self.pre3 = pre3
    @Preg4.setter
    def Preg4(self, pre4):
        self.pre4 = pre4
    @Geografia.setter
    def Geografia(self, geografia):
        self.geografia = geografia

    def cargaEncuestas():
        encabezados = ("Inflacion aumentara: ", "Producto mayor aumento: ", "Aumento sus ingresos: ","Compras extraordinarias: ","su Comuna: ","su Seccion :", "su Division :")
        fileName = "D:\Python-POO\Python-POO\Encuestas\procesadoEl" + date.today().strftime("%d-%m-%Y") + ".txt"
        guardar = "si"
        try:
            while guardar == "si":
                encuestasCargada = {}
                renglonCargado = []
                for cadaEncabezado in encabezados:
                        encuestasCargada[cadaEncabezado] = input(f"ingrese {cadaEncabezado}    ")
                geo=Geografias(encuestasCargada["su Comuna: "],encuestasCargada["su Seccion :"], encuestasCargada["su Division :"])
                encu=Encuestas(encuestasCargada["Inflacion aumentara: "],encuestasCargada["Producto mayor aumento: "],encuestasCargada["Aumento sus ingresos: "],encuestasCargada["Compras extraordinarias: "],geo)
                with open(fileName, "a", newline="") as file:
                    archivoCSV = csv.writer(file,  delimiter=",")
                    renglonCargado.append(encu.Preg1)
                    renglonCargado.append(encu.Preg2)
                    renglonCargado.append(encu.Preg3)
                    renglonCargado.append(encu.Preg4)
                    renglonCargado.append(geo.GeoCompleta())
                    renglonCargado.append(geo.Comuna)
                    archivoCSV.writerow(renglonCargado)

                guardar = input("\tDesea seguir agregando empleados? Si/No:  ").lower()


        except Exception as e:
            print(f"error: {e}")
        finally:

                Gestiones.Menu()


    def consultarEncuestas () :
        os.chdir('D:\Python-POO\Python-POO\Encuestas')
        filelist = os.listdir(os.getcwd())
        data = []
        for archivo in filelist: 
            encabezados = ("preg1", "preg2", "preg3", "preg4","geo","comuna")
            with open(archivo,"r", newline='') as lecCSV:
                reader = csv.DictReader(lecCSV,fieldnames=encabezados)
                for row in reader:
                    data.append(row)
        print(f"Datos cargados: {data}")  # Imprimir datos cargados            
        return data
            
        # encabezados = ("preg1", "preg2", "preg3", "preg4","geo")
        # # with open(archivo, "r") as lecCSV:
        # #     lectura = csv.DictReader(lecCSV,fieldnames=encabezados)
        # #     for linea in lectura:
        # #         if linea["geo"] == Encuestas.Geografia:
        # #             print(" es igual el dato")
        # with open(archivo,"r", newline='') as lecCSV:
        #     reader = csv.DictReader(lecCSV,fieldnames=encabezados)
        #    # next(reader, None)  # skip the headers
        #     data = []
        #     for row in reader:
        #         data.append(row)

        # return data
        

        


class Gestiones():
    # ESTA CLASE ADMINISTRA LOS METODOS DE GESTION DEL PROGRAMA
    def Login(pUsuario, pClave):
        try:
            
            with open("logins.csv", "r") as read_obj:
                try:
                    csv_reader = csv.reader(read_obj)
                    row = []
                    for row in csv_reader:

                        if pUsuario == row[0] and pClave == row[1]:
                            return True


                except Exception as e:
                    print(e)
                finally:
                    read_obj.close()

        # except:
        #     print("El Archivo de logeuo esta corrupto o no existe")
        except Exception as e:
            print(e)

    def CargaLiderYCoord():
        try:
            lider = 0
            coordinador = 0
            clave = input("Ingrese la clave habilitadora: ")
            # LEO EL ARCHIVO config.cfg PARA SABER SI PUEDE CREAR LIDERES Y COORDINADORES
            config_object = ConfigParser()
            config_object.read("config.cfg")
            userinfo = config_object["USERINFO"]
            if clave == userinfo["key1"]:
                # MIENTRAS NO LOS CARGUE TODOS SIGUE CARGANDO
                while lider < 90 or coordinador < 15:
                    # CARGO PRIMERO LOS COORDINADORES
                    if coordinador < 15:
                        try:
                            print('Cargando el Coordinador numero %2d, Maximo 15' % (coordinador + 1))
                            nombre = input('Nombre Coordinador: ')
                            apellido = input('Apellido Coordinador: ')
                            dni = input('DNI Coordinador: ')
                            legajo = 'C-' + dni
                            cargo = 'Coordinador'
                            # INTENTO GUARDARLO AL ARCHIVO
                            # ABRO EL ARCHIVO PARA AGREGAR AL FINAL
                            with open("Coordinadores.txt", "a") as file_object:
                                # GUARDO MI COORDINADOR Y SALTO DE LINEA
                                file_object.write(nombre + apellido + ',' + legajo + '\n')
                            coordinador += 1
                        except Exception as e:
                            print(e)
                        finally:
                            # CIERRO EL ARCHIVO
                            file_object.close()
                    # SIGO CON LOS LIDERES
                    elif lider < 90:
                        try:
                            print('Cargando el Lider numero %2d, Maximo 15' % (coordinador + 1))
                            nombre = input('Nombre lider: ')
                            apellido = input('Apellido lider: ')
                            dni = input('DNI lider: ')
                            legajo = 'L-' + dni
                            cargo = 'Lider'
                            # INTENTO GUARDARLO AL ARCHIVO
                            # ABRO EL ARCHIVO PARA AGREGAR AL FINAL
                            with open("Lideres.txt", "a") as file_object:
                                # GUARDO MI COORDINADOR Y SALTO DE LINEA
                                file_object.write(nombre + apellido + ',' + legajo + '\n')

                            coordinador += 1
                        except Exception as e:
                            print(e)
                        finally:
                            # CIERRO EL ARCHIVO
                            file_object.close()

                print('Finalizo la carga de Lideres y coordinadores')
                Gestiones.Menu()


        except Exception as e:
            print(e)



    def Menu():
        try:
            print('Menu:')
            print('Opcion 1: Cargar Lideres y Coordinadores')
            print('Opcion 2: Login')
            print('Opcion 3: Salir')
            #print('Opcion 4: Cargar Encuesta')
            print('Opcion 4: Consultar Encuestas') #ES NECESARIO CONSULTARLAS, EL NOMMBRE DEL ARCHIVO VA A SER RANDOM
            print('Opcion 5: Cantidad de Encuestados Totales?')
            print('Opcion 6: Porcentaje de personas creen precios aumentaran?')
            print('Opcion 10: Porcentaje de personas creen precios aumentaran?')
            opcion = input('Elija su opcion: ')
            match opcion:
                case '1':
                    Gestiones.CargaLiderYCoord()
                    Gestiones.Menu()

                case '2':
                    usuario = input('ingrese usuario: ')
                    clave = input('ingrese clave: ')
                    if Gestiones.Login(usuario, clave):
                        Encuestas.cargaEncuestas()
                    else:
                        print ('Usuario o Clave incorrectas.')
                    Gestiones.Menu()

                case '3':
                    # EL RETURN 0 ME SACA DE LA SELECCION
                    return 0
                case '4':
                    #ES NECESARIO CONSULTARLAS, EL NOMMBRE DEL ARCHIVO VA A SER RANDOM
                    Encuestas.consultarEncuestas()
                    Gestiones.Menu()
                    print(f"Encuestas: {Encuestas}")
                    

                case '5':
                    cantidad=Informes.cantEncuestados()
                    print(f"La cantidad de encuestados totales es {cantidad}")
                    Gestiones.Menu()

                case '6':
                    aumentaran=Informes.porcentajesAumentaran()
                    # print(f"Porcentaje de personas que creen que aumentaran es {aumentaran}%")
                    # print(f"Porcentaje de personas que creen no aumentara es {100-aumentaran}%")
                    Gestiones.Menu()
                case '10':
                    print("opcion 10!!!")
                    Gestiones.Menu()
        except Exception as e:
            print(e)

# METODO MAIN
Gestiones.Menu()
