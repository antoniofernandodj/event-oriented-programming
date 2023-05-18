import asyncio
import aiomysql
from dataclasses import dataclass

@dataclass
class User:
    username: str
    password: str
    name: str
    email: str

async def get_connection():
    connection = await aiomysql.connect(
        host='::', port=3306, user='antonio',
        password='senha123', db='aiomysql'
    )
    return connection

class DatabaseHandler:
    def __init__(self):
        self.host='::'
        self.port=3306
        self.user='antonio'
        self.password='senha123'
        self.db='aiomysql'
    
    async def __aenter__(self):
        self.connection = await aiomysql.connect(
            host=self.host, port=self.port, user=self.user,
            password=self.password, db=self.db
        )
        print('connection started!')
        return self.connection
    
    async def __aexit__(self, *args):
        self.connection.close()
        print('connection closed!')

class UserRepository:

    def __init__(self, connection):
        self.connection = connection
        self.table_name = User.__name__.lower()

    async def create_table(self):
        self.cursor = await self.connection.cursor()
        sql = f'''
            CREATE TABLE {self.table_name} (
                username VARCHAR(100),
                password TEXT,
                name VARCHAR(100),
                email VARCHAR(100)
            );
        '''

        await self.cursor.execute(sql)
        await self.cursor.close()

    async def save(self, user: User):

        self.cursor = await self.connection.cursor()
        sql = f"""
            INSERT INTO {self.table_name} (
                username, password, name, email
            ) VALUES (
                '{user.username}',
                '{user.password}',
                '{user.name}',
                '{user.email}'
            );
        """
        print(sql)

        await self.cursor.execute(sql)
        await self.connection.commit()
        result = await self.cursor.fetchall()
        await self.cursor.close()

    async def update(self, user: User):
        self.cursor = await self.connection.cursor()
        sql = f"""
            UPDATE {self.table_name}
            SET password = '{user.password}',
                name = '{user.name}',
                username = {user.username},
                email = '{user.email}'
            WHERE username = '{user.username}';
        """
        await self.cursor.execute(sql)
        await self.connection.commit()
        await self.cursor.close()

    async def delete(self, username: str):
        self.cursor = await self.connection.cursor()
        sql = f"""
            DELETE FROM {self.table_name}
            WHERE username = '{username}';
        """
        await self.cursor.execute(sql)
        await self.connection.commit()
        await self.cursor.close()

    async def find(self, username: str) -> User:
        self.cursor = await self.connection.cursor(aiomysql.DictCursor)
        sql = f"""
            SELECT username, password, name, email
            FROM {self.table_name}
            WHERE username = '{username}';
        """
        await self.cursor.execute(sql)
        result = await self.cursor.fetchone()
        print(result)
        await self.cursor.close()

        if result:
            return User(
                username=result['username'],
                password=result['password'],
                name=result['name'],
                email=result['email']
            )
        else:
            return None

async def main():
    async with DatabaseHandler() as connection:
        username='ricardo2'
        user_repo = UserRepository(connection)
        user = await user_repo.find(username=username)


asyncio.run(main())