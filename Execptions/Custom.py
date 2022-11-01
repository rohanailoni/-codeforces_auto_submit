# This page is for creating custom errors 


class SessionNotFound(Exception):
    def __init__(self,*args):
        super().__init__(args)
    def __str__(self):
        return "The session file is not found Try login in again to get fresh cookies"