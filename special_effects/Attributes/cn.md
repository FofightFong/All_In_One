
### 属性数据类型

要为属性手动指定 VEX 数据类型，请在 @ 符号前添加一个表示该类型的字符。
```
string s@name
int i@name
float f@name
vector2 (2 floats) u@name
vector（3 floats） v@name
vector4（4 floats） p@name
matrix2 (2×2 floats) 2@name
matrix3 (3×3 floats) 3@name
matrix (4×4 floats) 4@name
```
### 全局变量

wangles 中可用的变量列表。不需要类型指示器，但作为提醒包含在内。
```
f@Frame //当前浮动帧数，相当于$FF Hscript变量
f@Time //当前时间以秒为单位，相当于$T Hscript变量 
i@SimFrame //整数模拟时间步数（$SF），只出现在DOP上下文中。
f@SimTime //以秒为单位的模拟时间（$ST），仅存在于DOP上下文中。 
f@TimeInc //当前用于模拟或回放的时间步长。

// 在属性争吵中可用
v@P //当前元素的位置。
i@ptnum //附加到当前处理元素的点号。
i@vtxnum //当前处理顶点的线性数。
i@primnum //附加到当前处理元素的原始编号。
i@elemnum //当前处理元素的索引号。
i@numpt //几何中的总点数。
i@numvtx //当前处理元素的图元中的顶点数。 
i@numprim //几何体中的图元总数。 
i@numelem //正在处理的元素总数。  

// 在 Volume Wrangle 中可用
v@P //当前体素的位置。
f@density //当前体素位置的密度字段值。 
v@center //当前体积的中心。
v@dPdx, v@dPdy, v@dPdz //这些向量存储在 x、y 和 z 体素索引中发生的 P 变化。
i@ix, i@iy, i@iz //体素索引。对于密集卷（非 VDB），这些范围从 0 到分辨率 1。
i@resx, i@resy, i@resz //当前音量的分辨率。
```
### 常用几何属性

常用属性。Houdini 知道将这些转换为适当的 VEX 数据类型。不需要类型指示器，但包括作为提醒。

```
v@P // 点位置。使用它在 3D 空间中布置点。
v@N // 曲面或曲线法线。如果此属性不存在，Houdini 将计算法线。
v@uv // 此点/顶点的 UV 纹理坐标。
v@Cd // 漫反射颜色覆盖。视口使用它来为 OpenGL 几何体着色。
f@pscale // 粒子半径大小。统一比例尺。将显示粒子设置为“光盘”以进行可视化。
v@v // 点速度。以每秒单位数表示的运动方向和速度。
i@id // 始终保持不变的唯一索引号。用于匹配帧之间的元素。
v@rest // 由程序图案和纹理使用以粘贴在变形和动画表面上。
s@name // 标识哪些基元属于哪个部分的唯一名称。也用于标记卷。
v@up // 向上向量。局部空间的向上方向，通常为 (0, 1, 0)。
v@scale // 矢量比例。允许定向缩放或拉伸（在一个方向上）。
p@orient // 点的局部方向（表示为四元数）。
p@rot // 在 orient、N 和 up 属性之后应用额外的旋转。
f@width // 曲线的粗细。在对象节点上启用“Shade Open Curves In Viewport”以进行可视化。
f@Alpha // Alpha 透明度覆盖。视口使用它来设置 OpenGL 几何体的 alpha。
s@instance // 要在渲染时实例化的对象节点的路径。
f@Pw // 样条权重。在这一点上大多贬值。
```

### DOP 粒子属性

