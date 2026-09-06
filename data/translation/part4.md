# 英中对照·分片4：第6章（数值实验）、第7章（扩展）与附录要点

## 6. Numerical experiments｜第6章 数值实验

[EN] The properties of the EPRK(k+2)-HDG_k(B) (variant B, third HDG method in Table 5) and DIRK(k+1)-HDG_k (variant k, first HDG method in Table 5) schemes are tested. An EPRK method of order (k+2) is used with variant B — matching the expected convergence rate of the errors of the electric field and the magnetic vector potential; a DIRK method of order (k+1) is used with variant k — matching the expected rate of all variables. All experiments use the open-source finite element libraries NETGEN and NGSolve.

[中] 实验测试两套组合：**EPRK(k+2)-HDG_k(B)**（variant B，表5第三种 HDG）与 **DIRK(k+1)-HDG_k**（variant k，表5第一种）。variant B 下用 (k+2) 阶 EPRK——与电场、磁矢势的期望收敛阶匹配；variant k 下用 (k+1) 阶 DIRK——与各变量期望收敛阶匹配。全部实验基于开源有限元库 NETGEN 与 NGSolve。时间阶与空间阶的匹配设计体现了"整体最优、不浪费任何一侧"的思想。

### 6.1 Convergence tests｜收敛性试验

[EN] For each approximation (E_h, A_h, H_h), compute the maximum over time steps of the L²-error and estimate the order of convergence (e.o.c.). The experiment is carried out on the unit cube (0,1)³ with uniform triangulations h = 2-ˡ, using the exact solution from the HDG literature 〈E, H given by products of trigonometric functions with angular frequency ω = √3 π, ε = μ = 1〉. Table 6 shows the errors and orders for EPRK(k+2)-HDG_k(B): optimal convergence of order k+2 in L² for the electric field and the magnetic vector potential, and order k+1 for the magnetic field.

[中] 对每个逼近量 (E_h, A_h, H_h) 计算 L² 误差在时间步上的最大值并估计收敛阶（e.o.c.）。实验在单位立方体 (0,1)³ 上一致剖分（h = 2-ˡ）进行，精确解取自 HDG 文献的三角函数乘积驻波解 〈角频率 ω = √3 π，ε = μ = 1〉。表 6 给出 EPRK(k+2)-HDG_k(B) 的误差历史：电场与磁矢势的 L² 误差达到**最优阶 k+2**，磁场达到 **k+1 阶**——variant B 的超收敛特性（势与场误差阶不同）与时间辛积分器的阶配套，理论与数值完全吻合。

### 6.2 Conservation properties｜守恒性试验

[EN] To test conservation, consider a monochromatic plane wave traveling in vacuum (J = 0, ρ = 0, constant ε0, μ0), with 〈E, H = E0e^{i(k·x-ωt)}, H0e^{i(k·x-ωt)}〉 satisfying the dispersion relation; take k = (κ,0,0), H0 = (0,H0,0), i.e., a plane wave traveling along the x-axis. The computational domain is the box (0,2)×(0,1)×(0,1) with periodic boundary conditions, κ = ω = 2; the scheme is HDG1 (k = 1 for all variables) with the implicit-midpoint DIRK(2) integrator.

[中] 守恒性测试采用真空中的单色平面波（J = 0，ρ = 0，ε0、μ0 为常数），〈场解形式〉 满足色散关系；取 k = (κ,0,0)、H0 = (0,H0,0)，即沿 x 轴传播的平面波。计算域为 (0,2)×(0,1)×(0,1)，**周期边界条件**，κ = ω = 2；格式为 HDG1（全部变量取 k = 1）配隐式中点法 DIRK(2)。

[EN] Figure 2 plots the approximate energy, optical chirality, the first component of the linear momentum, the second component of the angular momentum, the electric charge and the magnetic charge for three successively refined triangulations (h, h/2, h/4, starting with h = 0.25). We observe the exact conservation of the energy for the three meshes and the fast convergence to the exact energy. The electric and magnetic charges oscillate around zero with extremely small oscillations (below 10^(-1)³). The quadratic functionals of optical chirality and of linear and angular electromagnetic momenta remain remarkably non-drifting, with oscillations whose amplitude decreases as the mesh is refined. Theoretical computations for the total linear momentum (not reported) show that when the continuous version remains constant, its discrete version varies in time as a quadratic function of the jumps of the approximate solution — which might explain that its order of convergence is at least 2k. A similar behavior is expected for the remaining quadratic functionals of Table 2, but more work needs to be done to understand their convergence properties.

