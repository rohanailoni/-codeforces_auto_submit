
# this page is sepcially dealting with custom exceptions for errors in arguments
class wrongproblemId(Exception):
    def __init__(self,id,def_list,*args):
        super().__init__(args)
        self.id=id
        self.def_list=def_list

    def __str__(self):
        return "The problem id {self.id} is not in the default list of ID's that are {self.def_list}"


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

    
class problemIdargnotfound(Exception):
    def __init__(self,*args):
        super().__init__(args)
    def __str__(self):
        return "The problem Id is mandetory to submit a contest problem"








