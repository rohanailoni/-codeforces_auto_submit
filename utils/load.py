import pickle



def load_session(name):
    dbfile = open(name, 'rb')     
    db = pickle.load(dbfile)
    dbfile.close()
    return db