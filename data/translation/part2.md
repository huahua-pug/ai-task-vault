# 英中对照·分片2：第2章（两种哈密顿结构）与第3章（空间离散）

## 2. The Hamiltonian structure of Maxwell's equations｜第2章 麦克斯韦方程组的哈密顿结构

[EN] In this Section, we show that the Maxwell's equations (1) and (2) are Hamiltonian. A dynamical system is Hamiltonian if it can be written as Ḟ = {F, H}, where F are the coordinate functionals, which can be identified to the space of test functions D, H is the Hamiltonian functional, both defined on the phase affine space M, and {·,·} denotes the Poisson bracket — a bilinear antisymmetric form satisfying the Jacobi identity. We then say that (M, {·,·}, H) defines a Hamiltonian dynamical system.

[中] 本章证明麦克斯韦方程组(1)与(2)都是哈密顿的。若动力系统可写成 Ḟ = {F, H}，则称其为哈密顿系统：F 是坐标泛函（可与检验函数空间 D 等同），H 是定义在相仿射空间 M 上的哈密顿泛函，{·,·} 为泊松括号——满足雅可比恒等式的双线性反对称双线性形式。此时称 (M, {·,·}, H) 定义了一个哈密顿动力系统。

### 2.1 Notation｜记号

[EN] The standard spaces: L²(D) := {v : D → R³ : ‖v‖_{L²(D)} < ∞}, H(curl, D) := {v ∈ L²(D) : ∇×v ∈ L²(D)}. For a vector-valued function v in Ω, v|_Γ is its trace on Γ; the exterior trace v^ext is defined independently of the regularity of v inside Ω, and need not coincide with v|_Γ. For any space S(∘) of functions defined in the interior of Ω, we set S^{trace}(∘; g) := {s ∈ S(∘) : n×s^{trace} = g on Γ}, where "trace" indicates the standard trace or the exterior trace ("ext"). The exterior trace allows us to incorporate the boundary condition on the electric field into the smooth manifold M.

[中] 标准函数空间：L²(D)（平方可积矢量场）与 H(curl, D)（旋度亦平方可积）。对 Ω 上矢量函数 v，v|_Γ 是其在 Γ 上的迹；**外迹**（exterior trace）v^ext 的定义不依赖 v 在 Ω 内部的正则性，且不必与 v|_Γ 相同。对 Ω 内部定义的函数空间 S(∘)，记 S^{trace}(∘; g) := {s ∈ S(∘) : n×s^{trace} = g 于 Γ}，其中 trace 取标准迹或外迹（记作 ext）。引入外迹的目的，是把电场的边界条件直接纳入光滑流形 M 的定义之中——这是本文哈密顿框架的一个关键技巧。

### 2.2 Electric and magnetic field formulation｜电场-磁场（E-H）形式

[EN] We assume ε, μ, ρ, J and g_E are independent of time, and that the current J is solenoidal, so J = ∇×Ĵ. The components of the Hamiltonian structure are: (i) phase manifold and test space M = L²_{ext}(Ω; g_E) × H(curl, Ω), D = C^∞_{ext}(Ω; 0) × C^∞(Ω); (ii) the Poisson bracket {F,G}_E ⟨公式(3c)：Ω 上 ε⁻¹(δF/δE)·∇×(μ⁻¹ δG/δH) 的反对称差，外加 Γ 上含外迹的边界项⟩; (iii) the Hamiltonian H_E(E,H) = ½∫_Ω(εE·E + μH·H) − ∫_Ω Ĵ·μH; (iv) coordinate functionals F_E(φ) = ∫_Ω εE·φ, F_H(ψ) = ∫_Ω μH·ψ.

