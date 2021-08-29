# ----------------------------------------------------------------------------------------------------------------------
# Funkcje do obslugi bazy danych
# ----------------------------------------------------------------------------------------------------------------------

# Polaczenie z baza danych
def db_conn():
    import pyodbc

    db_driver = '{SQL Server}'
    db_server = 'W-BOGACZR\SQLEXPRESS'
    db_database = 'MusicWorld'

    conn = pyodbc.connect(
        'Driver=' + db_driver + ';Server=' + db_server + ';Database=' + db_database + ';Trusted_Connection=yes;')
    return conn

# Wykonanie zapytania na bazie danych
def db_querry(zapytanie):
    conn = db_conn()
    cursor = conn.cursor()
    cursor.execute(zapytanie)
    conn.commit()

# Usunięcie wszystkich rekordów z tabeli bazy danych
def db_truncate_table(table_to_truncate):
    db_querry(f"TRUNCATE TABLE [MusicWorld].[dbo].[{table_to_truncate}]")

# Odczytywanie całej tabeli z bazy danych
def db_read_whole_table_to_pandas(table_to_read):
    import pandas as pd
    conn = db_conn()
    cursor = conn.cursor()

    data = pd.read_sql(f"SELECT * from [MusicWorld].[dbo].[{table_to_read}]", conn)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    return data

# Zwrócenie pojedynczej kolumny z bazy danych jako listy
def db_read_columns_to_pandas(kolumny, table_to_read):
    import pandas as pd
    conn = db_conn()
    cursor = conn.cursor()

    if len(kolumny) == 1:
        data = pd.read_sql(f"SELECT {kolumny[0]} from [MusicWorld].dbo.[{table_to_read}]", conn)
    elif len(kolumny) == 2:
        data = pd.read_sql(f"SELECT {kolumny[0]}, {kolumny[1]} from [MusicWorld].dbo.[{table_to_read}]", conn)
    elif len(kolumny) == 3:
        data = pd.read_sql(f"SELECT {kolumny[0]}, {kolumny[1]}, {kolumny[2]} from [MusicWorld].dbo.[{table_to_read}]",
                           conn)
    else:
        data = pd.read_sql(
            f"SELECT {kolumny[0]}, {kolumny[1]}, {kolumny[2]}, {kolumny[3]} from [MusicWorld].dbo.[{table_to_read}]",
            conn)

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    return data

# Zwrócienie wybranej kolumny z tabeli bazy danych
def db_read_column_to_table(kolumna, table_to_read):
    import pandas as pd
    conn = db_conn()
    cursor = conn.cursor()

    data = pd.read_sql(f"SELECT {kolumna} from [MusicWorld].dbo.[{table_to_read}]", conn)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    table = data[kolumna].values.tolist()
    return table
