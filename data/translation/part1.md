# Symplectic Hamiltonian finite element methods for electromagnetics（英中对照·分片1：摘要与引言）

说明：本对照文档以作者预印版（MIT，40页）为母本。数学公式不逐字誊抄，以 ⟨公式(编号)⟩ 指向原文；术语首次出现时括注英文。

## Abstract｜摘要

[EN] We present a general approach for devising high-order accurate finite element methods for the Maxwell's equations based on two different Hamiltonian structures of the Maxwell's equations, namely, the standard formulation of the equations in terms of the electric and magnetic fields, and a wave-like rewriting of the standard formulation in terms of the electric and the magnetic potential fields. For each of these Hamiltonian structures, we introduce spatial discretizations of the Maxwell's equations using mixed finite element, discontinuous Galerkin, and hybridizable discontinuous Galerkin methods to obtain a semi-discrete system of equations which inherit the Hamiltonian structure of the Maxwell's equations.

[中] 我们提出一种一般性构造框架，用于为麦克斯韦方程组设计高精度有限元方法。该框架基于麦克斯韦方程组的两种不同哈密顿结构：其一是以电场与磁场表示的标准形式；其二是把标准形式改写为以电场与磁（矢）势场表示的类波动形式。对每一种哈密顿结构，我们分别用混合有限元方法、间断伽辽金（DG）方法与可杂交间断伽辽金（HDG）方法对麦克斯韦方程组作空间离散，得到继承原方程哈密顿结构的半离散方程组。

[EN] We discretize the resulting semi-discrete system in time by using a symplectic integrator to ensure the conservation properties of the fully discrete system of equations. We show that the methods provide time-invariant, non-drifting approximations of the total electric, magnetic charges, and the total energy. There is a Symplectic DG method for the first formulation [J. Sci. Comput. 35, pp. 241–265, 2008] but all other methods are new. We show that there are no Symplectic HDG methods for the first formulation. In contrast, we devise Symplectic Hamiltonian mixed, DG, and HDG methods for the second formulation.

[中] 随后用辛积分器对半离散系统作时间离散，以保证全离散方程组的守恒性质。我们证明这些方法对总电荷（电与磁）与总能量给出时间不变、无漂移的逼近。对第一种（E-H）形式，此前已有辛 DG 方法（Xu–van der Vegt–Bokhove, 2008），但其余方法均为本文首创；我们还证明：**对第一种形式不存在辛 HDG 方法**。与此相对，对第二种（E-A）形式，我们构造出了辛哈密顿混合、DG 与 HDG 全套方法。

[EN] For the Symplectic HDG method, we present numerical experiments which confirm its optimal orders of convergence for all variables and its conservation properties for the total linear and angular momenta, the electric and magnetic charges, as well as the total energy. Finally, we discuss the extension of our results to other boundary conditions and to numerical schemes defined by different weak formulations.

[中] 针对辛 HDG 方法，我们给出数值实验，证实其所有变量都达到最优收敛阶，并且总动量（线动量与角动量）、电荷（电与磁）以及总能量均具有守恒性质。最后，我们讨论了结果向其他边界条件、以及由不同弱形式定义的数值格式的推广。

## 1. Introduction｜引言

[EN] This paper is part of a series devoted to the development of what can be called the Symplectic Hamiltonian (SH) finite element methods. These methods are developed for time-dependent partial differential equations (PDEs) with Hamiltonian structure. To obtain the methods, we first discretize the governing equations in space by using a finite element method which is devised to produce a system of ordinary differential equations (ODEs) with Hamiltonian structure. Then, we apply a symplectic, time-marching scheme to the system of ODEs in order to ensure that the discrete Hamiltonian (the discrete energy) is either perfectly conserved or does not drift in time. Arbitrary high-order accuracy in both time and space can be achieved by these methods.

[中] 本文是"辛哈密顿（SH）有限元方法"系列工作的第三篇。该类方法面向具有哈密顿结构的含时偏微分方程（PDE）：先用专门设计的有限元方法做空间离散，使得到的常微分方程（ODE）组仍具哈密顿结构；再对 ODE 组施加辛时间推进格式，使离散哈密顿量（离散能量）被严格守恒或随时间不漂移。此类方法在时间与空间上都可达到任意高阶精度。

