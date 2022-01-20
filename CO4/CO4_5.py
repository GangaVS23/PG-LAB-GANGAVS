class publisher:
    def __init__ (self,pn):
        self.publishername=pn
       
    def publisherdisplay(self):
        print(self.publishername)
       
class book(publisher):
    def __init__ (self,pn,tt,aut):
        super(). __init__(pn)
        self.title=tt
        self.author=aut
   
    def bookdisplay(self):
        print(self.title)
        print(self.author)
       
class python(book):
    def __init__ (self,pn,tt,aut,pr,pg):
        super(). __init__(pn,tt,aut)
        self.price=pr
        self.page=pg
   
    def pythondisplay(self):
        print("Publisher Name: ",self.publishername)
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Price: ",self.price)
        print("No. of Pages: ",self.page)
       
       
obj=python("Akshaya publishers","Python","Guido van Rossum",236,215);
obj.pythondisplay();