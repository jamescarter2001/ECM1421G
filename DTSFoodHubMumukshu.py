
from tkinter import *
from tkinter.ttk import Treeview
import pandas as pd
import pyodbc
        

class Initializer(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self._frame = None
        self.title('Nypmton Food Hub')
        
        ##window width and height
        app_width = 900
        app_height = 600
        ##this places the GUI window in the center of the displau
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)

        self.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.resizable(False,False)
        
        self.switch_frame(Login,data=None)

    def switch_frame(self, frame_class,data):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self,data)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    
    def exitApp(self): 
        self.destroy()

class Login(Frame):##JOSH 
    def __init__(self, master,data):
        Frame.__init__(self, master)
        Label(self, text="This is the LOGIN").pack(side="top", fill="x", pady=10)
        Button(self, text="Open CUSTOMER LIST",
                  command=lambda: master.switch_frame(CustomerList,data=None)).pack()
        # Button(self, text="Open ADD CUSTOMER",
        #           command=lambda: master.switch_frame(AddCustomer)).pack()
        # Button(self, text="Open CUSTOMER ORDER",
        #           command=lambda: master.switch_frame(CustomerOrder,data=None)).pack()
        # Button(self, text="Open ORDER DETAILS",
        #           command=lambda: master.switch_frame(OrderDetails)).pack()
        Button(self, text="Cancel/Exit",command=master.exitApp).pack()
        

class CustomerList(Frame):#TYLER
    def __init__(self, master,data):
        Frame.__init__(self, master)
        Label(self, text="Customer List").pack(side="top", fill="x", pady=10)
        
        
        self.details=[3,'Lareina','Swanson','EX43 0BA','012546325412','07856985698']
        
        Button(self, text="Orders",command=lambda: master.switch_frame(CustomerOrder,self.details)).pack()
    
    
        
    

# class AddCustomer(Frame):#MARK
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         Label(self, text="Add Customer").pack(side="top", fill="x", pady=10)
#         Button(self, text="Return to LOGIN",
#                   command=lambda: master.switch_frame(Login)).pack()


