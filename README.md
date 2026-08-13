# Licy 的小窝

基于 Astro、GSAP 与 Three.js 的个人博客，部署在 GitHub Pages。

## 本地运行

```bash
pnpm install
pnpm run dev
```

新增文章：在 `src/content/posts/` 新建 Markdown 文件，填写标题、日期、分类和标签。

## 发布

推送到 `main` 后，GitHub Actions 会自动构建并发布。首次发布前，在仓库 **Settings → Pages → Source** 中选择 **GitHub Actions**。
