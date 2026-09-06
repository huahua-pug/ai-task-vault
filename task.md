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

## 子任务3 · 检索批次B：固废活化剂（电石渣/碱渣/赤泥/石灰基）与微观机理 · 2026-09-06

检索与核验：Crossref API 8 组主题查询（限 2023-09 之后、一区期刊白名单）得 27 篇候选 → 剔除批次A已选 7 篇、金色 OA 5 篇（JRMGE 两篇、Soils and Foundations 三篇）、非一区 1 篇 → 保留 10 篇，全部 Unpaywall is_oa=false。氯盐侵蚀一篇（Jia 2026 CCB 146623，closed）留作批次C。

| # | 标题 | 第一作者 | 期刊·年·卷·页/文章号 | 分区 | DOI | 核心内容 | 与本文关联 | 开源 |
|---|------|---------|---------------------|------|-----|----------|-----------|------|
| B1 | Effect of soda residue on Skeleton formation and strength development in soil stabilization | Wei Wei | Eng Geol · 2026 · 362 · 108518 | 1区 | 10.1016/j.enggeo.2025.108518 | 碱渣对固化土骨架形成与强度发展的作用机理 | 同用碱渣（Soda residue）组分，直接对应本文双激发剂之一 | 非开源 |
| B2 | Multiscale experimental analysis of marine clay stabilized with coal gangue–calcium carbide residue geopolymer | Li Jianfeng | Acta Geotechnica · 2023 · 18 · 5921-5939 | 1区 | 10.1007/s11440-023-02055-4 | 煤矸石-电石渣地聚物固化海相黏土的多尺度试验 | 电石渣基地聚物+海相软土，XRD/SEM/MIP多尺度微观 | 非开源 |
| B3 | Treating sulfate-bearing soil by using sodium silicate and NaOH-activated ground granulated blast-furnace slag | Li Wentao | Acta Geotechnica · 2023 · 19 · 3129-3138 | 1区 | 10.1007/s11440-023-02097-8 | 水玻璃+NaOH激发矿渣处理含硫酸盐土 | 激发剂类型调控（对应本文激发剂配比）+硫酸盐环境 | 非开源 |
| B4 | Study on the solidification/stabilization of cadmium-contaminated soil by red mud-assisted blast furnace slag under excitation conditions | Chen Tao | J Clean Prod · 2024 · 435 · 140505 | 1区Top | 10.1016/j.jclepro.2023.140505 | 赤泥辅助矿渣在不同激发条件下固化/稳定化镉污染土 | 固废+激发条件优化，拓展污染土S/S应用 | 非开源 |
| B5 | Mechanical and microstructural analysis of soft kaolin clay stabilized by GGBS and dolomite-based geopolymer | Gupta Sanjoli | Constr Build Mater · 2024 · 421 · 135702 | 1区Top | 10.1016/j.conbuildmat.2024.135702 | 矿渣+白云石基地聚物固化软高岭土的力学与微观 | 碱激发矿渣固化软土+C-S-H/C-A-S-H微观分析 | 非开源 |
| B6 | Investigation of geotechnical and microstructure characteristics of gypsum soil using GGBS, fly ash, and lime | Parhizkar Amir | Constr Build Mater · 2024 · 418 · 135358 | 1区Top | 10.1016/j.conbuildmat.2024.135358 | 矿渣+粉煤灰+石灰三元固化石膏质土的岩土与微观特性 | 矿渣-粉煤灰-石灰三元组合接近SSF前驱体思路 | 非开源 |
| B7 | Role of Bayer red mud and phosphogypsum in cement-stabilized dredged soil with different water and cement contents | Wan Xing | Constr Build Mater · 2024 · 418 · 135396 | 1区Top | 10.1016/j.conbuildmat.2024.135396 | 拜耳赤泥+磷石膏在不同水/胶凝含量下对水泥固化疏浚土的作用 | 固废组分调控+含水率影响（对应本文含水率变量） | 非开源 |
| B8 | Strength and microstructure characteristics of red-bed weathered residual soil stabilized by Titanium Gypsum-Cement | Huang Kai | Constr Build Mater · 2023 · 403 · 133071 | 1区Top | 10.1016/j.conbuildmat.2023.133071 | 钛石膏-水泥固化红壤残积土的强度与微观结构 | 工业石膏固废改性固化土的强度-微观关联 | 非开源 |
| B9 | Stabilization/solidification of composite heavy metal contaminated soil using a novel red mud-slag based geopolymer (RM-SGP): Performance and mechanisms | Zhou Lu | Constr Build Mater · 2025 · 486 · 141996 | 1区Top | 10.1016/j.conbuildmat.2025.141996 | 赤泥-矿渣地聚物固化/稳定化复合重金属污染土的性能与机理 | 赤泥-矿渣地聚物凝胶产物机理（C-A-S-H/N-A-S-H） | 非开源 |
| B10 | Synergistic effects of sustained loading and wetting–drying cycles on strength and microstructure of slag–cement-stabilized marine soft soil | Xia Changqing | Acta Geotechnica · 2026 · 在线 | 1区 | 10.1007/s11440-026-03212-1 | 持续荷载+干湿循环耦合下矿渣-水泥固化海相软土的强度与微观 | 矿渣基固化土多因素耦合的强度与微观演化 | 非开源 |

