import contextlib 
class Query(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s...' % self.name)



@contextlib.contextmanager
def create_query(name):
    print('Begin')
    yield Query('Bob')
    print('End')

with create_query('Bob') as q:
    q.query()
        
# Begin
# Query info about Bob...
# End