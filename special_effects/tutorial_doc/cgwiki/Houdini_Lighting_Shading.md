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

7.  返回到network选项卡，进入shop网络，其中包含你刚制作的材料。

8.  将Principled 材质节点直接拖动到茶壶上（可以在opengl视图或渲染视图中执行此操作）。这将分配材质。

分配材质的另一种方法是直接从对象节点进行分配：

1.  返回到/obj网络，找到grid节点，转到其material菜单，单击选择器图标，将显示一个选择器。

2.  选择/obj/shopnet1/principledshader。启用export relative path,点击accpt。

如果保持渲染视图运行，你应该可以在对象上看到更新后的材质。

##  Things to note

The material palette is similar to the maya visor, ie, a place to get and store presets. Like the Visor, its clunky and no-one really uses it. For some strange reason, SideFx decided this is the place to store the mantrasurface node, rather than the expected tab-complete menu in SHOPs, which itself is unusually empty. Fixed in a future version perhaps? (note to self; find a way to add nodes to the tab menu...)

I find using relative paths ( ../shopnet/mymaterial ) easier to read than explicit paths ( /obj/shopnet1/mymaterial ). Also means if you have to copy and paste setups, its less likely to clash with existing nodes in other shots.

The mantrasurface node is the latest attempt by SideFx at an all purpose, mia_material/vray/arnold style all-in-one physically correct shader. It does diffuse, 2 reflect (for base and clearcoat), refract, translucence, emission, opacity, with support for maps on most parameters. The one in H14 has had a bit of a tidy up, the tabs are cleaner, shader parameters better named than previous versions. Prior to the mantrasurface node was the surfacemode node (which you can still find in the palette underthe mantrasurface)

A great feature of the mantrasurface node is you can dive inside and see how it works. A horrible feature is that its pretty messy under there and a bit overwhelming at first! Don't try and understand it all in one hit, its better if you have a specific interest to just dive into that section and poke around, most of it is clearly labelled.

Other Houdini users have made their own versions of an all-in-one physically correct shader. The layered pbr shader on the orbolt store is very nice. A key difference is that its written in vex rather than vop nodes, so isn't designed to be pulled apart. There's also been attempts to recreate the disney bsdf shader, also worth a look. (provide links here) 

##  Material attribute overrides

摘要：取一个材质属性名称（例如baseColor），在一个对象或点级别创建一个具有相同名称的属性，为其赋予一个新值，它将覆盖该对象/点的材质默认值。很强大。

