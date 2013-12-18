import sublime, sublime_plugin

class DeviceListCommand(sublime_plugin.TextCommand):
    """
    based add_selections.py from 
    https://github.com/Veedrac/Sublime-Extras
    """

    # set it to 1 if you want to see debugging messages in the console 
    MYDEBUG = 0

    def mydebug(self,s):
        if DeviceListCommand.MYDEBUG :
            print(s)

    def run(self, edit):
        self.mydebug("run")
        self._find_all_colons()
        self._filter_lines()
        self._copy_all_selected_lines()
        self._replace_test(edit)

    def _filter_lines(self):
        self.mydebug("_filter_lines")

        selections = self.view.sel()

        old_selection = []
        regions = []

        for region in selections:
            self.mydebug(region)
            old_selection.append(region)
            regions += (self.view.lines(region))


        self.regions = [regions]

        self.mydebug("the list of new regions:")
        self.mydebug(regions)
        self.mydebug(type(regions))
        self.mydebug(type(regions[0]))
        
        self.view.sel().clear()

        for region in regions:
           selections.add(region)


    def _copy_all_selected_lines(self):
        self.mydebug("_copy_all_selected_lines")

        self.lines  = []
        for region in self.view.sel() :
            (device_id, device_name) = self.view.substr(region).split(":")[0:2]
            self.lines.append( {"id": device_id, "name" : device_name })

        self.mydebug(self.lines)

    def _replace_test(self, edit):
        self.mydebug("_replace_test")

        replace_str = ""
        command = "port-cli -E -d "
        
        for elem in self.lines[0:-1] :
            replace_str += elem["id"] + ":" + elem["name"] + "\n"
            command += elem["id"] + ","

        elem = self.lines[-1] #last elem
        replace_str += elem["id"] + ":" + elem["name"]+"\n"
        command += elem["id"]

        region = sublime.Region(0, self.view.size())
        self.view.replace(edit, region, replace_str +"\n" + command)

        self._copy_last_line(command)

    def _copy_last_line(self, s):
        self.mydebug("_copy_last_line")

        sublime.set_clipboard(s)

    def _find_colon(self ):
        self.mydebug("_find_colon")

        req=self.view.find(":",0)
        self.mydebug(req)

        if req :
            selections = self.view.sel()
            selections.clear()
            selections.add(req)
        else:
            mydebug("didn't find colon")

    def _find_all_colons(self):
        self.mydebug("_find_all_colons")

        self._find_colon()
        self.view.window().run_command("find_all_under")
