import sqlite3 as sql


class DBTool:
    def __init__(self, address, **kwargs) -> None:
        self.address = address
        self.conn = sql.connect(self.address)
        self.cursor = self.conn.cursor()
        self.table = kwargs.get('table')
        self.columns = kwargs.get('columns')
        self.values = kwargs.get('values')
        self.condition = kwargs.get('condition')
        self.order = kwargs.get('order')
        self.limit = kwargs.get('limit')

    def select(self, **kwargs) -> list:
        table = kwargs.get('table')
        if not table:
            table = self.table
        columns = kwargs.get('columns')
        if not columns:
            columns = self.columns
        condition = kwargs.get('condition')
        if not condition:
            condition = self.condition
        order = kwargs.get('order')
        if not order:
            order = self.order
        limit = kwargs.get('limit')
        if not limit:
            limit = self.limit
        query = f"""
        SELECT {columns if columns else '*'} FROM {table} WHERE {condition if condition else '1=1'} 
        ORDER BY {order if order else 'id'} LIMIT {limit if limit else '10'}
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert_data(self, **kwargs) -> int:
        try:
            table = kwargs.get('table')
            if not table:
                table = self.table
            columns = kwargs.get('columns')
            if not columns:
                columns = self.columns
            values = kwargs.get('values')
            if not values:
                values = self.values
            query = f"""
            INSERT INTO {table} ({columns}) VALUES ({values})
            """
            self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
            self.conn.rollback()
            return None

    def update_data(self, *args, **kwargs) -> None:
        try:
            table = kwargs.get('table')
            if not table:
                table = self.table
            columns = kwargs.get('columns')
            if not columns:
                columns = self.columns
            values = kwargs.get('values')
            if not values:
                values = self.values
            condition = kwargs.get('condition')
            if not condition:
                condition = self.condition
            query = f"""
            UPDATE {table} SET {columns}={values} WHERE {condition}
            """
            self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(e)
            self.conn.rollback()
            return None

    def delete_data(self, *args, **kwargs) -> None:
        try:
            table = kwargs.get('table')
            if not table:
                table = self.table
            condition = kwargs.get('condition')
            if not condition:
                condition = self.condition
            query = f"""
            DELETE FROM {table} WHERE {condition}
            """
            self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(e)
            self.conn.rollback()
            return None

    def __del__(self) -> None:
        self.cursor.close()
        self.conn.close()
