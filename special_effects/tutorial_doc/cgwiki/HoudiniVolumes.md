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



<a href="Houdini_Lighting_Shading.md">
  <img src="https://github.com/BlenderCN/blenderTutorial/blob/master/mDrivEngine/blenderpng/logoleft.png" align="left">
</a>
<a href="HoudiniVex.md">
  <img src="https://github.com/BlenderCN/blenderTutorial/blob/master/mDrivEngine/blenderpng/logoright.png" align="right">
</a>

