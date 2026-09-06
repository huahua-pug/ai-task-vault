# 英中对照·分片3：第4章（半离散方法的哈密顿结构）与第5章（全离散HDG格式）

## 4. Hamiltonian structure of the semidiscrete methods｜第4章 半离散方法的哈密顿结构

[EN] We prove the Hamiltonian structure of the semidiscrete schemes based on the E-H and the E-A formulations. Subscript ‹ on the Poisson brackets distinguishes the formulations (‹ = E or w); superscript * distinguishes the methods (* = M mixed, DG, HDG). We claim that the semidiscrete methods of Section 3 define a Hamiltonian dynamical system for which: (i) the discrete phase and test space (M_h, D_h) approximates its continuous counterpart (M, D); (ii) the Poisson bracket {·,·}‹,h is a discrete version of {·,·}‹; (iii) the Hamiltonian H‹,h is a discrete version of H‹.

[中] 本章证明基于 E-H 与 E-A 两种形式的半离散格式都具有哈密顿结构。记号约定：泊松括号下标 ‹ 区分形式（E 或 w），上标 * 区分方法（M=混合、DG、HDG）。核心论断：第 3 章的半离散方法构成哈密顿动力系统，且 (i) 离散相空间与检验空间 (M_h, D_h) 逼近连续对应物 (M, D)；(ii) 离散泊松括号 {·,·}‹,h 是连续括号的离散版本；(iii) 离散哈密顿量 H‹,h 是连续哈密顿量的离散版本——**结构继承三要素**。

### 4.1 The electric and magnetic field formulation｜E-H 形式

[EN] For the E-H methods: phase/test spaces (mixed: M^M_h := V^ext_h(g_E)×W^curl_h; DG and HDG: V^ext_h(g_E)×W_h); a discrete Poisson bracket with volume terms plus boundary terms involving the exterior trace and the face function q(u) (equal to {||u||}+C12[[u]]_K on interior faces and u^ext on boundary faces); the discrete Hamiltonian H_{E,h} = ½((εE_h,E_h)_{T_h} + (μH_h,H_h)_{T_h}) - (Ĵ, μH_h); coordinate functionals F_{E_h} = (εE_h, v)_{T_h}, F_{H_h} = (μH_h, r)_{T_h}.

[中] E-H 方法的离散结构：混合法相空间为 V^ext_h(g_E)×W^curl_h，DG/HDG 为 V^ext_h(g_E)×W_h；离散泊松括号由体积分项与含外迹、面函数 q(u)（内部面上取 {||u||}+C12[[u]]_K、边界面上取外迹 u^ext）的边界项构成；离散哈密顿量 H_{E,h} = ½((εE_h,E_h)_{T_h} + (μH_h,H_h)_{T_h}) - (Ĵ, μH_h)；坐标泛函为 (εE_h, v)_{T_h} 与 (μH_h, r)_{T_h}。

[EN] Theorem 4.1 (Hamiltonian structure of the E-H formulation). (i) The mixed method (5) defines a Hamiltonian dynamical system with (M^M_h, {·,·}_{E,h}, H_{E,h}). (ii) The DG method (6), with numerical fluxes defined by Table 4, defines a Hamiltonian dynamical system if and only if C11 = C22 = 0. (iii) The HDG method (6), with numerical fluxes defined by Table 4, is such that (M^HDG_h, {·,·}_{E,h}, H_{E,h}) is never a Hamiltonian dynamical system.

[中] **定理 4.1（E-H 形式的哈密顿结构）**：(i) 混合法(5)以 (M^M_h, {·,·}_{E,h}, H_{E,h}) 构成哈密顿动力系统；(ii) 采用表 4 数值通量的 DG 方法(6)构成哈密顿动力系统，**当且仅当 C11 = C22 = 0**；(iii) 采用表 4 数值通量的 HDG 方法(6)**永远不能**构成哈密顿动力系统——这是一个明确的负面结果，也是全文转折点。DG 的哈密顿性排除了迎风迹（C11>0），意味着 E-H 路线只能用中心/交替迹。