[EN] Several symplectic Hamiltonian finite element methods were introduced for the acoustic wave equation (2017), and for the equations of linear elastodynamics (2021). In particular, the first HDG methods for the acoustic wave equation displaying a constant or non-drifting discrete energy, and the first HDG methods for linear elastodynamics conserving both the global linear and angular momentum and displaying a constant or non-drifting discrete energy, were devised there.

[中] 系列前两篇分别处理声波方程（2017）与线弹性动力学方程（2021）：前者首次给出离散能量恒定或无漂移的声波 HDG 方法；后者首次给出同时守恒全局线动量与角动量、且离散能量恒定或无漂移的线弹性动力学 HDG 方法。

[EN] In this paper, we continue this effort and develop SH finite element methods for the Maxwell's equations in a polyhedral domain Ω: ⟨公式(1a)–(1f)：ε ∂ₜE = ∇×H − J；μ ∂ₜH = −∇×E；∇·(εE)=ρ；∇·(μH)=0；边界条件 n×E=g_E；初始条件 E=E₀, H=H₀⟩. Here E and H are the electric and magnetic fields; ρ and J the scalar charge density and vector current density; ε and μ the electric permittivity and magnetic permeability, assumed positive and time-independent. The speed of light is c := 1/√(εμ).

[中] 本文延续该研究路线，对多面体区域 Ω 上的麦克斯韦方程组发展 SH 有限元方法：⟨公式(1a)–(1f)⟩。其中 E、H 为电磁场，ρ、J 为标量电荷密度与矢量电流密度，ε、μ 为（正的、不依赖时间的）介电常数与磁导率，光速 c := 1/√(εμ)。

[EN]（Table 1：电磁量词汇表）The SH finite element methods devised herein are of arbitrary order of accuracy and are able to approximate well the integral over Ω of each of the quantities in the rich set of conservation laws of the Maxwell's equations listed on Table 2: the linear functionals of total magnetic charge ∫∇·(μH) and total electric charge ∫∇·(εE), and the quadratic functionals of total electromagnetic energy, total linear and angular electromagnetic momenta, total optical chirality χ, its flux X, and the flux of its flux — the latter related to Lipkin's rank-three zilch tensor (1964).

[中]（表1：电磁量词汇表——能量 E=½(εE·E+μH·H)、坡印廷矢量 S=E×H、线动量 P=εE×μH、洛伦兹力 F=ρE+J×μH、角动量 L=x×P、麦克斯韦应力张量 σ，以及与 Lipkin zilch 张量相联系的光学手性量 χ、X 等）本文构造的 SH 有限元方法具有任意阶精度，并能很好地逼近表 2 所列麦克斯韦方程组丰富守恒律中每一个量在 Ω 上的积分：线性的总磁荷与总电荷，以及二次型的总电磁能量、总线动量与角动量、总光学手性 χ 及其通量 X、通量的通量——后者与 Lipkin 1964 年发现的三秩 zilch 张量的守恒律相关。

[EN] We prove that discrete versions of the magnetic and electric charges, and of the energy remain exactly constant or do not drift in time. To the best knowledge of the authors, none of these properties holds for any DG or HDG method for the time-dependent Maxwell's equations in three space dimensions. Moreover, our numerical results show that the conservation laws for the linear and angular momenta are extremely well approximated.

[中] 我们证明：磁荷、电荷与能量的离散版本随时间严格守恒或无漂移。据作者所知，对三维含时麦克斯韦方程组，此前的任何 DG 或 HDG 方法都不具备这些性质。此外，数值结果表明线动量与角动量的守恒律也被极好地逼近。

[EN] The schemes developed here are certainly not the first to maintain a constant discrete total electromagnetic energy — examples include Yee's finite-difference scheme (mid-1960s) and energy-conserved splitting FDTD schemes. However, the SH finite element methods maintain a discrete version of the Hamiltonian structure of the original PDEs, which can be exploited to systematically study the approximation of the functionals displayed on Table 2. The use of symplectic time-marching methods for Hamiltonian ODEs has a long history; SH schemes with finite-difference or finite-volume space discretizations for Maxwell's equations exist, but the schemes presented here are the first SH methods to use mixed, DG or HDG methods.