[中] 设 ε、μ、ρ、J、g_E 不依赖时间，且电流 J 无散（可写成 J = ∇×Ĵ）。哈密顿结构的四要素为：(i) 相流形与检验空间 M = L²_{ext}(Ω; g_E) × H(curl, Ω)，D = C^∞_{ext}(Ω; 0) × C^∞(Ω)；(ii) 泊松括号 ⟨公式(3c)⟩（Ω 上含 ε⁻¹、μ⁻¹ 的反对称体积分项，再加 Γ 上含外迹的边界项——边界项正是外迹技巧的用武之地）；(iii) 哈密顿量 H_E = ½∫_Ω(εE·E + μH·H) − ∫_Ω Ĵ·μH（总电磁能减去电流源耦合项）；(iv) 坐标泛函 F_E、F_H ⟨公式(3e)⟩。

### 2.3 Electric field and magnetic vector potential formulation｜电场-磁矢势（E-A）形式

[EN] Since μH = ∇×A, we consider H as a function of A, defined as the element of H(curl, Ω) such that ∫_Ω μH·ψ = ∫_Ω A·∇×ψ + ∫_Γ g_A·ψ for all ψ ∈ H(curl, Ω). The components: (i) M = L²(Ω) × L²_{ext}(Ω; g_A), D = C^∞(Ω) × C^∞_{ext}(Ω; 0); (ii) the Poisson bracket {F,G}_w = ∫_Ω (1/ε)(δG/δA · δF/δE − δF/δA · δG/δE) ⟨公式(4c)⟩ — simpler than the E-H bracket; (iii) the Hamiltonian H_w(E,A) = ½∫_Ω(εE·E + μH·H) − ∫_Ω A·J; (iv) coordinate functionals F_E(φ) = ∫_Ω εE·φ, F_A(ϕ) = ∫_Ω εA·ϕ.

[中] 由于 μH = ∇×A，把 H 视为 A 的函数：定义为满足 ∫_Ω μH·ψ = ∫_Ω A·∇×ψ + ∫_Γ g_A·ψ（∀ψ ∈ H(curl, Ω)）的 H(curl, Ω) 元素。结构四要素：(i) M = L²(Ω) × L²_{ext}(Ω; g_A)，D = C^∞(Ω) × C^∞_{ext}(Ω; 0)；(ii) 泊松括号 ⟨公式(4c)⟩——形式上比 E-H 括号简单，仅一个体积分项、无边界项；(iii) 哈密顿量 H_w = ½∫_Ω(εE·E + μH·H) − ∫_Ω A·J；(iv) 坐标泛函 F_E、F_A。注意：E-A 括号与声波/弹性波系列论文中的括号同构——这正是"类波动改写"的意义所在。

### 2.4 Conservation laws｜守恒律

[EN] The Hamiltonian systems described earlier satisfy all the conservation laws displayed in Table 2. For instance, to prove conservation of electric charge for the wave-like Hamiltonian system, take C := −∫_Ω εE·∇φ with φ ∈ C₀^∞(Ω); then ∫_Ω ρ̇φ = −∫_Ω ε Ė·∇φ = Ċ = {C, H_w}_w = ∫_Ω J·∇φ = −∫_Ω ∇·J φ, which proves the conservation of electric charge. The rest of the conservation laws can be obtained similarly by choosing different functionals C (Table 3).

[中] 前述哈密顿系统满足表 2 所列全部守恒律。以类波动（E-A）系统的电荷守恒为例：取泛函 C := −∫_Ω εE·∇φ（φ ∈ C₀^∞(Ω)），则 ∫_Ω ρ̇φ = −∫_Ω ε Ė·∇φ = Ċ = {C, H_w}_w = ∫_Ω J·∇φ = −∫_Ω ∇·J φ，即得电荷守恒。其余守恒律（磁荷、能量、线/角动量、光学手性及其通量等）只需换用不同泛函 C 同法可证（表 3 逐一列出了每个守恒律对应的泛函与泊松括号）。

## 3. The finite element methods for space discretization｜第3章 空间离散的有限元方法

### 3.1 Notation｜记号

