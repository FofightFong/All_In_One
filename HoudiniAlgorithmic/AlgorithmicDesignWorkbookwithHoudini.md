# Algorithmic Design Workbook with Houdini

https://github.com/all-in-one-houdini/Houdini_Algorithmic

感谢您对这本书感兴趣。 本书是针对Houdini的算法设计工作手册，其中包含21种不同的练习，每个练习都有两个示例答案。 这是为希望提高程序建模技能的Houdini初学者和中级用户而设计的。

您可以从以下网址下载所有hip文件，以获取本书中显示的答案。 

https://github.com/jhorikawa/AlgorithmicDesignWorkbookWithHoudini

尽管作者和出版者已尽一切努力确保本书中的信息在出版时是正确的，但作者和出版者不承担任何责任，并因此对由于错误或错误导致的任何损失，损害或破坏不承担任何责任。 疏忽，无论是由于疏忽，事故还是任何其他原因导致的此类错误或疏忽。

本书的每个练习分6页。 前两页显示了示意图和示例输出图像，显示了您必须使用Houdini解决的任务。 其他4页用于2个示例解决方案，这意味着2页用于一个解决方案。 解决方案页面包含有关如何解决任务的简短描述，以及示意图和带有注释的Houdini网络视图

本书的主要目的是让读者意识到对任何设计问题都没有正确的解决方案，并且意识到存在无限的可能性。 因此，我希望您在这里完成的工作是，在阅读任务页面以理解问题之后，我希望您暂停阅读并开始考虑自己的解决方案，然后再深入研究解决方案页面。 启动Houdini并开始构建自己的解决方案。 通过这样做，您将深刻理解设计任务在询问您什么

本书中为每个任务提供了两种解决方案，仅供您参考，以了解任务还有其他可能性。 通过在完成任务后检查它们，可以广泛地了解何时使用哪种解决方案。 在检查解决方案时，我建议您将其与打开的HIP文件一起阅读，您可以从前言页面（第2页）上的链接下载这些文件。


将框散布在XZ平面上，然后旋转每个框以查看可以在3d空间中自由移动的目标球体。 如果可能，即使目标球体位于框的上方或下方，也应尝试将旋转轴限制为Y轴（框的视角为水平，并避免向上或向下看）

为了观察目标，必须将方向作为矢量信息。 您可以通过用对象（在此情况下为方框）位置矢量减去目标位置矢量来轻松获取该信息。

看完方向后，接下来要做的就是将法线向量N设置到要放置框的点，然后使用“复制到点SOP”放置框，以使框自动旋转 在该点的法线方向上

使用Ray SOP创建法线您可以使用Ray SOP创建矢量外观，并将其设置为每个散布点的法线矢量属性。 然后，您可以使用“复制到点SOP”将框放置到该点以面向目标。

在某些情况下，您可能希望避免盒子向上或向下看而只能水平旋转。 一种用法是将这些盒子替换为不应向上或向下看的扁平纹理道具（树，人等）。

实现此目的的最简单方法是将法线向量的y值设置为0，以便可以强制法线向量始终面向水平。 使用VEX可以轻松完成这种操作。

使用VEX创建法线向量通过使用带有简单方程式的Point wrangle节点使用VEX，可以轻松地计算法线向量以水平查看目标

从任何输入几何图形创建轮廓（切片）曲面。 您应该能够更改轮廓的数量（或轮廓步距），并尽可能更改轮廓的方向

创建轮廓的一种方法是使用循环，在Houdini中，您可以使用For Each循环进行循环。 我能想到的一个示例是从一个输入几何图形的边界中提取一个面，并使用Transform SOP和Boolean SOP将其用于For Each循环中的几何图形部分。

从边界中提取面从输入几何图形创建边界框并检索一个面。 还要获取边界点的最小和最大位置，以使用它来计算应该移动的距离。

使用循环剪切截面使用For Each循环使用计算的最小和最大位置移动提取的面，并使用布尔SOP检索输入几何的一部分

创建轮廓的另一种方法是使用复制SOP同时创建剖面。 这样，它的计算比使用循环要快一些。 在此示例中，我还添加了其他参数，以便您可以指定轮廓的方向

特别是使用“线，边界和相交分析” SOP来创建芯线，并在该线上垂直放置多个平面，以使用它从输入几何图形中剪切出该截面

为轮廓创建中心线基于轮廓方向参数，在输入几何的中心创建中心线

