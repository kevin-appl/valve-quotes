FROM mysql

ENV MYSQL_DATABASE valvequotes

COPY quotes.csv /var/mysql-csv/

ADD script.sql /docker-entrypoint-initdb.d
