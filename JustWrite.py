from collections import defaultdict
import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import tkFont
from TextAnalyser import TextAnalyser 

class ButtonObject(Button):
    def __init__(self, master=None):
                ButtonObject.__init__(self, master)

class App(Tk):
    def createWidgets(self):       
                self.add_menus()
    def __init__(self, master=None):
                Tk.__init__(self, master)
                self.createWidgets()
                self.wm_title("Just Write")
                self.iconbitmap(r'/Users/matthias/Downloads/Heminyway Writing Improved/fav.ico')
                self.minsize(width=666,height=666)
                self.tagID = 0
                
#------get screen dimensions      
                w, h = self.winfo_screenwidth(), self.winfo_screenheight()
                rw, rh = self.winfo_width(), self.winfo_height()

#------- Place scrollable text

                self.text = ScrolledText(self, spacing1=1.5 , highlightthickness=0, 
                    width=int(round(rw*0.6)), height=2, padx=rw*0.16, pady=0.1)
                self.text.place(x=100,y=50,width=w/2 -100, height=5*h/6)
                #self.overrideredirect(1)
                self.geometry("%dx%d+%d+0" % (w/2, h, (2*w/8) + rw) ) #set geometry of application window - center in scren

#------- Labels
                self.filledLines = Label(self, text="filledLines: 0")
                #Label(self, text="Word count: ").grid(row=0, column=0)
                self.lineCount = Label(self, text="Line count: 0")
                self.wordCount = Label(self, text="Word count: 0")
                self.charCount = Label(self, text="Total characters: 0")
                #Label(self, text="Word count: ").grid(row=1, column=0)


#------Buttons
                P = Button(self, text="p", command=self.P)
                H1 = Button(self, text="H1", command=self.H1)
                H2 = Button(self, text="H2", command=self.H2)
                H3 = Button(self, text="H3", command=self.H3)
                Bold = Button(self, text="Bold", command=self.Bold)
                Italic = Button(self, text="Italic", command=self.Italic)
                Roman = Button(self, text="Roman", command=self.Roman)
                Underline = Button(self, text="Underline", command=self.Underline)




                fred = Button(self, fg = "red", bg = "blue",text="Set font",width=13, command=self.set_font)
                deleteSelection = Button(self, fg = "red", bg = "blue", text="Delete selection",width=13,command=self.delete_selection)
                nightMode = Button(self, fg = "white", bg = "black", text="Toggle Nightmode",width=13,command=self.onNightMode)
                self.editMode = Button(self, fg = "white", bg = "black", text="Toggle Editmode",width=13,command=self.onEditMode)

#------------- Indexes
                self.nightIndex = TRUE
                self.editIndex = TRUE

                

#------- Place UI elements
                self.top_buttons = [P,H1,H2,H3,Bold,Italic, Roman, Underline]
                self.left_buttons = [nightMode, fred,deleteSelection, self.wordCount, self.lineCount, self.filledLines, self.charCount]
                self.place_buttons_and_text()
               

    
                


                standardFont = tkFont.Font(family="Libre Baskerville",size=17,weight="normal")#slant="false"
                self.option_add("*Font",standardFont)
                self.text.configure(font=standardFont)
                

                self.add_keybindings()
                
                

