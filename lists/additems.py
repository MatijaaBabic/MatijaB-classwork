class NodeType:   
    def __init__(self,nane,ponter):
        self.name = nane                    #has to be different than atribute
        self.pointer = ponter
    def __repr__(self) -> str:
        return f'(Name: {self.name}; Pointer: {self.pointer})'