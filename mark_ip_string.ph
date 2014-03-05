
import sublime, sublime_plugin
import time

class MarkIpStringCommand(sublime_plugin.TextCommand):

    MYDEBUG = 1
 
    def mydebug(self,s):
        if MarkIpStringCommand.MYDEBUG :
            #t=str(time.time())
            print(s)

    def run(self, edit):
        self.mydebug("run")

        myview= self.view
        context = self.view.window()

        current_position=myview.sel()[0].begin()
        self.mydebug("current_position")
        self.mydebug(current_position)

        # at the current line move the cursor to the beginning of the line 
        context.run_command("move_to", {"extend": False, "to": "bol"} )

        # get the position number
        start=myview.sel()[0].begin()
        self.mydebug("start")
        self.mydebug(start)

        # from this position search for the first string matching IP addr
        reg=myview.find("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",start)
        self.mydebug("reg")
        self.mydebug(reg)

        # select it
        if reg :
            selections = self.view.sel()
            selections.clear()
            selections.add(reg)

            context.run_command("find_all_under")
            context.run_command("toggle_bookmark")
            context.run_command("single_selection")
        
        # move cursor to its original position
        myview.sel().clear()
        myview.sel().add(current_position)

