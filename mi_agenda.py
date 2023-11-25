import os
import sys
import sqlite3 # Librería de SQLite
#from prettytable import PrettyTable  # pip install prettytable   
    
"""           
                                      
"""
                               
   
def menu() :  
    os.system("cls")
    print("1-crear DBase (CREATE)")                                   
    print("2-Agregar una persona (INSERT)") 
    print("3-Actualizar info. de una persona (UPDATE)")
    print("4-Borrar una persona (DELETE)") 
    print("5-Mostrar la informacion (SELECT)")
    print("6-Mostrar la informacion-version 2 (SELECT)")
    print("7-Salir")      
    op = "0"                                          
    while op < '1' or op > '7' :  
       op = input("capturar una opcion: ")         
       if op >= '1' and op <= '7' :
           return op   
                       
def procCreate() :     
    print("\n--CREATE--") 
    c.execute("""CREATE TABLE gente (          
          clave int,              
          nombre char(100),         
          celular char(20),            
          email char(100),        
          direccion text)""") 
    c.execute("""CREATE TABLE citas 
       (dia date, 
       hora time, 
       motivo text, 
       persona int)""")                        
    c.commit()                 
    print("tablas creadas....")
    input("\n<pulsa ENTER para continuar....>")
      
                        
def procSelect() :                              
    print("\n--SELECT--")
    q.execute('SELECT clave, nombre, email, rowid FROM gente ORDER BY nombre')
    regs = q.fetchall()                             
    print("Clave\tNombre\t\tE-Mail") 
    print("-------------------------------------------")
    for renglon in regs :                             
        print(f"{renglon[0]}\t{renglon[1]}\t\t{renglon[2]}\t\t\t{renglon[3]}")
        #print(renglon[0], "\t" , renglon[1] )   
    input("\n<pulsa ENTER para continuar....>")                         
                           
"""                              
def procSelect2() :                              
    print("\n--SELECT--")
    q.execute('SELECT rowid, clave, nombre, email FROM gente ORDER BY nombre')
    regs = q.fetchall()
    
    tabla = PrettyTable(['id', 'Clave', 'Nombre', 'E-Mail'])
    for renglon in regs :
        tabla.add_row(renglon)                             
    print(tabla)    
    input("\n<pulsa ENTER para continuar....>")                         
"""  
    
def procSelect3() :
    res = c.execute("SELECT clave, nombre FROM gente ")
    d = res.fetchall()
    for dd in d :         
        print(f"{dd[0]}     {dd[1]}") 
    input("\n<pulsa ENTER para continuar....>")                         
                                                                          
def procDelete() :                                              
    print("\n--DELETE--")
    reg = input("Clave de registro a borrar: ")
    q.execute(f'DELETE FROM gente WHERE clave = "{reg}" ') 
    q.commit()
    print("Registro borrado....")              
    input("\n<pulsa ENTER para continuar....>")                                       
                                                     
                                                 
def procInsert() :                              
    print("\n--INSERT--")                                  

    clave = ""
    while clave == "" :
       clave = input("Clave: ")
       q.execute(f'SELECT rowid FROM gente WHERE clave = "{clave}" ')  
       reg = q.fetchone() 
       if not reg is None :
           print("la clave ya existe, prueba con otra.....")
           clave = ""
          
    nombre = ""                 
    while nombre == "" :      
       nombre = input("Nombre: ")
           
           
                            
    email = input("Correo Electronico: ")
    cel = input("Celular: ")
    dir = input("Direccion: ")
    q.execute(f"""INSERT INTO gente (clave, nombre, email, celular, direccion)
           VALUES       
           ('{clave}', '{nombre}', '{email}', '{cel}', '{dir}') """)
    c.commit()  
    print("Registro agregado....")
    input("\n<pulsa ENTER para continuar....>")                                       
                      
          
    
    
    
def procUpdate() :        
    print("\n--UPDATE--") 
    clave = input("Clave de registro a modificar: ")
    q.execute(f'SELECT clave, nombre, email, direccion, celular FROM gente WHERE clave = "{clave}" ')
    reg = q.fetchone()   #q.fetchall()                                            
    if reg is None :                                                               
        print("No se encontró ningún registro con esa clave.....")
    else :
        nombre = input(f"Nombre actual: {reg[1]} --- Nuevo nombre: ")                 
        email = input(f"Correo Electronico actual: {reg[2]} --- Nuevo correo electronico: ")     
        cel = input(f"Celular actual: {reg[4]} --- nuevo Celular: ") 
        dir = input(f"Direccion actual: {reg[3]} --- nueva Direccion: ")              
     
        q.execute(f"""UPDATE gente      
           SET nombre = '{nombre}', 
               email = '{email}',  
               direccion = '{dir}',     
               celular = '{cel}'                   
           WHERE clave = '{clave}'      
        """) 
        #q.execute("UPDATE gente SET nombre = '", nombre, "', email = '", email, ....)
        #q.execute("UPDATE gente SET nombre = '" + nombre + ", email = '" + email + "'...') 
        c.commit()           
        print("Registro modificado....")
                                                          
                              
    input("\n<pulsa ENTER para continuar....>")                                       
    
    
                                           
global c   
global q
c = sqlite3.connect("mis_citas.db") 
q = c.cursor()                
while True :      
    opc = menu()
    if opc == '1' :        
        procCreate()
    elif opc == '2' :
        procInsert()
    elif opc == '3' :
        procUpdate()
    elif opc == '4' :     
        procDelete()
    elif opc == '5' :
        procSelect() 
    elif opc == '6' :
        procSelect3() 
    elif opc == '7' :
        c.close()
        sys.exit()
        
        
        
        
        
                          
