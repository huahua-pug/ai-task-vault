# -*- coding: utf-8 -*-
"""生成《e1笔记-ANSYS学习总结.pptx》—— 第 1-11 页"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_lib import *
from deck_lib import _line
from pptx import Presentation
from pptx.util import Emu

OUT = r"C:\obsidian\我的仓库\e1笔记-ANSYS学习总结.pptx"

prs = Presentation()
prs.slide_width = Emu(12192000)
prs.slide_height = Emu(6858000)
BLANK = prs.slide_layouts[6]


def new_slide(dark=False):
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = rgb(NAVY if dark else PAGE)
    return s


# ================= S1 封面 =================
s = new_slide(dark=True)
mesh(s, 7.0, 0.75, 5.85, 6.0, step=0.485, color=NAVY3,
     cells=[(4, 3, ORANGE, 30), (9, 8, STEEL, 40), (7, 6, ORANGE, 15), (2, 1, STEEL, 25)])
text(s, 0.9, 2.0, 7.2, 0.4, [[("ANSYS WORKBENCH · 有限元分析学习笔记", 13, True, ORANGE, 300)]])
text(s, 0.88, 2.45, 7.6, 1.0, [[("有限元分析学习总结", 46, True, WHITE)]])
text(s, 0.9, 3.75, 7.0, 1.2, [
    {"r": [("几何建模 · 网格划分 · Mechanical 三阶段 · 线性分析", 14.5, False, DARKTXT)],
     "o": {"line": 1.5, "sa": 4}},
    {"r": [("结构动力学 · 非线性分析 · 热分析 · 疲劳与多物理场", 14.5, False, DARKTXT)],
     "o": {"line": 1.5}},
])
rect(s, 0.9, 6.32, 0.32, 0.055, fill=ORANGE)  # 小色块收尾装饰（非标题下划线，位于页脚元信息左侧）
text(s, 1.32, 6.18, 6.5, 0.35, [[("基于 e1-2 ~ e1-10 课程学习笔记整理 · 2026-09", 11.5, False, DARKMUT)]])

# ================= S2 目录 =================
s = new_slide()
text(s, 0.6, 0.55, 3.0, 0.6, [[("目录", 30, True, INK)]])
text(s, 8.0, 0.78, 4.73, 0.32, [[("ANSYS Workbench 有限元学习总结 · 共 21 页", 11, False, MUT)]], align="r")
toc = [
    ("01", "几何建模", "DM 建模五要点 · SC 定位", "P3"),
    ("02", "网格划分", "五类网格 · 划分方法 · 国标", "P4–5"),
    ("03", "Mechanical", "集成求解器 · 三阶段 · 材料库", "P6–7"),
    ("04", "线性分析", "前提假设 · 静力学与六类动力学", "P8–9"),
    ("05", "结构动力学", "模态·谱·谐响应·屈曲·瞬态", "P10–14"),
    ("06", "非线性分析", "类型·算法·单元控制·大变形", "P15–16"),
    ("07", "热力学分析", "传热方式 · 分析流程 · 耦合", "P17–18"),
    ("08", "疲劳与其他", "疲劳·刚体动力学·LS-DYNA·Fluent", "P19–20"),
]
cw, ch, gx, gy = 2.95, 2.28, 0.113, 0.22
for i, (no, t1, t2, pg) in enumerate(toc):
    x = 0.6 + (i % 4) * (cw + gx)
    y = 1.72 + (i // 4) * (ch + gy)
    card(s, x, y, cw, ch, accent=STEEL if i % 2 == 0 else ORANGE)
    text(s, x + 0.24, y + 0.2, 1.2, 0.42, [[(no, 20, True, ORANGE)]])
    text(s, x + 0.24, y + 0.68, cw - 0.45, 0.4, [[(t1, 15.5, True, INK)]])
    text(s, x + 0.24, y + 1.14, cw - 0.45, 0.62,
         [{"r": [(t2, 10.5, False, MUT)], "o": {"line": 1.25}}])
    chip(s, x + 0.24, y + ch - 0.48, est_w(pg, 9.5, pad=0.26), 0.3, pg,
         fill=ICE, color=STEEL, size=9.5)
text(s, 11.53, 7.08, 1.2, 0.28, [[("02 / 21", 10, False, MUT)]], align="r")

# ================= S3 e1-2 几何建模 =================
s = new_slide()
header(s, "e1-2 · 几何建模", "DesignModeler（DM）与 SpaceClaim（SC）", 3)
rows = [
    ("几何创建", "2D 草图绘制，3D 实体 / 面体 / 线体建模"),
    ("几何导入 / 导出", "支持 STEP、IGES、Parasolid、CATIA 等主流格式"),
    ("建模操作", "拉伸、旋转、扫掠、放样、布尔运算、倒角、抽壳"),
    ("参数化设计", "将尺寸 / 约束设为参数，联动 Workbench 优化模块"),
    ("冻结 / 非冻结", "控制特征是否参与布尔运算，是多体建模的基础"),
]
for i, (t1, t2) in enumerate(rows):
    y = 1.78 + i * 0.99
    card(s, 0.6, y, 7.35, 0.86, accent=STEEL)
    numdot(s, 1.06, y + 0.43, 0.4, i + 1, fill=ICE, color=STEEL, size=12.5)
    text(s, 1.38, y + 0.13, 2.6, 0.3, [[(t1, 13.5, True, INK)]])
    text(s, 1.38, y + 0.46, 6.4, 0.3, [[(t2, 11.5, False, MUT)]])
card(s, 8.2, 1.78, 4.53, 2.6, accent=ORANGE)
text(s, 8.44, 2.02, 4.0, 0.35, [[("SpaceClaim（SC）", 14.5, True, INK)]])
text(s, 8.44, 2.46, 4.06, 0.62,
     [{"r": [("直接建模思路的三维 CAD 系统，建模方式与 DM 不同。", 11.5, False, MUT)],
       "o": {"line": 1.3}}])
text(s, 8.44, 3.18, 4.06, 0.95,
     [{"r": [("本课程以 UG 建模为主，未对 SC 做过多介绍。", 11.5, True, INK)],
       "o": {"line": 1.3}}])
card(s, 8.2, 4.62, 4.53, 2.0, accent=STEEL)
card_title(s, 8.44, 4.84, "本章关键词")
chips_row(s, 8.44, 5.3, ["草图绘制", "实体建模", "布尔运算"], h=0.36, size=10.5)
chips_row(s, 8.44, 5.78, ["参数化", "冻结 / 多体"], h=0.36, size=10.5)
text(s, 8.44, 6.26, 4.06, 0.3, [[("—— 掌握 DM 五大要点即掌握本章主线", 10, False, MUT)]])

# ================= S4 e1-3 网格① =================
s = new_slide()
header(s, "e1-3 · 网格划分", "五类网格与参考标准", 4)
text(s, 0.6, 1.64, 12.1, 0.32, [[("Workbench 针对不同物理场提供相应的网格划分器：", 11.5, False, MUT)]])
types = [
    ("Meshing", "结构与热", "结构及热力学有限元网格（最常用）"),
    ("Electromagnetics", "电磁", "电磁场分析的专用网格"),
    ("CFD", "计算流体动力学", "流体力学分析网格"),
    ("Explicit", "显式动力学", "显式动力学分析网格"),
    ("水动力学", "海洋 / 船舶", "常应用于海洋装备、船舶领域"),
]
cw = 2.32
for i, (en, sub, desc) in enumerate(types):
    x = 0.6 + i * (cw + 0.1325)
    card(s, x, 2.05, cw, 2.45, accent=STEEL)
    text(s, x + 0.2, 2.28, cw - 0.36, 0.62,
         [{"r": [(en, 13.5, True, STEEL)], "o": {"line": 1.1}}])
    text(s, x + 0.2, 2.96, cw - 0.36, 0.3, [[(sub, 10.5, True, ORANGE)]])
    text(s, x + 0.2, 3.34, cw - 0.36, 0.95,
         [{"r": [(desc, 10.5, False, MUT)], "o": {"line": 1.3}}])
card(s, 0.6, 4.85, 12.13, 0.8, fill=ORANGE_BG, line_c=None, accent=ORANGE)
text(s, 0.9, 5.03, 1.6, 0.4, [[("参考标准", 13, True, "B05E1C")]])
text(s, 2.42, 5.05, 10.1, 0.4,
     [[("GB/T 33582-2017 ", 13, True, INK), ("《机械产品结构有限元力学分析通用规则》", 13, False, INK)]])
# 两个迷你网格示意图
gx0, gy0, st = 4.6, 5.98, 0.42
for i in range(4):
    _line(s, gx0 + i * st, gy0, gx0 + i * st, gy0 + 2 * st, STEEL, 1.2)
for j in range(3):
    _line(s, gx0, gy0 + j * st, gx0 + 3 * st, gy0 + j * st, STEEL, 1.2)
text(s, gx0 - 1.55, gy0 + 0.28, 1.4, 0.3, [[("四边形 / 六面体", 10, False, MUT)]], align="r")
tx0 = gx0 + 3 * st + 0.5
for i in range(4):
    _line(s, tx0 + i * st, gy0, tx0 + i * st, gy0 + 2 * st, STEEL, 1.2)
for j in range(3):
    _line(s, tx0, gy0 + j * st, tx0 + 3 * st, gy0 + j * st, STEEL, 1.2)
for j in range(2):
    for i in range(3):
        _line(s, tx0 + i * st, gy0 + j * st, tx0 + (i + 1) * st, gy0 + (j + 1) * st, ORANGE, 1.2)
text(s, tx0 + 3 * st + 0.18, gy0 + 0.28, 1.6, 0.3, [[("三角形 / 四面体", 10, False, MUT)]])

# ================= S5 e1-3 网格② =================
s = new_slide()
header(s, "e1-3 · 网格划分", "网格划分方法", 5)
card(s, 0.6, 1.72, 7.1, 5.0, accent=STEEL)
card_title(s, 0.9, 1.96, "三维划分（五种方法）", size=14.5, w=5.5)
m3 = [
    ("自动网格划分", "默认方法，快速获得整体网格"),
    ("四面体网格划分", "适应性最强，适合任意复杂几何"),
    ("六面体主导网格划分", "尽量生成六面体，过渡区域四面体"),
    ("扫略法", "源面网格沿路径扫略，规则高效"),
    ("多区法", "自动分块，块内结构化划分"),
]
for i, (t1, t2) in enumerate(m3):
    y = 2.48 + i * 0.82
    numdot(s, 1.14, y + 0.3, 0.36, i + 1, fill=ICE, color=STEEL, size=11.5)
    text(s, 1.46, y + 0.02, 3.0, 0.3, [[(t1, 13, True, INK)]])
    text(s, 1.46, y + 0.34, 5.9, 0.3, [[(t2, 11, False, MUT)]])
card(s, 7.95, 1.72, 4.78, 5.0, accent=ORANGE)
card_title(s, 8.22, 1.96, "二维划分（三种方法）", size=14.5, w=4.2)
m2 = ["四边形主导网格划分", "三角形主导网格划分", "四边形 / 三角形主导网格划分"]
for i, t1 in enumerate(m2):
    y = 2.52 + i * 0.56
    dot(s, 8.34, y + 0.14, 0.11, color=ORANGE)
    text(s, 8.5, y, 4.1, 0.32, [[(t1, 12.5, True, INK)]])
card(s, 8.22, 4.42, 4.24, 2.02, fill=ICE, line_c=None)
text(s, 8.46, 4.6, 3.8, 0.3, [[("划分思路", 12, True, STEEL)]])
text(s, 8.46, 4.96, 3.8, 1.4,
     [{"r": [("规则几何优先结构化方法（六面体 / 扫略 / 多区）；复杂几何用四面体或自动划分。", 10.5, False, INK)],
       "o": {"line": 1.35}}])

# ================= S6 e1-4 Mechanical① =================
s = new_slide()
header(s, "e1-4 · Mechanical", "集成式求解器与三阶段流程", 6)
text(s, 0.6, 1.64, 1.5, 0.32, [[("求解能力：", 12, True, INK)]])
chips_row(s, 1.72, 1.6, ["静力学", "动力学", "线性 / 非线性结构", "热力学", "磁场优化"],
          h=0.36, size=11, gap=0.16)
stages = [
    ("STEP 1", "前处理", ["几何模型系统的构建", "材料模型系统的构建", "有限元系统模型的构建"]),
    ("STEP 2", "求解", ["载荷边界条件", "位移边界条件", "求解设定"]),
    ("STEP 3", "后处理", ["结果趋势判定", "结果量级判定", "结果误差分析"]),
]
for i, (step, t1, items) in enumerate(stages):
    x = 0.6 + i * 4.2
    card(s, x, 2.3, 3.72, 3.42, accent=ORANGE if i == 2 else STEEL)
    text(s, x + 0.26, 2.52, 1.5, 0.3, [[(step, 10.5, True, ORANGE, 200)]])
    text(s, x + 0.26, 2.82, 2.8, 0.45, [[(t1, 17, True, INK)]])
    for j, it in enumerate(items):
        y = 3.5 + j * 0.62
        dot(s, x + 0.34, y + 0.11, 0.1, color=STEEL)
        text(s, x + 0.5, y, 3.0, 0.32, [[(it, 12, False, INK)]])
    if i < 2:
        arrow(s, x + 3.72 + 0.24, 4.0, w=0.36, h=0.32)
card(s, 0.6, 6.06, 12.13, 0.72, fill=ICE, line_c=None)
text(s, 0.9, 6.26, 11.6, 0.36,
     [[("三阶段贯穿所有分析类型：", 12, True, STEEL),
       ("几何 → 材料 → 有限元模型 → 边界与求解设定 → 结果校验", 12, False, INK)]])

# ================= S7 e1-4 Mechanical② =================
s = new_slide()
header(s, "e1-4 · Mechanical", "材料库与材料定义", 7)
card(s, 0.6, 1.72, 5.9, 2.4, accent=STEEL)
card_title(s, 0.9, 1.96, "工程数据源", size=14.5, w=4.5)
text(s, 0.9, 2.42, 5.3, 1.5,
     [{"r": [("直接调用内置工程数据（Engineering Data），为各类分析提供材料参数。", 12, False, INK)],
       "o": {"line": 1.4}}])
card(s, 6.83, 1.72, 5.9, 2.4, accent=ORANGE)
card_title(s, 7.13, 1.96, "自定义新材料", size=14.5, w=4.5, dot_color=ORANGE)
text(s, 7.13, 2.42, 5.3, 1.5,
     [{"r": [("可新建材料并定义属性：", 12, False, INK),
             ("各向同性弹性（杨氏模量、泊松比）、比热容等。", 12, True, INK)],
       "o": {"line": 1.4}}])
card(s, 0.6, 4.4, 12.13, 2.42)
card_title(s, 0.9, 4.62, "常用材料参数一览", size=13.5, w=4.5)
props = [
    ("弹性模量 E", "刚度基本量", "决定结构抵抗变形的能力"),
    ("泊松比 ν", "横向变形系数", "横向应变与轴向应变之比"),
    ("密度 ρ", "动力学必需", "模态、重力、惯性计算需要"),
    ("比热容 c", "热分析参数", "瞬态热分析升温计算需要"),
]
for i, (t1, t2, t3) in enumerate(props):
    x = 0.9 + i * 2.95
    text(s, x, 5.06, 2.7, 0.34, [[(t1, 13.5, True, STEEL)]])
    text(s, x, 5.44, 2.7, 0.3, [[(t2, 10.5, True, ORANGE)]])
    text(s, x, 5.78, 2.75, 0.6, [{"r": [(t3, 10.5, False, MUT)], "o": {"line": 1.25}}])
text(s, 0.9, 6.42, 11.6, 0.32,
     [[("模态等动力学分析的材料定义三要素：弹性模量 + 泊松比 + 密度", 11.5, True, INK)]])

# ================= S8 e1-5 线性分析① =================
s = new_slide()
header(s, "e1-5 · 线性分析", "定义、前提与弹性力学假设", 8)
card(s, 0.6, 1.66, 12.13, 0.86, fill=ICE, line_c=None, accent=STEEL)
text(s, 0.95, 1.86, 11.5, 0.5,
     [[("线性分析是最基本、应用最广泛的一类分析：", 13, True, STEEL),
       ("适用于线弹性材料、静态或动态稳定状态加载的工况。", 13, False, INK)]])
card(s, 0.6, 2.78, 5.9, 3.95, accent=STEEL)
card_title(s, 0.9, 3.02, "线性分析前提", size=14.5, w=4.5)
prem = [
    ("材料线性", "应力与应变关系呈线性状态"),
    ("小位移 · 小应变 · 小转动", "几何上处于小变形范围"),
    ("刚度不变", "刚度不随结构变形发生变化"),
]
for i, (t1, t2) in enumerate(prem):
    y = 3.56 + i * 1.02
    numdot(s, 1.14, y + 0.3, 0.36, i + 1, fill=ICE, color=STEEL, size=11.5)
    text(s, 1.46, y + 0.02, 4.8, 0.3, [[(t1, 13, True, INK)]])
    text(s, 1.46, y + 0.36, 4.8, 0.3, [[(t2, 11, False, MUT)]])
card(s, 6.83, 2.78, 5.9, 3.95, accent=ORANGE)
card_title(s, 7.13, 3.02, "弹性力学五大假设", size=14.5, w=4.5, dot_color=ORANGE)
asm = [
    ("连续性", "物质无间隙地充满所在空间"),
    ("线弹性", "应力与应变成正比，卸载可完全恢复"),
    ("均匀性", "各点材料属性相同"),
    ("各向同性", "各方向材料属性相同"),
    ("小变形", "变形远小于结构特征尺寸"),
]
for i, (t1, t2) in enumerate(asm):
    y = 3.52 + i * 0.62
    dot(s, 7.28, y + 0.15, 0.11, color=ORANGE)
    text(s, 7.46, y, 1.3, 0.3, [[(t1, 12.5, True, INK)]])
    text(s, 8.72, y + 0.02, 3.9, 0.3, [[(t2, 10.5, False, MUT)]])

# ================= S9 e1-5 线性分析② =================
s = new_slide()
header(s, "e1-5 · 线性分析", "线性分析内容体系", 9)
card(s, 0.6, 1.72, 8.2, 1.72, accent=STEEL)
card_title(s, 0.9, 1.96, "线性静力学分析", size=14.5, w=4.0)
text(s, 0.9, 2.44, 7.6, 0.72,
     [{"r": [("系统运动速度为 0，分析平衡状态下结构的受力与变形 —— 是最基础的分析类型。", 12, False, INK)],
       "o": {"line": 1.35}}])
rect(s, 9.0, 1.72, 3.73, 1.72, fill=NAVY, line_c=None)
text(s, 9.0, 2.02, 3.73, 0.66, [[("K X = F", 30, True, WHITE)]], align="c")
text(s, 9.0, 2.78, 3.73, 0.3, [[("刚度矩阵 × 位移 = 载荷", 10.5, False, DARKMUT)]], align="c")
text(s, 0.6, 3.72, 8.0, 0.34, [[("线性动力学分析 —— 六种类型", 13.5, True, STEEL)]])
dyn = [
    ("模态分析", "求固有频率与振型"),
    ("谐响应分析", "正弦稳态受迫振动"),
    ("随机振动分析", "PSD 统计响应"),
    ("响应谱分析", "频域峰值响应"),
    ("瞬态动力学", "载荷随时间变化"),
    ("线性屈曲分析", "临界载荷与稳定性"),
]
for i, (t1, t2) in enumerate(dyn):
    x = 0.6 + (i % 3) * 4.095
    y = 4.16 + (i // 3) * 1.32
    card(s, x, y, 3.94, 1.18, accent=ORANGE if i % 2 else STEEL)
    text(s, x + 0.24, y + 0.18, 3.4, 0.32, [[(t1, 13.5, True, INK)]])
    text(s, x + 0.24, y + 0.56, 3.5, 0.3, [[(t2, 10.5, False, MUT)]])

# ================= S10 e1-6 动力学总览 =================
s = new_slide()
header(s, "e1-6 · 结构动力学", "动力学分析总览", 10)
cw2, ch2 = 5.95, 2.45
card(s, 0.6, 1.72, cw2, ch2, accent=STEEL)
card_title(s, 0.9, 1.94, "求解类型", size=13.5, w=4.0)
text(s, 0.9, 2.36, 5.3, 0.34, [[("主要处理载荷随时间变化的动力问题", 11, False, MUT)]])
chips_row(s, 0.9, 2.82, ["瞬态", "冲击", "碰撞"], h=0.44, size=13, gap=0.2)
card(s, 6.78, 1.72, cw2, ch2, accent=STEEL)
card_title(s, 7.08, 1.94, "求解方法", size=13.5, w=4.0)
card(s, 7.08, 2.4, 2.55, 1.5, fill=ICE, line_c=None)
text(s, 7.08, 2.62, 2.55, 0.36, [[("显式动力学", 13, True, STEEL)]], align="c")
text(s, 7.08, 3.06, 2.55, 0.3, [[("高频冲击类", 11, False, INK)]], align="c")
card(s, 9.88, 2.4, 2.55, 1.5, fill=ICE, line_c=None)
text(s, 9.88, 2.62, 2.55, 0.36, [[("隐式动力学", 13, True, STEEL)]], align="c")
text(s, 9.88, 3.06, 2.55, 0.3, [[("低频振动类", 11, False, INK)]], align="c")
dot(s, 9.74, 3.15, 0.28, color=ORANGE)
card(s, 0.6, 4.42, cw2, 2.35, accent=ORANGE)
card_title(s, 0.9, 4.64, "惯性力", size=13.5, w=4.0, dot_color=ORANGE)
text(s, 0.9, 5.08, 5.35, 1.4,
     [{"r": [("动力学问题必须考虑惯性力的影响，", 12, False, INK),
             ("求解时需开启时间积分效应。", 12, True, INK)],
       "o": {"line": 1.4}}])
card(s, 6.78, 4.42, cw2, 2.35, accent=ORANGE)
card_title(s, 7.08, 4.64, "阻尼", size=13.5, w=4.0, dot_color=ORANGE)
text(s, 7.08, 5.02, 5.4, 0.62,
     [{"r": [("作用：常规情况下的能量消散；", 11.5, False, INK),
             ("常见形式：瑞利阻尼（α + β + 阻尼比）", 11.5, True, INK)],
       "o": {"line": 1.3}}])
segs = [("<1", "小阻尼", "F6C489"), ("1–5", "显著阻尼", "F0A05C"),
        ("5–10", "非常显著", "E8833A"), (">10", "大阻尼", "C4651F")]
for i, (v, lb, col) in enumerate(segs):
    x = 7.08 + i * 1.41
    sh = rect(s, x, 5.78, 1.35, 0.52, fill=col, line_c=None)
    stext(sh, [[(v, 11, True, WHITE)], [(lb, 8.5, False, WHITE)]], anchor="m", align="c")

# ================= S11 e1-6 模态分析 =================
s = new_slide()
header(s, "e1-6 · 结构动力学", "模态分析", 11)
card(s, 0.6, 1.72, 6.1, 2.9, accent=STEEL)
card_title(s, 0.9, 1.94, "作用", size=13.5, w=4.0)
acts = [
    "确定结构自身的振动特性：固有频率与振型",
    "振型为无量纲量，可反映结构的相对强弱",
    "改进结构固有频率或工况，避免共振",
    "作为响应谱、随机振动、谐响应等分析的基础",
]
box = text(s, 0.9, 2.4, 5.5, 2.1,
           [{"r": [(a, 12, False, INK)], "o": {"bullet": True, "line": 1.25, "sa": 8}}
            for a in acts])
card(s, 0.6, 4.86, 6.1, 1.94, accent=STEEL)
card_title(s, 0.9, 5.08, "种类", size=13.5, w=4.0)
chips_row(s, 0.9, 5.52, ["自由模态", "约束模态", "有预应力模态"], h=0.4, size=11)
chips_row(s, 0.9, 6.08, ["含接触模态分析"], h=0.4, size=11)
card(s, 6.98, 1.72, 5.75, 2.62, accent=ORANGE)
card_title(s, 7.28, 1.94, "实质", size=13.5, w=4.0, dot_color=ORANGE)
text(s, 7.28, 2.36, 5.2, 0.9,
     [{"r": [("求解方程的特征值 λ（自振圆频率的平方）", 11.5, False, INK)], "o": {"line": 1.3, "sa": 4}},
      {"r": [("与特征向量 v（对应的振型）", 11.5, False, INK)], "o": {"line": 1.3}}])
card(s, 7.28, 3.42, 5.15, 0.72, fill=ICE, line_c=None)
text(s, 7.28, 3.58, 5.15, 0.42, [[("固有频率  f = √λ / 2π", 19, True, NAVY)]], align="c")
card(s, 6.98, 4.58, 5.75, 2.22, accent=ORANGE)
card_title(s, 7.28, 4.8, "关键结论", size=13.5, w=4.0, dot_color=ORANGE)
text(s, 7.28, 5.22, 5.2, 0.62,
     [{"r": [("模态频率仅与结构的", 12, False, INK), ("质量矩阵、刚度矩阵", 12, True, INK),
             ("有关", 12, False, INK)], "o": {"line": 1.3}}])
chips_row(s, 7.28, 5.94, ["弹性模量", "泊松比", "密度"], h=0.4, size=11, gap=0.16)
text(s, 9.5, 6.02, 3.2, 0.3, [[("← 材料定义三要素", 10.5, False, MUT)]])

# ================= S12 e1-6 响应谱与随机振动 =================
s = new_slide()
header(s, "e1-6 · 结构动力学", "响应谱与随机振动", 12)
card(s, 0.6, 1.72, 5.95, 5.08, accent=STEEL)
text(s, 0.9, 1.94, 5.3, 0.36, [[("响应谱分析", 15, True, STEEL)]])
label_rows(s, 0.9, 2.42, 5.35, [
    ("是什么", "利用频域分析技术计算结构的峰值响应"),
    ("输入", "频谱可为位移谱 / 速度谱 / 加速度谱"),
    ("输出", "各阶振型在给定输入下的最大响应，按“响应系数 × 振型”叠加为总体响应"),
    ("作用", "替代瞬态分析快速获取峰值响应，常用于地震响应谱分析"),
    ("技术", "单点谱分析 / 多点谱分析 / 阻尼比"),
    ("注意", "缺失质量效应、缺失刚度响应效应"),
], gap=0.12)
card(s, 6.78, 1.72, 5.95, 5.08, accent=ORANGE)
text(s, 7.08, 1.94, 5.3, 0.36, [[("随机振动分析", 15, True, ORANGE)]])
label_rows(s, 7.08, 2.42, 5.35, [
    ("是什么", "谱分析技术的特定情况 —— 功率谱密度（PSD）分析"),
    ("输入", "功率谱密度函数 PSD：随机载荷时间历程的统计响应"),
    ("输出", "响应的概率统计结果"),
    ("场景", "汽车路谱平整度、火箭发射等载荷不确定工况"),
    ("怎么做", "分析流程与响应谱技术类似"),
], gap=0.16)

# ================= S13 e1-6 谐响应分析 =================
s = new_slide()
header(s, "e1-6 · 结构动力学", "谐响应分析", 13)
chip(s, 4.15, 1.08, 3.3, 0.36, "频率响应分析 / 扫频分析", fill=ICE, color=STEEL, size=10.5)
card(s, 0.6, 1.72, 5.95, 2.62, accent=STEEL)
card_title(s, 0.9, 1.94, "是什么 · 作用", size=13.5, w=4.0)
text(s, 0.9, 2.38, 5.4, 1.2,
     [{"r": [("时域计算 + 稳态受迫振动；确定结构在已知幅值与频率的正弦荷载下的稳态响应，及偏心质量旋转产生的离心力。", 11.5, False, INK)],
       "o": {"line": 1.35}}])
card(s, 0.9, 3.68, 5.35, 0.5, fill=ICE, line_c=None)
text(s, 0.9, 3.8, 5.35, 0.32, [[("m·a + c·v + k·x = f(t) ,  f = H·cos(ωt + φ)", 12.5, True, NAVY)]], align="c")
card(s, 6.78, 1.72, 5.95, 2.62, accent=ORANGE)
card_title(s, 7.08, 1.94, "结果表达形式", size=13.5, w=4.0, dot_color=ORANGE)
text(s, 7.08, 2.38, 5.4, 0.66,
     [{"r": [("方式一　幅值 + 相位角：", 11.5, True, INK)],
       "o": {"sa": 2, "line": 1.25}},
      {"r": [("响应 = 幅值·e^(iφ)，φ = arctan(虚部 / 实部)", 11.5, False, MUT)], "o": {"line": 1.25}}])
text(s, 7.08, 3.18, 5.4, 0.66,
     [{"r": [("方式二　实部 + 虚部：", 11.5, True, INK)],
       "o": {"sa": 2, "line": 1.25}},
      {"r": [("响应 = 实部 + i·虚部", 11.5, False, MUT)], "o": {"line": 1.25}}])
text(s, 7.08, 3.9, 5.4, 0.3, [[("输出随频率变化的幅值 / 相位曲线", 10.5, False, MUT)]])
card(s, 0.6, 4.58, 12.13, 2.22)
card_title(s, 0.9, 4.8, "频带划分", size=13.5, w=4.0)
bands = [
    ("1 倍频程", ["f2 = 2·f1", "中心频率 fc = √(f1·f2)", "f1 = fc/√2 ，f2 = fc·√2"]),
    ("1/2 频带", ["f2 = 2^(1/2)·f1 ≈ 1.41·f1"]),
    ("1/3 频带", ["f2 = 2^(1/3)·f1 ≈ 1.26·f1"]),
]
for i, (t1, lines) in enumerate(bands):
    x = 0.9 + i * 4.02
    text(s, x, 5.24, 3.6, 0.32, [[(t1, 13, True, STEEL)]])
    paras = [{"r": [(ln, 11.5, False, INK)], "o": {"line": 1.35, "sa": 3}} for ln in lines]
    text(s, x, 5.64, 3.75, 1.05, paras)

# ================= S14 e1-6 屈曲与瞬态 =================
s = new_slide()
header(s, "e1-6 · 结构动力学", "线性屈曲与瞬态动力学", 14)
card(s, 0.6, 1.72, 5.95, 5.08, accent=STEEL)
text(s, 0.9, 1.94, 5.3, 0.36, [[("线性屈曲分析", 15, True, STEEL)]])
label_rows(s, 0.9, 2.44, 5.35, [
    ("是什么", "结构在垂直轴向荷载下，因微小扰动出现系统崩溃 —— 即结构的稳定性计算"),
    ("作用", "确定临界载荷；相较非线性屈曲，可作为产品初始研发的评估指导手段"),
    ("常用对象", "细长杆、真空类零件"),
    ("怎么做", "需给定预应力条件（先施加预应力再求解特征值）"),
], gap=0.18)
card(s, 6.78, 1.72, 5.95, 5.08, accent=ORANGE)
text(s, 7.08, 1.94, 5.3, 0.36, [[("瞬态动力学分析", 15, True, ORANGE)]])
label_rows(s, 7.08, 2.44, 5.35, [
    ("是什么", "载荷随时间变化的动力学分析"),
    ("作用", "确定任意时刻载荷作用下结构的受力状态（位移、应力、应变）"),
    ("怎么做", "通过时间步（时间步长）控制求解过程"),
    ("关联", "惯性力相关 —— 求解需开启时间积分效应"),
], gap=0.22)

# ================= S15 e1-7 非线性① =================
s = new_slide()
header(s, "e1-7 · 非线性分析", "非线性行为、类型与求解算法", 15)
card(s, 0.6, 1.66, 12.13, 0.8, fill=ICE, line_c=None, accent=STEEL)
text(s, 0.95, 1.85, 11.5, 0.45,
     [[("非线性本质：", 13, True, STEEL),
       ("载荷引起结构刚度发生变化 —— 线性问题中刚度矩阵 [k] 保持不变", 13, False, INK)]])
nl = [
    ("几何非线性", "结构产生大变形，导致结构发生明显变化（细长杆、长薄板）"),
    ("材料非线性", "金属的弹塑性；橡胶材料的超弹性"),
    ("状态非线性", "接触；生死单元"),
]
for i, (t1, t2) in enumerate(nl):
    x = 0.6 + i * 4.095
    card(s, x, 2.66, 3.94, 1.95, accent=ORANGE)
    text(s, x + 0.24, 2.9, 3.4, 0.36, [[(t1, 14.5, True, INK)]])
    text(s, x + 0.24, 3.36, 3.5, 1.05, [{"r": [(t2, 11, False, MUT)], "o": {"line": 1.35}}])
card(s, 0.6, 4.88, 5.95, 1.9, accent=STEEL)
card_title(s, 0.9, 5.1, "求解算法", size=13.5, w=4.0)
text(s, 0.9, 5.52, 5.4, 1.1,
     [{"r": [("牛顿-拉夫逊迭代法 · 多次平衡迭代 · 迭代步的收敛", 12, False, INK)], "o": {"line": 1.4}}])
card(s, 6.78, 4.88, 5.95, 1.9, accent=ORANGE)
card_title(s, 7.08, 5.1, "关键认识", size=13.5, w=4.0, dot_color=ORANGE)
text(s, 7.08, 5.52, 5.4, 1.1,
     [{"r": [("收敛主要靠载荷步 / 子步控制；兼顾计算效率与精度；", 11.5, False, INK),
             ("结果收敛 ≠ 结果正确", 11.5, True, "C4651F")], "o": {"line": 1.35}}])

# ================= S16 e1-7 非线性② =================
s = new_slide()
header(s, "e1-7 · 非线性分析", "单元控制与大变形分析", 16)
card(s, 0.6, 1.72, 5.95, 2.52, accent=STEEL)
card_title(s, 0.9, 1.94, "单元类型控制", size=13.5, w=4.0)
label_rows(s, 0.9, 2.4, 5.35, [
    ("隐式求解", "高阶单元 —— 适用于弯曲主导问题"),
    ("显式求解", "低阶单元 —— 注意剪切锁定、体积锁定"),
], gap=0.2)
card(s, 0.6, 4.44, 5.95, 0.96, accent=STEEL)
card_title(s, 0.9, 4.62, "单元求解控制", size=13, w=2.2)
chips_row(s, 3.1, 4.68, ["完全积分", "缩减积分"], h=0.42, size=11.5, gap=0.18)
text(s, 0.9, 5.08, 5.4, 0.28, [[("—— 不同的积分方案影响求解精度与沙漏控制", 10, False, MUT)]])
card(s, 6.78, 1.72, 5.95, 3.68, accent=ORANGE)
card_title(s, 7.08, 1.94, "大变形分析", size=13.5, w=4.0, dot_color=ORANGE)
card(s, 7.08, 2.36, 5.35, 0.62, fill=ORANGE_BG, line_c=None)
text(s, 7.28, 2.52, 5.0, 0.36,
     [[("经验罚则：横向位移超过厚度 10% 时应启用大变形", 12, True, "B05E1C")]])
label_rows(s, 7.08, 3.14, 5.35, [
    ("作用", "考虑大变形 / 大转动 / 大应变引起的单元形状与方向变化导致的刚度改变"),
    ("代价", "结果更精确，但需迭代求解、可能分步加载，计算时间长"),
    ("其他场景", "系统存在失稳时；使用超弹性材料时"),
], gap=0.12)
card(s, 0.6, 5.6, 12.13, 1.2)
card_title(s, 0.9, 5.76, "主要链接关系", size=13, w=3.0)
chips_row(s, 3.7, 5.74, ["布尔运算", "共节点", "运动副", "接触", "刚性耦合"], h=0.36, size=10.5, gap=0.14)
chips_row(s, 3.7, 6.22, ["柔性耦合", "梁 / 杆", "CP", "CE"], h=0.36, size=10.5, gap=0.14)

# ================= S17 e1-8 热力学① =================
s = new_slide()
header(s, "e1-8 · 热力学分析", "概念、作用与分析种类", 17)
card(s, 0.6, 1.72, 5.95, 2.1, accent=STEEL)
card_title(s, 0.9, 1.94, "是什么", size=13.5, w=4.0)
text(s, 0.9, 2.38, 5.4, 1.2,
     [{"r": [("研究宏观物质与冷热有关的物理性质及其变化规律的学科。", 12.5, False, INK)],
       "o": {"line": 1.4}}])
card(s, 6.78, 1.72, 5.95, 2.1, accent=ORANGE)
card_title(s, 7.08, 1.94, "作用", size=13.5, w=4.0, dot_color=ORANGE)
text(s, 7.08, 2.36, 5.4, 1.35,
     [{"r": [("石油化工、核动力、制动器、压力容器的温度应力", 11.5, False, INK)],
       "o": {"bullet": True, "line": 1.3, "sa": 5}},
      {"r": [("系统暂态过程中产生的瞬态温度应力", 11.5, False, INK)],
       "o": {"bullet": True, "line": 1.3}}])
text(s, 0.6, 4.02, 6.0, 0.34, [[("热学分析种类", 13.5, True, STEEL)]])
kinds = [
    ("稳态热分析", "温度场不随时间变化"),
    ("瞬态热分析", "温度场随时间变化"),
    ("热结构间接耦合", "先热后结构，顺序求解"),
    ("热结构直接耦合", "热-结构同时求解"),
]
for i, (t1, t2) in enumerate(kinds):
    x = 0.6 + i * 3.095
    card(s, x, 4.44, 2.94, 1.32, accent=STEEL if i < 2 else ORANGE)
    text(s, x + 0.2, 4.66, 2.6, 0.56, [{"r": [(t1, 12.5, True, INK)], "o": {"line": 1.15}}])
    text(s, x + 0.2, 5.24, 2.65, 0.45, [{"r": [(t2, 10, False, MUT)], "o": {"line": 1.2}}])
card(s, 0.6, 6.0, 12.13, 0.82)
text(s, 0.95, 6.14, 3.6, 0.5, [[("瞬态热力学一般方程", 12, True, STEEL)]])
text(s, 4.4, 6.14, 4.3, 0.5, [[("[C]·d{T}/dt + [K]·{T} = {Q}", 17, True, NAVY)]])
text(s, 8.9, 6.2, 3.8, 0.55,
     [{"r": [("[C] 比热矩阵 · [K] 传导矩阵", 9.5, False, MUT)], "o": {"line": 1.3}},
      {"r": [("{T} 节点温度向量 · {Q} 热载荷向量", 9.5, False, MUT)], "o": {"line": 1.3}}])

# ================= S18 e1-8 热力学② =================
s = new_slide()
header(s, "e1-8 · 热力学分析", "三大传热方式与分析流程", 18)
ht = [
    ("热传导", "物体内部或系统内各部分存在温度差引起的热量传递"),
    ("热对流", "温度不同的流体之间的传热：高温附近空气膨胀 → 密度差 → 自然对流 / 强迫对流"),
    ("热辐射", "物体发射电磁能进行热量交换；真空中更显著；黑体辐射为理想基准；工程常考虑 2 个及以上物体的辐射 —— 高度非线性"),
]
for i, (t1, t2) in enumerate(ht):
    x = 0.6 + i * 4.095
    card(s, x, 1.72, 3.94, 2.55, accent=ORANGE if i == 2 else STEEL)
    numdot(s, x + 0.44, 2.14, 0.44, i + 1, fill=ICE, color=STEEL, size=13)
    text(s, x + 0.78, 1.98, 2.6, 0.36, [[(t1, 14.5, True, INK)]])
    text(s, x + 0.24, 2.56, 3.5, 1.6, [{"r": [(t2, 11, False, MUT)], "o": {"line": 1.35}}])
text(s, 0.6, 4.5, 8.0, 0.34, [[("热力学分析流程 —— 三大步三小步", 13.5, True, STEEL)]])
flow = [
    ("前处理", ["几何模型的构建", "材料模型的构建", "有限元系统的构建"]),
    ("求解", ["产热条件的定义", "散热条件的定义", "求解设定"]),
    ("后处理", ["结果趋势的判定", "结果量级的判定", "结果误差分析"]),
]
for i, (t1, items) in enumerate(flow):
    x = 0.6 + i * 4.2
    card(s, x, 4.94, 3.72, 1.78, accent=ORANGE if i == 2 else STEEL)
    text(s, x + 0.24, 5.1, 2.4, 0.34, [[(t1, 13.5, True, INK)]])
    for j, it in enumerate(items):
        y = 5.5 + j * 0.4
        dot(s, x + 0.32, y + 0.1, 0.09, color=STEEL)
        text(s, x + 0.46, y, 3.1, 0.3, [[(it, 11, False, INK)]])
    if i < 2:
        arrow(s, x + 3.72 + 0.24, 5.8, w=0.34, h=0.3)

# ================= S19 e1-10 疲劳分析 =================
s = new_slide()
header(s, "e1-10 · 疲劳与其他", "疲劳分析", 19)
card(s, 0.6, 1.72, 4.35, 5.08, accent=ORANGE)
text(s, 0.9, 1.98, 3.8, 0.95, [[("80%", 52, True, ORANGE)]])
text(s, 0.9, 2.98, 3.8, 0.6,
     [{"r": [("机械设备的损坏源于疲劳失效", 12, True, INK)], "o": {"line": 1.3}},
      {"r": [("—— 疲劳是产品失效的主要根源", 10, False, MUT)], "o": {"line": 1.3}}])
card_title(s, 0.9, 3.92, "是什么", size=13, w=3.0)
text(s, 0.9, 4.3, 3.8, 1.05,
     [{"r": [("评估材料或结构在重复荷载 / 循环应力作用下发生失效风险的方法。", 11, False, INK)],
       "o": {"line": 1.35}}])
card_title(s, 0.9, 5.42, "分类", size=13, w=2.0)
chips_row(s, 0.9, 5.78, ["高周疲劳（应力疲劳）"], h=0.38, size=10)
chips_row(s, 0.9, 6.28, ["低周疲劳（应变疲劳）"], h=0.38, size=10)
card(s, 5.18, 1.72, 7.55, 2.4, accent=STEEL)
card_title(s, 5.48, 1.94, "如何做 —— Workbench 疲劳工具（高周疲劳）", size=13.5, w=6.5)
label_rows(s, 5.48, 2.4, 7.0, [
    ("载荷", "恒定振幅载荷；成比例载荷 / 非比例载荷"),
    ("曲线", "应力-寿命（S-N）曲线 / 应变-寿命曲线"),
], gap=0.16)
card(s, 5.18, 4.32, 7.55, 1.7, accent=STEEL)
card_title(s, 5.48, 4.5, "S-N 曲线相关", size=13, w=3.0)
text(s, 5.48, 4.86, 7.0, 0.56,
     [{"r": [("试件疲劳测试所得结果；弯曲或轴向测试反映单轴应力状态；平均应力状态影响疲劳寿命。", 11, False, INK)],
       "o": {"line": 1.3}}])
chips_row(s, 5.48, 5.5, ["延展性", "加工工艺", "表面粗糙度", "残余应力", "载荷环境"], h=0.34, size=9.5)
card(s, 5.18, 6.22, 7.55, 0.58, fill=ICE, line_c=None)
text(s, 5.48, 6.36, 7.1, 0.32,
     [[("前提：线性静力分析（非线性问题慎用） · 接触用 bonded + no separation 保持状态不变", 10.5, True, STEEL)]])

# ================= S20 e1-10 刚体动力学 / LS-DYNA / Fluent =================
s = new_slide()
header(s, "e1-10 · 疲劳与其他", "刚体动力学 · LS-DYNA · Fluent 流体力学", 20)
cols = [
    ("刚体动力学", STEEL, [
        ("用途", "模拟各类运动机械及含弹簧系统的运动，各运动副的运动累积"),
        ("输入 / 输出", "力、力矩、位移、速度、加速度"),
        ("特点", "阻尼可通过弹簧考虑；无应力应变结果"),
        ("实现", "显式求解法；材料仅需密度；几何用壳体、面体、实体"),
    ]),
    ("LS-DYNA", ORANGE, [
        ("定位", "通用的非线性动力学分析软件"),
        ("能力", "求解爆炸、高速碰撞、金属成型等高度非线性动力学冲击问题"),
        ("延伸", "还可求解传热、流体、振动等多场耦合问题"),
    ]),
    ("Fluent 流体力学", STEEL, [
        ("定位", "CFD：对流体力学各类问题进行数值实验、计算机模拟与分析"),
        ("方法", "有限差分 FDM / 有限元 FEM / 有限体积 FVM"),
        ("模型", "定常与非定常、层流与湍流、可压与不可压流动、传热、化学反应等"),
    ]),
]
for i, (t1, ac, rows) in enumerate(cols):
    x = 0.6 + i * 4.095
    card(s, x, 1.72, 3.94, 5.08, accent=ac)
    text(s, x + 0.24, 1.94, 3.5, 0.4, [[(t1, 15, True, ac if ac != ORANGE else "C4651F")]])
    label_rows(s, x + 0.24, 2.5, 3.5, rows, gap=0.18, label_w=0.95, size=10.5)

# ================= S21 总结（深色收尾） =================
s = new_slide(dark=True)
mesh(s, 9.9, 4.9, 2.85, 2.0, step=0.475, color=NAVY3, cells=[(1, 1, ORANGE, 25), (4, 2, STEEL, 30)])
text(s, 0.6, 0.6, 8.0, 0.7, [[("有限元知识体系全景", 34, True, WHITE)]])
text(s, 8.9, 0.82, 3.83, 0.32, [[("ANSYS Workbench 学习总结 · 21 页", 10.5, False, DARKMUT)]], align="r")
path = ["几何建模", "网格划分", "Mechanical", "线性分析", "结构动力学", "非线性", "热力学", "疲劳·多场"]
cw3 = 1.28
x0 = (13.3333 - (8 * cw3 + 7 * 0.26)) / 2
for i, t1 in enumerate(path):
    x = x0 + i * (cw3 + 0.26)
    sh = rect(s, x, 1.85, cw3, 0.52, fill=NAVY2, line_c="2A5578", line_w=1.0, round_=0.28)
    stext(sh, [[(t1, 11, True, DARKTXT)]], anchor="m", align="c", ml=0.02, mr=0.02)
    if i < 7:
        arrow(s, x + cw3 + 0.13, 2.11, w=0.2, h=0.2, color=STEEL)
takes = [
    ("分析主线", "前处理（几何 / 材料 / 有限元模型）→ 求解（载荷与位移边界、求解设定）→ 后处理（趋势 · 量级 · 误差）"),
    ("选型逻辑", "先判断问题类型 —— 线性或非线性、静力或动力学、单场或耦合场，再选择分析类型与求解算法"),
    ("结果心法", "收敛 ≠ 正确；从结果趋势、量级、误差三重校验，兼顾计算效率与计算精度"),
]
for i, (t1, t2) in enumerate(takes):
    x = 0.6 + i * 4.095
    card(s, x, 3.05, 3.94, 2.6, fill=NAVY2, line_c="2A5578", accent=ORANGE, accent_w=0.07)
    text(s, x + 0.28, 3.35, 3.3, 0.4, [[(t1, 15.5, True, ORANGE)]])
    text(s, x + 0.28, 3.88, 3.42, 1.6, [{"r": [(t2, 11.5, False, DARKTXT)], "o": {"line": 1.45}}])
rect(s, 0.9, 6.35, 0.32, 0.055, fill=ORANGE)
text(s, 1.32, 6.2, 8.0, 0.35, [[("基于 e1-2 ~ e1-10 课程学习笔记整理 · 2026-09", 11.5, False, DARKMUT)]])
text(s, 11.53, 7.08, 1.2, 0.28, [[("21 / 21", 10, False, DARKMUT)]], align="r")

# ================= 保存 =================
prs.core_properties.title = "ANSYS Workbench 有限元分析学习总结"
prs.core_properties.author = "AI 整理"
prs.save(OUT)
print("saved:", OUT)
print("slides:", len(prs.slides.__iter__.__self__._sldIdLst))
