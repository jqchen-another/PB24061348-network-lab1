# 部署与 HTTP 协议版本检查

## 一、推荐方案：GitHub Pages

### 方案 A：使用自动部署工作流

1. 登录 GitHub。
2. 新建公开仓库，例如：

```text
PB24061348-network-lab1
```

3. 将本工程全部文件上传到仓库。
4. 打开仓库：

```text
Settings -> Pages
```

5. 在 **Build and deployment** 中选择：

```text
Source: GitHub Actions
```

6. 推送代码后，仓库中的 `.github/workflows/pages.yml` 会自动执行部署。
7. 部署完成后，GitHub Pages 会给出公开网址。

如果仓库名是：

```text
PB24061348-network-lab1
```

网址通常类似：

```text
https://你的GitHub用户名.github.io/PB24061348-network-lab1/
```

### 方案 B：从 main 分支直接部署

也可以在：

```text
Settings -> Pages
```

选择：

```text
Deploy from a branch
```

然后选择：

```text
main / (root)
```

---

## 二、检查网页实际使用的 HTTP 版本

不要在部署前提前填写协议版本。

推荐使用 Chrome / Edge：

1. 打开已经部署好的网页。
2. 按 `F12` 打开开发者工具。
3. 切换到 `Network` 面板。
4. 刷新网页。
5. 在请求列表的表头上右键。
6. 勾选 `Protocol` 列。
7. 找到主页 HTML 请求。
8. 记录该请求显示的协议。

常见值：

- `h2`：HTTP/2
- `h3`：HTTP/3
- `http/1.1`：HTTP/1.1

**必须以你部署后浏览器实际显示的结果为准。**

---

## 三、建议截图

为了实验报告更完整，建议保留两张截图：

1. 已部署网页首页截图。
2. DevTools `Network` 面板中带有 `Protocol` 列的截图。

---

## 四、最终提交信息

最终 PDF / DOC / DOCX 中填写：

```text
姓名：陈俊强
学号：PB24061348
个人主页网址：https://jqchen-another.github.io/PB24061348-network-lab1/
网页的 HTTP 版本号：HTTP/2（h2）
```

> 本工程已于 2026-09-30 完成部署，上述两项为实测填写值。
> 个人主页仓库：https://github.com/jqchen-another/PB24061348-network-lab1
