# 刘晓菊 - 视频作品展示页

## 文件结构

```
portfolio/
├── index.html       # 视频展示主页面
├── generate_qr.py   # 二维码生成脚本
├── README.md        # 本说明文件
└── assets/          # （自行创建）放本地视频文件
```

## 如何替换视频

打开 `index.html`，搜索 `VIDEO_URL_1`、`VIDEO_URL_2` ... `VIDEO_URL_6`，替换为：

| 视频来源 | 替换示例 |
|----------|----------|
| **B站** | `https://www.bilibili.com/video/BV1xxx` |
| **YouTube** | `https://youtu.be/xxxxx` |
| **抖音** | 将视频下载后放本地，用 `assets/douyin01.mp4` |
| **本地文件** | 视频/图片放进 `assets/` 文件夹，链接写 `assets/video01.mp4` |

同时修改 `video-meta` 下方的标题和浏览量数据。

如需增减视频卡片，复制或删除一个 `<div class="video-card">...</div>` 块即可。

## 部署到 GitHub Pages

### 1. 创建仓库
- 登录 [GitHub](https://github.com) → **New repository**
- 仓库名：`my-videos`（或任意）
- 选 **Public** → **Create repository**

### 2. 上传文件
- 点击 **uploading an existing file**
- 把 `portfolio/` 里的所有文件拖进去
- **Commit changes**

### 3. 开启 Pages
- **Settings** → **Pages**
- Source 选 **Deploy from a branch**
- Branch 选 `main` / `(root)` → **Save**
- 1-2 分钟后获得链接：`https://你的用户名.github.io/my-videos/`

### 4. 生成二维码
```bash
python generate_qr.py "https://你的用户名.github.io/my-videos/"
```
脚本会生成 `qr_code.png` 并自动更新 `index.html` 中的二维码区域。

## 本地预览
浏览器直接打开 `index.html`。