![Mat_attr_override.gif](http://www.tokeru.com/cgwiki/images/5/50/Mat_attr_override.gif)

###  Override at object level

[以下3,4,5步操作因为houdini版本的迭代没有了，类似的操作可以在geo内创建一个material节点，然后就可进行类似操作]()

1.  编辑材质的基础颜色，进行渲染。茶壶和地板都变成绿色。

2.  将鼠标悬停在baseColor标签上，请注意其名称为baseColor baseColorg baseColorb。baseColor是一个向量。

3.  选择茶壶，转到材质选项卡

4.  点击材质名称最右侧的下拉菜单，选择select and create local material parameters

5.  在弹出窗口，选择baseColor，点击Accept。

6.  将此颜色设为红色

7.  渲染视图现在显示红色的茶壶和绿色的地板，即使它们都使用相同的材质。

从同一下拉列表中你可以选择在对象上复制完整的材质界面，或将其重置为默认值，或删除局部替代。接下来，我们将在点层面进行覆盖

###  Override at point level

1.  进入grid对象，添加一个point vop节点，使其可以成为可渲染/显示的节点。

2.  进入point vop节点，

3.  创建一个bind export节点，将其类型设置为color，名称为baseColor。

4.  将P直接连接bind export节点。

5.  grid的baseColor材质属性已被点颜色覆盖

点级别替代的次要复杂之处是知道所需属性的名称（我发现工具提示悬停是最简便的方式），并且设置该属性（我的首选项是使用point vop，这样我就可以用vop纹理或其他技巧）。

##  Assign materials to faces

摘要：material sop节点使你可以按面分配。

![Per_face_material.jpg](http://www.tokeru.com/cgwiki/images/e/eb/Per_face_material.jpg)

在maya中进行按面分配是有风险的，使用渲染层进行更改很麻烦。在houdini中进行相同的操作非常好。添加material sop节点，告诉它你想要完成哪种材质。如果已定义，也可分配给face组。

1.  在视窗的左侧，确保模式为primitives(或视窗中的热键4)

2.  在视窗的左侧，单击箭头以进入选择模式（视窗中的热键s）

3.  拽出矩形框以选择一些面

4.  在视窗中按Tap键（重要！），选择group，它将会把你选择的面打包成一个组。

5.  使用其他选择的面进行同样的操作。

6.  添加一个材质节点，选择一种材质，然后从组下拉列表中选择一个组。该材料将仅限于该组。

##  Point Colour (Cd) and Alpha

摘要：颜色属性为Cd，透明度为Alpha（请注意大写字母a)

将Principled shader节点设置为读取点颜色和透明度（如果存在）（它们将与着色器颜色相乘）。要记住的唯一技巧是使用正确的属性名称。颜色非常简单，因为在vop网络中，其颜色在输出节点上列出。虽然没有列出Alpha，但每个人都经历了一次错误的尝试，即尝试看似明显的（Af），然后尝试其他的（af？）和其他事情(opacity?),直到最终记住正确的格式：输入float。

##  AOVs or Extra Image Planes
Houdini称它们为Extra Image Planes，其他人称它们为AOV（Renderman缩写为Arbitrary Output Variables）。与其他软件包相比，它的工作量要多一些，但是在另一方面，它可以自由地做任何你想做的事情（就像大多数houdini一样）。

### Defining AOVs in a shader

在着色器中，你连接到bind export的vop的任何内容都可以用作AOV。

1.  进入shopnet，然后进入principledshader着色器。

2.  创建一个bind export节点，名称为myaov,键入vector。

3.  将N连接到其输入。

你现在已经准备好将myaov用作AOV。

### Add AOVs to Rop

1.  进入ropnet，选择mantra节点。

2.  选择Image菜单，然后选择Extra Image Planes子菜单。有一些预定义AOV，但我们需要新的自定义AOV。

3.  单击Extra Image Planes字段旁边的+按钮，将出现一个新的参数子集合。

4.  在vex变量字段中输入myaov

5.  确保vex类型为Vector Type.

6.  渲染。弹出渲染视图顶部（在渲染按钮下方）的视图栏，并在显示C的位置使用下拉菜单选择myaov。

7.  有你之前定义的AOV。

像大多数现代渲染器一样，Mantra在添加AOV时不会造成很大的速度损失，而会增加内存和磁盘空间。通常会自动向大多数材质和rops添加几个标准AOV，因为它们在合成中非常有用。通常是P-cameraspace，P-worldspace，N-world，Diffuse，reflect，indirect。

##  Houdini rendering setup from a maya perspective

要回答的问题：

*   加载已发布的资产（相机，动画/FX alembics,vdb体积，材质，材质等）

Yes to all the above. The last time I used Maya it was still in the mindset of 'you load a thing in, thats a one-shot deal, now it belongs in the maya scene. You don't get to swap out for another obj on disk, or another fbx, or another camera'. You could use referencing of course, but that's specific to maya mb or ma files, and was super brittle and prone to failure. You could refer to particle caches or occasionally ncaches in a more general hot-swappable sense, but it seemed fraught.

Houdini by comparison is completely built around this idea of 'load stuff from anywhere in a myriad of formats, process it, spit it out as something else'. The file sop, the general purpose get-something-from-disk loader, can handle houdini's native geometry format ( bgeo, which in itself can be polys, or particles, or volumes, or any combo of the above), but also abc, and vdb, and more esoteric formats like fbx (rapidly getting better and better due to Sidefx's focus on games, which uses fbx a lot), and plenty of esoteric formats ( obj, ply, collada, blah blah)

The upshot is that you can load a high level format like alembic or vdb, and build a network that does stuff to it, assigns shaders, hides/shows things, and preps it for rendering. If you design the network in the right way, you can swap the path on the file rop, the rest of the network just updates. Best analogy is nuke; you can use it in a super custom way with lots of manual roto and paint nodes, so that if you swap the initial read node you have to start from scratch, or you avoid manual brittle nodes, keep your comp network procedural, and you can reuse the setup across similar shots.

