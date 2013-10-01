sublime
=======

Some of my code that i run to make my live and work easier when working with sublime editor.

Instalation instruction can be found below with the descrption as well. For more info you can refere to this blog entries as well:

[sublime-macro-error.html ] (http://rtomaszewski.blogspot.co.uk/2013/10/sublime-macro-error.html)


## Example instalation for the device_list.py file.

### Option 1

From the Tools menu select New Plugin. Replace the exmaple code with a code from one of the files (for exmaple from device_list.py)

#### Option 2 (full instalation)

Copy file(s) to your Sublime instalation directory: ...\Data\Packages\User\.
You may need to restart sublime for the file to be recoginised and loaded.
If the files are installed properly you should see similar line(s) in the console when subline finished loading:

```
Reloading plugin C:\Users\...\sublime2\Data\Packages\User\<file_name>
```

## Testing

To use the extension you can either :

- open console and type this comamnd

```
view.run_command("device_list")
```

- or create a keyborad shortcat to execute it

## Example for device_list.py

### Create new file with following content 

```
402927: fw.tg-server.net
fw
Firewall - Cisco ASA
Online/Complete
Kubik (LON3)
111.1.1.1
 
402928: lb.tg-server.net
lb
Load-Balancer
Online/Complete
Kubik (LON3)
2.2.2.2.
```
 
### When you run the extension it replacese the text with the following one

```
402927: fw.tg-server.net
402928: lb.tg-server.net

port-cli -E 402927,402928
```
 
## Debuging:

Set the the MYDEBUG to 1. You can see the various log messages in the console.

## References

(http://www.sublimetext.com/docs/2/api_reference.html)
(http://www.sublimetext.com/forum/)



