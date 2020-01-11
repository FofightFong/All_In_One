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

![Lighting_setup_geo_sm.gif](http://www.tokeru.com/cgwiki/images/1/17/Lighting_setup_geo_sm.gif)

1.  创建grid

2.  创建一个platonic solid，放置在入场景中，将其模式设置为茶壶，半径为3。

3.  将其向上平移约1.39，以便使其位于grid上

4.  从工具架上创建distant light，旋转和平移使其看起来不错，将其着色为黄色。（提示：单击微型色轮，然后依次点击RGB，HSV和TMI，直到显示TMI。这是一种更好的调色滑块，第一个滑块控制暖冷色温

5.  从工具架上创建环境灯，将其设置为蓝色。

6.  选择一个较好的相机视角，按住Ctrl键并单击工具架上相机的按钮，这将为你复制具有视角属性设置的相机。 


##  Setup a render node, render

摘要：在PBR模式下创建ROP（Render OPerator，即渲染全局节点），在大多数情况下，这是当今首选的渲染器

![Lighting_setup_rop_sm.gif](http://www.tokeru.com/cgwiki/images/7/7f/Lighting_setup_rop_sm.gif)

1.  创建一个rop网络。虽然你可以在更高层“/out”网络中创建节点，但我发现其更容易跟踪子网络中的所有内容，并且跳转变得更加本地化。

2.  进入所创建的rop，创建一个mantra节点。默认设置将指向你创建的相机（/obj/cam1）。

3.  在渲染标签下，将渲染引擎设置为physically based rendering(简称PBR）

4.  在主视图中，切换到渲染视图选项卡。

5.  点击渲染

6.  惊叹于你的阳光茶壶。

##  Material creation

摘要：从调色板创建材材质，进行分配。

如果还没有，请回到/obj网络的顶部。

![Lighting_setup_shop_sm.gif](http://www.tokeru.com/cgwiki/images/7/70/Lighting_setup_shop_sm.gif)

1.  创建一个shop网络

2.  在右下角的选项卡中找到Material Palatte选项卡。

3.  在material palette的右侧，单击/shop/标题旁边的上下箭头以将其折叠。现在你应该看到关闭了。

4.  单击/obj/shopnet1旁边的三角形以将其打开（这是你刚创建的shopnet）

5.  在左侧，找到Generic下的Principled shader节点（由于houdini版本的迭代，这里有所不同，你也可以选择其它houdini内置的材质进行测试）。

6.  将其拖到/obj/shopnet1标题下。短暂的延迟后，你将看到一个名为principledsh..的着色器正方形

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