同时创建轮廓使用“复制SOP”将许多平面垂直放置在芯线上，并使用“布尔SOP”将截面创建为轮廓表面

创建多个对象，以指定的速度和随机在指定的框区域内行走（随机选择每帧要移动的方向）。 如果可能的话，当物体移到盒子外面时，让它从盒子区域的另一侧出来。

让对象随机行走的一种方法是将Solver SOP与一些噪声函数一起使用来确定每帧的移动方向。

这里的重点是编写一个在求解器网络内随机移动的过程，该过程将递归地称为每一帧，而我正在使用VEX编写一个简单的代码，因为它具有灵活性，因此可以使用噪声函数让点随机移动，但是该过程也可以 使用属性噪声SOP替换

使用VEX进行随机游走编写一个简单的代码，以根据点的位置，帧数和点的数量使用VEX中的噪声功能随机移动点。 还添加另一个Point wrangle，通过使点跳出边界时跳到边界的另一侧，将点保持在边界内。

让点随机行走的另一种方法是仅使用具有噪声功能的VEX，而无需求解器网络。 最后一个示例使用噪声函数来确定随机行走方向，但是本示例使用噪声函数来确定点的位置本身。

使用噪声更新点位置使用“点缠绕”节点可以根据帧数和点编号使用噪声功能更新点位置。

沿提供的曲线路径从曲线的起点到终点移动任何对象。 移动对象时，请尝试根据路径的切线方向旋转对象

在此示例中，我使用“雕刻SOP”来确定曲线上您要将对象移动到的特定位置。 这是沿曲线移动对象的最简单方法之一。

从随机放置在框中的多个点创建随机曲线路径

使用雕刻SOP在曲线上获得一个点并将对象移动到该点

在此示例中，我使用曲线uv检索曲线上的位置以移动对象。 我正在使用VEX通过uv参数指定曲线上的位置

从随机放置在框中的多个点创建随机曲线路径

使用Wrangle节点通过使用uv参数编写VEX代码并在该点上移动对象，从而在曲线上获得一个点

根据条件将不同类型的对象放置在输入几何体上。 在这种情况下，请在几何图形上创建点数，然后根据每个点的法线方向的垂直度放置从三种类型（球体，盒子和金字塔）中选择的对象

在此示例中，我将Switch SOP与Copy Stamp SOP结合使用，根据条件将三种类型的对象放置在输入几何图形上。 特别是，此处的条件基于几何图形点法线方向的垂直度，可以使用“保持法线”选项和“ Group SOP”来确定。

使用“组SOP”可使用“保持法线”选项基于垂直角度在输入几何图形的每个点上设置组

在此示例中，我将Switch SOP与For Each循环一起使用。 该方法可以用于许多其他目的，但是比使用“复制图章”方法要慢一些。

在输入几何图形上创建点的数量，每个点都有一个用VEX计算的属性，该属性使用三种类型的对象，然后将其与循环内的Switch SOP一起使用。

创建三种类型的对象以便将其用于切换

在几何上创建点，并根据垂直角度计算出一个角度id


使用循环将对象放置在几何图形的每个点上。 将使用Switch SOP根据点的角度ID选择要放置的对象

创建一个带有width和height参数的倾斜屋顶。 尝试创建一个可以有多个分支的屋顶。

该示例的基本思想是为屋顶设置两条曲线，为屋檐设置一条曲线，为屋脊设置一条曲线，并使用PolyLoft将其连接以创建曲面。

本示例首先制作与山脊相对应的屋顶芯线，然后使用PolyExpand2D SOP创建屋檐和山脊。 然后将脊边缘向上移动一个屋顶高度，并使用PolyLoft SOP从这两个边缘创建表面

使用PolyExpand2D从核心线创建脊边，可用于放样。

使用另一个PolyExpand2D SOP创建屋檐边缘，并使用PolyLoft将其与屋脊边缘连接以创建屋顶表面。

本示例从与屋顶屋檐相对应的屋顶轮廓创建屋顶。 基本轮廓是通过使用VEX编码从网格中随机提取面来创建的，这有点复杂

其余的很简单，只需使用PolyExpand2D SOP创建山脊边缘，然后使用VEX将其沿屋顶高度向上移动即可完成屋顶表面

使用PolyExpand2D SOP从屋顶轮廓创建山脊边缘，并使用VEX将其沿屋顶高度向上移动以创建屋顶表面

