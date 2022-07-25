#importing libraries
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
import mysql.connector

 
 
class Super_Data(MDScreen):
    '''def __init__(self, **kwargs):
        super().__init__(**kwargs)pp

        self.mydb = mysql.connector.connect(
                    host = "localhost", 
                    user = "root",
                    passwd = "LAVEnder#12",
                    database = "solver",
                    )
        c = self.mydb.cursor()

      #  c.execute('INSERT INTO orders(id,Order_Code,Order_Type,Machine,Raised_by,Priority,status,Work_Centre,Assigned_to,Date_Raised,Expected_Comp,Date_Comp) VALUES')
        '''
    pass
        




class Welcome_Page(MDScreen):
    pass

    
class Login_Page(MDScreen):

    pass

class Main_Page(MDScreen):
    pass 

class Selection_Of_Orders(MDScreen):

    pass

class Window_Manager(ScreenManager):
    pass

class Preventive(MDScreen):
    pass

class Corrective(MDScreen):
    pass

class Breakdown(MDScreen):
    pass

class Supervisor(MDScreen):
    pass

class Level_Selection(MDScreen):
    pass

class List_Of_Orders(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mydb = mysql.connector.connect(
                host = "localhost", 
                user = "root",
                passwd = "",
                database = "solver",
                )
        c = self.mydb.cursor()
        c.execute('Select * from orders')
        records = c.fetchall()
        r = records[0]
         
        pswd = '894'
        name = 'Panashe'

       


#connecting database

        self.mydb = mysql.connector.connect(
                host = "localhost", 
                user = "root",
                passwd = "",
                database = "solver",
                )
        c = self.mydb.cursor()
        c.execute('Select * from orders')
        records = c.fetchall()

        word = ''
        m = []
        r = records[0]

        for i in r[0:]:
            m.append(i)
   
        m = tuple(m)
                

        #print(len(m))
        #m = ('Lathe','1','Power Machine','234','Material Removal','afan;in')
        Row_data=[]
        for i in range(10):
            Row_data.append(m)
        
        toolbar = Label(text='List Of Orders',size_hint =(1,.2))
# generating the table widget

        table = MDDataTable(
            size_hint =(1,.8),
            pos_hint = {'center_x':.5,'center_y':.5},
            check = True,
            column_data = [
                ('ordercode',dp(30)),
                ('Order_Type',dp(30)),
                ('Machine',dp(30)),
                ('Raised_by',dp(30)),
                ('Priority',dp(30)),
                ('status',dp(30)),
                ('Work_Centre',dp(30)),
                ('Assigned_to',dp(30)),
                ('Date_Raised',dp(30)),
                ('Expected_Comp',dp(30)),
                ('Date_Comp',dp(30)),
            ],

            row_data = Row_data

        )
        gridLayout=GridLayout(rows=2,cols=1)
        gridLayout.add_widget(toolbar)
        gridLayout.add_widget(table)
        self.add_widget(gridLayout)
        #self.add_widget(table)

# initialising the the app
class SolverApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'    
        kv = Builder.load_file("solverapp.kv")

        mydb = mysql.connector.connect(
                host = "localhost", 
                user = "root",
                passwd = "",
                database = "solver",
                )

    dialog = None
    def show_about_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text='What solver is about ',
                buttons=[
                    MDFlatButton(
                        text= 'Cancel', text_color = self.theme_cls.primary_color, on_release = self.close_dialog
                        ),
                   
                ],

            )

        self.dialog.open()

    def close_dialog(self,obj):

        self.dialog.dismiss()

    def inventory_check(self):
        self.mydb = mysql.connector.connect(
                host = "localhost", 
                user = "root",
                passwd = "",
                database = "solver",
                )
        c = self.mydb.cursor()
        c.execute('Select * from orders')
        records = c.fetchall() 
        if len(records) < 20:
            if not self.dialog:
                self.dialog = MDDialog(
                    text='What solver is about ',
                    buttons=[
                        MDFlatButton(
                            text= 'Cancel', text_color = self.theme_cls.primary_color, on_release = self.close_dialog
                            ),
                    
                    ],

                )
            self.dialog.open()
        
        

    


SolverApp().run()