import wx

insertables = {
    "Square Root": "**(.5)",
    }

class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        self.formulaTextBox = wx.TextCtrl(panel,size=(400,40),pos=(20,20),style=wx.TE_CHARWRAP|wx.TE_MULTILINE)
        self.operatorInfoBox = wx.StaticText(panel,pos=(20,65),label="+ Add, - Subtract, * Multiply, / Divide, ** Power Of, % Remainder")
        self.resultTextBox = wx.TextCtrl(panel,size=(400,100),pos=(20,120),style=wx.TE_READONLY|wx.TE_MULTILINE)

        self.InsertButton = wx.Button(panel,size=(50,25),pos=(20,85),label="Insert")

        self.Bind(wx.EVT_TEXT, self.updateResultTextBox, self.formulaTextBox)
        self.Bind(wx.EVT_BUTTON, self.insertProcess, self.InsertButton)

    def updateResultTextBox(self, event):
        formula = self.formulaTextBox.GetValue()
        formula = formula.replace(" ","")
        if formula == "":
            self.resultTextBox.SetValue("")
        else:
            try:
                result = eval(formula)
                self.resultTextBox.SetValue(str(result))
            except:
                self.resultTextBox.SetValue("Something went wrong")

    def insertProcess(self, event):
        with wx.TextEntryDialog(self, message="Please put an 'x' where you want to insert", caption="Insert Formula") as instdlg:
            formula = self.formulaTextBox.GetValue()
            formula = formula.replace(" ","")
            instdlg.SetValue(formula)
            if instdlg.ShowModal() == wx.ID_OK:
                formulaWithInsertLoc = instdlg.GetValue()
        with wx.SingleChoiceDialog(self, message="Select the formula you want to insert", caption="Insert Formula", choices=list(insertables.keys())) as chcdlg:
            if chcdlg.ShowModal() == wx.ID_OK:
                selection = chcdlg.GetSelection()
                n = -1
                for i in insertables.keys():
                    n = n+1
                    if n == selection:
                        selection = insertables.get(i)
                        break
        self.formulaTextBox.SetValue(formulaWithInsertLoc.replace("x",selection))



app = wx.App()
frame = MainWindow(None, title='Formula Calculator', size=(455,280), pos=(50,50))
frame.Show()
app.MainLoop()