Alembic itself is a special case. Alembic can be brought in via the file sop, as I mentioned above, and it essentially brings in whatever geo you have as a point cache. The geo itself will have lots of attributes (think like particles and per particle attributes), and houdini has excellent tools for manipulating data in this format. That's one of the key mode switches of moving from maya to houdini; maya is mostly high level transforms with mesh data carried underneath, and you mostly work at that top level. Houdini is better down below, so you tend to bring lots of geo into a single transform (which you barely touch, it functions like a null at the origin normally), while you do lots of manipulation to the mesh data underneath.

Anyway, you don't have to do this. Alembic can also be loaded as a high level thing if you need it, and houdini will create the full transform heirarchy with local mesh data. Normally this is avoided, unless, and this is a big unless. you need cameras. Cameras are inherently not mesh data, a camera is a fancy transform, so this is how you load camera data. While this method isn't as flexible as the other, it still allows the hot swap reloading for cameras like the file sop method.

The other thing that makes Houdini good for mass shot work is its heavy unix underpinnings. Again last I checked maya was terrible for data based file paths, both for input and output, so if you wanted to define a path to a shot cache via code, you need python/mel to be fiddling file paths. 

Houdini on the other hand allows for unix style variable substitution in paths. A path to a shot cache might look like 

    /jobs/$SHOW/$SEQ/$SHOT/assets/${CHAR}.abc
    
And either from your shell, or from houdini's own environment variable editor, or from an asset management tool like shotgun, you'd have all those variables defined, like:

    $SHOW = beemovie2
    $SEQ = sk02
    $SHOT = sk02_050
    $CHAR = joe

You can middle click on the file path, and see the path get the variables substituted in. Again, the idea is you setup the file sop to be procedural and data driven, and let the system swap the paths around for you.

Shaders are of course more render engine dependent. This is where I must confess I don't do much setup (I've been spoiled in my film fx career, and we have lots of pipeline tools to pre define shaders, or its handled downstream), but you've got a few options here. Maya uses shading groups, which is a set containing a link to a shader, and a link to either transforms (preferred) or shapes (also ok), or sub-shape selections (fraught). Houdini lets you assign shaders to the top level transform, or in that per-particle attribute style I mentioned earlier applied to the polys, or using stylesheets, similar to web css stylesheets. The latter is very powerful, but a bit arcane, I only know a few studios using it. Yet another thing you can do is material parameter overrides; say your material has an attribute called 'basecolor', and its red. If you have an extra attribute on your transform also called 'basecolor', and its green, because the names match, it will function as a local override. You can even do this per poly, which is pretty cool. This can also be defined via stylesheets if you want. 

*   connect stuff in a procedural, non-explicit fashion (like dynamically assigning shaders to geometry based on names/attributes/metadata/whatever)

What I alluded to above; houdini has excellent geo data manipulation tools, so within your sop network (the closest thing to maya's construction history but much cleaner to use and more powerful), you can put in things like switch nodes, and drive that switching from an expression, so that if its shot 10, it will assign materialA, but if its shot 20, assign materialB. Or you can do assignments based on geo attributes, so if the geometry sub-name is 'fred', assign the fred shader, but this can be as baroque or as simple as you want; again the maya particles analogy comes into play; you can do lots of 'if this do that' behaviour with particles, imagine that times 100, and to drive whatever attributes, wherever. 

*   keep a 'root' assembly/tree (like everything needed for a particular sequence of shots), that can then be branched out into multiple shot outputs with local overrides on attributes, caches and render output.

not so much. you can kindasorta do this, better than maya can, but not in the way katana can. you can do tricky tricks with branching switch nodes based on shot variables and stuff, but its not elegant. 

*   defer loading to rendertime for heavy assets

yep. right on the file sop is a toggle, 'delay load geometry'. this also has the effect that when translating geo to pass to the renderer, it will just use a reference to the cache on disk rather than trying to load it all into a big binary blog, so translate times are quick, and all the heavy lifting is left to the renderer. 

##  Renderstate vop

![](http://www.tokeru.com/cgwiki/images/6/6c/Renderstate_wiki.jpg)

##  Material wrangle via snippet

![](http://www.tokeru.com/cgwiki/images/3/3c/Material_wrangle_capture.gif)

##  Todo




<a href="HoudiniTutorials.md">
  <img src="https://github.com/BlenderCN/blenderTutorial/blob/master/mDrivEngine/blenderpng/logoleft.png" align="left">
</a>
<a href="HoudiniVolumes.md">
  <img src="https://github.com/BlenderCN/blenderTutorial/blob/master/mDrivEngine/blenderpng/logoright.png" align="right">
</a>

