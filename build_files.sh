# build_files.sh

pip install psycopg2-binary
sqlite3 db.sqlite .dump > sqlite_dump.sql
psql -U your_username -d your_database_name -f sqlite_dump.sql

# make migrations
python3.9 manage.py makemigrations
python3.9 manage.py migrate 

