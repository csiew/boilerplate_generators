import wx
from wx.core import DefaultValidator


class App(wx.Frame):
  def __init__(self, parent, id):
    wx.Frame.__init__(self, parent, id, 'Marble', size=(800, 600))
    self.create_menubar()
    self.create_main_window_panel()
  
  def create_menubar(self):
    status = self.CreateStatusBar()
    menubar = wx.MenuBar()
    menubar_file = wx.Menu()
    menubar_view = wx.Menu()

    menubar_file_items = {
      'newWindow': wx.MenuItem(menubar_file, wx.ID_NEW, "New Window", "Open a new window"),
      'newPopupOK': wx.MenuItem(menubar_file, wx.ID_NEW, "Give me an OK popup", "Opens a popup dialog box"),
      'newPopupYESNO': wx.MenuItem(menubar_file, wx.ID_NEW, "Give me a YES-NO popup", "Opens a popup dialog box")
    }
    self.Bind(wx.EVT_MENU, self.popup_dialog_ok, menubar_file_items['newPopupOK'])
    self.Bind(wx.EVT_MENU, self.popup_dialog_yes_no, menubar_file_items['newPopupYESNO'])
    for item in menubar_file_items.values():
      menubar_file.Append(item)
    menubar.Append(menubar_file, "File")
    menubar.Append(menubar_view, "View")
    self.SetMenuBar(menubar)
  
  def create_main_window_panel(self):
    panel = wx.Panel(self)

    button = wx.Button(panel, label="Exit", pos=(8, -8), size=(60, 60))
    self.Bind(wx.EVT_BUTTON, self.close_btn, button)
    self.Bind(wx.EVT_CLOSE, self.close_win)

    framework_menu = wx.ListBox(self, wx.ID_NEW, pos=(8, 64), size=(300, 300), choices=['Express', 'React', 'Vue'], style=wx.LIST_ALIGN_DEFAULT, validator=DefaultValidator, name="FrameworkMenu")
  
  def popup_dialog_ok(self, event):
    ok_box = wx.MessageDialog(self, "Hello world", "Popup", wx.OK)
    answer = ok_box.ShowModal()
    print(answer)
    ok_box.Destroy()
  
  def popup_dialog_yes_no(self, event):
    yes_no_box = wx.MessageDialog(self, "Hello world", "Popup", wx.YES_NO)
    answer = yes_no_box.ShowModal()
    print(answer)
    yes_no_box.Destroy()
  
  def close_btn(self, event):
    self.Close(True)

  def close_win(self, event):
    self.Destroy()


if __name__ == '__main__':
  app = wx.App()
  frame = App(parent=None, id=-1)
  frame.Show()
  app.MainLoop()
