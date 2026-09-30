# 计算机网络实验一：静态网页制作

姓名：陈俊强

学号：PB24061348

学校：中国科学技术大学

专业：人工智能

个人主页网址：https://jqchen-another.github.io/PB24061348-network-lab1/

网页的 HTTP 版本号：HTTP/2（h2）

## 网页说明

本网页为静态个人主页，主要包括：

- 个人简介
- 学习方向
- 项目记录
- 校园生活
- 一篇静态博客
- 多张图片
- 至少三个外部超链接

## HTTP 版本检查

检查方法：

```text
Chrome/Edge 开发者工具 -> Network -> Protocol
```

本工程部署后实测结果（2026-09-30，Chrome）：

```text
主页 HTML 请求 Protocol 列：h2
对应协议版本：HTTP/2
```

实测方式与结果：

1. Chrome DevTools Protocol `Network.responseReceived` 事件中，
   主页文档请求的 `response.protocol` 字段为 `h2`。
2. `performance.getEntriesByType("navigation")[0].nextHopProtocol`
   同样返回 `h2`。

两个来源一致，因此确认为 **HTTP/2**。

> 复核方法：用 Chrome / Edge 打开主页，按 `F12` → `Network` →
> 右键表头勾选 `Protocol` → 刷新，确认文档请求显示 `h2`。
