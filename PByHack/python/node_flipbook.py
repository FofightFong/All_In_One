#node.setDisplayFlag(True)
import os




def findNodeTree(start,end="",nodeTree=dict()):
    if start.outputs() == ():
        nodeTree[start.name()] = []
    else:
        nodeTree[start.name()] = [node.name() for node in start.outputs()]
        for node in start.outputs():
            if node.name() == end:
                nodeTree[node] = []
            else:
                findNodeTree(node)
    return nodeTree
    
# 找到所有从start到end的路径   
def findAllPath(nodeTree,start,end,path=[]):
    path = path+[start]
    if start == end:
        return [path]
        
        
    paths = []#存储所有路径 
    for nodes in nodeTree[start]:
        if nodes not in path:
            newpaths = findAllPath(nodeTree,nodes,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
    
# 查找最短路径
def findShortestPath(nodeTree,start,end,path=[]):
    path = path+[start]
    if start == end :
        return path   
    shortestPath = []
    for nodes in nodeTree[start]:
        if nodes not in path:
            newpath = findShortestPath(nodeTree,nodes,end,path)
            if newpath:
                if not shortestPath or len(newpath)<len(shortestPath):
                    shortestPath =newpath
    return shortestPath



def main(nodelist,startNodePath):
    cameras = [c for c in hou.node('/').allSubChildren() if c.type().name() == 'cam']

    if not cameras:
        hou.ui.displayMessage('No cameras to flipbook from', title='No Cameras', severity=hou.severityType.Error)
        return

    selected = [cameras[i] for i in hou.ui.selectFromList([c.name() for c in cameras], message='Select the camera(s) to flipbook from', title='Camera Selection', column_header='Cameras')]

    if not selected:
        return

    outputBase = hou.ui.selectFile(title='Save Sequence(s) as...', collapse_sequences=True, file_type=hou.fileType.Image, chooser_mode=hou.fileChooserMode.Write)

    if not outputBase:
        return

    if '$F' not in outputBase:
        hou.ui.displayMessage('Invalid output path specified (Make sure to use $F, $F4, etc. notation)', severity=hou.severityType.Error)
        return

    splitBase = os.path.split(outputBase)
    sceneViewer = hou.ui.curDesktop().paneTabOfType(hou.paneTabType.SceneViewer)

    frameStart = int(sceneViewer.flipbookSettings().frameRange()[0])
    frameEnd = int(sceneViewer.flipbookSettings().frameRange()[1])
    frameInc = sceneViewer.flipbookSettings().frameIncrement()

    frameInput = hou.ui.readMultiInput('Select frame range for flipbook(s)', ['Start', 'End', 'Inc'], initial_contents=[str(frameStart), str(frameEnd), str(frameInc)])

    frameStart = int(frameInput[1][0])
    frameEnd = int(frameInput[1][1])
    frameInc = int(frameInput[1][2])

    if not sceneViewer:
        hou.ui.displayMessage('Could not find Scene Viewer pane tab, please create it and try again', severity=hou.severityType.Error)
        raise SystemExit

    viewport = [vp for vp in sceneViewer.viewports() if vp.type() == hou.geometryViewportType.Perspective][0]

    if not viewport:
        hou.ui.displayMessage('Could not find the "Persp" viewport', severity=hou.severityType.Error)
        raise SystemExit

    viewportFullName = '{}.{}.world.{}'.format(hou.ui.curDesktop().name(), sceneViewer.name(), viewport.name())
    cameraOutputs = []

    for camera in selected:
        cameraOutputs.append((camera, os.path.join(splitBase[0], '{}_{}'.format(camera.name(), splitBase[1]))))

    for f in range(frameStart, frameEnd + 1, frameInc):
        unit = (frameEnd-frameStart)//len(nodelist)
        for camera, output in cameraOutputs:
            
            hou.setFrame(f)
            viewport.setCamera(camera)
            hou.node(os.path.split(startNodePath)[0]+ "/" + nodelist[f//unit]).setDisplayFlag(True)

            hou.hscript("viewwrite -f {} {} {} '{}'".format(f, f, viewportFullName, output))

startNodePath = hou.ui.selectNode(title="Start Node")
startNode = hou.node(startNodePath)
startNodeName = hou.node(startNodePath).name()
endNodePath = hou.ui.selectNode(title="End Node")
endNodeName = hou.node(endNodePath).name()
nodeTree = findNodeTree(startNode)
nodelist = findShortestPath(nodeTree,start=startNodeName,end=endNodeName)
main(nodelist,startNodePath)
