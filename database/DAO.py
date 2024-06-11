from database.DB_connect import DBConnect
from model.Nazioni import Nazione
from model.Contiguity import Contiguity


class DAO():



    @staticmethod
    def getAllNazioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.*
            from country c"""
        cursor.execute(query)
        for row in cursor:
            result.append(Nazione(row["CCode"],row["StateAbb"], row["StateNme"]))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getConnessioni(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.*
            from contiguity c 
            where c.year <= %s"""
        cursor.execute(query,(anno,))
        for row in cursor:
            result.append(Contiguity(row["dyad"], row["state1no"], row["state2no"],row["conttype"]))
        cursor.close()
        conn.close()
        return result