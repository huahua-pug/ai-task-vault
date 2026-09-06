# AI任务主输出文档

## 子任务1 · 解析论文主题与检索策略 · 2026-09-06

**论文主题要素**（源自《SSF体系固化软土试验研究》结果与讨论章节）：
- 固化对象：软土（高含水率），评价指标为 7d/28d 无侧限抗压强度（UCS）
- 固化体系：钢渣-矿渣-粉煤灰（SSF）三元全固废前驱体 + 电石渣-碱渣双碱激发剂（非水泥的碱激发/类地聚物路线，产物 C-S-H/C-A-S-H 凝胶 + 钙矾石调控）
- 设计变量：前驱体配比（1:1:1 最优）、激发剂掺量（24%）与配比（1:1）、固化剂总掺量（14%，"V型谷"）、初始含水率（35%）
- 耐久性：硫酸盐侵蚀（石膏分解+钙矾石膨胀双通道劣化）、冻融循环（粉煤灰界面薄弱区累积损伤）
- 微观表征：XRD（非晶弥散峰）、SEM（絮状/网状凝胶、针状钙矾石、板状 Ca(OH)2）、EDS（Si/Al=1.87、Ca/Si=0.83）

**英文检索关键词**：alkali-activated / geopolymer；stabilized / solidified soft soil、dredged sediment；steel slag、GGBS (ground granulated blast furnace slag)、fly ash；carbide slag (calcium carbide residue)、soda residue / alkali residue；unconfined compressive strength；sulfate attack、freeze-thaw；microstructure、C-(A)-S-H、ettringite；waste-based / low-carbon binder

**筛选口径**：
- 一区 = 中科院分区大类 1 区（以 2023 升级版为参考，Top 期刊标注）
- 近三年 = 2023-09 ~ 2026-09 发表（优先 2024–2026）
- 非开源 = Unpaywall is_oa=false（需机构订阅，排除金色/绿色 OA 与预印本）；无法核实时以出版社官网订阅标识为准
- 每篇记录：标题 / 作者 / 期刊 / 年份 / 中科院分区 / DOI / 核心研究内容 / 与本文关联 / 开源状态

**目标期刊池（与主题相关的一区）**：
- Construction and Building Materials（1区Top，本主题主战场）
- Cement and Concrete Research（1区Top）、Cement and Concrete Composites（1区）
- Journal of Cleaner Production（1区Top）、Resources, Conservation and Recycling（1区）
- Engineering Geology（1区）、Computers and Geotechnics（1区）、Acta Geotechnica（1区）、Géotechnique（1区）
- Journal of Rock Mechanics and Geotechnical Engineering（1区）
- Science of the Total Environment（1区）、Journal of Hazardous Materials（1区）
- Journal of Building Engineering（分区待核实）
- 备用（待核实，若非一区则弃用）：Transportation Geotechnics、Soils and Foundations、Canadian Geotechnical Journal、Applied Clay Science、Waste Management

**批次分工**：批次A=碱激发矿渣/粉煤灰/钢渣固化软土与力学性能；批次B=固废活化剂（电石渣/碱渣/石灰基）与微观机理；批次C=耐久性（硫酸盐/冻融）与低碳全固废固化。每批检索约 12 篇备选、验证后保留 10 篇，最终汇总 30 篇制表（xlsx + Markdown）。

**遗留说明**：旧任务「e1笔记PPT总结」已归档（archive/2026-09-06-e1笔记PPT总结.md），正式 PPT 已覆盖至 C:\obsidian\我的仓库\e1笔记-ANSYS学习总结.pptx。工作区待删除暂存文件夹中 6 个被 Mimosa 标记为高危的废弃调试脚本已删除（内容已留档会话记录），清理报告中的其余待删项仍等用户审核。

## 子任务2 · 检索批次A：碱激发矿渣/粉煤灰/钢渣固化软土与力学性能 · 2026-09-06

检索与核验：Crossref API 6 组主题查询（限 2023-09 之后发表、一区期刊白名单过滤）得 23 篇候选 → Unpaywall 逐篇核验，剔除 3 篇 OA（hybrid/gold）与 2 篇非一区期刊（Bulletin of Engineering Geology and the Environment）→ 保留 10 篇，全部 is_oa=false（closed，需机构订阅）。

