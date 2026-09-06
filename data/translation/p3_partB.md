# 英中对照·分片2：第4章（张量积 FEM 数值方法）、第5章（数值结果）、第6章（结论）

## 4. Numerical study of wave number dependent stability estimates｜波数依赖稳定性估计的数值研究

[EN] The tensor-product FEM Galerkin method [18] for (2.5): spaces S^D_{κ,N}, S^{DN}_{κ,M} of C⁰ piecewise polynomials of degree κ; on an N×M partition seek u_h ∈ S^D_{κ,N} ⊗ S^{DN}_{κ,M}. The linear system ⟨公式(4.1)：A u = f⟩ with A = A₁⊗B₂ + B₁⊗A₂ − k²B₁⊗B₂ (block structure with B, G blocks; T the matrix of the nonlocal operator). Defining B (mass), B^Γ, B_x, B_y (symmetric positive (semi-)definite) and their square roots, the quantities ⟨公式(4.2)：M = B^{1/2}A^{−H}BA^{−1}B^{1/2}, N = B^{1/2}A^{−H}(B_x+B_y)A^{−1}B^{1/2}, and M^Γ, N^Γ analogously with B^{1/2}_Γ⟩ yield, for g = 0 (distributed source), ⟨公式(4.3)：‖∇u_h‖ + k‖u_h‖ ≤ α_h(k)‖f_h‖, α_h(k) = √(‖N‖₂) + k√(‖M‖₂)⟩ and, for f = 0 (incident source), ⟨公式(4.5)：‖∇u_h‖ + k‖u_h‖ ≤ β_h(k)‖g_h‖, β_h(k) = √(‖N^Γ‖₂) + k√(‖M^Γ‖₂)⟩. M Hermitian positive definite, others positive semidefinite → ‖·‖₂ = λ_max; eigenvalues of PQ and QP coincide so B^{1/2} never needed explicitly; λ_max computed by implicitly restarted Arnoldi using only A^{−1} matrix-vector products (fast tensor-product algorithm of [18], no explicit inverse).

[中] 用张量积 FEM Galerkin 方法 [18] 解 (2.5)：κ 次 C⁰ 分片多项式空间的张量积，在 N×M 网格上求 u_h；线性系统 ⟨公式(4.1)⟩ 的 A = A₁⊗B₂ + B₁⊗A₂ − k²B₁⊗B₂（含非局部算子 T 的矩阵块 G）。定义质量阵 B、B^Γ 与梯度阵 B_x、B_y（对称正定/半正定），构造 ⟨公式(4.2)⟩ 的 M、N、M^Γ、N^Γ（形如 B^{1/2}A^{−H}(·)A^{−1}B^{1/2}），于是：分布源（g=0）时 ⟨公式(4.3)：‖∇u_h‖ + k‖u_h‖ ≤ α_h(k)‖f_h‖⟩，入射源（f=0）时 ⟨公式(4.5)：‖∇u_h‖ + k‖u_h‖ ≤ β_h(k)‖g_h‖⟩，其中 α_h = √‖N‖₂ + k√‖M‖₂、β_h = √‖N^Γ‖₂ + k√‖M^Γ‖₂。M 对称正定、其余半正定 → 范数即最大特征值；利用 PQ 与 QP 特征值相同的性质，**无需显式计算 B 的平方根**；大波数下用隐式重启 Arnoldi 求最大特征值，且只需 A^{−1} 的矩阵-向量积（用 [18] 的快速张量积算法实现，不求逆）——**离散问题的稳定性常数因此可以对任意 k 数值计算**。

## 5. Numerical results｜数值结果

[EN] Ω = (0,1)×(0,1), MATLAB, κ = 4. Representative wave numbers: k = π√(m²+1) (Dirichlet eigenvalues (5.1)) or k = π√((m+1/2)²+1) (Dirichlet–Neumann eigenvalues (5.2)), m = 10:64, and a fine sweep in [π√(312²+1), π√(332²+1)] with step ≈ 0.063. Observations (T = iku): α_h(k) ≈ 0.1k² and β_h(k) ≈ 0.45k at k = π√(m²+1); α_h, β_h almost constant for k = π√((m+1/2)²+1); β_h coincides with the theoretical β(k) — validating the numerical approach. Cavity problem: α_h(k) ≈ 0.18k^{3/2}, β_h(k) ≈ 0.47k at k = π√(m²+1); almost constant at k = π√((m+1/2)²+1); oscillation in between with slightly increasing averages. Two error examples (manufactured solution; empty cavity at normal incidence, errors from N=M=128 vs N=M=512 meshes): the errors highly depend on the stability — significantly large exactly where the stability constants are significantly large.