[中] 图 2 在三套逐步加密的网格（h、h/2、h/4，初始 h = 0.25）上给出能量、光学手性、线动量第一分量、角动量第二分量、电荷与磁荷的时程曲线。观察结果：① 三套网格上**能量被精确守恒**，并快速收敛到精确能量值——这源于辛龙格-库塔格式对二次型是精确积分的；② 电荷与磁荷在零附近振荡，振幅极小（低于 10^(-1)³）；③ 光学手性、线动量与角动量等二次泛函**显著无漂移**，振幅随网格加密而减小。作者还给出了总线动量的理论分析（未列入正文）：当连续量应为常数时，其离散版本随时间的变化是逼近解跳跃量的二次函数——这或许解释了其收敛阶至少为 2k。表 2 中其余二次泛函预计有类似行为，但**其收敛性质的理论理解仍是有待完成的工作**（这是作者自陈的开放问题）。

## 7. Extensions｜第7章 扩展

### 7.1 Other boundary conditions｜其他边界条件

[EN] For the boundary condition n×H = g_H on Γ, in the E-A formulation: H is taken as the element of H(curl, Ω; g_H) defined via ∫_Ω μH·ψ = ∫_Ω A·∇×ψ; since there are no boundary conditions on A, the manifold and test space become M = L²(Ω)×L²(Ω), D = C^∞(Ω)×C^∞(Ω); a term capturing the new boundary condition is added to the Hamiltonian: H_w(E,A) = ½∫_Ω(εE·E + μH·H) - ∫_Ω A·J - ∫_Γ A·g_H. The Poisson bracket and coordinate functionals are unchanged. For the mixed method the space becomes W^curl_h(g_H) and equation (17) replaces the H_h-equation; for DG and HDG only the numerical traces change (Table 7). In the discrete Hamiltonian an extra term -〈p̂A*_h, g_H〉_Γ appears, with the auxiliary trace p̂A^M_h well defined thanks to (17). With these modifications Theorem 4.2 and Corollary 4.2 still hold.

[中] 对边界条件 n×H = g_H（E-A 形式）：H 改为 H(curl, Ω; g_H) 中由 ∫_Ω μH·ψ = ∫_Ω A·∇×ψ 定义的元素；由于 A 没有边界条件，流形与检验空间退化为 M = L²(Ω)×L²(Ω)、D = C^∞(Ω)×C^∞(Ω)；哈密顿量需增加捕捉新边界条件的项 -∫_Γ A·g_H。泊松括号与坐标泛函不变。混合法的空间改为 W^curl_h(g_H) 并用公式(17)替换 H_h 方程；DG/HDG 只需更换数值迹（表 7）；离散哈密顿量额外出现 -〈p̂A*_h, g_H〉_Γ 项，其中辅助迹 p̂A^M_h 依赖公式(17)才良好定义。如此修改后，**定理 4.2 与推论 4.2 依然成立**——框架对边界条件类型的鲁棒性得到验证。

### 7.2 Other weak formulations｜其他弱形式

[EN] Since the roles of the electric and magnetic fields in Maxwell's equations are fairly symmetric, one can switch them. For the E-H formulation, the phase manifold and test space become M = H(curl, Ω; g_E)×L²(Ω), D = C^∞(Ω; 0)×C^∞(Ω), and the Poisson bracket 〈公式：∇×(ε^(-1)δF/δE) 与 μ^(-1)δG/δH 的反对称组合〉; the Hamiltonian and coordinate functionals remain unchanged. A simple computation shows that (M, {·,·}_E, H_E) is a Hamiltonian dynamical system yielding a (different) weak formulation of the first two equations. For the numerical methods: the mixed method uses the real trace instead of the exterior trace and the space V^curl_h(g_E)×W_h (Table 8 gives two examples with W^div_h); the DG and HDG methods need no changes. Theorem 4.1 and its corollary hold for these new methods.

[中] 麦克斯韦方程中电场与磁场的地位相当对称，故可将二者角色互换。E-H 形式下：相空间与检验空间改为 M = H(curl, Ω; g_E)×L²(Ω)、D = C^∞(Ω; 0)×C^∞(Ω)，泊松括号换成 〈∇×(ε^(-1)δF/δE) 与 μ^(-1)δG/δH 的反对称组合〉；哈密顿量与坐标泛函不变。简单计算验证这仍是哈密顿动力系统，且导出一个**不同于原弱形式**的新弱形式。数值方法上：混合法改用真实迹（而非外迹）并在 V^curl_h(g_E)×W_h 中逼近（表 8 给出两个 W^div_h 例子）；DG 与 HDG 无需任何改动。定理 4.1 及其推论对新方法依然成立。

