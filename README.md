# blhx_wiki

hoshinobot的碧蓝航线wiki插件

目前主要功能基本完成开发，将逐步新增其他功能。

终于有人来帮我一手了哈哈哈哈哈哈哈哈哈

## 更新
### 2021-09-22
**昵称匹配功能使用前必须发送 blhx 强制更新**

1.允许使用舰船模糊昵称搜索

2.允许用户使用 blhx备注 舰船正式名称 昵称 为舰船自定义昵称，并通过昵称查询

3.查询返回的信息新增舰船的备注

4.舰船皮肤快捷查询

命令看下文的命令示范

### 2021-08-26
1.优化数据适配，当bwiki数据更新延迟时，读取API数据(优点是可以获取比较新的舰船数据，缺点是没有汉化和部分bwiki特有信息)

### 2021-08-23
1.异步读写文件进一步优化性能

2.正式移除在线模式（太过鸡肋），以及在线/离线模式的切换，现在一律使用离线模式。

## 原理(Winodows系统优先）

1.调用https://azurapi.github.io/ 的碧蓝航线API返回JSON数据，再调用爬虫获取的[bwiki上的附加JSON数据](https://github.com/jiyemengmei/blhxwiki)

2.清洗数据并适配进模板html，生成目标html

3.调用imgkit将html转成图片

4.用opencv裁剪图片

5.bot发送图片

## 功能

计划将碧蓝航线wiki的主要功能搬入

首次运行请按以下教程准备资源文件

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

7.强制更新(目前已使用代理更新api数据为离线模式所用，如果出问题及时issue)

命令示范：blhx 强制更新

8.获取最新活动信息(有问题及时issue)

命令示范：blhx 最新活动

9.为舰船取昵称(以后你就可以用昵称查询了)

命令示范：blhx备注 光辉 太太

以后就可以用 blhx 太太 婚纱 这种昵称取代正式名称查询

10.删除舰船昵称

命令示范：blhx移除备注 光辉 太太

11.舰船昵称快捷查询

命令示范：blhx皮肤 光辉 0

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
pip install aiofiles
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

**首次使用请 发送“blhx 强制更新”来获取最新api数据，以后的api数据更新全部以该命令实现**

**注意，离线模式并非完全离线，而是最大限度的不依赖访问外网的能力，以及优化数据读取速度，起码在强制更新命令发布前，您需要保证您的网络可以接通，目前已将https://raw.githubusercontent.com/替换为https://raw.fastgit.org/进一步降低了国内用户离线强制更新的网络要求**

**关于更新：你们可以手动更新这些资源文件，如果你能提取到立绘，则可以手动添加到对应文件夹，总体来说，皮肤和小人立绘在skins文件夹对应的舰船编号里而半身立绘则是存在Texture2D里面，用拼音命名(代码里识别的是通过船名调用pinyin将汉字转中文，所以如果你加了半身立绘发现读不出来，你可能遇到多音字了比如朝潮，通常我们读作zhaochao，而pinyin则会将它转为chaochao。这点请注意)**

## 感谢

依样画葫芦赶鸭子上架写的代码。

大佬们凑合看看就行

**感谢[jiyemengmei](https://github.com/jiyemengmei)提供了bwiki的关键数据以及开发过程上的协助**

**感谢[Mythe51](https://github.com/Mythe51)加入开发组以及为一些重要模块提供帮助**

感谢[LmeSzinc](https://github.com/LmeSzinc)指路

**感谢hoshinobot开发群367501912里大佬们的技术支持**