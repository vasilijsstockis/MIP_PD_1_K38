class gameNode:
    def __init__(self, scoreFirst, scoreSecond, scoreBank
                 , currentValue, nodeTwo, nodeThree, nodeFour):
        
        #Punktu skaita glabāšana
        self.scoreFirst  :int = scoreFirst
        self.scoreSecond :int = scoreSecond
        self.scoreBank   :int = scoreBank

        #Skaitlis
        self.currentValue :int = currentValue

        #Nākamie iespējamie soļi
        self.nodeTwo    :gameNode = nodeTwo
        self.nodeThree  :gameNode = nodeThree
        self.nodeFour   :gameNode = nodeFour

        #kam ir kārta?
        #self.Turn :bool

        #self.previousNode :gameNode