在任何输入几何图形的顶部创建积雪。 创建一个参数，以便您可以控制几何图形的雪覆盖率

在此示例中，基本流程是使用Group SOP捕获想要堆积雪的输入几何图形的顶部。 然后使用VDB创建实际的雪花

使用带有角度参数的Group SOP获取输入几何的顶部，然后使用Scatter SOP在此顶部创建点数

使用来自粒子SOP的VDB，并在几何图形的顶部放置点以创建厚厚的积雪

与前面的示例相比，此示例创建了一层薄雪。 首先使用VEX提取输入几何图形的顶部，然后使用VDB作为最后一个示例来创建厚厚的积雪。 然后使用它通过布尔SOP提取几何图形的顶部

使用VEX获取几何图形的顶部并在其上放置点数。 然后使用来自粒子SOP的VDB，并在几何图形的顶部放置点以创建厚厚的积雪

通过使用布尔SOP获得以基本几何形状和厚雪作为输入的相交表面来创建薄雪层

通过设置体素分辨率对所有输入几何体进行体素化（将几何体转换为Minecraft之类的盒子集合）

本示例使用体积体素化输入几何体。 具体而言，此示例将输入几何转换为体积，并使用“体积SOP”中的“点”从体积中提取3d网格点，这是对对象进行体素化的最简单方法之一

这种方法确实很容易，但是您将拥有体素填充几何体，这使您无法实际看到不必要的几何体

根据输入几何图形创建体积，并使用“体积SOP”中的“点”从该体积中创建3d网格点，以将其用作体素框的中心

此示例使用VEX使体素仅在输入几何图形的表面上。 首先使用Scatter SOP在几何图形上创建许多随机点，然后使用VEX将每个点移动到最接近的对应3d网格位置，这样可以避免在几何图形内部出现看不见的体素。

使用Scatter SOP在几何图形表面上创建点，然后将每个点位置移动到最接近的3d网格点位置。 使用保险丝SOP删除重复的点，这将成为体素框的中心点

创建一个六边形网格并将多个点作为吸引子。 根据吸引点位置，从此六边形网格创建波浪表面。 如果可能，创建一个参数来控制波浪的形状

为了使用吸引子点变换对象，必须计算吸引子和要变换的对象之间的距离。 在此示例中，将射线SOP用于每个对象进行变换，以计算对象和吸引点之间的最短距离

保持一定距离后，此示例使用“ For Each”循环使用计算出的距离作为拉伸高度来拉伸对象

创建一个网格，并将其指向吸引子。 使用Ray SOP计算每个网格面到最近的吸引点的距离

使用For Each循环以使用PolyExtrude SOP之前计算出的距离值拉伸每个网格面

为了更灵活地进行吸引子变换，最好使用VEX来计算和修改每个网格面之间到最接近吸引子点的距离值。 特别是通过具有斜坡参数，您可以控制挤压山峰的形状细节。

使用VEX，您还可以避免使用For Each循环拉伸面，从而使整个过程更快。

通过将六角形形状复制到用VEX制成的六角形网格点来创建六角形网格表面

使用散点图SOP在网格表面上创建特定数量的吸引点。 然后使用它们使用渐变参数计算拉伸高度，并使用VEX实际为每个网格面拉伸。

创建一个参数圆桌会议，您可以更改其半径和高度并将其放置在二维网格上。 然后，根据一个轴逐渐更改每个工作台的半径参数，并根据另一轴逐渐更改高度参数。

使用嵌套的For Each循环可以很容易地完成参数在2d网格上的参数化对象布局

在此示例中，准备了一个带有两个参数的圆桌会议。 然后使用两个For Each Number循环逐步更改表格的两个参数。 在每次迭代中，您可以使用循环中的两个迭代值来计算表的参数。

使用两个嵌套的“每个数字”循环，以便可以进行x * y次迭代。 在每次迭代中，使用每个For Each循环的迭代值将其用作圆桌会议的参数。

本示例使用由VEX创建的属性，而不是使用嵌套的For Each循环进行逐渐变化的2d网格布局，从而使整个过程更快。

在这种情况下，我要逐渐更改的参数可以表示为比例尺值，因此在与“复制到点” SOP一起使用时，使用比例尺矢量属性设置每个网格点都可以完成工作。

