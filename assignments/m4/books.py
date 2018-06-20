class book:
    def __init__(self,ttl='Harry Potter',auth='J. K. Rowling',pub='Bloomsbury Publishers',pri=250,roy=10):
        self.title=ttl
        self.author=auth
        self.publisher=pub
        self.price=pri
        self.royal=roy

    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_publisher(self):
        return self._publisher
    def get_price(self):
        return self._price
    def get_royalty(self):
        return self._royal

    def set_title(self,a):
        self._title=a
    def set_author(self,a):
        self._author=a
    def set_publisher(self,a):
        self._publisher=a
    def set_price(self,a):
        self._price=a
    def set_royalty(self,a):
        self._royal=a

    title=property(get_title,set_title)
    author=property(get_author,set_author)
    publisher=property(get_publisher,set_publisher)
    price=property(get_price,set_price)
    royal=property(get_royalty,set_royalty)

    def royalty(self):
        return self.price*self.royalty/100

class ebook(book):
    def __init__(self,ttl='Harry Potter',auth='J. K. Rowling',pub='Bloomsbury Publishers',pri=250,roy=10,frmt='PDF'):
        super().__init__(ttl,auth,pub,pri,roy)
        self.eformat=frmt
    
    def get_format(self):
        return self._eformat
    def set_format(self,a):
        self._eformat=a
    eformat=property(get_format,set_format)

    def royalty(self):
        return self.price*12/100

    


