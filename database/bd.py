from prints.prints import Print
prints = Print()
class Conexion:
    def database(self, palabra):
        import mysql.connector
        db = {
            'host' : 'localhost',
            'user' : 'root',
            'password' : '',
            'database' : 'python'
        }
        try:
            prints.palabra_usada(str(palabra))
            conexion = mysql.connector.connect(**db)
            cursor = conexion.cursor()
            resultado = ""
            if palabra == 1:
                consulta = "select * from palabras"
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                prints.palabras_ingresadas_a_bd()
                for i in resultado:
                    prints.i(str(i[1]))
                    # print(str(i[1]))
                prints.n()
            # elif palabra == 2:
            #     consulta = "select * from palabras"
            #     cursor.execute(consulta)
            #     resultado = cursor.fetchall()
            # elif palabra == 3:
            #     consulta = "select * from jugadores"
            #     cursor.execute(consulta)
            #     resultado = cursor.fetchall()
            #     for i in resultado:
            #         if self.usuario == str(i[1]):
            #             self.comprobar = 1
            #             self.id = i[0]
            #     if self.comprobar == 0:
            #         ingresar = "INSERT INTO jugadores(id, nombre) VALUES (%s, %s)"
            #         cursor.execute(ingresar,('null', self.usuario))
            #         print("USUARIO INGRESADO A LA BASE DE DATOS\n")
            #     else:
            #         print("EL USUARIO YA SE ENCUENTRA EN LA BASE DE DATOS\n")
            #     self.comprobar = 0
            # elif palabra == 4:
            #     consulta = "select * from jugadores"
            #     cursor.execute(consulta)
            #     resultado = cursor.fetchall()
            #     for i in resultado:
            #         if self.usuario == str(i[1]):
            #             self.id = i[0]
            #     ingresar = "INSERT INTO puntajes(id, puntos, jugadores) VALUES (%s, %s, %s)"
            #     cursor.execute(ingresar,('null', self.puntos, self.id))
            # elif palabra == 5:
            #     consulta = "select * from jugadores"
            #     cursor.execute(consulta)
            #     resultado = cursor.fetchall()
            #     for i in resultado:
            #         if self.id == str(i[1]):
            #             self.id = i[0]
            #     actualizar = "select sum(puntajes.puntos) from puntajes where puntajes.jugadores = %s"
            #     # actualizar = "select * from jugadores"
            #     # cursor.execute(actualizar,(self.id,))
            #     cursor.execute(actualizar,(self.id,))
            #     resultado = cursor.fetchone()
            #     print(resultado)
            else:
                print("PRUEBON")
                ingresar = "INSERT INTO palabras(id, palabra) VALUES (%s, %s)"
                cursor.execute(ingresar,('null', palabra))
                print("PRUEBONZOTE")
            conexion.commit()
            return resultado
        except Error as e:
            print("Error while connecting to MySQL", e)
        # finally:
        #     if (conexion.is_connected()):
        #     cursor.close()
        #     conexion.close()
        #     # print("MySQL connection is closed")