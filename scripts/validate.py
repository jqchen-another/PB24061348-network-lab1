from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

checks = []

def check(name, condition, detail=""):
    checks.append((name, bool(condition), detail))

index = (ROOT / "index.html").read_text(encoding="utf-8")
blog = (ROOT / "blog" / "index.html").read_text(encoding="utf-8")
css = (ROOT / "assets" / "css" / "main.css").read_text(encoding="utf-8")
js = (ROOT / "assets" / "js" / "app.js").read_text(encoding="utf-8")

check("index.html exists", (ROOT / "index.html").exists())
check("blog page exists", (ROOT / "blog" / "index.html").exists())
check("CSS exists", (ROOT / "assets" / "css" / "main.css").exists())
check("JavaScript exists", (ROOT / "assets" / "js" / "app.js").exists())

external_links = re.findall(r'href="https://', index)
check("at least 3 external hyperlinks", len(external_links) >= 3, f"found={len(external_links)}")

img_tags = re.findall(r"<img\b", index + blog)
check("contains images", len(img_tags) >= 3, f"img_tags={len(img_tags)}")

svg_count = len(list((ROOT / "assets" / "images").glob("*.svg")))
check("local image assets", svg_count >= 3, f"svg_files={svg_count}")

# 公开页面上只展示姓名与学校/专业，学号不对外显示
required_identity = ["陈俊强", "中国科学技术大学", "人工智能"]
check("identity information", all(x in index for x in required_identity))

check("responsive CSS", "@media" in css)
check("dark mode", "body.dark" in css and "localStorage" in js)
check("GitHub Pages workflow", (ROOT / ".github" / "workflows" / "pages.yml").exists())
check("deployment guide", (ROOT / "docs" / "DEPLOYMENT.md").exists())

failed = 0
for name, ok, detail in checks:
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" ({detail})" if detail else ""))
    if not ok:
        failed += 1

print(f"\nSummary: {len(checks)-failed}/{len(checks)} checks passed.")
sys.exit(1 if failed else 0)
