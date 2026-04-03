class LibraryBook:
    def init (self , title : str , author: str):
        self.title = title
        self.author =author
        self.is_checkedout =False
        self.borrower =""
        self.renewcount=0
    def get_author(self):
        return self.author
    def get_title(self):
        return self.title
    def get_borrower(self):
        if self.is_checkedout==False:
            return "None"
        else: 
            return self.borrower
    def get_renew_count(self):
        return self.renewcount
    def check_out(self, borrower_name: str ):
        self.is_checkedout =True
        self.borrower = borrower_name
        pass
    def renew( self ) :
        self.renewcount+=1
        pass
    def return_book(self):
        self.is_checkedout=False
        pass
    def get_status( self ):
        return self.is_checkedout