粒子系统首先是由属性驱动的。以下是使用的一些属性。
```
f@age // 自粒子诞生以来的时间（以秒为单位）。
f@life // 允许粒子存活的时间（以秒为单位）。当 f@age>f@life 时，i@dead 将被设置为 1。
f@nage // 归一化年龄，f@age 除以 f@life。隐式属性，你不能写这个。
i@dead // 一个粒子是活的 (0) 还是死的 (1)。在收割阶段删除死粒子。
i@id // 粒子的唯一 id，在单个模拟中保持不变。

i@stopped // 粒子是移动 (0) 还是停止 (1)。
i@stuck // 粒子是自由 (0) 还是卡住 (1)。
i@sliding // 粒子是自由的 (0) 还是沿表面滑动 (1)。
f@cling // 施加到向内滑动粒子的力（根据碰撞的表面法线）。
s@pospath // 粒子碰撞的物体的路径。
i@posprim // 路径几何中我们希望引用其位置的哪个碰撞基元。
v@posuv // 碰撞基元上的参数化 uv。

i@hittotal // 粒子所有命中的累积总数（每个时间步仅增加一次）。
i@has_pprevious // 如果 v@pprevious 包含有效值，则设置为 1。
v@pprevious // 存储粒子在上一帧的位置。用于碰撞检测。
i@hitnum // 粒子在上次 POP Collision Detect 中碰撞的次数。
s@hitpath // 命中对象的路径。磁盘上文件的路径或 op: 路径。
i@hitprim // 原始命中。如果碰撞检测器无法确定哪个 prim，则可能为 -1。
v@hituv // 图元上的参数化 UV 空间。
v@hitpos // 命中实际发生的位置。如果碰撞对象正在移动，则很有用。
v@hitnml // 碰撞时表面的法线。
v@hitv // 碰撞时表面的速度。
f@hittime // 碰撞发生时，可能是在一帧内。
f@hitimpulse// 记录碰撞解决需要多少脉冲。随时间步长变化。
f@bounce // 当粒子从另一个物体反弹时，这控制了它们保持多少能量。
f@bounceforward // 控制它们在切线方向上保持多少能量。
f@friction // 当粒子弹跳时，它们的速度与它们撞击的力度成正比。
s@collisionignore // 匹配此模式的对象不会发生碰撞。

f@force // 在此帧的粒子上施加的力。
f@mass // 粒子的惯性。
v@spinshape // 乘以 f@pscale 来确定粒子旋转惯性的形状。
f@drag // 粒子受任何风效果影响的程度。
f@dragexp // 范围从 1 到 2，默认设置在求解器上。用于角度和线性拖动。
v@dragshape // 粒子在其每个局部轴上被拖动的程度。
v@dragcenter// 如果指定，阻力也会在粒子上产生扭矩。
v@targetv // 当地风速。被认为是粒子的目标或目标速度。
f@airresist // 匹配风速有多重要。空气的厚度。
f@speedmin // 粒子可以移动的最小速度，单位为每秒。
f@speedmax // 粒子可以移动的最大速度，单位为每秒。

p@orient // 粒子的方向。用于找出“本地”力量。
v@w // 粒子的角速度。给出旋转轴的向量。
v@torque // 相当于自旋的力。不支持惯性张量（相当于质量）。
v@targetw // 该粒子的目标旋转方向和速度。
f@spinresist//匹配targetw有多重要。
f@spinmin // 粒子可以旋转的每秒弧度的最小速度。
f@spinmax // 粒子可以旋转的每秒弧度的最大速度。
```

### DOP 谷物属性

受 POP Grains 控制的粒子的 ispbd 属性设置为 1。这导致它们不会在 POP 解算器中执行正常的运动更新，因为实际的运动更新是在此节点中完成的。
```
i@ispbd // 值为 1 会使粒子表现为颗粒。
f@pscale // 用于确定每个粒子的半径。
f@repulsionweight // 粒子碰撞力的加权程度。
f@repulsionsstiffness// 粒子之间的距离有多强。较高的值导致较少的弹性排斥。
f@attractionweight // 当靠近时粒子会自然粘在一起的程度。
f@attractionsstiffness // 附近粒子相互粘连的强度。
v@targetP // 粒子被限制在这个位置。
f@targetweight // v@targetP 约束的权重。
f@targetstiffness // 粒子固定到其 v@targetP 属性的刚度。

f@restlength// 多段线连接的粒子将被强制保持这个距离（prim 属性）。
f@constraintweight // 缩放，基于每个粒子的约束力。
f@constraintstiffness // 这可以控制基于每个粒子的刚度。
f@strain // 这个基元属性记录了约束被拉伸了多少。
f@strength // 如果 f@strain 超过了这个原始属性，则约束将被移除。
```
### DOP 打包 RBD 属性