[中] 本文格式并非第一个保持离散总电磁能量恒定的格式——早在 1960 年代中期的 Yee 时域有限差分（FDTD）格式、以及守恒型分裂 FDTD 格式都能做到。但 SH 有限元方法保持的是原偏微分方程哈密顿结构的离散版本，因而可以系统性地研究表 2 中各泛函的逼近问题。辛时间积分用于哈密顿 ODE 由来已久；对麦克斯韦方程组也有基于有限差分/有限体积的辛格式，但本文是**首批将混合法、DG 与 HDG 用于麦克斯韦方程组的 SH 方法**。

[EN]（与 Fu–Shu 2019 的比较）In the recent work on new DG discretizations of linear, symmetric hyperbolic systems which conserve exactly the energy, the methods rely on high-order accurate energy-conserving time-marching methods whereas our methods rely on symplectic methods. Also, those methods use twice as many variables as ours. On the other hand, our methods can only be applied to equations with Hamiltonian structure, whereas theirs can be applied to any linear, symmetric hyperbolic system.

[中]（与 Fu–Shu 2019 的比较）近期有针对线性对称双曲系统（含麦克斯韦方程）的严格能量守恒 DG 离散：它们依赖高精度能量守恒时间推进，而本文依赖辛方法；且那些方法所需变量数是本文的两倍。反过来说，本文方法只适用于具有哈密顿结构的方程，而 Fu–Shu 方法适用于任何线性对称双曲系统——两者互有短长。

[EN] The SH finite element schemes are devised in two ways, each associated with a different Hamiltonian structure. The first is associated with the original form of the equations (1), which we call the E-H formulation. Standard DG methods for this formulation do not make use of the Hamiltonian structure; they use the fact that the equations constitute a symmetric hyperbolic system, which naturally results in dissipative methods that do not conserve the total energy. We show how to take advantage of the Hamiltonian structure of the original Maxwell's equations: such methods can be obtained with a mixed method, or with a DG method using alternating fluxes. However, it is not possible to obtain Symplectic HDG methods for this formulation. This motivates the second way.

[中] SH 有限元格式的构造有两条路径，各对应一种哈密顿结构。第一条对应方程组(1)的原始形式，称为 **E-H 形式**。该形式下的标准 DG 方法并未利用哈密顿结构，而是利用方程组构成对称双曲系统这一事实，这自然导致耗散的、不守恒总能量的方法。本文展示如何利用原始麦克斯韦方程组的哈密顿结构：用混合法、或用交替通量（alternating fluxes）的 DG 方法可以做到；但对这一形式**无法**得到辛 HDG 方法——这正是引出第二条路径的动因。

[EN] The second is associated to a rewriting of the E-H formulation, which we call the E-A formulation: ⟨公式(2a)–(2e)：∂ₜA = −E；ε ∂ₜE = ∇×(μ⁻¹∇×A) − J；∇·(εE)=ρ；n×A=g_A；E=E₀, A=A₀⟩, where A is a magnetic potential (μH = ∇×A) and g_A(t) := −∫₀ᵗ g_E. The above system has a different Hamiltonian structure, associated to a wave equation for A. We shall devise a new class of mixed, DG and HDG methods providing time-invariant non-drifting approximations of the E-A formulation.

[中] 第二条路径对应 E-H 形式的一种改写，称为 **E-A 形式**：⟨公式(2a)–(2e)⟩，其中 A 是磁矢势（μH = ∇×A），g_A(t) := −∫₀ᵗ g_E。该系统具有不同的哈密顿结构，与 A 的波动方程相联系。我们将为此构造全新的一类混合、DG 与 HDG 方法，使 E-A 形式的逼近时间不变、无漂移。

[EN] The remaining of the paper is organized as follows. Section 2 discusses the two Hamiltonian structures; Section 3 presents the spatial discretization methods; Section 4 proves they result in ODEs with Hamiltonian structure and proves the corresponding conservation laws; Section 5 presents the fully discrete SH methods (for an HDG method for the E-A formulation); Section 6 explores convergence and conservation; Section 7 discusses other boundary conditions and weak formulations.

[中] 全文结构：第 2 章详述两种哈密顿结构；第 3 章给出空间离散方法；第 4 章证明半离散格式构成哈密顿动力系统并证明相应守恒律；第 5 章针对 E-A 形式的 HDG 方法给出全离散 SH 格式；第 6 章考察收敛性与守恒性；第 7 章讨论其他边界条件与不同弱形式下的方法构造。