根据位置创建具有比例尺属性的网格点。 然后使用“复制到点” SOP来放置使用此属性缩放的管几何图形以创建圆桌会议

将任意数量的面板放置在任何输入几何图形上，然后旋转每个面板以创建整体起伏。

可以使用多种方法制作起伏的面板，但最简单的方法之一是无需使用任何复杂的设置即可将属性噪声SOP与“复制到点” SOP结合使用

为了简化起见，本示例在不需要考虑各种法线方向的平面上创建面板。

对网格中的每个点使用“属性噪声SOP”来创建法线（N）属性。

使用“复制到点SOP”将面板放置在网格点上。 由于每个栅格点都具有法线属性，因此面板会自动旋转。

为了使用比平面更复杂的形状来放置面板，最好使用VEX来实现噪声功能，该功能比使用属性噪声SOP更为灵活。 这样，您可以直接使用VEX设置法向矢量。 在此示例中，我选择的是基本几何形状的管形形状，但此方法可以使用其他任何几何形状

使用噪声函数和VEX为管几何上的每个点创建法线向量

使用旋转对球体对象进行切片。 尝试以圆柱形（一个轴旋转）或球形（三维旋转）对对象进行切片。

本示例使用For Each循环对圆柱体进行切片。 这里的基本过程是创建一个缩放圆柱体，并在带有布尔SOP的循环中使用它来对球体进行切片。 同样在循环的每次迭代中，切片球体都基于恒定的旋转轴逐渐旋转

对于循环的每次迭代，从管几何图形创建切割对象

使用布尔SOP对球进行切片并使用“变换SOP”旋转对象。

本示例使用For Each循环将球体切成球形。 因为此示例使用球体而不是圆柱体来切片物体，所以与圆柱体旋转相比，旋转轴是自由的，这使其设置更为复杂

对于循环的每次迭代，请从球体几何形状创建切割对象。

使用布尔SOP对球进行切片，并使用“变换SOP”使用三个轴旋转对象。

使用图像修饰平面。 特别是要根据图像的对比度控制每个修复细胞的形状，大小和颜色

本示例使用图像将平面重新划分为彩色和大小合适的voronoi细胞。 具体而言，可以使用Map SOP中的“属性”将图像加载为具有可能具有颜色属性的点的网格平面。 在这种情况下，将加载灰度值并将其用作Scatter SOP的密度值，以便根据其对比度将点分散在图像平面上。 然后将这些点与Voronoi Fracture SOP一起使用来创建voronoi细胞

使用Map SOP中的Attribute加载图像，并使用Scatter SOP基于图像对比度放置点

使用Voronoi裂缝重新划分平面，并根据图像创建点

本示例使用双重网格重新划分平面。 为了创建双重网格，本示例首先使用Remesh SOP重新定型平面，该网格基于从Map SOP的Attribute加载的灰度属性。 然后使用Divide SOP创建一个双重网格

使用Map SOP中的“属性”作为平面上的灰度属性加载图像。

使用Remesh SOP使用图像平面中的灰度属性对平面进行网格化，然后使用Divide SOP创建双重网格。

可视化受文本影响的向量字段。 特别是将文本轮廓用作控制矢量场方向的驱动力。 在2d或3d中创建矢量场。

本示例创建一个受文本轮廓影响的二维矢量场。 文字轮廓的切线矢量将确定附近矢量场的方向

由于向量字段本身是向量的集合，因此除非您以某种方式专门对其进行可视化，否则您将无法真正看到它们。 本示例通过使用网格平面上的分散点作为基于文本轮廓附近切线向量旋转的线的起点来可视化2d向量场。

在网格平面上创建基点，该基点继承文本轮廓的附近切线向量作为法线向量

通过将线复制到使用其法线属性自动旋转的每个点上来显示2d矢量场

在很多情况下，您可能希望制作3d矢量场而不是2d矢量场。 在这种情况下，创建3d矢量场的最简单方法之一就是使用速度量

为了使用文本几何体修改速度量，最好使用“体积扭曲”来编写VEX以控制矢量方向，因为这是最灵活的方法之一。 您可以使用Volume Trail SOP可视化由速度体积构成的矢量场的流动

基于拉伸文本几何体，使用“体积扭曲” SOP创建和修改3d矢量场

使用体积轨迹SOP可以在体积区域内以特定数量的点可视化3d矢量场

