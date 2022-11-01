
# this page is sepcially dealting with custom exceptions for errors in arguments



class submitargnotfound(Exception):
    def __init__(self,*args):
        super().__init__(args)
    def __str__(self):
        return "The submit argument is required as contestId is mentioned"
class fileargnotfound(Exception):
    def __init__(self,*args):
        super().__init__(args)
    def __str__(self):
        return "The submit argument is required as contestId is mentioned"

    
    




