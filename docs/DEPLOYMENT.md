# 部署与 HTTP 协议版本检查

## 一、GitHub Pages 部署

### 方案 A：使用自动部署工作流（推荐）

1. 登录 GitHub，新建公开仓库。
2. 将本工程全部文件推送到仓库。
3. 打开仓库的：

```text
Settings -> Pages
```

4. 在 **Build and deployment** 中选择：

```text
Source: GitHub Actions
```

5. 推送代码后，仓库中的 `.github/workflows/pages.yml` 会自动执行部署。
6. 部署完成后，GitHub Pages 会给出公开网址，形如：

```text
https://<你的GitHub用户名>.github.io/<仓库名>/
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

也可以直接在 `Console` 里执行：

```js
performance.getEntriesByType('navigation')[0].nextHopProtocol
```

两个来源结果应当一致；以浏览器实际显示的结果为准。
