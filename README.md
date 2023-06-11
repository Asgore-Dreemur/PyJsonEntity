# PyJsonEntity

## 简介

PyJsonEntity是一个用于在python中json序列化/反序列化的工具

与原版json不同的是,它对于json与实体类的转换有很好的支持

## 使用方法

PyJsonEntity中有两个静态方法:`JsonToEntity`和`EntityToJson`

`JsonToEntity`把json转换为实体类

参数:

- `jsonstr`:json字符串
- `classobj`:目标类的一个实体,必须有不需要参数的构造方法

`EntityToJson`把实体类转为json

参数:

- `classobj`:要转换的实体类

## 转换规则

- json中的键名对应实体类中的成员名
- 如果初始化类成员为None,则直接用json中对应键名的值进行赋值(json object会被赋值为字典)
- 如果需要套娃(如实体类中使用实体类,json中有json object),则给定类成员赋值为目标类的实例,如:`self.x = Class1()`
- 如果需要处理列表数据,则给定类成员赋值为列表,并给定第一个元素为该列表对应json的类型,如:`self.x = \[Class1()\]`,如果不给定任何元素,则直接赋值
- 当json反序列化时,如果出现json有键但类没有该成员的情况,会直接忽略
- 实体类中的None值会被直接省略
- 如果类成员没有对应的json键,则为初始化的默认值