#--------- Constructor methods

    def add_menus(self):
           self.menuBar = Menu(master=self)
           self.filemenu = Menu(self.menuBar, tearoff=0)
           self.filemenu.add_command(label="Quit!", command=self.quit)
           #self.menuBar.add_cascade(label="File", menu=self.filemenu)
           self.config(menu=self.menuBar)
           self.filemenu = Menu(self.menuBar)
           self.menuBar.add_cascade(label="File", menu=self.filemenu)
           self.filemenu.add_command(label="New", command=self.new_command)
           self.filemenu.add_command(label="Open...", command=self.open_command)
           self.filemenu.add_command(label="Save", command=self.save_command)
           self.filemenu.add_separator()
           self.filemenu.add_command(label="Exit", command=self.exit_command)
           self.helpmenu = Menu(self.menuBar)
           self.menuBar.add_cascade(label="Help", menu=self.helpmenu)
           self.helpmenu.add_command(label="About...", command=self.about_command)


    def add_keybindings(self):
            self.bind("<Configure>", self.on_resize)
            self.text.bind("<Key>", self.any_key)
            #self.text.bind("<Key>", update)
            #self.text.bind("<Enter>", self.turn_red) #enter = maus entered das window
            self.text.bind("<Return>", self.return_key)
            self.text.bind("<Command-A>", self.select_all)
            self.text.bind("<Command-a>", self.select_all)

    def place_buttons_and_text(self):
            #top_y, left_x = 3, self.winfo_reqwidth*4 - 100
            top_y, left_x = 3, self.winfo_width() - 150

            i = 0
            for b in self.top_buttons:
                b.place(x=i,y=top_y)
                i += 65

            self.editMode.place(x=left_x,y=75)

            if (self.editIndex):
                i = 100#self.winfo_reqheight()
                #i = self.winfo_height() * 0.5
                for b in self.left_buttons:
                    b.place(x=left_x,y=i)
                    i += 25
            else:
                i = 100#self.winfo_reqheight()
                #i = self.winfo_height() * 0.5
                for b in self.left_buttons:
                    b.place(x=self.winfo_screenwidth() * 2,y=i)
                    i += 25
            w, h = self.winfo_screenwidth(), self.winfo_screenheight()
            rw, rh = self.winfo_width(), self.winfo_height()
            self.text.place(x=75,y=50,width=rw - 80, height=h - 95)
            #self.text.place()

            
    #def SetTextSize(self, size):

#---------helper methods:
    def is_text_empty(self):
            return FALSE

    




#----------Text formating methods


    def P(self):
            tag = "sel_" + str(self.tagID)
            self.tagID += 1
            self.text.tag_ad(tadg,SEL_FIRST,SEL_LAST)
            self.text.tag_config(tag,font=tkFont.Font(family="Libre Baskerville",size=17,weight="normal"))
            self.text.tag_config(tag,underline=FALSE)
    def H1(self):
            tag = "sel_" + str(self.tagID)
            self.tagID += 1
            self.text.tag_add((tag),SEL_FIRST,SEL_LAST)
            self.text.tag_config((tag),font=tkFont.Font(family="Libre Baskerville",size=27,weight="bold"))

    def H2(self):
            tag = "sel_" + str(self.tagID)
            self.tagID += 1
            self.text.tag_add((tag),SEL_FIRST,SEL_LAST)
            self.text.tag_config(tag,font=tkFont.Font(family="Libre Baskerville",size=24,weight="bold"))
            #self.text.tag_config("sel",font=tkFont.Font(family="Libre Baskerville"))

    def H3(self):
            tag = "sel_" + str(self.tagID)
            self.tagID += 1
            self.text.tag_add((tag),SEL_FIRST,SEL_LAST)
            self.text.tag_config(tag,font=tkFont.Font(family="Libre Baskerville",size=21,weight="bold"))

#TODO if already set to P 

    def Bold(self):
            tag = "sel_" + str(self.tagID)
            self.tagID += 1
            self.text.tag_add(tag,SEL_FIRST,SEL_LAST)
            self.text.tag_config(tag,font=tkFont.Font(family="Libre Baskerville", weight="bold"))

    def Underline(self):
            tag = "sel_" + str(self.tagID)
            self.tagID += 1
            self.text.tag_add(tag,SEL_FIRST,SEL_LAST)
            self.text.tag_config(tag,underline=TRUE)
           

    def set_font(self):
            self.text.tag_add("sel", "1.9", "1.12")

    def Italic(self):
            tag = "sel_" + str(self.tagID)
            self.tagID += 1
            self.text.tag_add(tag,SEL_FIRST,SEL_LAST)
            self.text.tag_config(tag,font=tkFont.Font(family="Libre Baskerville"))

    def Roman(self):
            
            tag = "sel_" + str(self.tagID)
            self.tagID += 1
            self.text.tag_add(tag,SEL_FIRST,SEL_LAST)
            #self.text.tag_config("sel",background="red")
            self.text.tag_config(tag,font=tkFont.Font(family="Libre Baskerville"))           



    def underline_selection(self):
            print self.call(textwidget,"count","1.0","sel.first")

    def print_it(self):
            print "test"

