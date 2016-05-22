import readURL
import DataStore
import DataYahoo

strYahooURL = "http://table.finance.yahoo.com/table.csv?s="
def makeRequestMsg(code):
	return strYahooURL + code

def generateCodeList():
    listCode = []
    listCode.append('000001.sz')
    return listCode

if __name__ == "__main__":
    print 'DataStore'
    DataStore dataStore
    
    print 'generateCodeList'
	listCode = generateCodeList()
    for code in listCode:
        URL = makeRequestMsg(code)
        print 'request msg: ', URL
        
        print 'read URL'
        html = getHtml(URL)
        
        DataYahoo dataYahoo(html)
        dataStore.addYahooData(dataYahoo)
        
      
        
    
    
	