创建凹槽表面的方法很少，但我能想到的最简单的方法就是直接使用Mountain SOP，只需更改一些参数即可。 有一种称为Worley的噪声类型，通常用于波浪海域，但是通过调整参数可以很容易地将其用作挖沟的表面图案。 使用此方法的不利之处在于，当使噪声量太大时，无法使脊的高度相同，而这会破坏原始形状。

使用具有Worley杂色类型的Mountain SOP在输入表面上创建类似凿状的图案。

如果要进行更多控制以创建刨槽表面（尤其是保持山脊边缘的高度），则该过程将比使用一个可用于任何输入几何的Mountain SOP更为复杂。

在此示例中，Voronoi骨折用于创建凿刻图案基础，并使用VEX为每个voronoi细胞创建平滑凹痕。 根据每个单元格点与单元格轮廓线之间的最短距离来计算凹痕量

使用Voronoi Fracture SOP从输入几何图形创建voronoi细胞。

通过使用每个单元格中的点之间的最短距离和该单元格的轮廓，使用VEX为每个voronoi单元格创建凹痕

创建粒子变形，以使由粒子（点）集合构成的一个形状通过时间或滑块值变形为另一种形状。 如果可能，请尝试从一种形状变形为另一种形状时增加扩散效果

为了创建粒子变形，您必须在源形状和目标形状上具有相同数量的粒子。 请记住，当您只想进行线性粒子变形时，其余的工作非常简单

具体来说，您可以只使用Blend Shape SOP来创建从源形状粒子到目标粒子的变形形状。 这里的一个技巧是使用相同的规则对源点和目标点进行排序，因为变形是在具有相同id的点之间完成的。 在此示例中，使用“按X轴对SOP排序”对点进行排序

从文本几何图形创建源粒子和目标粒子

用户混合形状SOP以在两组粒子之间创建线性变形

如果您想更好地控制变形，Blend Shape SOP不够好，但您可能想使用VEX以获得更大的灵活性

在此示例中，使用Wrangle SOP而不是Blend Shape SOP进行变形，以便在变形过程中添加扩展效果。 具体来说，噪声函数与简单的三角函数一起用于在变形过程中增加扩展效果。

从文本几何图形创建源粒子和目标粒子。

使用VEX基于噪声函数创建变形效果和扩散效果

准备三个几何并从中创建轮廓轮廓。 然后在这三个轮廓轮廓之间创建变形动画。 如果可能，尝试使用渐变参数来控制变形动画的缓动

轮廓变形的方法类似于粒子变形的方法，但是在此示例中，变形是在多个轮廓形状之间完成的。 前提是粒子变形相同，即所有变形形状之间的点数相同

本示例使用Blend Shape SOP来创建形状之间的线性变形。 此外，它使用Delete SOP根据变形时间为源和目标选择相应的一对形状

准备多种形状以创建轮廓

使用For Each循环主要使用Triangulate SOP为每种形状创建轮廓曲线

将Delete SOP与morphing time参数一起使用以获取两个要变形的形状，并使用Blend Shape SOP实际进行线性变形

先前的线性变形示例缺少点排序的可控性以及变形的平滑性。 如果线性变形不足以满足视觉需求，那么为什么不使用VEX以获得更好的可控性。

在此示例中，为了获得更平滑的变形，通过对原始轮廓进行平滑处理（直到其变为凸形）并使用从轮廓中心测量的点的角度进行排序，来修改每个轮廓的点顺序。 当使用VEX从一种形状变形为另一种形状时，它还具有缓动功能

使用VDB和布尔SOP从每个形状创建轮廓，并通过将轮廓制成圆形凸形形状以获得圆角来对点的顺序进行排序

使用源和目标形状的VEX使用缓动功能创建变形

使用等值面作为元素（如图像下一页）创建晶格结构。 如果可能，请尝试使用数学方程式来创建独特的晶格结构。

创建等值面的最简单方法是使用元球，这是等值面的一种类型。 将metaball放置在一个框的每个顶点上，然后使用具有相同大小的框的boolean修剪此形状，您可以拥有一个基本形状，可以将其无缝地放置在3d网格上。 当您这样做时，可以构造一个晶格结构。

通过在3d网格上无缝复制用metaball制作的晶格元素来创建晶格结构。

当您想对形状进行更多控制时，仅使用元球进行等值面可能是不够的，因为涉及等值面时，存在多种类型的形状

