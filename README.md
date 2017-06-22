# api
php+python写的一款天气爬虫

## 运行说明
1. iptables不可关闭，开放相应的端口
2. 确保selinux关闭 `setenforce 0`
3. 运行`python php_python.py`
4. 如果有镜像，跳过5
5. 在docker目录编译生成镜像 `docker build -t xzjs/xf . `
6. 运行镜像并映射端口以及音频保存文件`docker run -p 8080:8080 -t -v /var/www/html/api/audio:/audio xzjs/xf`