[EN] A straightforward corollary (proven in Appendix C) is discrete conservation: the mixed method and the (restricted) DG method satisfy conservation of electric charge (ε ∂E_h/∂t, ∇v)_{T_h} = 0, magnetic charge (μ ∂H_h/∂t, ∇w)_{T_h} = 0, and energy dH_{E,h}/dt = 0, for test functions v, w ∈ H¹0(Ω) with (∇v, ∇w) ∈ D*_h. The restriction C11 = C22 = 0 immediately implies (Appendix B) that the HDG methods do not possess a Hamiltonian structure, consistent with the fact that their discrete energy always decreases in time.

[中] 直接推论（推论 4.1，附录C证明）：满足条件的混合法与 DG 方法在离散层面守恒电荷、磁荷与能量（三条守恒式对检验函数 v, w ∈ H¹0(Ω) 成立）。而 DG 的哈密顿性限制 C11 = C22 = 0 立即蕴含（附录B）**HDG 方法不可能具有哈密顿结构**——这与"HDG 离散能量随时间恒衰减"的已知事实完全一致。

### 4.2 The electric and magnetic vector potential formulation｜E-A 形式

[EN] For the E-A methods: phase/test spaces M*_h := V_h × V^ext_h(g_A), D*_h := V_h × V^ext_h(0) for all three methods; the discrete Poisson bracket 〈公式(12b)〉 has only two volume terms (no boundary terms!); the discrete Hamiltonian 〈公式(12c)〉 carries a third term — the stabilization term S*_h(A_h, H_h) := 〈n×(Ĥ*_h - H_h), A_h - p̂A*_h〉_{∂T_h}; coordinate functionals F_{E_h} = (εE_h, v)_{T_h}, F_{A_h} = (εA_h, v)_{T_h}.

[中] E-A 方法的离散结构：三种方法共用相空间 M*_h := V_h × V^ext_h(g_A) 与检验空间 D*_h；离散泊松括号 〈公式(12b)〉 只含两个体积分项、**没有边界项**（对比 E-H 括号的复杂边界项——这是 E-A 改写带来的本质简化）；离散哈密顿量 〈公式(12c)〉 多出第三项——**稳定化项** S*_h(A_h, H_h) := 〈n×(Ĥ*_h - H_h), A_h - p̂A*_h〉_{∂T_h}；坐标泛函为 (εE_h, v)_{T_h} 与 (εA_h, v)_{T_h}。

[EN] Proposition 4.1 (The form of the stabilization term). S^M_h = 0; S^DG_h = 〈C11[[A_h]]_K, [[A_h]]_K〉_{F_h} + 〈C22[[H_h]]_K, [[H_h]]_K〉_{F0_h}; S^HDG_h = 〈τ(P_M A_h - p̂A_h)×n, (P_M A_h - p̂A_h)×n〉_{∂T_h}. Theorem 4.2 (Hamiltonian structure of the E-A formulation). (i) The mixed method (7), (ii) the DG method (8), and (iii) the HDG method (8) — each with numerical fluxes defined by Table 4 — defines a Hamiltonian dynamical system with (M*_h, {·,·}_{ω,h}, H*_{ω,h}).

[中] **命题 4.1（稳定化项的形态）**：混合法的稳定化项为零；DG 的稳定化项是 C11、C22 加权的跳跃平方项；HDG 的稳定化项是 τ 加权的 (P_M A_h - p̂A_h) 投影差平方项。**定理 4.2（E-A 形式的哈密顿结构）**：(i) 混合法(7)、(ii) DG 方法(8)、(iii) HDG 方法(8)（数值通量均按表 4）**全部**构成哈密顿动力系统 (M*_h, {·,·}_{ω,h}, H*_{ω,h})——与定理 4.1 的负面结果形成鲜明对照，E-A 改写彻底解决了 HDG 的结构缺失问题。

