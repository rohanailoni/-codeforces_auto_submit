from fileinput import filename
import pickle
import os
def dump_session(session,filename):
    if os.path.isfile(filename):
        os.remove(filename)
    dbfile = open(filename, 'ab')
    pickle.dump(session, dbfile)                     
    dbfile.close()
    return ""