# network-lab1

> 中国科学技术大学 · 人工智能专业 · 陈俊强

个人主页的静态站点工程。纯 HTML + CSS + 原生 JavaScript，没有构建步骤，直接部署在 GitHub Pages 上。

## 1. 项目特点

- 纯静态：无第三方框架、无 CDN 依赖、无构建步骤
- 响应式布局：桌面 / 平板 / 手机均可正常浏览
- 支持明暗主题切换，跟随 `prefers-color-scheme`
- 支持移动端导航
- 支持 `prefers-reduced-motion`
- 包含独立博客页面
- 包含多个外部超链接与本地 SVG 图片
- 附带 GitHub Pages 自动部署工作流
- 附带本地静态检查脚本

## 2. 目录结构

```text
network-lab1/
├─ index.html
├─ 404.html
├─ robots.txt
├─ site.webmanifest
├─ blog/
│  └─ index.html
├─ assets/
│  ├─ css/
│  │  └─ main.css
│  ├─ js/
│  │  └─ app.js
│  └─ images/
│     ├─ favicon.svg
│     ├─ hero-ai.svg
│     ├─ campus.svg
│     ├─ project-ranking.svg
│     ├─ project-agent.svg
│     ├─ project-web.svg
│     └─ blog-cover.svg
├─ docs/
│  └─ DEPLOYMENT.md
├─ scripts/
│  └─ validate.py
├─ .github/
│  └─ workflows/
│     └─ pages.yml
├─ .editorconfig
└─ .gitignore
```

## 3. 本地运行

### 方法 A：快速预览首页

直接打开 `index.html` 可以查看首页的静态效果。

页面中的目录链接（如 `blog/`）依赖 Web 服务器解析，这种模式下不一定按预期跳转。

### 方法 B：使用本地 HTTP 服务（推荐）

在工程根目录运行：

```bash
python -m http.server 8000
```

然后浏览器访问：

```text
http://localhost:8000
```

## 4. 本地检查

```bash
python scripts/validate.py
```

正常情况下会输出所有检查项 `PASS`。

## 5. 部署

详细步骤见：

```text
docs/DEPLOYMENT.md
```

本项目已包含 GitHub Pages 的 GitHub Actions 工作流，推送到 `main` 后自动部署。
