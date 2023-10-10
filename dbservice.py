import psycopg2


conn = psycopg2.connect(
    host='127.0.0.1',
    database = "twitter-clone",
    user = "postgres",
    password = "2345"
    
)

