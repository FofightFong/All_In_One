## 项目要求：

  1.  海面要自然：

    a.  海豚要顺风而游，即海浪的方向和海豚游的方向要保持一致。（Ocean Spectrum节点控制海浪方向）。
    b.  海浪的噪波要自然。（使用工具架上的Large Ocean可得较满意的效果）。
    c.  海豚游过的地方也应有泡沫（Ocean Foam节点region参数选择Grid，且受海豚位置影响）。
    
  2.  灯光（光影）要自然：

    a.  海豚是往东游的，即逆光游（存在阴影关系）
    
  3.  海豚要有湿漉漉的效果（wet texture）:
  
## 项目流程：

  1.  外部文件导入：
    
    a.  一般建议使用fbx文件，可以附带贴图动画信息
    
  2.  导入文件预处理：
    
    a.  破面封口。
    b.  删除多余属性。
    
  3.  实际操作

  4.  解算
  
    a.水花层，guidedoceanlayer_fluid中使用blast节点将guidedoceanlayer层分离出来供后续渲染。
    
    b.白水


  5.  渲染

    a.  分层渲染
    
    b.  分通道输出渲染
  
  5.  合成



# 走不通的路，就用拳头把它打开

* 碰撞不太理想，使用体积组范围限定--体积使用box加物体本身脱尾
* [【Houdini】根据相机距离控制粒子大小](http://blog.sina.com.cn/s/blog_13f902b690102yfdb.html)

    
