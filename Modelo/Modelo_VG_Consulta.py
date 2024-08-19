
class  Consulta:
        
    CREATE= '''
            CREATE TABLE empleado(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(50) NOT NULL,
            Cargo VARCHAR(50) NOT NULL,
            Salario INT NOT NULL)
            '''
    DELETE_TABLE="DROP TABLE empleado"
    INSERT="INSERT INTO empleado VALUES(NULL,?,?,?)"
    SELECT="SELECT * FROM empleado"
    UPDATE="UPDATE empleado SET Nombre=?,Cargo=?,Salario=? WHERE ID="
    DELETE="DELETE FROM empleado WHERE ID="
    BUSCAR="SELECT * FROM empleado WHERE Nombre Like '%' || ?|| '%'"
