---
layout: post
title: "Linux Increase Partition Space"
date: 2014-01-12 15:19
comments: true
categories: Linux
---

<!-- more -->

对于做了lvm的分区，扩容比较方便。

非lvm分区，如果想保证在数据不丢失的情况下扩容，如果是 `ext2` / `ext3` / `ext4` 的格式，保证 **分区的起始位置不变** 的情况下，只改变结束位置，就可以通过 `resize2fs` 进行扩容/缩容。

一般的情况下是先unmount掉需要扩容的分区(通过 `lsof` 查看有哪些进程在使用指定分区)，当然，针对 `ext3` / `ext4` 的分区，在 `Linux Kernel 2.6` 已经支持了在线扩容（NOTE: on-line resize只支持扩容，不支持缩容）。(man resize2fs)

扩容主要的步骤:

1.修改分区表结束位置:

使用 `fdisk` / `parted` 先删除掉原来的分区，然后重新新建分区，保证分区的起始位置不变，只增大结束的位置。

2.`partprobe` 通知操作系统内核分区表有改动，重读分区表。

3.`e2fsck` 检查分区，保证没问题:

	e2fsck -f /dev/sdb1

4.`resize2fs` 扩容:

	resize2fs /dev/sdb1

5.最后重新挂载上去, `df -lTh` 确认下.




