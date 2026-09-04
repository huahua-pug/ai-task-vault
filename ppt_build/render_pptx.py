# -*- coding: utf-8 -*-
"""用 PowerPoint/WPS COM 将 pptx 渲染为 PNG（独立实例，不影响已打开的文档）"""
import os
import sys
import win32com.client

src = os.path.abspath(sys.argv[1])
outdir = os.path.abspath(sys.argv[2])
os.makedirs(outdir, exist_ok=True)


def render(app_name, use_dispatch_ex=True):
    maker = win32com.client.DispatchEx if use_dispatch_ex else win32com.client.Dispatch
    app = maker(app_name)
    pres = None
    try:
        pres = app.Presentations.Open(src, True, False, False)  # ReadOnly, Untitled, WithWindow=False
        n = pres.Slides.Count
        for i in range(1, n + 1):
            out = os.path.join(outdir, "slide-%02d.png" % i)
            pres.Slides(i).Export(out, "PNG", 1600, 900)
        print("OK", app_name, "->", n, "slides")
        return True
    finally:
        try:
            if pres is not None:
                pres.Close()
        except Exception:
            pass
        try:
            app.Quit()
        except Exception:
            pass


ok = False
for name in ("PowerPoint.Application", "Kwpp.Application", "wpp.Application"):
    try:
        render(name)
        ok = True
        break
    except Exception as e:
        print("fail:", name, "->", repr(e)[:160])
if not ok:
    sys.exit("no COM presenter available")