[EN] The proof of Theorem 4.2 uses Lemma 4.1, 〈n×(δĤ*_h - δH_h), A_h - p̂A*_h〉 = 〈n×(Ĥ*_h - H_h), δA_h - δp̂A*_h〉 (a symmetry identity of the stabilization term, proven in Appendix F for the three methods). The key step is computing δH^HDG_{w,h}/δA_h via variation of the third equation of the method, using the single-valuedness of (δp̂A_h, n×Ĥ_h) on Γ; this yields 〈公式(13)〉, from which both Θ_{A_h} and Θ_{E_h} vanish, completing the proof.

[中] 定理 4.2 的证明依赖**引理 4.1**——稳定化项的一个对称性恒等式（附录F对三种方法分别验证）。关键步骤：对格式的第三个方程取变分，借助 (δp̂A_h, n×Ĥ_h) 在 Γ 上的单值性，算出哈密顿量对 A_h 的变分导数 〈公式(13)〉，由此两个偏差量 Θ_{A_h} 与 Θ_{E_h} 同时归零，证毕。证明的难点在于 Ĥ_h 通过 p̂A_h 隐式依赖 A_h，需要引理 4.1 把变分"搬移"到正确的一侧。

[EN] Corollary 4.2 (discrete conservation). The mixed method (7) and the DG and HDG methods (8) satisfy: (electric charge) (ε ∂E_h/∂t, ∇v)_{T_h} = (∇·J, v)_{T_h}; (magnetic charge) (μ ∂H_h/∂t, ∇w)_{T_h} = 0; (energy) dH_{w,h}/dt = 0. Proof (for DG): define F_ec := (εE_h, ∇v)_{T_h}; using (13), the single-valuedness of (∇v)_t on F0_h and v = 0 on Γ give dF_ec/dt = (∇·J, v)_{T_h}. Magnetic charge conservation follows directly from equation (8c) taking r := ∇w. Energy conservation follows immediately from the antisymmetry of the Poisson bracket {·,·}_{w,h}.

[中] **推论 4.2（离散守恒）**：三种方法都满足——电荷守恒 (ε ∂E_h/∂t, ∇v)_{T_h} = (∇·J, v)_{T_h}（含源项的守恒律）；磁荷守恒 (μ ∂H_h/∂t, ∇w)_{T_h} = 0；能量守恒 dH_{w,h}/dt = 0。证明（以 DG 为例）：定义 F_ec := (εE_h, ∇v)_{T_h}，用公式(13)与 (∇v)_t 在内部面的单值性、v 在 Γ 上为零即得电荷守恒；磁荷守恒直接由格式第三方程取 r := ∇w 得到；能量守恒由泊松括号的**反对称性**立即推出——∂H/∂t = {H, H} = 0，这是哈密顿框架最优雅的红利。

## 5. Fully discrete HDG schemes｜第5章 全离散 HDG 格式

### 5.1 Symplectic diagonally implicit Runge-Kutta methods｜辛对角隐式龙格-库塔（DIRK）

[EN] A DIRK scheme computes y^{n+1} from y^n by y^{n+1} = y^n + Δt Σ b_i k_i, with k_i = f(t_{n,i}, y_{n,i}), y_{n,i} = y^n + Δt Σ_{j≤i} a_{ij} k_j; the coefficients (a_{ij}, b_i, c_i) form a Butcher tableau, with a_{ij} = 0 for j > i. These schemes are symplectic under the condition b_i a_{ij} + b_j a_{ji} - b_i b_j = 0, 1 ≤ i,j ≤ s. The semidiscrete HDG scheme of the E-H formulation reduces to the ODE system M ∂y/∂t + T y = F(t) 〈公式(15)〉, where y contains the degrees of freedom of (E_h, H_h, p̂E_h); applying an s-stage DIRK scheme gives Algorithm 1 (DIRK-HDG). Static condensation can locally eliminate the degrees of freedom of (E_h, H_h) to obtain a smaller linear system in terms of p̂E_h.

