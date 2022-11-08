# from tkinter import*
# from PIL import Image, ImageTk

import datetime #Librería para mostrar fecha y hora actual
from reportlab.pdfgen import canvas  #Creación del lienzo
from reportlab.lib.pagesizes import letter
import qrcode #Importamos la libreria de Qr
import platform #Nos ayuda a reconocer cuál es el sistema operativo que estemos usando en la computadora
import os #Nos sirve para invocar el comando de limpieza en pantalla
import time #Librería de tiempo que nos ayudará hacer una simulción de tiempo de espera

Pelicula = ["Vikingos","I'm the number four","I love you","Jumper","Transformers","Rápido furioso","Guerra Mundial Z","Policía y Medio"]

class Factura:

    hora = datetime.datetime.now().hour
    minuto = datetime.datetime.now().minute
    segundos = datetime.datetime.now().second

    Informacion = {'Nombre_empresa':'The Wikyland S.A','NIT':'860508791-1','Respondable Iva':' CIIU  10B124','Agente':'Agente Retenedor de ICA','TEL':3156299375,'Pagina':'TheWiky1824_Sur-Neiva@gmail.com','Place':'Ruta nueva Selanda','N&C':'DG 23 69 55 LC 126','Dian':'Aut. DIAN 18764027319797','Desde':'JK - 33449','Hasta':' JK -1000000','DCTO':'JK  -52357','Cajero':'Desconocido','Cliente':'Desconocido','Celular': 123456,'CEDULA':12345678}

    def __init__(self) -> None:
        pass

    def Preguntar_cliente(self,diccionario):

        self.Cliente = input("Nombre del cliente: "); diccionario["Cliente"] = self.Cliente      
        self.CC = int(input("Nit/C.C. : "));diccionario["CEDULA"] = self.CC 
        self.numero = int(input("Celular: "));diccionario["Celular"] = self.numero 
    
    def Preguntar_producto(self, diccionario):
        self.Descripcion = input("Digita la pelicula: ")
        self.Cantidad = int(input("Cantidad de boletos: "))
        self.Precio = float(input("Digital el precio del producto : $"))
        self.Pagar = input("Forma de pago: ")
        self.Cajero = input("Digita el nombre del cajero: ")
        diccionario["Cajero"] = self.Cajero
    
    def Limpiar(self):
        time.sleep(2)

        if platform.system() == 'Windows':
            print("Preparando Factura....")
            time.sleep(2)
            os.system('cls')
        else:
            os.system('clear')
    
    def Generar_Qr(self):

        input = (f'{"Cajero: ",self.Cajero} {"Cliente: ",self.Cliente} {"Fecha: ",datetime.datetime.now().day,datetime.datetime.now().month,datetime.datetime.now().year} {"Hora: ",self.hora,":",self.minuto,":",self.segundos}')
        #'https://the-wiki.000webhostapp.com/' # Esta cadena permitirá convertilo en QR,  se crea una variable  que Almacena los datos, en este caso se alamacena un dato de un link de una página web.

        qr = qrcode.QRCode(version=1,box_size=10,border=5) #Estrcutura de QR
        qr.add_data(input)
        qr.make(fit=True)
        img = qr.make_image(fill='black',back_color='white')
        img.save('QR_INFORMATION_FACT.png')
        # img.save('Mi_Pagina_QR.png')

    def Mostrar(self,diccionario):

        self.sub = self.Cantidad * self.Precio
        self.pp =  self.sub - (self.sub * .19)
        self.Value =  diccionario.items()
        print("\t                           ",list(self.Value)[0][1])
        print("\t                         NIT: ",list(self.Value)[1][1])
        print("\t                RESPONSABLE DE IVA.  ",list(self.Value)[2][1])
        print("\t                      ",list(self.Value)[3][1])
        print("\t                        TELEFONO:",list(self.Value)[4][1])
        print("\t                  ",list(self.Value)[5][1])
        print("\t                        ",list(self.Value)[6][1])
        print("\t                        ",list(self.Value)[7][1])
        print("\n\t          ",list(self.Value)[8][1], "      FEC  01/04/2022")
        print("\t           Desde    ",list(self.Value)[9][1], "    Hasta",list(self.Value)[10][1])
        print("\t           DCTO/EQUIVALENTE POS:", list(self.Value)[11][1])
        print("\t           VIGENCIA HASTA: 31/03/2023")
        print("\t           FECHA: ",datetime.datetime.now().day,"/",datetime.datetime.now().month,"/",datetime.datetime.now().year,"      Hora:",self.hora,":",self.minuto,":",self.segundos)
        print("\t           CAJERO: ",self.Cajero)
        print("\t           CLIENTE: ",self.Cliente)
        print("\t           NIT/C.C: ",self.CC)
        print("\t           CIUDAD: Neiva")
        print("\t           Celular: ",self.numero)
        print("\t           ===============================================")
        print("\t           Uds  PRODUCT.DESCRIPCION     PRECIO        TOTAL")
        print("\t           ===============================================")
        print("\t           ",self.Cantidad,"  ",self.Descripcion,f"                ${self.Precio:.0f}","         $", self.Cantidad * self.Precio)
        print("\t           ============[ DETALLE DE VALORES ]=============")
        print(f"\t                                SUBTOTAL          ${self.pp:.0f}")
        print("\t                                DTO   0%          $ 0")
        print(f"\t                                TOTAL             ${self.sub:.0f}")
        print("\t           ========[ DISCRIMINACION DE IMPUESTOS ]========")
        print(f"\t           I BASE 19%   {self.pp:.0f} IVA       {self.sub * .19:.0f}")
        print(f"\t             TOTAL      {self.pp:.0f}           {self.sub * .19:.0f}")
        print("\t           ================[ FORMA DE PAGO ]==============")
        print("\t                          ",self.Pagar,f"        ${self.sub:.0f}")
        print("\t           ===============================================")
        print("\t                        !GRACIAS POR TU COMPRA!")
        print("\t        !Unete a nuestro programa de prestación con The Wiky!")
        print("\t                          AQUÍ VA EL CÓDIGO QR              ")
        print("\t                    ",list(self.Value)[5][1])
        print("\t                  Registrate con el código: 80")
        print("\t            =============================================")
        print("\t              FACTURA GENERDADA por software JEPC_2003")
        print("\t               DESARROLLADO por ICG NIT:",list(self.Value)[1][1])
        print("\t            =============================================")
        print("\t               PARA MAYOR INFORMACION SOBRE DEVOLUCIONES, ")
        print("\t                         GARANTIAS Y RETRACTO             ")
        print("\t                    CONSULTA TODO SOBRE NOSOTROS EN:    ")
        print("\t                     SOLICITUDTHEWIKY_JECP.COM.CO      ")
    
    def Mostrar_PDF(self):
        # print("Hola")
        w, h = letter
        C = canvas.Canvas("Factura.pdf",pagesize=letter)
        C.setLineWidth(.2)
        C.setFont('Helvetica',10)
        C.rect(160,h-660,300,655) #Ancho = 300 y alto = 660
        C.drawString(250, h-30, list(self.Value)[0][1])
        C.drawString(251, h-42,f"NIT:{list(self.Value)[1][1]}")
        C.drawString(198, h-55,f"RESPONSABLE DE IVA.  {list(self.Value)[2][1]}")
        C.drawString(238, h-67, list(self.Value)[3][1])
        C.drawString(236, h-79,f"TELEFONO:   {list(self.Value)[4][1]}")
        C.drawString(210, h-90, list(self.Value)[5][1])
        C.drawString(248, h-101, list(self.Value)[6][1])
        C.drawString(248, h-113, list(self.Value)[7][1])
        C.drawString(175, h-140,f"{list(self.Value)[8][1]}                   FEC  01/04/2022")
        C.drawString(175, h-152,f"Desde   {list(self.Value)[9][1]}     Hasta   {list(self.Value)[10][1]}")
        C.drawString(175, h-164,f"DCTO/EQUIVALENTE POS:  {list(self.Value)[7][1]}")
        C.drawString(175, h-176,"VIGENCIA HASTA: 31/03/2023")
        C.drawString(175, h-188,f"FECHA:  {datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year}       Hora:{self.hora}:{self.minuto}:{self.segundos}")
        C.drawString(175,h-200,f"CAJERO:  {self.Cajero}")
        C.drawString(175,h-212,f"CLIENTE:  {self.Cliente}")
        C.drawString(175,h-224,f"NIT/C.C:  {self.CC}")
        C.drawString(175,h-236,"CIUDAD:  NEIVA")
        C.drawString(175,h-248,f"CEL:  {self.numero}")
        C.drawString(175,h-260,"=============================================")
        C.drawString(175,h-272,f"Uds  PRODUCT.DESCRIPCION     PRECIO        TOTAL")
        C.drawString(175,h-284,f"{self.Cantidad}        {self.Descripcion}                        ${self.Precio:.0f}          $ {self.Cantidad * self.Precio:.0f}")
        C.drawString(175,h-296,"============[ DETALLE DE VALORES ]============")
        C.drawString(260,h-308,f"SUBTOTAL          $ {self.pp:.0f}")
        C.drawString(260,h-320,"DTO 0%               $ 0")
        C.drawString(260,h-332,f"TOTAL                 ${self.sub:.0f}")
        C.drawString(175,h-344,"=======[ DISCRIMINACION DE IMPUESTOS ]========")
        C.drawString(190,h-356,f"I BASE 19%    {self.pp:.0f}    IVA      {self.sub * .19:.0f}")
        C.drawString(190,h-368,f"  TOTAL          {self.pp:.0f}               {self.sub * .19:.0f}")
        C.drawString(175,h-380,"===============[ FORMA DE PAGO ]==============")
        C.drawString(190,h-392,f"            {self.Pagar}      ${self.sub:.0f}")
        C.drawString(175,h-404,"=============================================")
        C.drawString(230,h-416,"!GRACIAS POR TU COMPRA!")
        C.drawString(175,h-428,"!Unete a nuestro programa de prestación con The Wiky!")
        C.drawImage("QR_INFORMATION_FACT.png",250, h-540, width=100, height=100)
        C.drawString(220,h-552,f"{list(self.Value)[5][1]}")
        C.drawString(175,h-564,"=============================================")
        C.drawString(180,h-576,"FACTURA GENERDADA por software JEPC_2003")
        C.drawString(185,h-588,f"DESARRROLLADO por ICG NIT: {list(self.Value)[1][1]}")
        C.drawString(175,h-600,"=============================================")
        C.drawString(180,h-612,"PARA MAYOR INFORMACION SOBRE DEVOLUCIONES,")
        C.drawString(235,h-624,"GARANTIAS Y RETRACTO")
        C.drawString(200,h-636,"CONSULTA TODO SOBRE NOSOTROS EN:")
        C.drawString(210,h-648,"SOLICITUDTHEWIKY_JECP.COM.CO")
        C.save()
 

