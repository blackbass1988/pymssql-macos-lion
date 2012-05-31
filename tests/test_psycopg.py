from nose.tools import eq_
from nose.plugins.skip import SkipTest

import psycopg2

from .helpers import CursorBase

# this module is only for testing how a different DBAPI driver handles things
# it isn't really part of our testing, just nice to have handy.
raise SkipTest

class TestCursor(CursorBase):
    dbmod = psycopg2

    def newconn(self):
        self.conn = psycopg2.connect(database='test', user='postgres', password='postgres', host='rcsserver')

    def test_select_rowcount(self):
        cur = self.execute('select * from test')
        eq_(cur.rowcount, 5)
        cur.fetchall()
        eq_(cur.rowcount, 5)