[EN] Let T_h = {K} be a family of conforming, regular triangulations of Ω; h the maximum element diameter. Define ∂T_h, F_h (all faces), F⁰_h (interior faces), F^B_h (boundary faces), ∂K. For a vector w, its tangential and normal components on F are w_t = (n×w)×n, w_n = n(n·w). Inner products (·,·)_D and ⟨·,·⟩_B over volumes and (d−1)-dimensional sets; sums over T_h and face collections G. On an interior face F = ∂K⁺∩∂K⁻, with traces w±, define average {‖w‖} = ½(w⁺+w⁻) and jump ⟦w⟧_K = n⁺×w⁺ + n⁻×w⁻; on boundary faces ⟦w⟧_K := n×(w − w^ext).

[中] 设 T_h 为 Ω 的一族协调正则三角剖分，h 为最大单元直径；定义边界单元集 ∂T_h、面集 F_h（全部面）、内部面集 F⁰_h、边界面集 F^B_h。矢量 w 在面 F 上的切向/法向分量为 w_t = (n×w)×n 与 w_n = n(n·w)。定义体积分内积与面上内积，及其在 T_h 与面集合 G 上的求和记号。对内部面 F = ∂K⁺∩∂K⁻ 定义**平均** {‖w‖} = ½(w⁺+w⁻) 与**跳跃** ⟦w⟧_K = n⁺×w⁺ + n⁻×w⁻；边界面上的跳跃用外迹延拓：⟦w⟧_K := n×(w − w^ext)。

[EN] The finite dimensional spaces: V_h := {v ∈ L²(Ω) : v|_K ∈ V(K)}, W_h := {w ∈ L²(Ω) : w|_K ∈ W(K)}, M_h := {η ∈ L²(F_h) : η|_F ∈ M(F)}. As indicated in Section 2.1, we incorporate the boundary condition into the spaces by setting V^ext_h(g) := {v ∈ V_h : n×v^ext = g on Γ} (similarly W^ext_h(g), M_h(g)). These are used for DG and HDG; for mixed methods one uses V^curl_h := V_h ∩ H(curl; Ω) and W^curl_h — the spaces of edge elements (Nédélec elements).

[中] 有限维空间：分片多项式空间 V_h、W_h（单元级 V(K)、W(K)）与面空间 M_h（迹空间）。依 §2.1 的思路，把边界条件直接吸收进空间：V^ext_h(g) := {v ∈ V_h : n×v^ext = g 于 Γ}（W、M 同理）——DG/HDG 用之。混合法则用 H(curl) 协调空间 V^curl_h、W^curl_h，即所谓的**棱边元**（Nédélec 边元）空间。

### 3.2 The weak formulations｜弱形式

[EN] For mixed methods of the E-H formulation, (E_h, H_h) ∈ V^ext_h(g_E) × W^curl_h satisfies ⟨公式(5a)–(5b)⟩. For DG and HDG methods, (E_h, H_h) ∈ V_h × W_h solves ⟨公式(6a)–(6b)⟩, where the tangential components of the numerical traces (p̂E_h, Ĥ_h) approximate those of (E|_{F_h}, H|_{F_h}) and must be suitably defined; on ∂Ω, n×p̂E_h = n×E^ext. Furthermore, p̂E_h must satisfy the additional equation (9) ensuring single-valuedness of the numerical trace Ĥ_h. For the E-A formulation, mixed methods take (E_h, A_h, H_h) ∈ V_h × V^ext_h(g_A) × W^curl_h satisfying ⟨公式(7a)–(7c)⟩; HDG and DG take (E_h, A_h, H_h) ∈ V_h × V_h × W_h solving ⟨公式(8a)–(8c)⟩ with numerical traces (p̂A_h, Ĥ_h).