[中] 设置：Ω = (0,1)×(0,1)，MATLAB，κ = 4 次。代表性波数取 Dirichlet 特征值 k = π√(m²+1) 或 Dirichlet–Neumann 特征值 k = π√((m+1/2)²+1)（m = 10:64），并在区间 [π√(312²+1), π√(332²+1)] 内以步长 ≈0.063 细扫描。观察（T = iku）：在 k = π√(m²+1) 处 α_h(k) ≈ 0.1k²、β_h(k) ≈ 0.45k；在 k = π√((m+1/2)²+1) 处 α_h、β_h 几乎为常数；β_h 与理论 β(k) 吻合得很好——数值方法有效性得到验证。**腔体问题**：在 k = π√(m²+1) 处 α_h(k) ≈ 0.18k^{3/2}、β_h(k) ≈ 0.47k；在 k = π√((m+1/2)²+1) 处几乎为常数；其间随 k 振荡、各区段平均值随 m 略增。两个误差算例（人工制造解；法向入射空腔，128 与 512 网格对比）：**误差强烈依赖稳定性——稳定性常数显著大的地方，误差恰好显著大**。

## 6. Concluding remarks｜结论

[EN] For (2.5) with T = iku: α_h(k) ≲ k², β_h(k) ≲ k — coinciding with theoretical results; for cavity problems: α_h(k) ≲ k^{3/2}, β_h(k) ≲ k. By the sharp example (2.8), these are believed to be optimal uniform stability bounds with explicit k-dependence. The stability constants are large only for countable k values (geometry-dependent) and behave like constants for most k — independent of k in an average sense; hence it is not surprising that stable, accurate reconstruction can be obtained for inverse problems with multi-frequency data. For a deep cavity model, T = iku approximates the exact cavity problem, but its distributed-source stability is worse — such an approximation may not be advisable; a better approximation is under investigation. Numerical stability study for the TE polarization will be reported elsewhere.

[中] 结论：T = iku 时 α_h(k) ≲ k²、β_h(k) ≲ k（与理论吻合）；腔体问题 α_h(k) ≲ k^{3/2}、β_h(k) ≲ k。结合尖锐算例 (2.8)，作者**相信这些是波数显式的最优一致稳定性界**。稳定常数仅在一组可数的 k 值（依赖区域几何）处很大，多数 k 处表现为常数——**平均意义下与 k 无关**；因此"多频数据能得到稳定、精确的重建"并不令人意外。附注：深腔模型常用 T = iku 近似精确透明边界条件，但其分布源稳定性比精确问题更差——这种近似可能并不可取，更好的近似正在研究中。TE 极化的稳定性数值研究将另行报告。

## Appendix A｜附录A 要点

[EN] Energy proof for (2.6) with T = iku: multiply by u and integrate by parts ⟨公式(A.1)⟩; imaginary part gives ⟨公式(A.2)：k∫|u(x,b)|²dx ≤ ‖f‖‖u‖⟩; multiply by ∂_yu, integrate over (0,1)×(y,b) and combine ⟨公式(A.3)⟩ to get ‖∂_yu‖ ≤ (kb+3/2)‖f‖ ⟨公式(A.4)⟩; Poincaré-type ‖u‖ ≤ (b/√2)‖∂_yu‖ then ‖u‖ ≤ b(kb+3/2)/√2 ‖f‖ ⟨公式(A.5)⟩; real part of (A.1) yields ‖∇u‖ + k‖u‖ ≲ k²b²‖f‖.

[中] 附录A（分布源问题 T = iku 的能量法证明）：乘 u 分部积分 ⟨公式(A.1)⟩，取虚部得 ⟨公式(A.2)⟩；乘 ∂_yu 在 (0,1)×(y,b) 上积分并合并 ⟨公式(A.3)⟩ 得 ‖∂_yu‖ ≤ (kb+3/2)‖f‖ ⟨公式(A.4)⟩；用 Poincaré 型不等式 ‖u‖ ≤ (b/√2)‖∂_yu‖ 得 ⟨公式(A.5)⟩；最后由 (A.1) 实部推出 ‖∇u‖ + k‖u‖ ≲ k²b²‖f‖。
