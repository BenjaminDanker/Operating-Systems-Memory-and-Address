pageTable = {1: "0x1000", 20: "0xAA00"}

def getOffset(logicalAddress):
    # splice last two digits
    return logicalAddress[4:]

def getPagenum(logicalAddress):
    # convert to decimal, divide by size, convert back to hex
    pageNum = int(logicalAddress, 16)
    pageNum //= 1024
    
    return pageNum

def addAddress(pageNum):
    # latest frame base
    newFrameBase = list(pageTable.values())[-1]
    # convert to decimal and add 0x1000 to frame base
    newFrameBase = int(newFrameBase, 16) + 4096
    # convert back to hex
    newFrameBase = hex(newFrameBase)
    pageTable[pageNum] = str(newFrameBase)
    
def getPhysicalAddress(pageNum, offset):
    # get base address from table
    physicalAddress = pageTable[pageNum]
    # create physical address
    physicalAddress = "0x" + physicalAddress[2:4].upper() + offset

    return physicalAddress

def main():
    ### Testing cases
    logicalAddress = "0x3A7F"
    pageNum, offset = getPagenum(logicalAddress), getOffset(logicalAddress)
    addAddress(pageNum)
    
    logicalAddress = "0xABCD"
    pageNum, offset = getPagenum(logicalAddress), getOffset(logicalAddress)
    addAddress(pageNum)
    
    logicalAddress = "0x5678"
    pageNum, offset = getPagenum(logicalAddress), getOffset(logicalAddress)
    addAddress(pageNum)
    
    logicalAddress = "0x143F"
    pageNum, offset = getPagenum(logicalAddress), getOffset(logicalAddress)
    addAddress(pageNum)
    ###
    
    ### Guide printing
    print("Input 0 to exit\n\n")
    print("Input hexical value to return Page Number, Offset, and Physical Address\n")
    print("Example:")
    print("    Input: 0x143F")
    print("    Output: Page Number = 14, Offset = 3F, Physical Address = 0xAA3F")
    ###

    while True:
        inp = input()
        
        if inp == "0": # Exit
            break
        elif inp[:2] != "0x" or len(inp) != 6: # Invalid input
            print("Invalid input")
            continue
        
        ## Get and display hex address info
        pageNum, offset = getPagenum(inp), getOffset(inp)
        if pageNum not in pageTable:
            print("Page fault")
            addAddress(pageNum)
        physicalAddress = getPhysicalAddress(pageNum, offset)
        
        print("Page Number = " + str(pageNum) + ", Offset = " + str(offset) + ", Physical Address = " + physicalAddress)
        ##
       
    

if __name__ == "__main__":
    main()