Bullet Solver 使用多个点属性来存储每个打包对象的属性。

```
i@active // 指定对象是否能够对其他对象做出反应。
i@animated // 指定是否应在每个时间步从其 SOP 几何体更新变换。
i@deforming // 指定是否应该在每个时间步从其 SOP 几何体重建碰撞形状。

f@bounce // 物体的弹性。
i@bullet_add_impact // 模拟过程中发生的影响将记录在影响或反馈数据中。
i@bullet_ignore // 指定 Bullet 求解器是否应完全忽略该对象。
f@bullet_angular_sleep_threshold// 对象角速度的休眠阈值。
f@bullet_linear_sleep_threshold // 对象线速度的睡眠阈值。
i@bullet_want_deactivate// 禁用非移动对象的模拟，直到该对象再次移动。 
i@computecom// 指定是否应根据碰撞形状计算质心。
i@computemass // 指定是否应根据碰撞形状和密度计算质量。
f@creationtime // 存储创建对象的模拟时间。
i@dead // 指定在下一次求解期间是否应删除对象。
f@密度 // 一个物体的质量是它的体积乘以它的密度。
f@friction // 物体的摩擦系数。
f@inertialtensorstiffness // 旋转刚度。应用于惯性张量的比例因子。
i@inheritvelocity // SOP 几何中的 v 和 w 点属性将覆盖初始速度。
f@mass // 物体的质量。
s@name // 对象的唯一名称。由约束网络使用。
p@orient// 对象的方向。
v@P // 对象质心的当前位置。
v@pivot // 方向适用的枢轴。如果 i@computecom 非零，则自动计算。
v@v // 物体的线速度。
v@w // 物体的角速度，以弧度每秒为单位。

i@bullet_adjust_geometry // 缩小碰撞几何体。
i@bullet_autofit // 将对象的边界用于 Box、Capsule、Cylinder、Sphere 或 Plane。
f@bullet_collision_margin // 碰撞形状之间的填充距离。
s@bullet_georep // 可以是凸包、凹面、盒、胶囊、圆柱、复合、球体或平面。
i@bullet_groupconnected // 为每组连接的基元创建凸包。
f@bullet_length // Capsule 或 Cylinder 碰撞形状在 Y 方向的长度。
v@bullet_primR // Box、Capsule、Cylinder 或 Plane 碰撞形状的方向。
v@bullet_primS // Box 碰撞形状的大小。
v@bullet_primT // Box、Sphere、Capsule、Cylinder 或 Plane 碰撞形状的位置。
f@bullet_radius // 球体、胶囊或圆柱体碰撞形状的半径。
f@bullet_shrink_amount // 指定收缩碰撞几何完成的大小调整量。

s@activationignore // 不会因与任何匹配此模式的对象发生碰撞而被激活。
s@collisiongroup // 指定该对象所属的碰撞组的名称。
s@collisionignore // 对象不会与任何匹配此模式的对象发生碰撞。
f@min_activation_impulse// 将导致对象从非活动状态切换到活动状态的最小脉冲。

f@speedmin // 粒子可以移动的最小速度，单位为每秒。
f@speedmax // 粒子可以移动的最大速度，单位为每秒。
f@spinmin // 粒子可以旋转的每秒弧度的最小速度。
f@spinmax // 粒子可以旋转的每秒弧度的最大速度。
f@accelmax // 限制由强制约束引起的对象速度变化。
f@angaccelmax // 限制由强制约束引起的对象角速度的变化。

f@airresist // 指定匹配目标速度（v@targetv）的重要性。
f@drag // v@targetv 和 f@airresist 属性对对象的影响程度。
f@dragexp // 范围从 1 到 2，默认设置在求解器上。用于角度和线性拖动。
v@force // 指定将应用于对象质心的力。
f@spinresist// 指定匹配目标角速度（v@targetw）的重要性。
v@targetv // 物体的目标速度。与 f@airresist 属性结合使用。
v@targetw // 对象的目标角速度。与 f@spinresist 属性结合使用。
v@torque // 指定将应用于对象的扭矩。

i@bullet_autofit_valid // 存储求解器是否已经计算了碰撞形状属性。
i@bullet_sleeping // 跟踪对象是否已被求解器置于睡眠状态。
f@deactivation_time // 速度低于线性阈值或角度阈值的时间。
i@found_overlap // 被求解器用来判断是否进行了重叠测试。
i@id // 对象的唯一标识符。
i@nextid// 存储求解器将分配给下一个新对象的 i@id。
```
### DOP 约束网络属性

