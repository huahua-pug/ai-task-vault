# -*- coding: utf-8 -*-
"""PPT 生成公共库：深蓝工程风配色、字体与版式助手"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn

# 16:9 画布
SW, SH = 13.3333, 7.5

# ---------- 配色：深蓝工程风 + ANSYS 橙 ----------
NAVY = "0F2B46"      # 深藏青（封面/底色主色）
NAVY2 = "16395C"     # 深色页面卡片
NAVY3 = "1C4166"     # 深色页面网格线
STEEL = "2E6DA4"     # 钢蓝（次级强调）
BLUE = "3E7CB1"      # 亮钢蓝
ICE = "E8F1F8"       # 冰蓝浅底（标签/公式底）
PAGE = "F6F9FC"      # 内容页底色
ORANGE = "E8833A"    # 主强调橙
ORANGE_BG = "FDEFE2" # 橙浅底
INK = "1C2B38"       # 正文深色
MUT = "5C6E7D"       # 弱化灰蓝
LINE = "D8E3EC"      # 细边框
WHITE = "FFFFFF"
DARKTXT = "C9DAE8"   # 深色页面正文
DARKMUT = "7E99AE"   # 深色页面弱化

F = "Microsoft YaHei"
ALIGN = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}
ANCH = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}


def rgb(h):
    return RGBColor.from_string(h)


def est_w(text, size, pad=0.30):
    """按字符宽度估算文本所需英寸宽度（CJK≈1，ASCII≈0.55）"""
    units = sum(1.0 if ord(c) > 0x2000 else 0.55 for c in text)
    return units * size / 72.0 + pad


# ---------- 文本 ----------
def _set_run_font(run, name=F, size=12, bold=False, color=INK, spc=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = rgb(color)
    rPr = run._r.get_or_add_rPr()
    if spc is not None:
        rPr.set("spc", str(int(spc)))
    for tag in ("a:ea", "a:cs"):
        e = rPr.find(qn(tag))
        if e is None:
            e = rPr.makeelement(qn(tag), {})
            rPr.append(e)
        e.set("typeface", name)


def _apply_bullet(p, color=STEEL, char="▪", marL=0.22):
    pPr = p._p.get_or_add_pPr()
    pPr.set("marL", str(int(Inches(marL))))
    pPr.set("indent", "-" + str(int(Inches(marL))))
    buClr = pPr.makeelement(qn("a:buClr"), {})
    srgb = pPr.makeelement(qn("a:srgbClr"), {"val": color})
    buClr.append(srgb)
    buFont = pPr.makeelement(qn("a:buFont"), {"typeface": "Arial"})
    buChar = pPr.makeelement(qn("a:buChar"), {"char": char})
    pPr.append(buClr)
    pPr.append(buFont)
    pPr.append(buChar)


def _fill_tf(tf, paras, anchor="t", align="l", wrap=True):
    tf.word_wrap = wrap
    tf.vertical_anchor = ANCH[anchor]
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        opts = para.get("o", {}) if isinstance(para, dict) else {}
        runs = para["r"] if isinstance(para, dict) else para
        p.alignment = ALIGN[opts.get("align", align)]
        if "sa" in opts:
            p.space_after = Pt(opts["sa"])
        if "sb" in opts:
            p.space_before = Pt(opts["sb"])
        if "line" in opts:
            p.line_spacing = opts["line"]
        if opts.get("bullet"):
            bc = opts["bullet"]
            _apply_bullet(p, color=bc[1] if isinstance(bc, (list, tuple)) else STEEL,
                          char=bc[0] if isinstance(bc, (list, tuple)) else "▪",
                          marL=opts.get("marL", 0.22))
        for run in runs:
            r = p.add_run()
            r.text = run[0]
            _set_run_font(r, size=run[1], bold=(run[2] if len(run) > 2 else False),
                          color=(run[3] if len(run) > 3 else INK),
                          spc=(run[4] if len(run) > 4 else None))


def text(slide, x, y, w, h, paras, anchor="t", align="l", wrap=True):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    _fill_tf(box.text_frame, paras, anchor=anchor, align=align, wrap=wrap)
    return box


def stext(sh, paras, anchor="m", align="l", wrap=True, ml=0.08, mr=0.08, mt=0.02, mb=0.02):
    tf = sh.text_frame
    tf.margin_left, tf.margin_right = Inches(ml), Inches(mr)
    tf.margin_top, tf.margin_bottom = Inches(mt), Inches(mb)
    _fill_tf(tf, paras, anchor=anchor, align=align, wrap=wrap)
    return sh


# ---------- 形状 ----------
def rect(slide, x, y, w, h, fill=WHITE, line_c=None, line_w=1.0, round_=None):
    shp = MSO_SHAPE.ROUNDED_RECTANGLE if round_ is not None else MSO_SHAPE.RECTANGLE
    sh = slide.shapes.add_shape(shp, Inches(x), Inches(y), Inches(w), Inches(h))
    if round_ is not None:
        try:
            sh.adjustments[0] = round_
        except Exception:
            pass
    sh.fill.solid()
    sh.fill.fore_color.rgb = rgb(fill)
    if line_c:
        sh.line.color.rgb = rgb(line_c)
        sh.line.width = Pt(line_w)
    else:
        sh.line.fill.background()
    sh.shadow.inherit = False
    return sh


def fill_alpha(sh, transparency_pct):
    """设置纯色填充透明度，transparency_pct 为透明百分比(0-100)"""
    xClr = sh.fill.fore_color._color._xClr
    a = xClr.makeelement(qn("a:alpha"), {"val": str(int((100 - transparency_pct) * 1000))})
    xClr.append(a)


def card(slide, x, y, w, h, fill=WHITE, line_c=LINE, accent=None, accent_w=0.065):
    sh = rect(slide, x, y, w, h, fill=fill, line_c=line_c, line_w=1.0)
    if accent:
        rect(slide, x, y, accent_w, h, fill=accent, line_c=None)
    return sh


def chip(slide, x, y, w, h, label, fill=ICE, color=STEEL, size=10.5, bold=True, line_c=None):
    sh = rect(slide, x, y, w, h, fill=fill, line_c=line_c, round_=0.5)
    stext(sh, [[(label, size, bold, color)]], anchor="m", align="c", ml=0.04, mr=0.04)
    return sh


def chips_row(slide, x, y, labels, h=0.34, size=10.5, gap=0.14, **kw):
    cx = x
    for lb in labels:
        w = est_w(lb, size)
        chip(slide, cx, y, w, h, lb, size=size, **kw)
        cx += w + gap
    return cx - gap


def numdot(slide, cx, cy, d, n, fill=ICE, color=STEEL, size=12, line_c=None):
    sh = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - d / 2), Inches(cy - d / 2),
                                Inches(d), Inches(d))
    sh.fill.solid()
    sh.fill.fore_color.rgb = rgb(fill)
    if line_c:
        sh.line.color.rgb = rgb(line_c)
        sh.line.width = Pt(1.0)
    else:
        sh.line.fill.background()
    sh.shadow.inherit = False
    stext(sh, [[(str(n), size, True, color)]], anchor="m", align="c", ml=0, mr=0)
    return sh


def dot(slide, cx, cy, d, color=ORANGE):
    sh = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - d / 2), Inches(cy - d / 2),
                                Inches(d), Inches(d))
    sh.fill.solid()
    sh.fill.fore_color.rgb = rgb(color)
    sh.line.fill.background()
    sh.shadow.inherit = False
    return sh


def arrow(slide, cx, cy, w=0.34, h=0.30, color=STEEL):
    sh = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(cx - w / 2), Inches(cy - h / 2),
                                Inches(w), Inches(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = rgb(color)
    sh.line.fill.background()
    sh.shadow.inherit = False
    return sh


def _line(slide, x1, y1, x2, y2, color, weight):
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1),
                                    Inches(x2), Inches(y2))
    ln.line.color.rgb = rgb(color)
    ln.line.width = Pt(weight)
    ln.shadow.inherit = False
    return ln


def mesh(slide, x, y, w, h, step=0.48, color="1C4166", weight=0.75, cells=None):
    """网格（FEA 母题）装饰：横竖线 + 可选高亮单元"""
    n, m = int(round(w / step)), int(round(h / step))
    for i in range(n + 1):
        _line(slide, x + i * step, y, x + i * step, y + m * step, color, weight)
    for j in range(m + 1):
        _line(slide, x, y + j * step, x + n * step, y + j * step, color, weight)
    for c, r, col, al in (cells or []):
        sh = rect(slide, x + c * step + 0.025, y + r * step + 0.025,
                  step - 0.05, step - 0.05, fill=col)
        fill_alpha(sh, al)


# ---------- 页面框架 ----------
def header(slide, tag_text, title_text, page, total=21):
    """内容页页眉：章节标签 + 标题 + 右上角说明 + 右下角页码"""
    w = est_w(tag_text, 11, pad=0.44)
    chip(slide, 0.6, 0.5, w, 0.34, tag_text, fill=NAVY, color=WHITE, size=11)
    text(slide, 0.6, 0.98, 10.6, 0.62, [[(title_text, 26, True, INK)]])
    text(slide, 9.2, 0.56, 3.53, 0.3,
         [[("ANSYS Workbench 有限元学习总结", 10, False, MUT)]], align="r")
    text(slide, 11.53, 7.08, 1.2, 0.28,
         [[("%02d / %d" % (page, total), 10, False, MUT)]], align="r")


def card_title(slide, x, y, title, color=STEEL, size=13.5, w=4.0, dot_color=None):
    """卡片内小标题：色点 + 加粗标题"""
    dot(slide, x + 0.07, y + 0.12, 0.13, color=dot_color or ORANGE)
    text(slide, x + 0.24, y, w, 0.32, [[(title, size, True, color)]])


def label_rows(slide, x, y, w, rows, gap=0.10, lh=None, size=11.5, label_w=0.85,
               label_fill=ICE, label_color=STEEL, text_color=INK, line=1.15):
    """带小标签的行：[标签] 说明文字。rows: [(label, desc), ...]"""
    cy = y
    for lb, desc in rows:
        ltxt = lb
        lw = max(label_w, est_w(ltxt, 10, pad=0.22))
        chip(slide, x, cy, lw, 0.28, ltxt, fill=label_fill, color=label_color, size=10)
        # 说明文字粗略高度：按宽度估算行数
        if lh is None:
            chars_per_line = max(1, int((w - lw - 0.15) / (size / 72.0)))
            import math
            units = sum(1.0 if ord(c) > 0x2000 else 0.55 for c in desc)
            nlines = max(1, math.ceil(units / chars_per_line))
            h = nlines * (size / 72.0) * line + 0.06
        else:
            h = lh
        text(slide, x + lw + 0.15, cy - 0.02, w - lw - 0.15, h,
             [{"r": [(desc, size, False, text_color)], "o": {"line": line}}])
        cy += max(h, 0.28) + gap
    return cy