**累计：20/30 篇。** 期刊构成（批次B）：CCB×5、Acta Geotechnica×3、Engineering Geology×1、Journal of Cleaner Production×1。

## 子任务4 · 检索批次C：耐久性（硫酸盐侵蚀/冻融循环）与低碳全固废固化 · 2026-09-06

检索与核验：Crossref API 8 组主题查询（限 2023-09 之后、一区期刊白名单）得 27 篇候选 → 剔除批次A/B已选 5 篇、金色/混合 OA 5 篇（含主题最契合的 Qi 2026 JRMGE 三元全固废、Mu 2025 JRMGE 低碳碳化、Luo K. 2026 CCC one-part 地聚物）、非一区与主题不符 7 篇 → 保留 10 篇，全部 Unpaywall is_oa=false。

| # | 标题 | 第一作者 | 期刊·年·卷·文章号 | 分区 | DOI | 核心内容 | 与本文关联 | 开源 |
|---|------|---------|------------------|------|-----|----------|-----------|------|
| C1 | Strength and microscopic pore structure characterization of cement-fly ash stabilized organic soil under freeze-thaw cycles | Shi Xin | Constr Build Mater · 2024 · 420 · 135635 | 1区Top | 10.1016/j.conbuildmat.2024.135635 | 冻融循环下水泥-粉煤灰固化有机土强度与微观孔结构 | 粉煤灰固化土冻融损伤与孔结构，对应本文粉煤灰界面薄弱区机制 | 非开源 |
| C2 | Performance of heterogeneous cement-based stabilized soft clay under cyclic freeze-thaw environments | Zhan Shaohu | Constr Build Mater · 2025 · 499 · 144022 | 1区Top | 10.1016/j.conbuildmat.2025.144022 | 循环冻融环境下非均质水泥基固化软土性能 | 固化软土冻融性能演化规律 | 非开源 |
| C3 | Investigating on dynamic and static mechanical characteristics and microscopic mechanism of fiber-reinforced and rubberized cement stabilized soil under dry-wet cycle sulfate erosion | Ding Jinmeng | Constr Build Mater · 2025 · 487 · 142083 | 1区Top | 10.1016/j.conbuildmat.2025.142083 | 干湿循环+硫酸盐侵蚀下改性水泥土动静力学与微观机理 | 硫酸盐侵蚀劣化路径（对应本文石膏+钙矾石双通道） | 非开源 |
| C4 | Effect of chloride ion erosion on alkali-activated solid waste-based stabilized soil: macro deterioration and microstructure evolution | Jia Jinming | Constr Build Mater · 2026 · 531 · 146623 | 1区Top | 10.1016/j.conbuildmat.2026.146623 | 氯盐侵蚀下碱激发固废固化土宏观-微观关联 | 同为碱激发固废固化土的耐侵蚀性能 | 非开源 |
| C5 | Effect of glass fiber (GF) on the mechanical properties and freeze-thaw (F-T) durability of lime-nanoclay (NC)-stabilized marl clayey soil | Salimi Mahdi | Constr Build Mater · 2024 · 416 · 135227 | 1区Top | 10.1016/j.conbuildmat.2024.135227 | 玻璃纤维对石灰-纳米黏土固化泥灰土冻融耐久性的影响 | 固化土冻融耐久性增强策略 | 非开源 |
| C6 | Effect of humic acid and fulvic acid on mechanical and durability properties of geopolymer stabilized soft soil | Luo Zhengdong | Constr Build Mater · 2023 · 409 · 133875 | 1区Top | 10.1016/j.conbuildmat.2023.133875 | 腐殖酸/富里酸对地聚物固化软土力学与耐久性的影响 | 有机质干扰地聚物固化软土（软土环境因素） | 非开源 |
| C7 | Effect of organic matter on the stabilization of dredged sediment using waste-activated ground granulated blastfurnace slag | Meng Ranqi | Constr Build Mater · 2026 · 522 · 146206 | 1区Top | 10.1016/j.conbuildmat.2026.146206 | 有机质对废弃活化矿渣固化疏浚底泥的影响 | 矿渣基固化疏浚土+有机质干扰机理 | 非开源 |
| C8 | Sustainable subgrade application of dredged sediment stabilized with solid waste-based supersulfated cement: Strength, water stability, and micro-mechanisms | Lang Lei | Constr Build Mater · 2026 · 542 · 148022 | 1区Top | 10.1016/j.conbuildmat.2026.148022 | 固废基过硫水泥固化疏浚底泥用于路基：强度、水稳定性与微观 | 全固废基过硫水泥体系（近SSF全固废理念）+水稳定性 | 非开源 |
| C9 | Direct incorporation of categorical geotechnical variables in CatBoost-based prediction of UCS of stabilized saline soils under freeze–thaw cycles | Ahmadi Hadi | Engineering Geology · 2026 · 373 · 109041 | 1区 | 10.1016/j.enggeo.2026.109041 | 融合类别岩土变量的CatBoost预测冻融下固化盐渍土UCS | 冻融环境下固化土强度智能预测 | 非开源 |
| C10 | Shear strength of biopolymer amended soil under freeze-thaw cycles: Experimental investigation and DEM modeling | Gu Jiayu | Engineering Geology · 2025 · 353 · 108108 | 1区 | 10.1016/j.enggeo.2025.108108 | 冻融循环下生物聚合物改良土抗剪强度试验与DEM模拟 | 冻融循环下改良土强度演化与细观模拟 | 非开源 |

