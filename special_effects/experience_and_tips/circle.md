# 关于圆周和球的一些计算和技巧

1.  计算圆周的角度（0-360）
```
vector center = point(1,"P",0);
vector aim = @P-center;
vector up = point(0,"P",0)-center;
vector z= cross(up,(point(0,"P",1)-center));
float angle = acos(dot(up, aim));
int first_half = sign(dot(z, cross(up, aim))) >= 0;
angle = first_half ? angle : 2*PI - angle;

@angle = rint(degrees(angle));
```