[中] DIRK 格式由 y^{n+1} = y^n + Δt Σ b_i k_i 递推，系数 (a_{ij}, b_i, c_i) 构成 Butcher 表，且 a_{ij} = 0（j > i）。**辛条件**为 b_i a_{ij} + b_j a_{ji} - b_i b_j = 0（1 ≤ i,j ≤ s）。E-H 半离散 HDG 可约化为线性 ODE 组 M ∂y/∂t + T y = F(t) 〈公式(15)〉（y 含 (E_h, H_h, p̂E_h) 自由度），套用 s 级 DIRK 即得**算法 1（DIRK-HDG）**；还可做**静态凝聚**，局部消去 (E_h, H_h) 自由度，只解 p̂E_h 的较小线性系统——HDG 计算效率优势的体现。

### 5.2 Symplectic explicit partitioned Runge-Kutta methods｜辛显式分区龙格-库塔（EPRK）

[EN] For the Hamiltonian system ∂p/∂t = -∂H/∂q, ∂q/∂t = ∂H/∂p, an EPRK scheme uses an s-stage DIRK for the first ODE and an explicit RK for the second; the global scheme is explicit if the Hamiltonian is separable, and symplectic if b_i ã_{ij} + b̃_j a_{ji} - b_i b̃_j = 0. The HDG semidiscrete scheme is written in the separable structure M1 ∂p/∂t = -T1 q, M2 ∂q/∂t = T2 p + F(t) 〈公式(16)〉 and solved by Algorithm 2 (EPRK-HDG).

[中] 对哈密顿系统 ∂p/∂t = -∂H/∂q、∂q/∂t = ∂H/∂p，EPRK 格式对第一个 ODE 用 s 级 DIRK、对第二个用显式 RK；当哈密顿量**可分离**时整体显式，且辛条件为 b_i ã_{ij} + b̃_j a_{ji} - b_i b̃_j = 0。本文把 HDG 半离散格式写成可分离结构 M1 ∂p/∂t = -T1 q，M2 ∂q/∂t = T2 p + F(t) 〈公式(16)〉，用**算法 2（EPRK-HDG）**求解——由此获得显式辛时间推进，避免 DIRK 的多次隐式求解。

### 5.3 Fully discrete HDG schemes for the E-A formulation｜E-A 形式的全离散 HDG 格式

[EN] The HDG scheme (8)-(9) is rewritten as: find (A_h, E_h, H_h, p̂A^t_h) ∈ V_h×V_h×W_h×M^t_h satisfying the five equations 〈ε ∂A/∂t_h + εE = 0; ε ∂E_h/∂t - ∇×H_h - τ(P_M A_h - p̂A_h)×n = J; μH_h - n×p̂A^t_h - ∇×A_h = 0; single-valuedness of n×(H^t_h + τP_M(A_h - p̂A_h)); n×p̂A^t_h = g_A on Γ〉. For the implicit scheme, note the ODE structure (15) with M block diagonal (zero blocks for H_h and p̂A^t_h which have no time derivative). For the explicit scheme, write (16) with p, q the coefficients of A_h and E_h; H_h and p̂A^t_h must be expressed in terms of A_h via the third and fourth equations — a local system for (H_h, p̂A^t_h) given A_h.

[中] 把 HDG 格式(8)-(9)重写为求 (A_h, E_h, H_h, p̂A^t_h) 的五方程组 〈ε∂A/∂t_h + εE = 0；ε ∂E_h/∂t - ∇×H_h - τ(P_M A_h - p̂A_h)×n = J；μH_h - n×p̂A^t_h - ∇×A_h = 0；数值迹单值性；边界条件 n×p̂A^t_h = g_A〉。隐式方案：注意其 ODE 结构(15)中 M 为块对角（H_h 与 p̂A^t_h 无时间导数、对应块为零）。显式方案：按(16)取 p、q 为 A_h 与 E_h 的系数；但第二个方程中的 H_h、p̂A^t_h 需要用 A_h 表出——利用第三、四方程，对给定 A_h 解一个**局部子问题**求 (H_h, p̂A^t_h)。这一"局部消元+可分离写法"是显式辛 EPRK 得以实施的关键一步。
