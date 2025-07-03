# Created by PAGE version 7.6
# https://page.sourceforge.io
set ::_appname "IO Mentor Bot GUI"
set ::_appclass "IOMentor"

package require Tk
package require ttk

set mainWin [ttk::frame .mainframe -padding "10 10 10 10"]
pack $mainWin -fill both -expand true

label $mainWin.lblInput -text "Input:"
entry $mainWin.entryInput -width 50
button $mainWin.btnSend -text "Send"
label $mainWin.lblOutput -text "Output:"
text $mainWin.textOutput -width 50 -height 10

grid $mainWin.lblInput  -row 0 -column 0 -sticky w
grid $mainWin.entryInput -row 1 -column 0 -sticky ew
grid $mainWin.btnSend   -row 2 -column 0 -pady 10
grid $mainWin.lblOutput -row 3 -column 0 -sticky w
grid $mainWin.textOutput -row 4 -column 0 -sticky ew

grid columnconfigure $mainWin 0 -weight 1
grid rowconfigure $mainWin 4 -weight 1
