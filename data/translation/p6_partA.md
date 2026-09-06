# 双腔体瞬态电磁散射的分析与数值解（英中对照·分片1：摘要、引言、问题表述、变分形式与适定性）

体例：[EN] 原文（公式用字体安全 Unicode），[中] 汉译。

## Abstract｜摘要

[EN] A finite-element boundary integral method is presented to model transient scattering from two cavities embedded in a ground plane. Multiple-cavity scattering in the time domain both increases the computational complexity and introduces cross-talk between scatterers. By modeling the cavities together, coupling effects are enforced directly and multiple reflections are readily observable. The variational formulation is shown to be well-posed for each time step and a stable numerical implementation for rectangular cavities is demonstrated.

[中] 本文提出一种有限元-边界积分方法，用于模拟接地平面上两个腔体的瞬态散射。时域多腔体散射既增加计算复杂度，又引入散射体之间的串扰。通过把两个腔体一起建模，耦合效应被直接强加于格式之中，多次反射也易于观察。文中证明变分形式对每个时间步都是适定的，并给出矩形腔体的稳定数值实现。

## 1. Introduction｜引言

[EN] EM scattering from open cavities and cavity-backed apertures is an active research area (aircraft design, RCS modeling). Scattering sources: reentrant structures, specular scattering, traveling wave echoes, edge/vertex diffraction, creeping waves, interactions, surface discontinuities — the greatest contributors being reentrant structures and specular scattering. As RCS reduction grows sophisticated, lesser sources (edge diffraction, interactions, discontinuities) matter more: control surfaces, access panels, ordnance bay doors, engine inlets, exhaust nozzles create gaps/cavities. Cavity spacing and interactions may maximize or minimize constructive/destructive effects. A structure responding like a gap at one frequency may act as a reentrant structure at higher frequency — transient analysis generates a wide-band solution and may capture nonlinear behavior and interactions invisible in time-harmonic solutions.

[中] 开口腔体与腔体口径的电磁散射是活跃研究方向（飞机设计、RCS 建模）。散射源分类：凹入结构、镜面散射、行波回波、棱边/顶点绕射、爬行波、相互作用、表面不连续——前两类贡献最大。随着 RCS 缩减技术日益精细，次要散射源（棱边绕射、相互作用、不连续）愈发重要：控制面、检修口盖、弹药舱门、发动机进气道、尾喷口都会形成缝隙/腔体。研究腔体间距与相互作用有助于放大或抑制散射场的相长/相消效应。同一结构在某频段表现为缝隙、在更高频段可能表现为凹入结构——**瞬态分析一次给出宽带解**，还能捕获时谐解看不到的非线性行为与相互作用。

