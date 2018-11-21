Stack=[]
Code=[]
Jumps={}

ExecuteLine = -1
JumpLine= 0
AX = 0x0;
BX = 0x0;
CX = 0x0;
DX = 0x0;


carryFlag = False
parityFlag = False
auxCarryFlag = False
zeroFlag = False
overflowFlag = False
traceFlag = False
interruptFlag = False
DirectionFlag = False
signFlag = False

#MOV, POP, PUSH
def Mov(register, operator):
    global AX,BX,CX,DX

    operator = int(operator, 16)
    if(register=="AX"):
        AX=operator
        
    if(register=="BX"):
        BX=operator

    if(register=="CX"):
        CX=operator

    if(register=="DX"):
        DX=operator

    printEstatus()


def Pop(register):
    global AX,BX,CX,DX

    if(register=="AX"):
        AX=Stack.pop()
        
    if(register=="BX"):
        BX=Stack.pop()

    if(register=="CX"):
        CX=Stack.pop()

    if(register=="DX"):
        DX=Stack.pop()
    printEstatus()
    
def Push(register):

    global AX,BX,CX,DX
    
    if(register=="AX"):
        AX=Stack.append(AX)
        
    if(register=="BX"):
        BX=Stack.append(BX)

    if(register=="CX"):
        CX=Stack.append(CX)

    if(register=="DX"):
        DX=Stack.append(DX)
    printEstatus()

#ADD, SUB, DIV, MUL, DEC, INC


def Add(register,value):
    global AX, BX, CX, DX

    if value in ["AX","BX","CX","DX"]:
        value = globals()[value]
    else:
        value=int(value,16)
    if (register=="AX"):
        AX+=value
    elif (register=="BX"):
        BX+=value

    elif (register=="BX"):
        CX+=value

    elif (register=="CX"):
        DX+=value
    printEstatus()


def Sub(register,value):
    global AX, BX, CX, DX
    
    if value in ["AX","BX","CX","DX"]:
        value = globals()[value]
    else:
        value=int(value,16)

    if (register=="AX"):
        AX-=value
    elif (register=="BX"):
        BX-=value

    elif (register=="BX"):
        CX-=value

    elif (register=="CX"):
        DX-=value
    printEstatus()

def Div(register):
    global AX,BX,CX,DX

    if(register=="AX"):
        DX =  AX%AX
        AX = AX//AX

    elif(register=="BX"):
        DX =  BX%AX
        AX = BX//AX
        
    elif(register=="CX"):
        DX =  CX%AX
        AX = CX//AX
        
    elif(register=="DX"):
        DX =  DX%AX
        AX = DX//AX
    printEstatus()

def Mul(register):
    global AX,BX,CX,DX

    if (register=="AX"):
        AX= AX*AX

    elif(register=="BX"):
        AX=BX*AX
        
    elif(register=="CX"):
        AX=CX*AX
        
    elif(register=="DX"):
        AX=DX*AX
    printEstatus()
        
def Inc(register):
    global AX,BX,CX,DX

    if (register=="AX"):
        AX+=1

    elif(register=="BX"):
        BX+=1
        
    elif(register=="CX"):
        CX+= 1
        
    elif(register=="DX"):
        DX+=1
    printEstatus()

def Dec(register):
    global AX,BX,CX,DX

    if (register=="AX"):
        AX-=1

    elif(register=="BX"):
        BX-=1
        
    elif(register=="CX"):
        CX-= 1
        
    elif(register=="DX"):
        DX-=1
    printEstatus()

# CMP, AND, OR, XOR, NOT

def Cmp(register,value):
    global AX,BX,CX,DX
    
    if register == 'AX':
        if value == AX:
            return True
        elif value != AX:
            return False
    elif register == 'BX':
        if value == BX:
            return True
        elif value != BX:
            return False
    elif register == 'CX':
        if value == CX:
            return True
        elif value != CX:
            return False
    elif register == 'DX':
        if value == DX:
            return True
        elif value != DX:
            return False
    printEstatus()