当您想探索各种有趣的等值面形状时，最好使用一些数学方程式来处理体积。 在此示例中，通过简单的三角方程，使用“体积扭曲”来创建两种类型的等值面

使用体积扭曲SOP使用等值面创建无缝晶格结构。 使用以下数学方程式具体计算每个体素的密度值。

使用长度和绳索厚度参数创建编织绳索。 如果可能，尝试沿着自由3D曲线创建编织绳

本示例通过准备三个完全相同的由三角法制成的波浪形曲线并水平地重复复制以创建长的连续编织绳，来创建一条直的编织绳

使用VEX使用正弦函数创建三个水平偏移的相同波浪曲线

通过水平复制三个波浪曲线来创建直的连续编织绳。 然后您可以使用PolyWire SOP来加厚绳索

如果只能将绳索拉直，则不太灵活，但您可能想沿任意自由曲线创建编织绳。

本示例通过使用大量的VEX代码将直编织绳重新映射到一条自由绘制的曲线上，而不是使用“导线变形SOP”，沿着一条曲线创建一条编织绳。 该示例未使用Wire Deform SOP的原因是，该节点无法避免扭曲自由绘制的曲线，但是使用VEX可以通过引用由PolyWire SOP创建的几何图形的清理矢量来避免扭曲

首先主要使用正弦波的VEX创建一条直的编织绳曲线。

通过参考由PolyWire SOP使用VEX创建的几何图形来获得未扭曲的矢量。

使用VEX通过使用先前检索到的向量将直编织绳曲线映射为自由曲线而不会扭曲

创建一个分形列，如下一页所示。 规则是首先准备具有指定边号的多边形。 然后将其复制以应用诸如旋转，缩放和平移之类的转换以创建下一个列层。 使用最后创建的列图层重复此过程，以创建逐渐变换的列。 如果可能，请根据一些迭代时间创建一个列分支。

为了创建分形几何体，在Houdini中有多种方法可以实现，而实现此方法的一种方法是使用“带有反馈的循环”选项。 您想要对分形几何图形使用反馈类型循环的一种情况是，当不需要动画时就需要静止几何图形，因为所有计算都在一帧中完成

本示例使用具有指定边数的多边形作为基本形状，并使用带有反馈选项的“每个数字”循环具有分形列。 它还将嵌套循环与Switch SOP一起使用，以便列计划将在每一次迭代中拆分

使用带有反馈选项的“每个数字”循环可从简单多边形开始创建分形列。 在每次循环迭代中，最后创建的多边形被复制并旋转

在Houdini中创建分形几何体的另一种流行方法是使用Solver，它与反馈循环非常相似，唯一的区别是，当您使用Solver时，在循环中完成的计算是按帧进行的，这使得可以轻松地生成生成动画 。 在此示例中，求解器用于创建分形列，而不是用于For Each循环，但是其余过程与前面的示例几乎相同。

使用求解器SOP从一个简单的多边形开始创建一个分形列。 在每帧上，最后创建的多边形被复制并旋转

在任何输入几何图形上创建大理石花纹。 此处的大理石图案应创建为在表面上绘制的曲线的集合，并且相邻曲线之间的距离应始终相同，并且可以作为参数进行修改。

与分形几何相似，此示例使用的方法是反馈环。 反馈循环对于包括分形在内的递归计算很有用，也可以使用此递归计算来制作大理石花纹

本示例首先通过使用球体切割从输入几何图形检索裸露的边缘开始。 然后，通过使用For Each反馈类型循环，您可以从裸边缘递归创建管道几何，该管道几何再次用于切割几何以创建另一个裸边缘。 最后，您将使用轮廓曲线等大理石花纹覆盖基本输入几何图形

使用反馈循环，通过使用从最后创建的裸边缘生成的管道切割几何来递归地在几何上创建轮廓曲线，该管道将生成新的裸边缘

此示例使用求解器而不是反馈循环，这使得可以像分形几何图形一样创建生成动画。 这个示例与前面的示例几乎相同，只是它使用了Solver SOP而不是For Each循环。

使用求解器SOP通过使用从最后创建的裸边缘生成的管道切割几何来递归地在几何上创建轮廓曲线，该管道将生成新的裸边缘。

再次感谢您对这本书感兴趣。 我希望您从本书中学到了一些有用的东西，也希望您在必须解决自己的设计问题时喜欢探索无限的可能解决方案






