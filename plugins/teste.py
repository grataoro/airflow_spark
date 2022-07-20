import json 

from airflow.hooks.base import BaseHook

class teste(BaseHook):

    def def_teste(self):

        conn = self.get_connection('OpenTripMapAPI')
        print(json.loads(conn.get_extra())['Autorization'])



if __name__ == "__main__":
    teste().def_teste()        