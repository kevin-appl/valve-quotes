import sqlalchemy, os
from flask import Flask, jsonify
from sqlalchemy.dialects.mysql import INTEGER

ENV_DB_PASSWORD = os.environ['ENV_DB_PASSWORD']

engine_url = 'mysql+pymysql://root:' + ENV_DB_PASSWORD + '@mysql:3306/valvequotes'

# 'pool_recycle': A connection can persist for 3600 seconds.
#   By default, MySQL will disconnect automatically if no activity is detected on a connection for eight hours.
engine = sqlalchemy.create_engine(engine_url, pool_size=5, pool_recycle=3600)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET'])
def main():
    return 'Cannot GET /v1/', 404

@app.route('/quotes/', methods=['GET'])
@app.route('/quotes/<int:count>', methods=['GET']) # Converter type 'int' accepts positive integers.
def quotes(count=1):

    if count == 0:
        return 'Cannot GET /v1/quotes/0', 404
    
    # Create a parameterized SQL query.
    stmt = sqlalchemy.sql.text('SELECT content, author FROM quote ORDER BY RAND() LIMIT :c')
    stmt = stmt.bindparams(sqlalchemy.sql.bindparam('c', type_=INTEGER))

    cnx = engine.connect()
    cursor = cnx.execute(stmt, {'c': count})
    result = cursor.fetchall()

    cnx.close() # Since we're using a connection pool, this sends the connection back to the pool instead of closing it.

    quotes = []
    
    for row in result:
        quotes.append(
            {
                "quote":row[0],
                "author":row[1]
            }
        )

    return jsonify(
        quotes
    )

if __name__ == '__main__':
    app.run()