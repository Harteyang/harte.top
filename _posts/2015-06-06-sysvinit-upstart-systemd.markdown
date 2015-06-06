---
layout: post
title: "SysVinit / Upstart / Systemd"
date: 2015-06-06 16:00
---

`init` 是Linux内核加载后执行的第一个进程, 是所有程序的父进程. 使用`pstree -lp`可以看到`init(1)`位于数的最顶级.

init常见的有三种程序: [SysVinit](http://en.wikipedia.org/wiki/Init), [Upstart](http://en.wikipedia.org/wiki/Upstart), [Systemd](http://en.wikipedia.org/wiki/Systemd)


## SysVinit ##

SysVinit (System-V style init) 是一个传统的初始化进程.

配置在 `/etc/rcX.d/` (X表示运行级别)下, 比如nginx服务:

	$ ls -l /etc/rc*.d/*nginx
	lrwxrwxrwx 1 root root 15 May 19 13:51 /etc/rc0.d/K20nginx -> ../init.d/nginx
	lrwxrwxrwx 1 root root 15 May 19 13:51 /etc/rc1.d/K20nginx -> ../init.d/nginx
	lrwxrwxrwx 1 root root 15 May 19 13:51 /etc/rc2.d/S20nginx -> ../init.d/nginx
	lrwxrwxrwx 1 root root 15 May 19 13:51 /etc/rc3.d/S20nginx -> ../init.d/nginx
	lrwxrwxrwx 1 root root 15 May 19 13:51 /etc/rc4.d/S20nginx -> ../init.d/nginx
	lrwxrwxrwx 1 root root 15 May 19 13:51 /etc/rc5.d/S20nginx -> ../init.d/nginx
	lrwxrwxrwx 1 root root 15 May 19 13:51 /etc/rc6.d/K20nginx -> ../init.d/nginx

K(Kill)表示关闭, S(Start)表示运行, 数字20表示优先级.

使用`update-rc.d`命令可以管理启动项(TODO 不确定RHEL系默认是否有这个命令, RHEL系有`chkconfig`):

* update-rc.d xxx remove 删除启动项
* update-rc.d xxx enable|disable 开启/关闭 启动项, 必须在有启动项软链接时才可用
* update-rc.d xxx defaults 加入到启动项(默认级别)

另外通过`service`命令来控制SysV服务的启动,停止及状态查看 (service  runs a System V init script or upstart job in as predictable environment as possible).

`service --status-all` 可以查看所有SysVinit和Upstart的服务状态


## Upstart ##

Upstart是基于事件(event-based)的初始化进程. [官方主页](http://upstart.ubuntu.com/)

最开始是给Ubuntu设计的, 后来也被一些其它发行版使用. 不过Ubuntu 和 Debian 也在逐步考虑迁往 systemd.

管理命令是 `initctl`, 显示的是`/etc/init`下的启动配置.

* initctl start xxx
* initctl stop xxx
* initctl status xxx
* initctl list
* initctl show-config xxx 可以查看job的详细配置


	$ initctl show-config ssh
	ssh
	  start on (filesystem or runlevel [2345])
	  stop on runlevel [!2345]

另外 `initctl start` 等可以简写为 `start`, 后者是前者的软链接:

	$ ls -al `which start`
	lrwxrwxrwx 1 root root 7 Mar 12 06:54 /sbin/start -> initctl



## Systemd ##

NULL


## 参考 ##

* [浅析 Linux 初始化 init 系统，第 1 部分: sysvinit](http://www.ibm.com/developerworks/cn/linux/1407_liuming_init1/)
* [浅析 Linux 初始化 init 系统，第 2 部分: UpStart](http://www.ibm.com/developerworks/cn/linux/1407_liuming_init2/index.html)
* [浅析 Linux 初始化 init 系统，第 3 部分: Systemd](http://www.ibm.com/developerworks/cn/linux/1407_liuming_init3/)
* [理解Upstart](http://www.mike.org.cn/articles/understand-upstart/)
* [Linux init系统system V、upstart和systemd](http://www.php101.cn/2014/10/29/Linux-init%E7%B3%BB%E7%BB%9Fsystem-V%E3%80%81upstart%E5%92%8Csystemd/)
* [Linux 的启动流程](http://www.ruanyifeng.com/blog/2013/08/linux_boot_process.html)
