# 注意的项

* 1. RBD Material Fracture节点基于材质破碎（更高层级的封装节点）对木头，玻璃和混泥土三大类材质进行破碎设置。

* 2. Houdini调用以前版本的节点-----[打开textport输入opadd -e "相应节点名"](https://blog.csdn.net/A13155283231/article/details/89151158)

* 3. Houdini高亮显示VEX创建的组----[i@group_sel = @primnum % 2 ==0](http://blog.sina.com.cn/s/blog_b11f872e0102xbr7.html)


# 常用变量

* 1. [sin($F)](),F即Frame,表示按当前帧数进行正弦运算,生成的是正弦曲线,可做小球跳动动画(无衰减,想想怎么做有衰减的动画?);

* 2. [sin($PT)](),PT是指当前处理点的序号,表示根据当前点的序号进行正弦运算(T是否有"当前"的含义,即time?);

* 3. [$T](),T即time,当前时间,注意H中24帧=1S,所以在N帧的时候,对应的是N*(1/24);