[EN] Recent work focuses on the FE-BI method coupling the interior (FEM) with the exterior (analytical Green's function). Transient single-cavity 3D analysis [6]; 2D numerical modeling with the Newmark method [7] — Newmark discretizes time-variant equations into forced time-harmonic Helmholtz equations per time step. Multiple-cavity time-harmonic problem well explained with well-posedness proof [8]. This work extends [7,8] to the transient two-cavity problem; the key result: the variational formulation for transient scattering from two cavities using the Newmark method is well-posed.

[中] 近期工作集中于 FE-BI 方法：内部腔域用 FEM、外部区域用格林函数解析求解。三维单腔瞬态分析见 [6]；二维数值建模用 Newmark 方法时间推进 [7]——Newmark 把时变方程逐时间步化为受迫的时谐 Helmholtz 方程。多腔时谐问题的数值处理与适定性证明见 [8]。本文把 [7,8] 的成果扩展到**瞬态双腔问题**，关键结论是：采用 Newmark 方法的双腔瞬态散射变分形式是适定的。

## 2. Problem statement｜问题表述

[EN] Infinite PEC ground plane with two fully-embedded 2D cavities (3D: z-invariant grooves); TMz polarization (E fully z-directed); free space above (ε0, μ0); cavities Ω₁, Ω₂ may contain non-magnetic homogeneous dielectric fill (ε_j ∈ C, Re > 0, Im = 0); PEC walls S₁, S₂; apertures Γ₁₁, Γ₁₂. Initial-boundary value problem ⟨公式(1)：−Δu + εr ∂²u/∂t² = 0 in R²₊ ∪ Ω₁ ∪ Ω₂；u = 0 on Γ_c ∪ S₁ ∪ S₂；√r(∂/∂r + ∂/∂t)u_s → 0 as r→∞⟩, where u_s = u − u^inc − u^ref (the exterior field attributable to the cavities). Solution space H¹(R²₊ ∪ Ω₁ ∪ Ω₂). Approach (following [7,17]): discretize in time first, then solve each step by FE-BI, iterate with Newmark.

[中] 无限大 PEC 接地平面上两个完全嵌入的二维腔体（三维上为 z 向不变的槽/通道）；TMz 极化（E 全沿 z 方向、随 x,y 变化）；上方为自由空间；腔体 Ω₁、Ω₂ 可含非磁性均匀介质填充（ε_j 复数、实部正虚部零）；PEC 壁 S₁、S₂，口面 Γ₁₁、Γ₁₂。初边值问题 ⟨公式(1)⟩，其中 u_s = u − u^inc − u^ref 是"因腔体存在而产生的外场差"。解空间取 H¹。方法路线（沿 [7,17]）：**先时间离散、再逐时间步用 FE-BI 求解、以 Newmark 方法推进**。

[EN] 2.3 Newmark method: unconditionally stable with correctable linear error growth, computationally lean (vs Kirchhoff-type methods storing all history). Generating equations ⟨公式(2)(3)⟩ with parameters β, γ; discretized system ⟨公式(4)⟩; γ = 0.5 gives Newmark-β; implicit for β > 0 — implemented via prediction–correction: prediction ⟨公式(5)：ũ^{n+1} = u^n + h u̇^n + (½−β)h² ü^n⟩, then ⟨公式(6)(7)：−Δu^{n+1} + α²εr u^{n+1} = α²εr ũ^{n+1}⟩ with α² = (βh²)⁻¹ — of the same form as a time-harmonic wave equation with source; correction ⟨公式(8)⟩.

[中] 2.3 Newmark 方法：无条件稳定、误差线性增长可校正、计算精简（相比需存储全部历史时间的 Kirchhoff 型方法）。生成方程 ⟨公式(2)(3)⟩（参数 β、γ 控制稳定性与精度）；离散系统 ⟨公式(4)⟩；γ = 0.5 即 Newmark-β 法；β > 0 时为隐式——用预测-校正实现：预测 ⟨公式(5)⟩，再化成 ⟨公式(7)：−Δu^{n+1} + α²εr u^{n+1} = α²εr ũ^{n+1}⟩（α² = (βh²)⁻¹）——与带源项的时谐波动方程同形；最后校正 ⟨公式(8)⟩。

[EN] 2.4 Exterior solution: by image theory u^ref is known; solve for u_s satisfying (1) and (7) ⟨公式(9)⟩ with g0 = u on apertures, 0 on Γ_C ⟨公式(10)⟩; Trace Theorem: g0 ∈ H^{1/2}(R). The exterior problem is solved analytically with the half-space Green's function ⟨公式(13)：G_α = (1/2π)[K0(α|r−r′|) − K0(α|r−r′_i|)]⟩ (K0 = modified Bessel, second kind; image point r_i): ⟨公式(11)(12)⟩. G_α satisfies the homogeneous modified wave equation except at the source ⟨公式(14)⟩. 2.5 Interior problem: forced wave equation ⟨公式(15)⟩ per time step, Neumann BC at the apertures from the exterior solution ⟨公式(16)(18)(19)：∂u^{n+1}/∂y|_{y=0} = 2∂u^inc/∂y + H̃^{n+1} + [T_α g]⟩, Dirichlet on PEC walls ⟨公式(17)⟩.

[中] 2.4 外部解：由镜像理论 u^ref 已知，只需求 u_s： ⟨公式(9)⟩，口面上 Dirichlet 数据 g0 = u、接地平面其余处为 0 ⟨公式(10)⟩；由迹定理 g0 ∈ H^{1/2}(R)。外部问题用**半空间格林函数**解析求解 ⟨公式(13)——含镜像点的修正贝塞尔函数 K0⟩，得 ⟨公式(11)(12)⟩；G_α 除源点外满足修正齐次波动方程 ⟨公式(14)⟩。2.5 内部问题：每个时间步解受迫波动方程 ⟨公式(15)⟩，口面 Neumann 边界由外部解导出 ⟨公式(16)(18)(19)⟩，PEC 壁上 Dirichlet ⟨公式(17)⟩。口面 Neumann 条件中的算子 T_α 作用于口面数据 g，H̃ 项来自上半平面预测场的格林积分。

[EN] 2.6 Variational formulation: test space H¹_S(Ω) (zero on S₁ ∪ S₂); after Green's theorem ⟨公式(20)(21)⟩, the formulation reads ⟨公式(22)：a(u^{n+1}, v) = b^{n+1}(v)⟩ with a(u,v) = ⟨∇u,∇v⟩_Ω + α²⟨εr u, v⟩_Ω − ⟨Tu, v⟩_{Γ₁₁∪Γ₁₂} and b(v) = α²⟨εr ũ, v⟩_Ω + ⟨2∂u^inc/∂y + H̃, v⟩_{Γ₁₁∪Γ₁₂}.

[中] 2.6 变分形式：检验空间 H¹_S(Ω)（在 PEC 壁上为零）；由格林定理 ⟨公式(20)(21)⟩ 得 ⟨公式(22)：a(u^{n+1}, v) = b^{n+1}(v)⟩，其中双线性形式 a 含体积刚度、质量项与**口面算子 T_α 的负内积**，右端 b 含预测场与入射场法向导数、H̃ 项。

## 3. Well-posedness｜第3章 变分形式的适定性（定理1）

[EN] Sobolev norms ⟨H¹(Ω), H^{1/2}(Γ) with |g|²_{1/2} = ∫∫|g(x)−g(x′)|²/|x−x′|², H^{−1/2} as dual, disjoint-union spaces ‖·‖²_{H^m(D₁∪D₂)} = ‖·‖²_{D₁} + ‖·‖²_{D₂}⟩. Theorem 1: a unique solution exists to (22) — via Lax–Milgram through three lemmas. Lemma 1: T_α : H^{1/2}(Γ₁₁∪Γ₁₂) → H^{−1/2}(Γ₁₁∪Γ₁₂) is bounded — decomposed into single-cavity operators (bounded by [7]: ‖T_{1,1}‖ ≤ c₁‖g‖ etc.) plus cross-cavity terms; for x ≠ x′, [∂²_x − α²]K0(α|x−x′|) = (α/|x−x′|)K₁(α|x−x′|) is strictly positive and decreasing, so cross terms are bounded with c₃ = αK₁(αd(Γ₁₁,Γ₁₂))/(πd), d = minimal cavity separation. Lemma 2: ⟨T_α g, g⟩ is non-positive — extend g by zero to R, integrate by parts twice using antisymmetry of ∂_x K0 ⟨公式(27)(28)：I₁, I₂ ≤ 0⟩, extending the single-cavity argument of [7]. Lemma 3: coercivity and boundedness of a: a(u,u) ≥ min_{r∈Ω}[1, α²εr(r)]‖u‖²_{H¹} (since −⟨T_α u, u⟩ ≥ 0 by Lemma 2); boundedness via Cauchy–Schwarz on volume terms and Lemma 1 + Trace theorem on the four aperture cross terms. Additionally b(v) bounded: the H̃ term ⟨公式：∂_yG_α = −(1/2π)∂_{y′}[K0(α√((x−x′)²+(y−y′)²)) + K0(α√((x−x′)²+(y+y′)²))]⟩ reduces the double integral to a single one, and |ũ| ≤ M_u gives ⟨H̃, v⟩ ≤ (2α²M_u/π)(π/(2α))∫|v| ≤ c_h‖v‖_{H¹}. Conclusion: Lax–Milgram ⟹ unique u^{n+1} ∈ H¹_S(Ω) per time step.

[中] 定义 Sobolev 范数与不相交并集空间范数。**定理 1：变分形式(22)存在唯一解**——经三条引理满足 Lax–Milgram 条件。引理 1：T_α 从 H^{1/2} 到 H^{−1/2} 有界——分解为单腔算子（[7] 已证有界）加**跨腔项**；利用 [∂²_x − α²]K0(α|x−x′|) = (α/|x−x′|)K₁(α|x−x′|) 严格正且随距离递减，跨腔项以 c₃ = αK₁(αd)/(πd)（d 为两腔最小间距）界定。引理 2：⟨T_α g, g⟩ 非正——把 g 零延拓到全直线、用 ∂_x K0 的反对称性分部积分两次 ⟨公式(27)(28)⟩，把 [7] 的单腔论证推广到双腔。引理 3：a 的强制性（由引理 2，−⟨T_α u, u⟩ ≥ 0，故 a(u,u) ≥ min[1, α²εr]‖u‖²）与有界性（体积分用 Cauchy–Schwarz、四个口面交叉项用引理 1 + 迹定理）。此外 b(v) 有界：∂_yG_α 可写成对 y′ 的导数 ⟨公式⟩，把二重积分化为一重积分，|ũ| ≤ M_u 得 ⟨H̃, v⟩ ≤ c_h‖v‖。综上，**Lax–Milgram 定理给出每个时间步的唯一解 u^{n+1} ∈ H¹_S(Ω)**。
