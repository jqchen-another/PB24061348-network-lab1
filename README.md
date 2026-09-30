# PB24061348-陈俊强-计网实验一

> 中国科学技术大学 · 人工智能专业  
> 学生：陈俊强  
> 学号：PB24061348

这是“计算机网络实验一：静态网页制作”的完整工程。

## 1. 项目特点

- 纯静态工程：HTML + CSS + 少量原生 JavaScript
- 无第三方框架、无 CDN 依赖、无构建步骤
- 响应式布局：桌面 / 平板 / 手机均可正常浏览
- 支持明暗主题
- 支持移动端导航
- 支持 `prefers-reduced-motion`
- 包含独立博客页面
- 包含至少 3 个外部超链接
- 包含多张本地图片（SVG）
- 附带 GitHub Pages 自动部署工作流
- 附带本地静态检查脚本
- 附带实验提交模板与 HTTP 协议版本检查说明

## 2. 目录结构

```text
PB24061348-陈俊强-计网实验一/
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
│  ├─ DEPLOYMENT.md
│  ├─ SUBMISSION_TEMPLATE.md
│  └─ REQUIREMENTS_TRACEABILITY.md
├─ scripts/
│  └─ validate.py
├─ .github/
│  └─ workflows/
│     └─ pages.yml
├─ .editorconfig
└─ .gitignore
```

## 3. 本地运行

### 方法 A：直接打开

双击 `index.html` 即可。

### 方法 B：推荐，使用本地 HTTP 服务

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

本项目已包含 GitHub Pages 的 GitHub Actions 工作流。

## 6. 实验提交

最终提交文件中需要填写：

- 姓名：陈俊强
- 学号：PB24061348
- 个人主页网址：部署后填写
- 网页 HTTP 版本号：部署后检查填写

模板见：

```text
docs/SUBMISSION_TEMPLATE.md
```
