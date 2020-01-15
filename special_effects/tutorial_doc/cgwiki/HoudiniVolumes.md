# HoudiniVolumes

## Contents

* 1 [Volumes are primitives]()

  * 1.1 [VDB?]()

  * 1.2 [VDB interactive tutorial]()

  * 1.3[ VDB vs Houdini volumes]()

  * 1.4 [Scalar and vector volumes]()

  * 1.5 [SDF]()

  * 1.6 [Viewing volume data]()
  
* 2 [Volumes, SDFs, Trails]()

* 3 [Volume magnetic lines]()

* 4 [Swirly lines, or worms with volumes and curl noise]()

* 5 [Convert geometry to velocity volumes efficiently]()

* 6 [Volume displacement]()

* 7 [Volume deform]()

* 8 [VDB combine]()

* 9 [Cloud light]()

* 10 [Further learning]()

## Volumes are primitives

一开始我有点困惑，所以值得一提。volume是primitive，就像point是primitive或p网格不同，没有r，与多边形imitive sphere是primitive一样。这意味着，例如，与polygon mesh不同，没有深入到其子组件的操作。你无法打开任何geometry spreadsheet以查看各个体素的值。

还有其他工具可以帮助你查看体积中发生了什么（volume slice sop,volume visualisation sop,volume trails sop等），但最终，如果将400×400×400体素volume与primitive sphere进行merge，则如果检查merge，将显示你有两个primitives，一个volume和一个sphere。

houdini支持2种volume类型，其自己的volume格式和VDB。这些被视为诸如polys或nurbs之类的primitives，如果你在节点上按住中键不放，则会看到它说1VDB或1volume或类似内容。

### VDB？

对于volumes，最简单的描述方式是Alembic。这是一种开源的标准格式，因此你可以从houdini中导出VDB，将其加载到maya中，然后在vray中进行渲染。它有多家公司来推动它的发展（Dreamworks，Double Negative，SideFx最引人注目），通常是一件好事。

但是它比Alembic更重要，因为Alembic主要是一种文件格式，并且是一些用于操纵和查看Alembic文件的示例工具。VDB工具箱既是存储volume的一种方式，又是一套用于处理volume算法。

VDB最有趣的特性之一是它不会浪费空像素上的存储空间。与其他格式相比，磁盘上的VDB可以小得多。

VDB存储格式在Houdini中作为primitive（足够有趣的是VDB primitive）公开，而操纵工具则作为sops公开，大多数带有VDB前缀或后缀。

原始论文中提到的VDB名称来自...Volumetric,Dynamic grid that shares several characteristics with B+ trees.

进一步阅读[http://www.openvdb.org/about/](http://www.openvdb.org/about/)

### VDB interactive tutorial

也可以从openvdb网站上获得VDB功能的精彩介绍。这是一个单一的houdini文件，就像VDB上的一本互动书;它分成几章，有很多便笺，我很惊讶我最近才发现它。非常感谢odforce上的人指出这一点！

如果你想和老板一样使用VDB，请立即下载。

[http://www.openvdb.org/download/](http://www.openvdb.org/download/)

[https://nexus.aswf.io/content/repositories/releases/io/aswf/openvdb/houdini_examples.hip/1.0.0/houdini_examples.hip-1.0.0.zip](https://nexus.aswf.io/content/repositories/releases/io/aswf/openvdb/houdini_examples.hip/1.0.0/houdini_examples.hip-1.0.0.zip)

### VDB vs Houdini volumes

houdini自己的volume格式在VDB到来之前已经存在了一段时间，因此那里有大量的节点可以使用它们（你可以通过选项卡菜单中键入volume在sops中看到它）。VDB拥有自己的节点集合（以VDB为前缀或后缀）。

VDB可以比houdini本地volume小得多（通常可节省50%），而且VDB sops通常比houdini本地volume更快，并且具有更有趣的功能。

有一种.vdb文件格式（可用于导出到其他应用程序），但你无需导出.vdb文件即可节省空间，只需在houdini中使用vdb primitive就足够了。可以随时将houdini volume primitive转换为vdb primitive，只需要创建convertvdb节点，并将其模式设置为VDB。如果在节点上单击鼠标中键，将看到Volume primitive已被VDB替换。现在，你可以像其他任何houdini geo一样将其缓存到.bgeo,但比不进行转换的情况要小得多。

令人高兴的是，许多houdini volume工具也已更新，可以与VDB primitive一起使用。例如，Volume VOPS和Volume Wrangles都可以与VDB一起使用。这意味着在任何时候使用VDB都相当安全，因为你可以根据需要轻松地将VDB临时转换为本地volume，然后再次转换。

进一步阅读[http://www.sidefx.com/docs/houdini15.0/model/volumes](http://www.sidefx.com/docs/houdini15.0/model/volumes)

### Scalar and vector volumes

例如，用于表示云的volume仅需要为每个体素密度存储一个值。如果密度为0,则体素是完全透明的;如果密度为1,则体素是不透明的。例如，cloud sop使用引擎盖下的噪音功能将密度雕刻成令人愉悦的云形。

如果要存储在整个云中变化的颜色，则需要存储红色/绿色/蓝色分量。这意味着你需要一个向量volume（或向量字段，你会发现文档和论坛经常将volume称为字段）来存储此信息。

向量场的更常见用途是速度。houdini中的一个约定是将速度体积命名为vel。体积中的每个体素都存储一个方向。pyro solver将使用该速度场在周围传递密度，从而给人以运动感。pyro sims的其他属性是修改速度场本身，因此你可能会得到向上滚动的蘑菇云，或使密度回旋的噪声。





<a href="Houdini_Lighting_Shading.md">
  <img src="https://github.com/BlenderCN/blenderTutorial/blob/master/mDrivEngine/blenderpng/logoleft.png" align="left">
</a>
<a href="HoudiniVex.md">
  <img src="https://github.com/BlenderCN/blenderTutorial/blob/master/mDrivEngine/blenderpng/logoright.png" align="right">
</a>