| # | 标题 | 第一作者 | 期刊·年·卷·文章号 | 分区 | DOI | 核心内容 | 与本文关联 | 开源 |
|---|------|---------|------------------|------|-----|----------|-----------|------|
| A1 | Stabilized/solidified chlorine saline soils with ground granulated blast furnace slag and calcium carbide residue | Wang Huixian | Constr Build Mater · 2024 · 449 · 138490 | 1区Top | 10.1016/j.conbuildmat.2024.138490 | 矿渣+电石渣固化氯盐渍土的强度与固化机理 | 同用"矿渣+电石渣"钙基激发体系，盐渍土环境对照 | 非开源 |
| A2 | Use of gasification fly ash, sodium carbonate, and ground granulated blast-furnace slag for soft clay stabilization | Qin Junde | Constr Build Mater · 2024 · 426 · 136072 | 1区Top | 10.1016/j.conbuildmat.2024.136072 | 气化飞灰+碳酸钠+矿渣固化软土的强度与配比优化 | 多固废前驱体+碳酸盐激发，与SSF多固废思路一致 | 非开源 |
| A3 | Investigation on strength properties of phosphogypsum-dredged soil stabilized by carbide slag activated ground granulated blast-furnace slag | Xi Lei | Constr Build Mater · 2024 · 457 · 139427 | 1区Top | 10.1016/j.conbuildmat.2024.139427 | 电石渣激发矿渣固化磷石膏-疏浚土强度特性 | 电石渣激发矿渣+固废复合改良疏浚土，双钙源思路同本文 | 非开源 |
| A4 | Strength and microscopic properties of S95 GGBS-calcium carbide slag-phosphogypsum carbonation and standard-cured waste soil | Ma Wene | Constr Build Mater · 2025 · 465 · 140167 | 1区Top | 10.1016/j.conbuildmat.2025.140167 | 矿渣-电石渣-磷石膏固化土在碳化/标养下的强度与微观 | 同为矿渣-电石渣基全固废固化剂，微观表征可对照 | 非开源 |
| A5 | Hydraulic and strength characteristics of chloride saline soil improved with carbide slag and ground granulated blast furnace slag | Xu Xing | Constr Build Mater · 2025 · 492 · 142971 | 1区Top | 10.1016/j.conbuildmat.2025.142971 | 电石渣+矿渣改良氯盐渍土的水力与强度特性 | 电石渣-矿渣配比设计与强度/渗透协同评价 | 非开源 |
| A6 | Mechanical properties of phosphogypsum-soil stabilized by lime activated ground granulated blast-furnace slag | Zheng Pangkun | Constr Build Mater · 2023 · 402 · 132994 | 1区Top | 10.1016/j.conbuildmat.2023.132994 | 石灰激发矿渣固化磷石膏-土的力学性能 | 钙质激发剂活化矿渣固化土的力学基线数据 | 非开源 |
| A7 | Mechanical and microstructural properties of cemented marine dredged clay with pre-hydrated ground granulated blast furnace slag | Zhang Sai | Constr Build Mater · 2023 · 404 · 133162 | 1区Top | 10.1016/j.conbuildmat.2023.133162 | 预水化矿渣改性水泥固化海相疏浚土的力学与微观 | 矿渣改性胶凝体系固化疏浚土，XRD/SEM机理对照 | 非开源 |
| A8 | Strength, stiffness, and microstructure of marine soft clay stabilized by ground granulated blast-furnace slag and bio enzyme | Shi Zhouhuan | Engineering Geology · 2025 · 357 · 108361 | 1区 | 10.1016/j.enggeo.2025.108361 | 矿渣+生物酶固化海相软土的强度、刚度与微观结构 | 海相软土+矿渣固化的强度-微观关联印证 | 非开源 |
| A9 | Effect of granite powder on the strength, durability and sustainability of soil treated using steel slag or cement | Nakayenga Joyce | Constr Build Mater · 2024 · 451 · 138793 | 1区Top | 10.1016/j.conbuildmat.2024.138793 | 花岗岩粉对钢渣/水泥固化土强度、耐久性与可持续性的影响 | 钢渣基固化土强度与耐久性评价 | 非开源 |
| A10 | Gel ice packs as a sustainable additive for geopolymer-stabilized soft clay | Yoon Boyoung | Acta Geotechnica · 2026 · 在线 | 1区 | 10.1007/s11440-026-03011-8 | 凝胶冰袋作为养护介质对地聚物固化软土的调控 | 地聚物固化软土的养护/添加剂新思路 | 非开源 |

备选池（后续批次有缺口时启用）：Yao Q. 2024 CCB 138242（XGBoost预测固废-水泥固化黏土UCS，closed）；Zhang S. 2023 JOBE 107351（GGBS疏浚淤泥CLSM，closed，JOBE分区待核实）；Shaji S. 2024 CCB 137460（蛋壳石灰+稻壳灰固化软土，closed）。

**累计：10/30 篇。**
