import os
import hou
import objecttoolutils

hdas = "/root/houdini17.5/houdini_linux_addon/learnbgame/poqbdb_hda"

def findAllFile(hdas):
    for root, ds, fs in os.walk(hdas):
        for f in fs:
            fullname = os.path.join(root, f).split(hdas)[1].split(".")[0]
            yield fullname
            
selected = hou.ui.selectFromTree(list(findAllFile(hdas)))

hou.hda.installFile(hdas+selected[0]+".hda")


nodename = hou.hda.definitionsInFile(hdas+selected[0]+".hda")[0].nodeType().name()



node = objecttoolutils.customStateTool(kwargs,nodename)


#hou.node("obj/"+nodename).allowEditingOfContents()

#hou.hda.uninstallFile(hdas+selected[0]+".hda")