[中] E-H 形式的混合法：在 V^ext_h(g_E) × W^curl_h 中求 (E_h, H_h)，满足 ⟨公式(5a)–(5b)⟩。DG 与 HDG：在 V_h × W_h 中求解 ⟨公式(6a)–(6b)⟩，其中**数值迹** (p̂E_h, Ĥ_h) 的切向分量逼近真实迹，须恰当定义（见表4）；在边界上 n×p̂E_h = n×E^ext；且 p̂E_h 还须满足附加方程(9)以保证数值迹 Ĥ_h 的**单值性**。E-A 形式：混合法在 V_h × V^ext_h(g_A) × W^curl_h 中求 (E_h, A_h, H_h)，满足 ⟨公式(7a)–(7c)⟩；DG/HDG 在 V_h × V_h × W_h 中求解 ⟨公式(8a)–(8c)⟩，数值迹为 (p̂A_h, Ĥ_h)。

### 3.3 The numerical traces｜数值迹

[EN] The numerical traces for the HDG and DG methods are listed in Table 4; they incorporate the boundary conditions, and some are defined in terms of P_M, the L² projection onto ∏_K ∏_{F∈∂K} M(F). Only the tangential components of the numerical traces are seen by the schemes. As typical for HDG, the new hybrid unknown can be obtained either explicitly as a function of (E_h, H_h) or globally by imposing the single-valuedness of the tangential component of the other numerical trace: ⟨n×Ĥ_h, η⟩_{∂T_h\Γ} = 0 ⟨公式(9)⟩. If τ is a constant per face, the explicit solution (Appendix A) is: p̂E_h = (Y⁺P_M E⁺ + Y⁻P_M E⁻)/(Y⁺+Y⁻) − ⟦H_h⟧_K/(Y⁺+Y⁻) with Y := τ; Ĥ_h = (Z⁺H⁺ + Z⁻H⁻)/(Z⁺+Z⁻) + ⟦P_M E_h⟧_K/(Z⁺+Z⁻) with Z := τ⁻¹. To enforce stability it suffices that τ be positive; if ε, μ are piecewise constant and τ := √(ε/μ), Z becomes the impedance, Y the admittance, and the numerical traces become (a generalization of) the well-known upwinding traces.

[中] HDG 与 DG 的数值迹汇总于表 4：它们把边界条件吸收进定义，部分迹通过 L² 投影 P_M 表达；格式只"看见"数值迹的切向分量。按 HDG 的标准套路，杂交新未知量既可显式地表示为 (E_h, H_h) 的函数，也可通过强加另一数值迹切向分量的**单值性条件** ⟨公式(9)⟩ 全局求解。当 τ 逐面取常数时，显式解（附录A）为：p̂E_h = (Y⁺P_M E⁺ + Y⁻P_M E⁻)/(Y⁺+Y⁻) − ⟦H_h⟧_K/(Y⁺+Y⁻)（Y := τ）；Ĥ_h = (Z⁺H⁺ + Z⁻H⁻)/(Z⁺+Z⁻) + ⟦P_M E_h⟧_K/(Z⁺+Z⁻)（Z := τ⁻¹）。稳定性只需 τ > 0；若 ε、μ 分片常数且取 τ := √(ε/μ)，则 Z 恰为波阻抗、Y 为波导纳，数值迹退化为著名的**迎风（upwinding）数值迹**的推广形式。

[EN] For classic DG methods, consider C11, C22 scalars and C12 a matrix; stability holds when C11, C22 are non-negative. Three popular cases: (i) upwinding traces with C11 = 1/(Z⁺+Z⁻), C22 = 1/(Y⁺+Y⁻) and skew-symmetric C12; (ii) alternating traces with C11 = C22 = 0: p̂E_h = θ(E_h)⁺_t + (1−θ)(E_h)⁻_t, Ĥ_h = θ(H_h)⁻_t + (1−θ)(H_h)⁺_t for θ ∈ [0,1]; (iii) centered traces with C11 = C22 = C12 = 0.

