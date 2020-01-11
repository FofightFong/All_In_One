# Houdini Lighting shading

可能还有其他快速的mantra灯光材质渲染概述，但是我找不到，至少在我需要的5分钟或更短的类别中找不到。这是我通常对任何新渲染器执行的kick-the-tyres过程，认为其他好奇的灯光师和材质师会发现它很有趣。


* 1. [Build a simple test scene](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#build-a-simple-test-scene)

* 2. [Setup a render node, render](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#setup-a-render-node-render)

* 3. [Material creation](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#material-creation)

* 4. [Things to note](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#things-to-note)

* 5. [Material attribute overrides](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#material-attribute-overrides)

     * 1. [Override at object level](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#override-at-object-level)
        
     * 2. [Override at point level](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#override-at-point-level)
        
* 6. [Assign materials to faces](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#assign-materials-to-faces)

* 7. [Point Colour (Cd) and Alpha](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#aovs-or-extra-image-planes)

* 8. [AOVs or Extra Image Planes](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#aovs-or-extra-image-planes)

    * 1. [Defining AOVs in a shader](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#defining-aovs-in-a-shader)

    * 2. [Add AOVs to Rop](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#add-aovs-to-rop)

* 9. [Houdini rendering setup from a maya perspective](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#houdini-rendering-setup-from-a-maya-perspective)

* 10. [Renderstate vop](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#renderstate-vop)

* 11. [Material wrangle via snippet](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#material-wrangle-via-snippet)

* 12. [Todo](https://github.com/FofightFong/All_In_One/blob/master/special_effects/tutorial_doc/cgwiki/Houdini_Lighting_Shading.md#todo)

## Build a simple test scene

摘要：茶壶放在地板上，有阳光，天空，相机

这些快速入门都假定你使用“Build”界面（Windows>Desktop>Build),并且熟悉选项卡菜单和基本的houdini导航。

![](http://www.tokeru.com/cgwiki/index.php?title=File:Lighting_setup_geo_sm.gif)

1.  创建grid

2.  创建一个platonic solid，放置在入场景中，将其模式设置为茶壶，半径为3。

3.  将其向上平移约1.39，以便使其位于grid上

4.  从工具架上创建distant light，旋转和平移使其看起来不错，将其着色为黄色。（提示：



##  Setup a render node, render

##  Material creation

##  Things to note

##  Material attribute overrides

##  Override at object level

##  Override at point level

##  Assign materials to faces

##  Point Colour (Cd) and Alpha

##  AOVs or Extra Image Planes

### Defining AOVs in a shader

### Add AOVs to Rop

##  Houdini rendering setup from a maya perspective

##  Renderstate vop

##  Material wrangle via snippet

##  Todo


