# 拍屏

# 一些经验和技巧

* 1. [外部导入模型清除多余数据技巧](https://www.bilibili.com/video/BV14V411z7Bq/?p=3)-----5'06''

* 2. [group和attribute的正则表达式](https://zhuanlan.zhihu.com/p/80050303)

* 3. [海面由粒子体积转为平面](https://vod1.yiihuu.com/vod/video_mp4/6598/f56875a6f17c109e15d1f4fc9f0171fd-sd-130484.mp4?pid=1572834106552X1465002)----12'

* 4. [小海域拓展无限大海域](https://www.bilibili.com/video/av40309512)----7'

* 5. [布尔运算说明](https://www.bilibili.com/video/av67141329)----1'06''

* 6. [物体中心点$CEX,$CEY,$CEZ](https://www.bilibili.com/video/av67240826)----15'10''

* 7. [读取物体的属性及属性值](https://zhuanlan.zhihu.com/p/79783942)


* 8. [缝合点线](https://www.bilibili.com/video/av71723682)----1'

* 9. [破面模型封口](https://www.bilibili.com/video/av16210606?p=6)----1'10''

* 10. [houdini粒子输出速度通道方法](http://blog.sina.com.cn/s/blog_809e17170102w3vl.html)--[houdini怎么渲染出流体的速度通道](https://blog.csdn.net/liujiufu/article/details/82146206)

* 11. [【Houdini】根据相机距离控制粒子大小](http://blog.sina.com.cn/s/blog_13f902b690102yfdb.html)

* 12. [houdini安装renderman](https://blenderartists.org/t/pixar-renderman-for-blender/646404/615)

# 分类

### 渲染

* 1.提高light的sampling quality能有效减少noise

* 2.提高mantra的pixelsamples的值能有效减少noise。

* 3.提高mantra的min ray samples能提高ray trace的采样值。

* 4.mantra的dicing的shading quality multipler的值是raytrace渲染引擎发射更多的raytrace光线来采样多边形。如果使用micropolgon算法，这个值就是多边形渲染的更加细小。提高这个值，渲染精度就越高，时间越长。

# 数学常用理论和技巧

### [关于圆周和球的一些计算和技巧](https://github.com/FofightFong/All_In_One/blob/master/special_effects/experience_and_tips/circle.md)

1.  可用ray节点计算点到面的距离[dist]()————用法：如积雪厚度,[setdetailattrib(0, 'dist_max', @dist, "max");setdetailattrib(0, 'dist_min', @dist, "min")]()获得最大最小值。

2.  计算碎块大小：   
    *   [f@piece_size = length(getbbox_size(0))](),需要for循环，此方法在一定程度上不是那么准确，但是一个不错的可行性方案
    *   Labs Delete Small Parts节点计算面积

3.  计算粒子密度: [i@point_density =  len(nearpoints(0, @P,chf("dist")))]()，不需要for循环

4.  删除重合的点[i@near = nearpoint(0,@P,0);if(i@near!=@ptnum) removepoint(0,@ptnum)]();

5.  [Houdini 删除相机看不到的点\背面的点或面](https://blog.csdn.net/weixin_44517539/article/details/109468314)-[HIP](https://github.com/FofightFong/All_In_One/blob/master/special_effects/experience_and_tips/camera_scan_v01.hip)


#  建模技巧

[使用sweep建模避免穿插技巧](https://forums.odforce.net/topic/50358-stop-sweep-from-interseting-itself/)