#---------- Info bar methods

    def delete_selection(self): 
            #(self._w, 'tag', 'add', tagName, index1) + args)
            self.text.tag_add("sel_first",SEL_FIRST,SEL_LAST)
            self.text.tag_config("sel_first",background="red")

#----------- Update methods 
    def analyse_text(self):
                self.lineCount.config(text=("Display-lines:"+str(self.text.count("1.0", "end", "displaylines"))))
                self.filledLines.config(text=("Filled Lines:"+str(self.text.count("1.0", "end", "lines"))))
                currText = self.text.get("1.0",END)
                #textAnalyser = TextAnalyser(currText)
                words_last_file = 0
                self.wordCounter = 0
                self.charCounter = 0
                self.words = defaultdict(int)
                self.total_words = 0
                for line in currText:
                    words_in_line = line.split()
                    self.total_words += len(words_in_line)
                    self.wordCounter += 1
                    for word in words_in_line:
                        self.charCounter += 1
                        self.words[word] += 1
                        words_last_file += 1





                self.wordCount.config(text=("spaces:" + str(self.wordCounter - self.charCounter))) 
                self.charCount.config(text=("chars \spaces:" + str(self.charCounter))) 



    def on_resize(self, event):
                #TODO if width < 600 - set left padding to 0
            if (TRUE):
                #self.underline_selection
                newWidth = self.winfo_width()*0.16
                self.text.config(width=int(round(self.winfo_width()*0.6)), height=50,padx=newWidth)
                i = self.winfo_width()*0.2
                for b in self.top_buttons:
                    b.place(x=i,y=3)
                    i += 45

                i = self.winfo_height() * 0.5
                for b in self.left_buttons:
                    b.place(x=self.winfo_width()*0.7,y=i)
                    i += 25
            self.place_buttons_and_text()

    def onNightMode(self):
            if self.nightIndex:
                self.text.config(font=tkFont.Font(family="Libre Baskerville",size=17,weight="normal"), background='black', fg='green')
                self.nightIndex = FALSE
            else:
                self.text.config(font=tkFont.Font(family="Libre Baskerville",size=17,weight="normal"), background='white', fg='black')
                self.nightIndex = TRUE
    def onEditMode(self):
            if (self.editIndex):
                self.editIndex = FALSE
            else: 
                self.editIndex = TRUE
            self.place_buttons_and_text()    



#-----------------Key pressed methods

    def any_key(self, event):
            self.analyse_text()
               

    def return_key(self, event):
            print "enter"

    def select_all(self,event):
            event.widget.tag_add("sel","1.0","end")

  
#--------------File menu and menu methods 


    def open_command(self):
            if (FALSE): #text not empty
                self.new_command()
            file = tkFileDialog.askopenfile(parent=self,mode='rb',title='Select a file')
            if file != None:
                contents = file.read()
                self.text.insert('1.0',contents)
                file.close()

    def save_command(self):
        file = tkFileDialog.asksaveasfile(mode='w')
        if file != None:
        # slice off the last character from get, as an extra return is added
            data = self.text.get('1.0', END+'-1c')
            file.write(data)
            file.close()
        
    def exit_command(self):
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            self.destroy()

    def new_command(self):
        if tkMessageBox.askokcancel("Save", "Do you want to save your file?"):
            self.save_command()
        self.text.delete('1.0', END)

    def about_command(self):
        label = tkMessageBox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")
#------ Start App 
  
myapp = App("Editor")
myapp.focus()
myapp.lift()
#TODO set framerate 
myapp.mainloop()