print("\t\t    Bienvenido a the wikyland  S.A \n")
print("Tienda de pelicula, a continuación verás las peliculas que está disponible: ")
contador = 1
for peli in Pelicula:
    print(f"{contador} {peli}")
    contador +=1
info = input("Comenzar la infomarción para la compra?")

if info == "Si" or info == "si": #and contador == contador:
    contador = 1
    os.system('cls')
    print("Pelicula disponible:")
    for peli in Pelicula:
        print(f"{contador} {peli}")
        contador +=1
    print("|"*40)
    print("\t\t Información ")
    Objeto = Factura()
    Objeto.Preguntar_cliente(Objeto.Informacion)
else:
    exit()

Objeto.Preguntar_producto(Objeto.Informacion)
Objeto.Limpiar()
Objeto.Generar_Qr()
Objeto.Mostrar(Objeto.Informacion)
Objeto.Mostrar_PDF()

'''
import datetime
from tkinter import*
from PIL import Image, ImageTk
from reportlab import*
import platform #Nos ayuda a reconocer cual es el sistema operativo que se estamos usando 
import os #Nos sirve para invocar el comando de limpieza en pantalla
import time #Simulación de tiempo de espera

Pelicula = ["Vikingos","I'm the number four","I love you","Jumper","Transformers vs Rápido furioso"]
(f'{"Cajero: ",self.Cajero} {self.hora}{self.minuto}{self.segundos}')
class Factura:

    hora = datetime.datetime.now().hour
    minuto = datetime.datetime.now().minute
    segundos = datetime.datetime.now().second

    Informacion = {'Nombre_empresa':'The Wikyland S.A','NIT':'860508791-1','Respondable Iva':' CIIU  10B124','Agente':'Agente Retenedor de ICA','TEL':3156299375,'Pagina':'TheWiky1824_Sur-Neiva@gmail.com','Place':'Ruta nueva Selanda','N&C':'DG 23 69 55 LC 126','Dian':'Aut. DIAN 18764027319797','Desde':'JK - 33449','Hasta':' JK -1000000','DCTO':'JK  -52357','Cajero':'Desconocido','Cliente':'Desconocido','Celular': 123456,'CEDULA':12345678}

    def __init__(self) -> None:
        pass

    def Preguntar_cliente(self,diccionario):

        self.Cliente = input("Nombre del cliente: "); diccionario["Cliente"] = self.Cliente      
        self.CC = int(input("Nit/C.C. : "));diccionario["CEDULA"] = self.CC 
        self.numero = int(input("Celular: "));diccionario["Celular"] = self.numero 
    
    def Preguntar_producto(self, diccionario):
        self.Descripcion = input("Digita la pelicula: ")
        self.Cantidad = int(input("Cantidad de boletos: "))
        self.Precio = float(input("Digital el precio del producto : $"))
        self.Pagar = input("Forma de pago: ")
        self.Cajero = input("Digita el nombre del cajero: ")
        diccionario["Cajero"] = self.Cajero
    
    def Limpiar(self):
        time.sleep(2)

        if platform.system() == 'Windows':
            print("Preparando Factura....")
            time.sleep(2)
            os.system('cls')
        else:
            os.system('clear')

    def Mostrar(self,diccionario):

        self.sub = self.Cantidad * self.Precio
        self.pp =  self.sub - (self.sub * .19)
        self.Value =  diccionario.items()
        print("\t                           ",list(self.Value)[0][1])
        print("\t                         NIT: ",list(self.Value)[1][1])
        print("\t                RESPONSABLE DE IVA.  ",list(self.Value)[2][1])
        print("\t                      ",list(self.Value)[3][1])
        print("\t                        TELEFONO:",list(self.Value)[4][1])
        print("\t                  ",list(self.Value)[5][1])
        print("\t                        ",list(self.Value)[6][1])
        print("\t                        ",list(self.Value)[7][1])
        print("\n\t          ",list(self.Value)[8][1], "      FEC  01/04/2022")
        print("\t           Desde    ",list(self.Value)[9][1], "    Hasta",list(self.Value)[10][1])
        print("\t           DCTO/EQUIVALENTE POS:", list(self.Value)[11][1])
        print("\t           VIGENCIA HASTA: 31/03/2023")
        print("\t           FECHA: ",datetime.datetime.now().day,"/",datetime.datetime.now().month,"/",datetime.datetime.now().year,"      Hora:",self.hora,":",self.minuto,":",self.segundos)
        print("\t           CAJERO: ",self.Cajero)
        print("\t           CLIENTE: ",self.Cliente)
        print("\t           NIT/C.C: ",self.CC)
        print("\t           CIUDAD: Neiva")
        print("\t           Celular: ",self.numero)
        print("\t           ===============================================")
        print("\t           Uds  PRODUCT.DESCRIPCION     PRECIO        TOTAL")
        print("\t           ===============================================")
        print("\t           ",self.Cantidad,"  ",self.Descripcion,f"                ${self.Precio:.0f}","         $", self.Cantidad * self.Precio)
        print("\t           ============[ DETALLE DE VALORES ]=============")
        print("\t                                SUBTOTAL          $",self.pp)
        print("\t                                DTO   0%          $ 0")
        print("\t                                TOTAL             $",self.pp + self.sub)
        print("\t           ========[ DISCRIMINACION DE IMPUESTOS ]========")
        print("\t           I BASE 19%   ", self.pp," IVA        ", self.sub * .19)
        print("\t             TOTAL      ", self.pp,"            ", self.sub * .19)
        print("\t           ================[ FORMA DE PAGO ]==============")
        print("\t                          ",self.Pagar,f"        ${self.sub:.0f}")
        print("\t           ===============================================")
        print("\t                        !GRACIAS POR TU COMPRA!")
        print("\t        !Unete a nuestro programa de prestación con The Wiky!")
        print("\t                          AQUÍ VA EL CÓDIGO QR              ")
        print("\t                    ",list(self.Value)[5][1])
        print("\t                  Registrate con el código: 80")
        print("\t            =============================================")
        print("\t              FACTURA GENERDADA por software JEPC_2003")
        print("\t               DESARROLLADO por ICG NIT:",list(self.Value)[1][1])
        print("\t            =============================================")
        print("\t               PARA MAYOR INFORMACION SOBRE DEVOLUCIONES, ")
        print("\t                         GARANTIAS Y RETRACTO             ")
        print("\t                    CONSULTA TODO SOBRE NOSOTROS EN:    ")
        print("\t                     SOLICITUDTHEWIKY_JECP.COM.CO      ")
    
    def Mostrar_Interfaz(self):
        Ventana = Tk()
        Ventana.title("Factura Electrónica")

        Qr = Image.open("./Mi_Pagina_QR.png")
        Qr_redimensionada = Qr.resize((150,150),Image.ANTIALIAS)
        Qr_procesada = ImageTk.PhotoImage(Qr_redimensionada)

        Contenedor = Frame(Ventana, width=500, height=2500, bg="blue")
        Contenedor.pack()
        ##################################################################################
        Titulo_Fac = Label(Contenedor, text=list(self.Value)[0][1], fg="Black",bg="blue")
        Titulo_Fac.place(x=180,y=1)
        Nit = Label(Contenedor, text=f"Nit:{list(self.Value)[1][1]}",bg="blue",fg="black")
        Nit.place(x=175,y=20)
        Responsable = Label(Contenedor, text=f"Responsable de IVA.  {list(self.Value)[2][1]}",bg="blue",fg="black")
        Responsable.place(x=135,y=35)
        Agente = Label(Contenedor, text="Agente Retenedor de ICA",bg="blue",fg="black")
        Agente.place(x=155,y=53)
        Telefono = Label(Contenedor, text=f"TELEFONO:  {list(self.Value)[4][1]}",bg="blue",fg="black")
        Telefono.place(x=160,y=71)
        Pagina = Label(Contenedor, text=list(self.Value)[5][1],bg="blue",fg="black")
        Pagina.place(x=125,y=88)
        Ruta = Label(Contenedor, text=list(self.Value)[6][1],bg="blue",fg="black")
        Ruta.place(x=175,y=106)
        Codigo= Label(Contenedor, text=list(self.Value)[7][1],bg="blue",fg="black")
        Codigo.place(x=175,y=122)
        Dian = Label(Contenedor, text=f"{list(self.Value)[8][1]}    FEC  01/04/2022", bg="blue", fg="black")
        Dian.place(x=100,y=140)
        Desde = Label(Contenedor, text=f"Desde      {list(self.Value)[9][1]}  Hasta   {list(self.Value)[10][1]}",bg="blue",fg="black")
        Desde.place(x=100,y=160)
        Dcto = Label(Contenedor, text =f"DCTO/EQUIVALENTE POS:  {list(self.Value)[11][1]}",bg="blue",fg="black")
        Dcto.place(x=100, y=177)
        Vigencia = Label(Contenedor, text="VIGENCIA HASTA: 31/03/2023",bg="blue",fg="black")
        Vigencia.place(x=100,y=194)
        Datos = Label(Contenedor, text=f"FECHA:    {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}    Hora:    {self.hora}:{self.minuto}:{self.segundos}",bg="blue",fg="black")
        Datos.place(x=100,y=210)
        Cajero = Label(Contenedor, text=f"CAJERO: {self.Cajero}", bg="blue",fg="black")
        Cajero.place(x=100,y=225)
        Cliente = Label(Contenedor, text=f"CLIENTE: {self.Cliente}", bg="blue",fg="black")
        Cliente.place(x=100,y=243)
        Cedula = Label(Contenedor, text=f"NIT/C.C: {self.CC}", bg="blue",fg="black")
        Cedula.place(x=100,y=261)
        Ciudad= Label(Contenedor, text=f"CIUDAD: Neiva", bg="blue",fg="black")
        Ciudad.place(x=100,y=276)
        Tele = Label(Contenedor, text=f"Telefono: {self.numero}", bg="blue",fg="black")
        Tele.place(x=100,y=292)
        Linea1 = Label(Contenedor,text="========================================",bg="blue",fg="black")
        Linea1.place(x=100,y=308)
        Linea1 = Label(Contenedor,text="Uds  PRODUCT.DESCRIPCION     PRECIO        TOTAL",bg="blue",fg="black")
        Linea1.place(x=100,y=322)
        Linea1 = Label(Contenedor,text="========================================",bg="blue",fg="black")
        Linea1.place(x=100,y=337)
        Tele = Label(Contenedor, text=f" {self.Cantidad}            {self.Descripcion}              ${self.Precio:.0f}               ${self.sub:.0f}", bg="blue",fg="black")
        Tele.place(x=100,y=351)
        Linea1 = Label(Contenedor,text="============[ DETALLE DE VALORES ]============",bg="blue",fg="black")
        Linea1.place(x=100,y=369)
        Sub = Label(Contenedor, text=f"  TOTAL                  ${self.sub:.0f}             SUBTOTAL         ${self.pp:.0f}",bg="blue",fg="black")
        Sub.place(x=100,y=385)
        Iva = Label(Contenedor, text=f"  I BASE 19%           ${self.pp:.0f}             IVA                  ${self.sub * .19:.0f}",bg="blue",fg="black")
        Iva.place(x=100,y=400)
        Pago = Label(Contenedor,text="==============[ FORMA DE PAGO ]=============",bg="blue",fg="black")
        Pago.place(x=100,y=415)
        Decir = Label(Contenedor,text=f"               {self.Pagar}             ${self.sub:.0f}",bg="blue",fg="black")
        Decir.place(x=100,y=431)
        Linea1 = Label(Contenedor,text="========================================",bg="blue",fg="black")
        Linea1.place(x=100,y=447)
        A = Label(Contenedor,text="                           ¡GRACIAS POR TU COMPRA!                 ",bg="blue",fg="black")
        A.place(x=100,y=462)
        Visita = Label(Contenedor,text=f" Visita nuestra página: {list(self.Value)[5][1]} ",bg="blue",fg="black")
        Visita.place(x=100,y=478)
        Q = Label(Contenedor, image= Qr_procesada, bg="blue",border=30,pady=20)
        Q.place(x=160,y=498)
        ##################################################################################
        Ventana.mainloop()

print("\t\t    Bienvenido a the wikyland  S.A \n")
print("Tienda de pelicula, a continuación verás las peliculas que está disponible: ")
contador = 1
for peli in Pelicula:
    print(f"{contador} {peli}")
    contador +=1
info = input("Comenzar la infomarción para la compra?")

if info == "Si" or info == "si" and contador == contador:
    contador = 1
    os.system('cls')
    print("Pelicula disponible:")
    for peli in Pelicula:
        print(f"{contador} {peli}")
        contador +=1
    print("|"*40)
    print("\t\t Información ")
    Objeto = Factura()
    Objeto.Preguntar_cliente(Objeto.Informacion)
else:
    exit()

Objeto.Preguntar_producto(Objeto.Informacion)
Objeto.Limpiar()
Objeto.Mostrar(Objeto.Informacion)
Objeto.Mostrar_Interfaz()'''