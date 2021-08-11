# blhx_wiki

hoshinobot的碧蓝航线wiki插件

目前主要功能还在开发中，有没有来帮我一手啊啊啊啊啊啊

## 原理

1.调用https://azurapi.github.io/ 的碧蓝航线API返回JSON数据

2.清洗数据并适配进模板html，生成目标html

3.调用imgkit将html转成图片

4.用opencv裁剪图片

5.bot发送图片

## 功能

计划将碧蓝航线wiki的主要功能搬入

### 目前已经实现：

0.帮助信息

命令示范：blhx 帮助

1.根据船名查舰船信息

命令示范： blhx 长门

2.根据船名和皮肤名查询皮肤立绘

blhx 圣路易斯 Luxury_Handle

命令示范：blhx 长门 御狐的辉振袖

命令示范：blhx 长门 原皮

命令示范：blhx 长门 婚纱

3.随机返回游戏加载页面的插画

命令示范：blhx 过场

4.返回bwiki的PVE强度榜信息

命令示范：blhx 强度榜

### 还在规划中：

1.武器装备信息查询

2.再说吧


## 依赖

推荐 Python3.8版本

```pip
pip install azurlane
pip install imgkit
pip install beautifulsoup4
pip install opencv-python
```

这里要注意imgkit框架需要配合工具包，本项目现在的工具包文件夹wkhtmltopdf是Windows环境的，当然工具包也有不同系统的版本，具体迁移请移步https://wkhtmltopdf.org/downloads.html 选择对应系统的工具包

本项的图片资源基本都来源于本地，具体在项目的ship_html/images文件夹里，大小在2.7G左右，项目在https://github.com/AzurAPI/azurapi-js-setup 打包下载，将下载来的项目里的images文件夹放入本项目的ship_html里面

## 使用

自行想办法解决github.io这个域名的封锁，否则墙内的服务器不一定能用

将依赖装好，尤其是资源包要放对位置

克隆项目到hoshinobot的hoshino/modules里

在hoshino/config/__bot__.py对应位置加入blhx_wiki

```
MODULES_ON = {
	'blhx_wiki'
}
```
重启hoshinobot


## 感谢

connfigpython，依样画葫芦赶鸭子上架写的代码。

大佬们凑合看看就行

感谢[LmeSzinc](https://github.com/LmeSzinc)指路

感谢hoshinobot开发群367501912里大佬们的技术支持
