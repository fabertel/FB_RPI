import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("^a") # CTRL+A may "select all" depending on which window's focused
shell.SendKeys("{F1}") # Delete selected text?  Depends on context. :P
#shell.SendKeys("{TAB}") #Press tab... to change focus or whatever