[EN] We end by noting that the introduction of SH finite element methods for nonlinear Hamiltonian systems modeling physical phenomena of practical interest constitutes the subject of ongoing work.

[中] 全文以一句话收尾（论文未设独立结论章）：**把 SH 有限元方法推广到模拟实际物理现象的非线性哈密顿系统，是正在进行的工作**——这句也是作者明示的后续研究边界。

## 附录要点（Appendices A-G 摘译）

[EN/中] Appendix A: the HDG numerical traces are rewritten in classic DG format — eliminating p̂E_h on an interior face gives p̂E_h = τ+/(τ++τ-) P_M E+ + τ-/(τ++τ-) P_M E- - [[H_h]]_K/(τ++τ-) and the corresponding upwinding-type Ĥ_h.｜附录A：把 HDG 数值迹改写为经典 DG 形式——在内部面上消去杂交量 p̂E_h，得到 τ 加权的两侧加权平均再加跳跃项的迎风型迹。

[EN/中] Appendix B (proof of Theorem 4.1): using the jump identity 〈n×a, b〉_{∂T_h} = 〈[[a]]_K, {||b||}〉_{F0_h} - 〈{||a||}, [[b]]_K〉_{F0_h} + 〈n×a, b〉_Γ (Lemma B.1, proven in Appendix D), the proof shows the deviation terms θ¹_{E_h} = 〈C11[[E_h]]_K, [[v]]_K〉 and θ_{H_h} = 〈C22[[H_h]]_K, [[r]]_K〉 vanish if and only if C11 = C22 = 0 — hence DG is Hamiltonian iff C11 = C22 = 0, and HDG never (its own hybrid equation introduces an unavoidable extra term).｜附录B（定理4.1证明）：借助跳跃恒等式（引理B.1，附录D证明），把偏差量归为 〈C11[[E_h]], [[v]]〉 与 〈C22[[H_h]], [[r]]〉 两项，当且仅当 C11 = C22 = 0 时恒为零——DG 的哈密顿性条件由此而来；HDG 因杂交方程引入不可消除的额外项而永不满足。

[EN/中] Appendix C (conservation proofs): electric charge via F_ec := (εE_h, ∇v)_{T_h} using that (∇v) ∈ H(curl) so |∇v = ∇v (Nédélec's lemma); magnetic charge via F_mc := (μH_h, ∇w)_{T_h} with the three terms vanishing by single-valuedness of p̂E_h and of (∇w)_t and w = 0 on Γ; energy by antisymmetry of the bracket.｜附录C（守恒证明）：电荷用 F_ec 并借助 Nédélec 引理（∇v ∈ H(curl) 故 |∇v = ∇v）；磁荷三项分别因 p̂E_h 与 (∇w)_t 的单值性、w 在 Γ 为零而消失；能量由括号反对称性直接得到。

[EN/中] Appendix E (Proposition 4.1): for the mixed method Ĥ_h = H_h so the stabilization term vanishes identically; for HDG it is the τ-weighted projection-difference square; for DG it is the C11/C22-weighted jump squares. Appendix F proves the symmetry Lemma 4.1 case by case (mixed: trivial; HDG: direct from Table 4; DG: via Lemma B.1).｜附录E：混合法因 Ĥ_h = H_h 而稳定化项恒为零；HDG 为 τ 加权投影差平方；DG 为 C11/C22 加权跳跃平方。附录F按方法分情况证明对称性引理4.1（混合法平凡、HDG 由表4直接可得、DG 借助引理B.1）。

[EN/中] Appendix G: Butcher tableaux of the explicit symplectic partitioned Runge-Kutta schemes used in the computations — ESPRK(3,3) (Ruth 1983), ESPRK(6,4), and ESPRK(6,5) (McLachlan-Atela 1992), with coefficients b_i, b̃_i listed.｜附录G：给出计算所用显式辛分区龙格-库塔格式的 Butcher 表——ESPRK(3,3)（Ruth 1983）、ESPRK(6,4) 与 ESPRK(6,5)（McLachlan-Atela 1992），并列出系数 b_i、b̃_i。
