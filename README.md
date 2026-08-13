# Licy 的小窝

基于 Astro、GSAP 与 Three.js 的个人博客，部署在 GitHub Pages。

## 本地运行

```bash
pnpm install
pnpm run dev
```

新增文章：在 `src/content/posts/` 新建 Markdown 文件，填写标题、日期、分类和标签。

## 在线写文章

访问 [Pages CMS](https://app.pagescms.org/)，使用 GitHub 登录并选择 `licy2001/licy2001.github.io` 仓库。进入“博客文章”后可新建、编辑或删除文章；保存会自动提交到 GitHub，并触发部署。

## 发布

推送到 `main` 后，GitHub Actions 会自动构建并发布。首次发布前，在仓库 **Settings → Pages → Source** 中选择 **GitHub Actions**。
