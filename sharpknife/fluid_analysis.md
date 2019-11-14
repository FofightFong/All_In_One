
## 白水解算器中的力场分析

白水粒子的动力学形态受几种机制的控制。


* 由重力（gravity）驱动的加速度均匀地分布在每一个白水粒子上。

* 默认设置下，浮力（[Buoyancy]()）将粒子推向与重力相反的方向，并推动气泡上浮。

* 白水粒子被它们下面的液体流动的速度场驱动。、

* 流体表面散布一些特殊点（repellant）会推动附近的白水粒子，打破泡沫的形态并产生类似细胞的图案。

* 流体的表面张力（surface tension）和附着力（adhesion）会使泡沫黏附到表面，不会使其浸没或分离。可以通过启用“深度控制”（depth control）来模拟这种效果。

* density control控制局部白水粒子分布，防止粒子之间距离太近。此外，这种机制可以产生白水凝聚力（cohesion），它可以抵消分散（dispersion)。

白水粒子解算器面板拥有丰富的ramp曲线。用来精细地控制这些力场。比如，想让液体表面的白水多，而空气中的较稀薄，就可以调节density曲线。

## 白水粒子的生命周期

whitewater source节点中的emission是控制生成白水粒子的参数。

白水解算器控制粒子的生命值和死亡周期。随着解算的进行，白水粒子以普通的方式增加年龄值。不过，粒子没有预设置的寿命值，而是通过分析其当前的状况，动态计算每个粒子的死亡概率。在确定粒子的死亡概率时，会考虑以下因素：

* 年龄（age） – 更老的粒子更容易被杀死。

* 深度（depth） – 随着深度的变化，白水的衰老几率也随着老化率（Aging Rates）的变化而变化。

* 密度（density） – 当启用侵蚀（erosion）时，粒子附近的白水密度也会影响其死亡概率。

高级用户可以通过点属性deathchance来进一步控制粒子生命值。

通常情况下，Lifespan代表白水粒子的平均生命值。

##  Repellants(排斥力）

这是H17白水系统的新特性之一。它们是一些覆盖在流体表面的点。这些点对附近的白水施加排斥力，破坏其结构并形成“光秃的”斑块，形成更大的“细胞状”形态。除了计算和施加这些力之外，解算器还会移动repellants点的位置来使泡沫随着流体运动，并动态增删这些点来控制repellents点的分布。在它们产生时，这些点会被归到一个叫“justborn”的组中。

repellants影响白水的形态受以下这些点属性控制：

* action：当前推动白水粒子的强度值。是repellents强度（magnitude）的系数（两者是相乘关系）。

* magnitude：代表repellant的强度。与action不同的是，这个属性代表永久（或长期）属性，而不是action那种临时的。

* noise：控制repellant的形态。值为0代表正圆（circle），为1代表最大化的扰乱。

* phase：具有相同noise属性的repellants可能形态不同，这就受phase控制。

* pulse：代表phase属性的变化率。随着phase属性的变化，repellant的形状也会发生变化。值为0表示形状是静态的，而远离0的值导致repellant不断演变其形状。

* radius：控制repellant的大小。

默认情况下，repellant没有生命值不会死亡。不过，如果解算器中的Life Range参数开启，它们会在出生时被赋予一个生命值（lifespan）存储到life这个点属性中（同时生成一个age属性）。当age超过了life，repellant就会消亡。

在whitewater object节点上开启相应的参数，可以可视化repellant的系列属性。

repellant还有一个crampedness属性，代表repellant的紧密程度，解算器使用这个属性来reseed白水粒子。该属性的区间是0到1。

除非Density Threshold参数开启，否则repellant不受白水的影响。因此可以通过暂时关闭whitewater发射源来查看repellant的运动形态。


##  whitewater Source(发射源)

水雾和泡沫由此产生，在这里蕴含许多重要的参数来控制白水的数量和分布。

* Whitewater Source节点内的Curvature选项卡控制白浪的产生位置。你可以指定在哪个曲率（curvature）处发射白水以及Max Velocity Angle（最大速度角度）。

* Whitewater Source节点内的Acceleration选项卡控制白水速度的变化。例如，当海浪撞到礁石改变运动方向。

* Whitewater Source节点内的Vorticity选项卡控制水流“打转”的区域，或速度的卷曲。当水被搅动，气泡（bubbles）便会产生。通常用来模拟船只经过或是有物体在水中搅动。





