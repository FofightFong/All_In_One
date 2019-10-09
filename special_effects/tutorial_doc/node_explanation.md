Add Generators|polygon 创建点或Polygon线/面,为输入添加点或polys   
	Align Filters|NURBS 互相对齐一组面或和辅助输入节点对齐, 通过绕着某一轴心点平移或旋转   
	Ambient Light         Generators环境灯，控制场景里环境光的颜色和亮度     
	Atmosphere         Generators在渲染时创建大气效果     
	Attrib Composite Attribute 用于在多个选择中合成顶点，点，面，或其他属性   
	Attrib Copy   用于在多组顶点，点，或面之间copy属性   
	Attrib Create   用于添加或修改用户定义的属性   
	Attrib Mirror   从镜像平面的一侧向另外一侧镜像属性   
	Attrib Promote   用于提升或降级属性，转换属性类型。比如把点转成面   
	Attrib Reorient   属性再适应，用于修改基于两个不同几何体之间差异修改点属性   
	Attrib String Edit   用于编辑字符串属性   
	Attrib Transfer   用于在两个选择之间传递顶点，点，面等属性.   
	Attribute Attribute|Material 允许你手动重命名或删除点和面属性.可用于renderman 渲染   
	Auto Rig Biped         Generators自动生成一套两足角色的骨架装配     
	Bake VEX   渲染前的烘培操作，只对具有VEX shader 的mesh,Bezier或NURBS 有效   
	Basis NURBS 提供一组对样条曲线或表面的参数空间可用的操作   
	Blast Edge 删除面，点，边，断点   
	Blend  *         Filters 允许各种操作，象混合输入,动画物体的父物体，序列，部分变换继承，方向或其他效果     
	Blend Shapes   融合变形，计算拓扑相同的形体之间的3D变形.   
	Bodypart Arm         Generators手臂装配     
	Bodypart Hand         Generators手装配     
	Bodypart Head and Neck     Generators头和脖子装配     
	Bodypart Leg         Generators腿装配     
	Bodypart Spine         Generators脊椎装配     
	Bone             Generators一节骨     
	Bone Link   创建骨头棒   
	Bound   边界框计算，为输入几何体创建绑定体积，可以是方盒或球形   
	Box primitive 创建方盒.   
	Bridge   桥，对于有洞的，剪切表面的蒙皮很有用，在手臂和身体之间，分支或管的相交部位创建高度可控的连接   
	Bulge Manipulate 凸起.用来自第二输入的一个或多个磁体变形来自第一个输入的点   
	Cache Misc 缓存输入的几何体，用于快速播放.   
	Camera             Generators构建摄像机     
	Cap   用于闭合开放的几何体   
	Capture character 用于蒙皮。一般和Deform op还有Capture Region op一起使用   
	Capture Correct 　 CaptureCorrect readjusts the capture regions and capture weights.   
	Capture Layer Paint 　 Capture Layer Paint is a specialized paint operation for painting capture attributes.   
	Capture Metaball 　 用metaball结合几何体上的点   
	Capture Mirror 　 镜像点的蒙皮权重   
	Capture Override 　 CaptureOverride overrides the capture weights on individual points.   
	Capture Proximity 　 CaptureProximity works in conjunction with the Deform operation and the CaptureRegion operation b...   
	Capture Region   相当于骨头蒙皮的影响范围，是一个两头闭合的管体积   
	Carve   用于切开或提取点或相交部分.   
	Channel Sourcing 从一个CHOP读取采样数据并把它转换成点的坐标和点的属性.   
	Circle   创建开放或闭合的弧，圆或椭圆.   
	Clay   变形表面，通过拉点   
	Clean   清理脏模型.   
	Clip   剪切模型,删除和模型相交的一个假想平面一侧的模型面   
	Cloth Create Seam   创建点属性，定义布料在DOPs里如何被连接在一起.
	Cloth Match Panels   使得接缝处两边的点数一致.   
	Cloth Match Seams   ClothMatchSeams由Cloth Match Panels在内部使用，一般不直接用   
	Cloth Refine   重新用三角形生成优化的布片.布片必须是平的   
	Color   为几何体快速添加颜色   
	Comb   梳子，用笔刷修改表面上的点法线方向   
	Connectivity   创建属性，并为每组连接的面或点分配一个唯一的值   
	Control   创建简单的几何元素   
	Convert   几何体类型转换。比如NURBS转成mesh   
	Convert Meta   把metaball几何体转成多变形   
	Cookie   多变形布尔操作或计算两个多变形物体相交线   
	Copy   创建输入几何体的多个copy,或者把几何体第二个输入的点上.   
	Crease   手动添加或删除多变形的折边权重，用于细分表面的SOP   
	Creep     沿着一个输入的几何体的路径表面变形和动画一个输入几何体   
	Curve   创建 polygons, NURBS 或 Bezier 曲线   
	Curveclay   类似 Clay op ，不通过修改CV点就可以变形样条表面，同样地，不支持多边形mesh   
	Curvesect   找到多条曲线的相交部分   
	Deform character 变形， 蒙皮时用的   
	Deform Metaball   根据metaball变形，变形蒙皮点   
	Deform Muscle   用肌肉去变形蒙皮点.   
	Delete   删除几何体.可用于精简场景   
	Dissolve   删除输入几何体的点，边，面，并且补洞   
	Divide   平滑多变形，清理多变形，如修正凹形，把n边形转成三角或四边面，三角化非平面面   
	Dop Network         Generators包含动力学模拟的DOP网络入口.     
	Dop Transform   有两种操作模式。根据一个DOP物体的transform去变换所有输入几何体，或者变换输入几何体上单独的小面组，通过用同样的名字匹配DOP物体   
	Duplicate   copy 输入几何元素的子集,并对copy体作变换（不同于copy op,速度更快）
	Edge Collapse   把边和面塌陷到他们的中心   
	Edge Cusp   边锐化，合并点,重新计算法线   
	Edge Divide   边细分，在边插入点   
	Edge Flip   把边换连到不同的顶点上.   
	Edit   编辑修改几何体的点，边，面.   
	Ends   闭合，打开，和夹切几何元素端点.   
	Extrude   沿法线方向挤出.   
	Facet 磨光面   控制物体表面的平滑.整理统一表面的点和法线   
	Fetch  *         Generators通过拷贝其他物体的transform来获得它的transform.这使得从一个子网络里的物体获得transform变得容易，并            把它作为在object层级的一个物体的父。
	File   读入模型，从外部或内部的op   
	Fillet   在两条曲线或表面的相交处建立平滑的过渡几何小面,不改变原始表面   
	Fit   拟和一串点的曲线.拟和一面网格点的样条表面   
	Font   创建字体.   
	Force Particle 用 metaball 来吸引和排斥粒子和弹簧   
	Fractal   创建分形   
	Fuse   根据距离阀值合并点(消除重合的点)   
	Geometry         Generators模型的容器.建模的开始     
	Grid   网格表面   
	Group   生成点组或元面组   
	Group Copy   组copy ,copy元面或点组   
	Group Transfer   传递组   
	Handle             Filters IK手柄,用于操纵骨骼.
	Hole   对一个合并后的模型做洞.   
	Inflate   膨胀变形.   
	Iso Offset   根据输入几何体构建隐函数表面.   
	Iso Surface 等距表面   使用隐函数生成等距曲面   
	Join   把一系列的表面连接成一个元面，但区别于Fillet SOP和Stitch SOP   
	Lattice character 晶格变形.   
	Layer   做分层属性。如多层纹理坐标，甚至是多种坐标系   
	Light             Generators灯光     
	Line   创建直线   
	LOD   根据离摄像机远近构建输入几何体的不同细节，但并不真正改变几何体   
	LSystem   创建分形几何体.   
	Magnet   变形输入几何体，使用一个受metaball场定义的物体   
	Match Topology   匹配拓扑，使一个几何体的元面和点的序号匹配另一个参考几何体   
	Measure   测量几何体的面积，周长，曲率   
	Merge   合并来自不同OP的几何体   
	Metaball   创建 metaballs 和融合超二次曲面.   
	MetaGroups   定义metaball的分组.   
	Microphone         Generators麦克风，为立体声CHOP网指定一个听点(大概是入口点)     
	Mirror   复制和镜像几何体. 
	Muscle             Generators创建平滑的肌肉表面，用于角色蒙皮     
	Muscle   和muscle Objs一同被自动创建   
	Network   无该节点   
	Null             Generators不能渲染的空物体（类似maya里的locator）     
	Null   相当于maya的locator   
	Object Merge   把其他网络的物体合并到当前的SOP网络.   
	Paint   在几何体表面用笔刷绘画颜色或其他属性.   
	Paint Group   修改组里的点的集合    
	Particle   创建并控制粒子的运动。适合大多数情况使用，但是如果你需要构建更为复杂的粒子系统，请使用POPs   
	Partition   根据用户制定的规则把点和元面分组   
	Paste   把一个表面粘到另外一个基础表面上,或直接从基础表面上产生一个表面   
	Peak   沿法线方向平移元面，点，边，端点   
	Platonic Solids   帕拉图实体   
	Point   手动添加和修改点属性.   
	Poly Bevel   对点和边做倒角.用面替换点和边，去除尖锐的点和边   
	Poly Cap   构建多变形的边界边(瞎猜)   
	Poly Extrude   挤出多边形的面和边   
	Poly Knit   接合多边形面。如补洞   
	Poly Loft   通过连接开放或闭合的面上的点来生成三角形mesh(也就是放样和缝合)   
	Poly Patch   用一个mesh元面或一组面(polygons,NURBS,Bezier 曲线)创建一个平滑的polygonal patch   
	Poly Reduce   简化高精度多边形   
	Poly Spline   用样条拟和一条多边形线，可以在原始点之间细分，或忽略原始点把线细分成等长度的段   
	Poly Split   划分多边形，即在多边形面上加线   
	Poly Stitch   缝合多边形   
	Poly Wire   在polygon骨线周围创建polygon管线.   
	POP Merge   将POP网络里的几何体(粒子)装回(显示)到你的场景   
	POP Network   包含一个 POP 网络   
	Primitive   编辑元面.几何变换，仿射变换等等   
	Primitive Split   分离元面   
	Profile   轮廓线操作，你通常需要 Trim SOP,Bridge SOP,或Project SOP之后的Profile SOP.用Trim在一个投影面上剪洞;使用Bridge SOP在两条profile曲线之间放样
	Project   在样条曲面上创建投影线轮廓线 profile curve   
	Rails   在两条轨道线之间生成一串轮廓线   
	Ray   把一个曲面的所有点沿其法线方向贴到另外一个曲面上.(相当于maya里的包裹变形)   
	Refine   增加或简化任意 NURBS, Bezier, or polygonal curve,primitive meshes 或 surface的CV点   
	Resample   把Bezier curves, NURBS curves, circles, 和 polygons重新采样成等长度小段的polygons   
	Rest Position   让第一个变形表面的纹理参考第二个静态表面   
	Reverse   反转和循环所有定点的顺序(没理解)   
	Revolve   创建旋转表面   
	Rivet             Generators在一个表面上粘一个点     
	RMan Shader Material 允许你把不同的 RenderMan shaders 赋予不同的 primitives 组
	Round   在两组曲面之间生成指定半径的圆形过渡表面，方向由两组面的法线方向决定，也可以被自身参数修改
	Sound             Generators音响，为立体声chop网定义一个声音发射点(大概是出口点)     
	Sticky  *         Generators粘性物体从有纹理坐标的多边形表面获得它的transform     
	Subnet             Generators子网.    物体容器     
	Switcher         Filters 摄像机切换     
