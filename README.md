# blhx_wiki

hoshinobot的碧蓝航线wiki插件

目前主要功能基本完成开发，将逐步新增其他功能。

终于有人来帮我一手了哈哈哈哈哈哈哈哈哈

## 原理

1.调用https://azurapi.github.io/ 的碧蓝航线API返回JSON数据，再调用爬虫获取的[bwiki上的附加JSON数据](https://github.com/jiyemengmei/blhxwiki)

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

命令示范：blhx 圣路易斯 Luxury_Handle

命令示范：blhx 长门 御狐的辉振袖

命令示范：blhx 长门 原皮

命令示范：blhx 长门 婚纱

3.随机返回游戏加载页面的插画

命令示范：blhx 过场

4.返回bwiki的PVE强度榜信息

命令示范：blhx 强度榜

5.启用离线模式(这个功能最大限度为墙内用户考虑，并且最大限度提升反应速度，具体是将api的数据保存到本地调用)

命令示范：blhx 启用离线模式

6.启用在线模式(如果想确保数据时效，且网络性能满足确保可以可靠访问github的文件服务器，可以启用在线模式)

命令示范：blhx 启用在线模式

7.强制更新(需要能稳定访问github文件服务器的网络环境，更新api数据为离线模式所用)

命令示范：blhx 强制更新

### 还在规划中：

1.抽卡

2.攻略

## 依赖

推荐 Python3.8版本

```python
pip install azurlane
pip install imgkit
pip install beautifulsoup4
pip install opencv-python
pip install pypinyin
```

这里要注意imgkit框架需要配合工具包，本项目现在的工具包文件夹wkhtmltopdf是Windows环境的，当然工具包也有不同系统的版本，具体迁移请移步https://wkhtmltopdf.org/downloads.html 选择对应系统的工具包

**本项的图片资源基本都来源于本地，具体在项目的ship_html/images文件夹里，大小在2.7G左右，项目在https://github.com/AzurAPI/azurapi-js-setup 打包下载，将下载来的项目里的images文件夹放入本项目的ship_html里面，这点十分重要，本插件功能90%依赖这个资源包，请自行留意它的更新** 

## 使用

自行想办法解决github文件资源服务器：https://raw.githubusercontent.com/这个域名的封锁，否则墙内的服务器不一定能用（20%），在离线模式下也许能用（80%）

将依赖装好，尤其是资源包要放对位置

克隆项目到hoshinobot的hoshino/modules里

在hoshino/config/**bot**.py对应位置加入blhx_wiki

```
MODULES_ON = {
	'blhx_wiki'
}
```

重启hoshinobot

**注意，离线模式并非完全离线，而是最大限度的不依赖访问外网的能力，以及优化数据读取速度，起码在强制更新命令发布前，您需要保证您的网络可以访问https://raw.githubusercontent.com/**

## 感谢

依样画葫芦赶鸭子上架写的代码。

大佬们凑合看看就行

**感谢[jiyemengmei](https://github.com/jiyemengmei)提供了bwiki的关键数据以及开发过程上的协助**

感谢[LmeSzinc](https://github.com/LmeSzinc)指路

感谢hoshinobot开发群367501912里大佬们的技术支持