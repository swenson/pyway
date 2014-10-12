# run sqlite3 migrations
#
# usage: python pyway.py your.db migrations/
# where:
#   - your.db is the name of your database (sqlite3 in this case)
#   - migrations/ is a directory of migrations, i.e.,
#     migrations/001_initial.sql, migrations/002_something.sql, etc.

import glob
import os.path
import subprocess as sp
import sys

if len(sys.argv) < 3:
  exit("usage: python pyway.py yourdb.db dir_of_migrations/")

dbfile = sys.argv[1]

table_migration = '''
create table if not exists migrations (
  id text primary key
);'''

check_migration = 'select id from migrations;'
insert_migration = 'insert into migrations (id) values (\'%s\');'

def run_sql(sql):
  return sp.check_output(['/usr/bin/sqlite3', '-line', dbfile, sql])

run_sql(table_migration)
existing_migrations = set([l.split('=')[-1].strip() for l in run_sql(check_migration).strip().split('\n')])

migrations = sorted(glob.glob(os.path.join(sys.argv[2], '*.sql')))
for file in migrations:
  if file not in existing_migrations:
    print 'Running migration', file
    print run_sql(open(file).read())
    print run_sql(insert_migration % file)

print 'All %d migrations accounted for' % len(migrations)