class CustomerOrder(Frame):#MUMUKSHU
    def __init__(self, master,data):
        Frame.__init__(self, master)
        details = data
    
        TitleBar = Frame(self)

        Label(TitleBar,text='Customer Order',bg='#bccbe3',width=100,height=4,font=('ariel',20),justify=LEFT).pack(fill='x',expand=FALSE)
        
        TitleBar.pack(side=TOP,pady=(0,12),fill='x')
       
        widthofdetailsbox = 10
        padxbetweenboxcols = 5

        Cols = Frame(self)

        CustomerDetailsHeaders = Frame(Cols)

        id = Label(CustomerDetailsHeaders,text='ID',borderwidth=1,relief='solid',padx=6,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        firstName = Label(CustomerDetailsHeaders,text='First Name',borderwidth=1,relief='solid',padx=padxbetweenboxcols,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        lastName = Label(CustomerDetailsHeaders,text='Last Name',borderwidth=1,relief='solid',padx=padxbetweenboxcols,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        postcode = Label(CustomerDetailsHeaders,text='Post Code',borderwidth=1,relief='solid',padx=padxbetweenboxcols,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        landline = Label(CustomerDetailsHeaders,text='LandLine',borderwidth=1,relief='solid',padx=padxbetweenboxcols,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        mobile = Label(CustomerDetailsHeaders,text='Mobile',borderwidth=1,relief='solid',padx=padxbetweenboxcols,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        
        CustomerDetailsHeaders.pack(side=TOP)

        CustomerDetailsValues = Frame(Cols)
        
        
        id_value = Label(CustomerDetailsValues,text=str(details[0]),borderwidth=1,relief='solid',padx=6,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        firstName_value = Label(CustomerDetailsValues,text=details[1],borderwidth=1,relief='solid',padx=padxbetweenboxcols,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        lastName_value = Label(CustomerDetailsValues,text=details[2],borderwidth=1,relief='solid',padx=padxbetweenboxcols,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        postcode_value = Label(CustomerDetailsValues,text=details[3],borderwidth=1,relief='solid',padx=padxbetweenboxcols,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        landline_value = Label(CustomerDetailsValues,text=details[4],borderwidth=1,relief='solid',padx=padxbetweenboxcols,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        mobile_value = Label(CustomerDetailsValues,text=details[5],borderwidth=1,relief='solid',padx=padxbetweenboxcols,pady=4,width=widthofdetailsbox).pack(side=LEFT,padx=20)
        
        CustomerDetailsValues.pack(side=TOP)

        Cols.pack(side=TOP)
        
        DetailsAndCancelButtons = Frame(self)

        self.detailsbutton = Button(DetailsAndCancelButtons,text='Details',padx=4,pady=4,state=DISABLED,command=lambda: master.switch_frame(OrderDetails,data=None))
        self.detailsbutton.pack(side=TOP)
        butt = Button(DetailsAndCancelButtons,text='Cancel',padx=4,pady=4,command=lambda: master.switch_frame(Login,data=None))
        butt.pack(side=TOP,pady=(15,0))
        
        DetailsAndCancelButtons.pack(side=RIGHT,padx=15)
        
        TableView = Frame(self)
        columns = ('id', 'customer_id', 'order_date','goods','total')
        scrollbar = Scrollbar(TableView, orient=VERTICAL,)
        self.tree = Treeview(TableView, columns=columns, show='headings',height=25,yscrollcommand=scrollbar.set)
       
        self.tree.heading('id', text='ID')
        self.tree.heading('customer_id', text='Customer ID')
        self.tree.heading('order_date', text='Order Date')
        self.tree.heading('goods', text='£ Goods')
        self.tree.heading('total', text='£ Total')

        self.tree.column('id', width=75)
        self.tree.column('customer_id', width=150)
        self.tree.column('order_date', width=150)
        self.tree.column('goods', width=150)
        self.tree.column('total', width=150)
        
        dataframe=self.getDataFromDB(details[0])
        for index in dataframe.index:
            self.tree.insert(parent='', index=index, iid=index, text='', values=(dataframe['id'][index],dataframe['customerid'][index],dataframe['orderdate'][index],dataframe['goodscost'][index],dataframe['totalcost'][index]))
        
        self.tree.bind('<<TreeviewSelect>>',lambda event, arg=master: self.makeDetailButtonNormalandGetSelectedData(event, arg))
        self.tree.pack(side=LEFT)
        
        scrollbar.pack(side=RIGHT,fill=Y)
        scrollbar.config(command=self.tree.yview)
        TableView.pack(side=BOTTOM,padx=15,pady=15)
    
    def getDataFromDB(self,id):
        conn = pyodbc.connect(r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=NymptonFoodHub;Trusted_Connection=yes;')
        df = pd.read_sql(f'SELECT [id],[customerid],[orderdate],[goodscost],[totalcost] FROM [NymptonFoodHub].[dbo].[SalesOrder] WHERE customerid = {id}',conn)  
        conn.close()
        return df
    
    def getSelectedRecord(self):
        item = self.tree.focus()
        return self.tree.item(item)['values']

    def makeDetailButtonNormalandGetSelectedData(self,event,master):
        data = self.getSelectedRecord()
        self.detailsbutton['state'] = NORMAL
        self.detailsbutton.configure(command=lambda: master.switch_frame(OrderDetails,data=data))
   
        
class OrderDetails(Frame):#JACK
    def __init__(self, master,data):
        Frame.__init__(self, master)
        Label(self, text="Order Details").pack(side="top", fill="x", pady=10)
        print('orderdetails data: ',data)
        Button(self, text="Return to LOGIN",
                  command=lambda: master.switch_frame(Login,data=None)).pack()

if __name__ == "__main__":
    app = Initializer()#runs the app 
    app.mainloop()