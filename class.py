class gameNode:
    def __init__(self, scoreFirst, scoreSecond, scoreBank
                 , currentValue,turn):
        
        #Punktu skaita glabāšana
        self.scoreFirst  :int = scoreFirst
        self.scoreSecond :int = scoreSecond
        self.scoreBank   :int = scoreBank

        #kam ir kārta
        self.turn :bool = turn

        #Skaitlis
        self.currentValue :int = currentValue

        #Nākamie iespējamie soļi
        self.nodeTwo    :gameNode = None
        self.nodeThree  :gameNode = None
        self.nodeFour   :gameNode = None

        #self.previousNode :gameNode
    def __str__(self):
        return f"Number is {self.currentValue}\nFirst player score is: {self.scoreFirst}\nSecond player score is: {self.scoreSecond}\nBank: {self.scoreBank}\nfirts's turn == {self.turn}\n----------------------------------"


def populateTree(start : gameNode, maxValue : int) ->None:
    if(start.currentValue>=maxValue):
        ## last node is an end node, that means the previous player achived it. Therefore turn is oposite
        if(start.turn):
            start.scoreSecond=start.scoreSecond+start.scoreBank
        else:
            start.scoreFirst=start.scoreFirst+start.scoreBank

        start.scoreBank=0
        return
    else:
        bank=0
        even=0
        if (not (start.currentValue%5)):
            bank=1
        if (not start.currentValue%2):
            even=-1
        else:
            even=1
        
        start.nodeTwo=  gameNode(start.scoreFirst+start.turn*-1, start.scoreSecond+(not start.turn)*-1, start.scoreBank+bank, start.currentValue*2, not start.turn)
        start.nodeThree=gameNode(start.scoreFirst+start.turn*even, start.scoreSecond+(not start.turn)*even, start.scoreBank+bank, start.currentValue*3, not start.turn)
        start.nodeFour= gameNode(start.scoreFirst+start.turn*-1, start.scoreSecond+(not start.turn)*-1, start.scoreBank+bank, start.currentValue*4, not start.turn)

        populateTree(start.nodeTwo,   maxValue)
        populateTree(start.nodeThree, maxValue)
        populateTree(start.nodeFour,  maxValue)
    

if __name__ == "__main__":
    x=gameNode(0,0,0,20,True)
    populateTree(x,5000)

    while(x is not None):
        print(x)
        s=int(input("2, 3 or 4\n"))
        if(s==2):
            x=x.nodeTwo
        if(s==3):
         x=x.nodeThree
        if(s==4):
            x=x.nodeFour
