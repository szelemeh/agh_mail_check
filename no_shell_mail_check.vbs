Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c agh_email_check.bat"
oShell.Run strArgs, 0, false