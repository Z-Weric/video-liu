#!/usr/bin/env python3
"""
二维码生成脚本（独立工具，不修改网站）
用法: python generate_qr.py <URL>
示例: python generate_qr.py https://用户名.github.io/my-videos/

生成的 qr_code.png 可以印名片、发朋友圈、放社交媒体简介，
别人扫码即打开你的视频网站。
"""

import sys
import os

def generate_qr(url: str, output_path: str = "qr_code.png"):
    try:
        import qrcode
    except ImportError:
        print("正在安装 qrcode 库...")
        os.system(f"{sys.executable} -m pip install qrcode[pil]")
        import qrcode

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#2d1b2e", back_color="#fff9f5")
    img.save(output_path)
    print(f"二维码已生成: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        url = input("请输入网站公开链接 (如 https://用户名.github.io/my-videos/): ").strip()
    else:
        url = sys.argv[1]

    if not url:
        print("错误: 请提供有效的 URL")
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(script_dir, "qr_code.png")
    generate_qr(url, output)
    print(f"\n完成!")
    print(f"  二维码图片: {output}")
    print(f"  指向链接: {url}")
    print("把这张图发到任何地方，别人扫码就能打开你的视频网站。")
