from sqlalchemy import create_engine, text


class DatabaseHandler:
    def __init__(self, url):
        self.engine = create_engine(url)

    def run_query(self, query, is_select=False):
        with self.engine.connect() as conn:
            try:
                result = None
                if is_select:
                    result = conn.execute(text(query))
                else:
                    conn.execute(text(query))
                conn.commit()
            except Exception as e:
                conn.rollback()
                print(str(e))

        if result:
            return result

    def insert_data(self, query, data):
        with self.engine.connect() as conn:
            try:
                # bulk insert funkció
                conn.execute(text(query), data)
                conn.commit()
            except Exception as e:
                conn.rollback()
                print(str(e))


if __name__ == '__main__':
    url = "postgresql://postgres:postgres@localhost:5432/postgres"
    test = DatabaseHandler(url)

    test.run_query('create table python_test(name text)')
