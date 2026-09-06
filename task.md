# AI任务主输出文档

## 子任务1 · 需求解析、分类体系与检索方案定稿（含管道测试） · 2026-09-06

**用户确认口径**（AskUserQuestion）：电磁优先、放宽电磁刊分区——电磁耦合约800篇（一区非开源约600 + 电磁核心二区专业刊约200），其他方向约200篇（一区非开源）；全部非开源（OpenAlex is_oa=false，其OA数据聚合自Unpaywall）。

**硬约束事实**（探测数据，"finite element"+electromagnetic+is_oa:false+2015-2026）：TIE 234、TGRS 52、TPEL 34、MSSP 21、IJHMT 18、JMPT 12、CMAME 8、ATE 6、Applied Energy 5、TII 4 → 严格一区电磁总量约450，故二区电磁主场（T-Mag、IJNME、FEAD、EABE、JCP）按用户确认纳入。

**分类体系与配额（电磁800+其他200）**：
- A 电磁FEM方法学110（棱边元/误差估计/网格自适应/FEM-BEM/时域）——CMAME、IJNME、T-Mag、FEAD、EABE、JCP
- B 电磁-结构/力学耦合110（电磁成形/磁致伸缩/磁悬浮/电磁力/MHD）——JMPT、IJMTM、M&D、IJMS
- C 电磁-热耦合130（感应加热/涡流加热/损耗-温度耦合）——IJHMT、ATE、Applied Energy、ECM、Energy、Renewable Energy
- D 电机与电力设备250（永磁/感应电机设计、变压器、WPT、执行器）——TPEL、TIE、TII、MSSP
- E 高频与波动电磁120（天线/微波/散射/超材料/光子）——TGRS及上述二区组
- F 屏蔽/EMC/GPR/生物电磁等应用80
- G 其他方向200（结构/热/流体/岩土/断裂）——Composite Structures、IJFatigue、CCB、EngGeol、CnG、ActaG、JCLP、RCR等

**检索口径**：OpenAlex works，filter=title_and_abstract.search:{关键词}+primary_location.source.issn:{组}|+is_oa:false+publication_year:2015-2026+type:article|review；按相关性排序，cursor分页（per-page=200）；分区标注一区/二区组；时间窗兼顾现代软件生态（学习用途）。

**管道测试结论**：OpenAlex返回结构确认（display_name/doi/authorships/primary_location/cited_by_count可选裁剪）；cursor=*翻页正常；title_and_abstract.search精度良好（默认search混入大量噪声，弃用）；每页200条、抓取间隔≥0.3s；期刊组以ISSN OR列表过滤，分类以后处理标注。