def And(register,Op2):
    global AX,BX,CX,DX
    
    if Op2 in ["AX", "BX", "CX","DX"]:
        Op2 = globals()[Op2]
    else:
        Op2 = int(Op2, 16)

    y =globals()[register[:2]]
    Op1 = int(bin(y),2)
    Op2 = int(bin(Op2), 2)

    if (register == "AX,"):
        AX = int(hex(Op1.__and__(Op2)), 16)
    elif (register == "BX,"):
        BX = int(hex(Op1.__and__(Op2)), 16)
    elif (register == "CX,"):
        CX = int(hex(Op1.__and__(Op2)), 16)
    elif (register == "DX,"):
        DX = int(hex(Op1.__and__(Op2)), 16)

    printEstatus()

def Or(register, Op2):
    global AX,BX,CX,DX
    if Op2 in ["AX", "BX", "CX", "DX"]:
        Op2 = globals()[Op2]
    else:
        Op2 = int(Op2, 16)

    y = globals()[register[:2]]
    Op1 = int(bin(y), 2)
    Op2 = int(bin(Op2), 2)

    if (register == "AX,"):
        AX = int(hex(Op1.__or__(Op2)), 16)
    elif (register == "BX,"):
        BX = int(hex(Op1.__or__(Op2)), 16)
    elif (register == "CX,"):
        CX = int(hex(Op1.__or__(Op2)), 16)
    elif (register == "DX,"):
        DX = int(hex(Op1.__or__(Op2)), 16)

    printEstatus()
    
def Xor(register, Op2):
    global AX,BX,CX,DX
    
    if Op2 in ["AX", "BX", "CX", "DX"]:
        Op2 = globals()[Op2]
    else:
        Op2 = int(Op2, 16)

    y = globals()[register[:2]]
    Op1 = int(bin(y), 2)
    Op2 = int(bin(Op2), 2)

    if (register == "AX,"):
        AX = int(hex(Op1.__xor__(Op2)), 16)
    elif (register == "BX,"):
        BX = int(hex(Op1.__xor__(Op2)), 16)
    elif (register == "CX,"):
        CX = int(hex(Op1.__xor__(Op2)), 16)
    elif (register == "DX,"):
        DX = int(hex(Op1.__xor__(Op2)), 16)

    printEstatus()

def NOT(register):
    global AX,BX,CX,DX

    if register in ["AX", "BX", "CX", "DX"]:
        Op1 = globals()[register[:2]]

    Op1 = int(bin(Op1),2)
    exp = Op1.bit_length()
    xor = 2**exp-1

    if (register == "AX"):
        AX = int(hex(Op1.__xor__(xor)), 16)
    elif (register == "BX"):
        BX = int(hex(Op1.__xor__(xor)), 16)
    elif (register == "CX"):
        CX = int(hex(Op1.__xor__(xor)), 16)
    elif (register == "DX"):
        DX = int(hex(Op1.__xor__(xor)), 16)

    printEstatus()

#JE JNE JZ JNZ JMP

def printEstatus():
    global carryFlag
    global parityFlag
    global auxCarryFlag
    global zeroFlag
    global overflowFlag
    global traceFlag
    global interruptFlag
    global DirectionFlag
    global signFlag

    print("STACK")
    for x in range(len(Stack)):
        print(Stack[x])
    print("                                 ")
    print("AX =     ", hex(AX))
    print("BX =     ", hex(BX))
    print("CX =     ", hex(CX))
    print("DX =     ", hex(DX))
    print("                      ")
    print("FLAGS    CF      PF      ACF     ZF      OF      TF      IF      DF      SF")
    print("        ", carryFlag ," ", parityFlag ," ", auxCarryFlag ," ", zeroFlag ," ", overflowFlag ," ", traceFlag ," ", interruptFlag ," ", DirectionFlag ," ", signFlag)
    #print(codigoEJECUTAR)
    print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////// \n")

def main():
    Mov(AX,10)












        


        
    
