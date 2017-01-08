
#开源的Django项目
##BootCamp
[一个开源的社区网站BootCamp](https://github.com/vitorfs/bootcamp)

*需要安装数据库postgresql

[MacOs下图形化安装](http://postgresapp.com)

*国内使用需要做如下修改

base.html:

1.google的js

	<!--
		<script src="{% static 'js/ga.js' %}"></script>
	-->

2.更换jquery

	<script src="http://apps.bdimg.com/libs/jquery/1.6.4/jquery.min.js"></script>

3.static/css/bootcamp.css中修改字体库url，改成360的CDN

	@import url(http://fonts.useso.com/css?family=Audiowide);