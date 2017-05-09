def detectDict(dictItem):
    datatype=[list,tuple,dict]
    for x in dictItem:
        if type(dictItem[x]) in datatype:
            print(x,":")
            open_item(dictItem[x])
            print("--------------;")
        else: print(x,":",dictItem[x])
    
def open_item(itm):
    datatype=[list,tuple,dict]
    datatype2=[str,int,float,bool]
    if type(itm) in datatype2:
        print(itm)

    elif type(itm)==dict:
        detectDict(itm)
    else:
        for item in itm:
            if type(item) in datatype:
                if type(item)==dict:
                    detectDict(item)
                else:
                    open_item(item)
            else:
                print(item)

items=["game","ball",["phone","cat",["here","there",("them","their"),"where"],"mouth"],
       dict(me=dict(wel=100,bel=200,cel=dict(rat=100,bel=dict(rat=100,bel=dict(rat=100,
        bel=dict(rat=100,bel=dict(rat=[1,2,3],bel=200))))),nel=300),we=["wow","waw",dict(aa=100,bb=1000)]),"end"]
open_item(items)

