class conexion:
    usuario = ""
    comprobar = 0
    id = 0
    puntos = 0
    fin = 0
    def database(self, palabra):
        import mysql.connector
        db = {
            'host' : 'localhost',
            'user' : 'root',
            'password' : '',
            'database' : 'python'
        }

        try:
            conexion = mysql.connector.connect(**db)
            cursor = conexion.cursor()
            resultado = ""
            if palabra == 1:
                consulta = "select * from palabras"
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                print("\nPALABRAS INGRESADAS EN LA BASE DE DATOS:")
                for i in resultado:
                    print(str(i[1]))
                print("\n")
            elif palabra == 2:
                consulta = "select * from palabras"
                cursor.execute(consulta)
                resultado = cursor.fetchall()
            elif palabra == 3:
                consulta = "select * from jugadores"
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                for i in resultado:
                    if self.usuario == str(i[1]):
                        self.comprobar = 1
                        self.id = i[0]
                if self.comprobar == 0:
                    ingresar = "INSERT INTO jugadores(id, nombre) VALUES (%s, %s)"
                    cursor.execute(ingresar,('null', self.usuario))
                    print("USUARIO INGRESADO A LA BASE DE DATOS\n")
                else:
                    print("EL USUARIO YA SE ENCUENTRA EN LA BASE DE DATOS\n")
                self.comprobar = 0
            elif palabra == 4:
                consulta = "select * from jugadores"
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                for i in resultado:
                    if self.usuario == str(i[1]):
                        self.id = i[0]
                ingresar = "INSERT INTO puntajes(id, puntos, jugadores) VALUES (%s, %s, %s)"
                cursor.execute(ingresar,('null', self.puntos, self.id))
            elif palabra == 5:
                consulta = "select * from jugadores"
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                for i in resultado:
                    if self.id == str(i[1]):
                        self.id = i[0]
                actualizar = "select sum(puntajes.puntos) from puntajes where puntajes.jugadores = %s"
                # actualizar = "select * from jugadores"
                # cursor.execute(actualizar,(self.id,))
                cursor.execute(actualizar,(self.id,))
                resultado = cursor.fetchone()
                print(resultado)
            else:
                ingresar = "INSERT INTO palabras(id, palabra) VALUES (%s, %s)"
                cursor.execute(ingresar,('null', palabra))
            conexion.commit()
            return resultado
        except:
            print("!!!NO HAY CONEXION A LA BASE DE DATOS!!!\n"
            + "SE LIMITARÁN ALGUNAS FUNCIONES COMO:"
            + "    1 - NO PODRÁ CONSULTAR SU PUNTUACIÓN"
            + "    2 - NO PODRÁ REGISTRAR SU USUARIO EN LA BASE DE DATOS")
            return ""