[中] 对经典 DG 方法，设 C11、C22 为标量、C12 为矩阵，C11、C22 非负即稳定。三个常见特例：(i) **迎风迹**：C11 = 1/(Z⁺+Z⁻)、C22 = 1/(Y⁺+Y⁻)，C12 反对称；(ii) **交替迹**（alternating traces）：C11 = C22 = 0，p̂E_h 按参数 θ ∈ [0,1] 在两侧切向迹间取加权交替；(iii) **中心迹**：C11 = C22 = C12 = 0。这一统一参数化让后文"何时哈密顿"的结论可以精确表述（DG 当且仅当 C11 = C22 = 0）。

### 3.4 Examples of finite element spaces｜有限元空间实例

[EN] Specific choices of local spaces V(K), W(K), M(F) are summarized in Table 5: for mixed methods, Nédélec-type choices on tetrahedra (P_k / P_{k+1}); for HDG on polyhedra, P_k × P_k × P^t_k (variant k), P_{k+1} × P_k × P^t_{k+1} with ∇_F P_{k+2} (a superconvergent variant), and P_{k+1} × P_k × P^t_{k+1} (variant B, optimal); for DG, P_k × P_k. For mixed methods the trace space M is unnecessary since H(curl)-conformity is built into W^curl_h; H(curl)-conforming elements exist for hexahedra, prisms and pyramids via exact sequences. For HDG fewer references exist for the time-dependent Maxwell equations; for DG no hybrid unknown is needed.

[中] 局部空间的具体选取汇总于表 5：混合法用四面体上的 Nédélec 型空间（P_k 或 P_{k+1}）；HDG（多面体）三种变体——variant k（P_k×P_k×P^t_k）、超收敛变体（P_{k+1}×P_k×P^t_{k+1} 加 ∇_F P_{k+2}）、variant B（P_{k+1}×P_k×P^t_{k+1}，最优）；DG 用 P_k×P_k。混合法不需要迹空间 M，因为 H(curl) 协调性已在 W^curl_h 的构造中保证；借助恰当（exact）序列，六面体、棱柱、金字塔单元也能构造 H(curl) 协调元。含时麦克斯韦方程的 HDG 文献相对较少；DG 则无需杂交未知量。

### 3.5 The initial conditions｜初始条件

[EN] For the E-H methods, the initial conditions are simply the L²-projections of E₀ and H₀. For the E-A methods, the initial condition for E_h is the L²-projection of E₀; the definition of the initial condition for A is more involved since the initial data for A is not given and εA must be divergence-free. (H_h, A_h) is defined as an approximation to the solution of the system ⟨公式(10a)–(10e)：μH − ∇×A = 0；∇×H + ε∇p = ∇×H₀；∇·(εA) = 0；n×A = g_A；p = 0 on Γ⟩, where p is a Lagrange multiplier enforcing the divergence-free condition on εA explicitly; this auxiliary pressure turns out to be zero since ∇×H₀ is divergence-free. The HDG approximation (H_h, A_h, p_h, p̂A_h, p̂p_h) solves ⟨公式(11a)–(11f)⟩ with stabilization τ_n and scalar spaces Q_h, M^n_h. Remark 3.1: variant k uses P_k×P_k×P^t_k×P_k×P_k; variant B uses P_{k+1}×P_k×P^t_{k+1}×P_k×P_{k+1}.

[中] E-H 方法的初始条件就是 E₀、H₀ 的 L² 投影。E-A 方法的电场初始条件同样取 L² 投影；但 A 的初始条件更讲究——初始数据没有直接给出 A，且要求 εA 无散。做法：把 (H_h, A_h) 定义为约束系统 ⟨公式(10a)–(10e)⟩ 解的逼近，其中 p 是显式强加无散条件的拉格朗日乘子；由于 ∇×H₀ 本身无散，这个辅助"压力"最终恒为零。HDG 初始投影即求解带乘子的完整系统 ⟨公式(11a)–(11f)⟩（含稳定参数 τ_n 与标量空间 Q_h、M^n_h）。注 3.1：variant k 全部取 k 次多项式；variant B 中 A 的空间升为 k+1 次——后者在频域麦克斯韦 HDG 的统一误差分析中已被证明最优。