您可以在几何体上创建属性以自定义每个约束的行为和类型。如果存在与约束属性（例如阻尼）同名的原始属性，则属性值将与约束子数据中的值相乘。

```
s@constraint_name // 通过名称指定一段关系数据，例如'Glue'或'Spring'。
s@constraint_type // 指定约束是否影响“位置”、“旋转”或“所有”自由度。
f@restlength // 指定所需的约束长度。
f@width // 每条边的宽度。
f@density // 每个点的密度。
p@orient// 每个点的初始方向。该值存储为四元数。
v@v // 每个点的初始速度。
v@w // 以每秒弧度为单位测量的每个点的初始角速度。
f@friction // 每个点的摩擦力。
f@klinear // 定义线抵抗拉伸的强度。
f@damplinear// 定义线抵抗拉伸力引起的振荡的强度。
f@kangular // 定义电线抵抗弯曲的强度。
f@dampangular // 定义线抵抗弯曲力引起的振荡的强度。
f@targetstiffness // 定义线抵抗动画位置变形的强度。
f@targetdamping // 定义导线抵抗拉伸力引起的振荡的强度。
f@normaldrag// 线法线方向上的阻力分量。
f@tangentdrag // 与线相切的方向上的阻力分量。
i@nocollide // 禁用边缘碰撞检测（仅在碰撞处理为 SDF 时使用）。
v@restP // 每个点的静止位置。
p@restorient// 每个点的静止方向。
i@gluetoanimation // 使点的位置和方向受输入几何体的约束。
i@pintoanimation // 使点的位置受限于输入几何体。
v@animationP// 每个点的目标位置。
p@animationorient // 每个点的目标方向。
v@animationv// 每个点的目标速度。
v@animationw// 每个点的目标角速度。
i@independentcollisionallowed // 切换外部碰撞（仅限非 SDF 几何碰撞）。
i@independentcollisionresolved // 未解决的外部碰撞（仅限非 SDF 几何碰撞）。
i@codependentcollisionallowed // 切换软体碰撞（仅限非 SDF 几何碰撞）。
i@codependentcollisionresolved // 未解决的切换软体碰撞（仅限非 SDF 几何碰撞）。
i@selfcollisionallowed // 切换自碰撞（仅限非 SDF 几何碰撞）。
i@selfcollisionresolved // 未解决的切换自碰撞（仅限非 SDF 几何碰撞）。
```
### DOP 翻转属性
FLIP 求解器包含一个嵌入式 POP 求解器，因此上面列出的所有 POP 属性都适用。

```
f@pscale// 粒子尺度
v@v // 粒子速度
f@viscosity // 流体的“厚度”。
f@密度 // 每单位体积的质量。
f@temperature // 流体的温度。
f@vorticity // 测量流体中的循环量。
f@divergence// 正值导致粒子散开，负值导致它们聚集在一起。
v@rest // 用于随时间跟踪流体的位置。
v@rest2 // 用于混合双重休息属性，避免拉伸。 
f@droplet // 识别与流体主体分离的粒子。
f@underresolved // 网格上尚未完全解析的粒子。
i@ballistic // 指定流体求解将忽略的粒子。
v@Lx // 角动量 X 轴
v@Ly // 角动量 Y 轴
v@Lz // 角动量 Z 轴
```
### DOP 牛皮纸属性
Vellum 几何体也被视为粒子，因此上面列出的所有 POP 属性都适用。