**备注**：3 篇主题与本文 SSF 体系最契合的论文因开源（Unpaywall is_oa=true）未纳入——若用户接受开源论文可替换加入：Qi 2026 JRMGE（三元全固废胶凝材料固化疏浚土，doi:10.1016/j.jrmge.2025.05.024）、Mu 2025 JRMGE（废混凝土低碳固化剂碳化固铅，doi:10.1016/j.jrmge.2024.07.008）、Luo K. 2026 CCC（疏浚海泥+贝壳废弃物共煅烧 one-part 地聚物，doi:10.1016/j.cemconcomp.2026.106701）。

**累计：30/30 篇。** 期刊总构成：CCB×21、Acta Geotechnica×3、Engineering Geology×3、JCLP×1、JRMGE×1（wait — JRMGE 为0，此行更正为 CCB×21 + Acta Geotech×3 + Eng Geol×4 + JCLP×1 + CCC×1 = 30）。—— 见下方更正行

更正：批次构成 A(8×CCB+1×EngGeol+1×ActaGeotech)、B(5×CCB+3×ActaGeotech+1×EngGeol+1×JCLP)、C(8×CCB+2×EngGeol)；合计 CCB×21、Acta Geotechnica×4、Engineering Geology×4、Journal of Cleaner Production×1，共 30 篇。
