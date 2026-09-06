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

## 子任务2 · 电磁耦合主库批量拉取与分桶 · 2026-09-06

- 抓取：28 组 OpenAlex 查询（title_and_abstract.search × ISSN 组 × is_oa:false × 2015-2026 × article|review），relevance_score 降序，per-page=200 cursor 翻页，原始页 JSON 共 32 个
- 去重合并：DOI 去重（缺失 DOI 用标题归一化兜底，实测 0 篇缺 DOI）；跨桶先到先得；桶内按查询优先序截断配额
- 结果：**781/800 篇**（A方法学110、B电磁-结构110、C电磁-热130、D电机设备250、E高频波动103/120、F屏蔽EMC等78/80；E/F池子偏小为唯一缺口）
- 期刊分布 TOP：TIE×318、T-Mag×92、TGRS×52、ATE×44、EABE×42、TPEL×40、IJHMT×36、JCP×34、MSSP×27、CMAME×21
- 样本抽查：各桶主题命中良好（A=数值方法、B=电磁成形、C=感应加热、D=电机FEM、E=电磁正演反演、F=屏蔽建模），无 DOI 缺失
- 快照：data/em_corpus_snapshot.csv（bucket/zone/year/journal/first_author/n_authors/cited/type/doi/title）

## 子任务3 · 其他方向库拉取与全库组装 · 2026-09-06

- 抓取：5 组 OpenAlex 查询（岩土/断裂/传热/结构/数值方法 × 对应一区期刊 ISSN 组 × is_oa:false × 2015-2026），各取 1 页相关性前 200
- 清洗：剔除 EM 库已收 DOI；非一区期刊记录剔除（IJNME/JCP 仅限电磁专业刊使用）
- 结果：G 库 **220 篇**（岩土70、断裂与损伤35、传热40、结构与复合材料45、数值方法30）
- 全库组装：**1001 篇**（电磁 781 + 其他 220；其中二区电磁专业刊 212 篇，符合用户确认的"电磁优先放宽"口径）；年份分布 2015-2026 均匀（39–111 篇/年）
- 快照：data/full_corpus_snapshot.csv（bucket/sub/zone/year/journal/first_author/n_authors/cited/type/doi/title）

## 子任务4 · xlsx总表制作 · 2026-09-07

- 产出：C:\Users\zhang\OneDrive\文档\FEM学习文献库_电磁耦合方向_1001篇.xlsx
  - Sheet1「总表1001篇」：序号/大类/子方向/分区/年份/期刊/第一作者/作者数/被引/类型/DOI/论文标题，12列×1001行，冻结窗格+筛选器+分桶底色
  - Sheet2「分类统计」：子方向/分区/年份/期刊TOP20分布
  - Sheet3「检索说明」：口径（电磁优先放宽、is_oa=false、2015-2026、分区复核提示）与使用建议
- 验证：抽样第1/119/499/899/1001行，分类、分区、DOI均正确