```
i@isgrain // 值为 1 会使粒子表现为颗粒。区分布料和谷物。
f@attractionweight // 接近时粒子自然粘在一起的程度，零禁用结块。
f@friction // 静摩擦的缩放比例。
f@dynamicfriction // 动态摩擦的缩放比例。
f@inertia // 粒子对旋转头发或线约束的阻力。如果它为零，粒子将不会旋转。
v@v // 点速度。
p@w //（头发或电线）角速度。
p@orient //（头发或电线）方向。
i@stopped // 使用@stopped 而不是@mass 控制引脚（0=自由，1=没有运动，2=没有旋转，3=没有旋转或移动）。
i@pintoanimation // 如果为 1，将更新固定点的位置以匹配目标路径几何体的目标点。
i@gluetoanimation // 如果为 1，则位置和方向都会更新
s@target_path // 任何引脚的目标路径（当在 Vellum Source 中设置了 Target 参数时）
i@target_pt // 任何针脚的目标点编号（当在 Vellum Source 中设置 Target 参数时）
f@targetweight // 使用 0..1 的权重值影响固定点的强度。
i@weld // 将此点焊接到一个点编号。如果有@id 属性，则给一个点id。
i@branchweld // 当它被强制分割点进行头发模拟时，由头发约束构建。
i@collisionweld // 按需生成，为 detangle 算法提供单个焊缝。
f@breakthreshold // 断焊缝和支焊缝的阈值
s@breaktype // 以下之一：'stretchstress'、'bendstress'、'stretchdistance'、'stretchratio' 或 'bendangle'。

// 碰撞
f@pscale // 用于确定布料的厚度或每个粒子的半径。
f@overlap_self // 存储原始 pscale 有多少重叠。
f@overlap_external // 存储原始 pscale 有多少重叠。
i@layer // 点属性，表示属于不同的布料层。更高的数字指的是更高的层。
i@disableself // 值为 0 表示该点将使用自碰撞。
i@disableexternal // 值为 0 表示该点将使用外部碰撞。
s@collisionignore // 存储对象和碰撞组不碰撞的模式。
s@collisiongroup // 给出这个点所属的碰撞组。


// 当一个点是压力约束的一部分时，这些属性保存在约束评估期间计算的值。
v@pressuregradient // 一个沿着最大体积增益方向向外指向的向量。
i[]@volumepts // 包含计算体积属性所需的点数组。
i@volume // 与压力约束的剩余长度进行比较

// 内部工作变量（避免每帧删除/添加属性）
v@pprevious // 对于一阶积分，前一帧的位置（时间步长的开始）。
v@plast // 对于二阶积分，前两帧的位置。
v@vprevious // 对于一阶积分，前一帧速度（时间步长的开始）。
v@vlast // 对于二阶积分，前两帧的速度。
p@orientprevious // 对于一阶积分，前一帧方向（时间步长的开始）。
p@orientlast // 对于二阶积分，提前两帧的方向。
p@wprevious // 对于一阶积分，前一帧的角速度（时间步长的开始）。
p@wlast // 对于二阶积分，两帧之前的角速度。
f@dP // 约束位移。可能是最后一次迭代。
f@dPw // 约束权重。可能是最后一次迭代。
s@patchname // 标识模拟中生成的每个补丁，以便更新/替换。
```
### DOP 牛皮纸约束属性
约束的类型很多，因此这些变量的含义往往取决于约束类型。他们通常过着原始生活。

```
s@type // 约束的类型。
    距离 // 显示几何中的每条边都变成了保持该边长度的距离约束。
    缝合 // 使用距离约束将同一几何体中的点缝合在一起。这些点实际上不需要通过几何连接。这对于保持夹克关闭或防止口袋拍打很有用
    分枝线 // 
    ptprim // 
    弯曲 // 每对三角形（或隐含三角形，如果输入是四边形或更高）创建一个约束，保持三角形之间的初始二面角。
    trianglebend // 每对三角形（或隐含三角形，如果输入是四边形或更高）创建一个约束，保持三角形之间的初始二面角。
    角度
    四倍体
    压力 // 每块，由定义块参数确定，存储其原始体积，并构建多点约束来维持它。执法是全球性的，因此挤压一个地方会扩大另一个地方，就像气球一样。
    贴，别针
    附加正常
    东方
    弯扭
    拉伸剪切
    四纤维
    三合一
    四爪鱼*

f@阻尼比 // 
f@stress // 约束所做工作的估计（由 Vellum 求解器更新）。
```
