# comments

strYahooURL = "http://table.finance.yahoo.com/table.csv?s="
def makeRequestMsg(code):
	return strYahooURL + code

def generateCodeList():
    listCode = []
    listCode.append('000001.sz')
    return listCode

if __name__ == "__main__":
    print 'generateCodeList'
	
	

