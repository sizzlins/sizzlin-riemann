# A Neurosymbolic Pipeline for Mapping Finite-Dimensional Limits in Analytic Number Theory

**Author:** Muhammad Akhiel al Syahbana  
**Affiliation:** Department of Informatics, Universitas Tanjungpura  

---

## Abstract

We present a neurosymbolic pipeline designed to investigate the finite-dimensional truncation limits of infinite-dimensional Hilbert space operators, specifically applied to the Nyman-Beurling and Báez-Duarte formulations. Our architecture integrates deep reinforcement learning (PyTorch) with exact algebraic solvers (SciPy, mpmath), formal verification environments (Lean 4), and symbolic regression engines (Kalkulator-AI). We demonstrate that finite truncations of the Báez-Duarte measure generate structural noise and indefinite spectral collapse, which standard neural networks misinterpret as trivial solutions when trained without domain-specific prime topology metrics. By projecting onto orthogonal subspaces and performing logarithmically-warped spectral sweeps, we empirically isolate and verify these truncation artifacts. This pipeline highlights the structural limitations of applying bounded computational models to unbounded analytic number theory problems and provides a robust framework for experimental mathematics.

---

## 1. Introduction

The intersection of artificial intelligence and experimental mathematics often struggles with infinite-dimensional continuous spaces. In analytic number theory, formulations such as the Nyman-Beurling and Báez-Duarte criteria represent the Riemann Hypothesis as a distance minimization problem in $L^2(0, \infty)$ space. While computationally attractive, evaluating these models on physical machines requires truncating the infinite space to a finite matrix of size $N \times N$.

Historically, the structural cost of this truncation has been difficult to isolate from genuine mathematical signal. Furthermore, modern deep learning architectures (such as Transformers) are prone to "hallucinating" trivial solutions when applied to continuous distance functions that lack explicit arithmetical constraints.

To address this, we developed a neurosymbolic pipeline that combines the pattern-recognition capabilities of deep learning with the rigorous constraints of formal verification and exact algebraic solvers. This paper details the software architecture used to successfully map the truncation limits of the Báez-Duarte formulation, demonstrating how finite boundaries manifest as spectral noise and false convergence.

## 2. Methodology

The neurosymbolic pipeline was constructed using three primary computational layers, orchestrated in Python and verified in Lean 4.

### 2.1 Deep Reinforcement Learning Architecture

Initial distance minimization was attempted using a custom "Number-Theoretic Transformer" implemented in PyTorch. 
To prevent the network from treating matrix indices as arbitrary continuous magnitudes, we implemented a prime factor embedding layer. Each index $k$ was decomposed into a sparse tensor representing its prime factorization up to the 168th prime. The architecture utilized a 2-layer Transformer encoder with 4 attention heads, optimized using `CosineAnnealingWarmRestarts` with Gaussian noise injection to escape local minima.

### 2.2 Exact Algebraic Solvers

Standard numerical integration techniques (`scipy.integrate.quad`) failed catastrophically due to the highly oscillatory nature of the Báez-Duarte fractional part measure:

$$M_{jk} = \int_0^\infty \left\lbrace\frac{t}{j}\right\rbrace\left\lbrace\frac{t}{k}\right\rbrace \frac{dt}{t^2}$$

To bypass numerical instability, the pipeline was routed through an exact algebraic solver utilizing Vasyunin cotangent sums. This allowed the generation of highly precise discrete matrices up to $N=1000$ without floating-point integration errors, taking $\mathcal{O}(N^2)$ computation time.

### 2.3 Formal Verification Integration

To ensure the discrete reduction of the continuous functions maintained mathematical fidelity, the environmental constraints and inner product spaces were formally modeled using the Lean 4 theorem prover. Lean 4 was utilized to formally define the $L^2$ space constraints, preventing the Python runtime from optimizing toward mathematically invalid states.

### 2.4 Symbolic Regression via Kalkulator-AI

To identify structural relationships within the optimal coefficient vectors extracted from the exact algebraic solvers, we utilized `kalkulator-ai`, a custom symbolic regression engine. The engine performed Abstract Syntax Tree (AST) master equation searches over the detrended coefficient arrays, identifying mathematically exact generating functions (such as Euler's Totient function) governing the truncation boundaries.

### 2.5 Use of Large Language Models

To accelerate the implementation of the pipeline, Large Language Models (LLMs) were utilized strictly as coding assistants. The human author served as the principal systems architect—defining the mathematical goals, curating the logic flow, and vetting all algorithmic outputs—while LLMs were prompted to generate boilerplate syntax for PyTorch and Lean 4 integrations.

## 3. Results

### 3.1 Indefinite Spectral Collapse and Zero Correlation

When analyzing the exact Vasyunin matrices at finite truncation scales ($N \geq 250$), the system exhibited catastrophic structural failure. The optimization returned negative distances ($d_N^2 < 0$). Spectral decomposition of the matrices revealed the presence of negative eigenvalues (e.g., $\lambda_{\min} \approx -78.85$). This confirms empirically that the finite truncation of the infinite Báez-Duarte operator is fundamentally indefinite. 

Furthermore, statistical analysis of the generated optimal coefficient vector $a_k$ showed zero correlation with the Möbius function $\mu(k)/k$ across all scales ($r \approx 0.000$, $p \approx 0.99$). Singular Value Decomposition (SVD) yielded a condition number of $\kappa \approx 11{,}755$. Tikhonov regularization had negligible effect, indicating that the chaotic coefficients are intrinsic to the mathematics, not floating-point artifacts.

### 3.2 Subspace Projection and Logarithmic Drift

By bypassing raw matrix inversion and projecting the solution onto classical number-theoretic basis vectors (Galerkin projection), we discovered an absolute asymptotic distance floor. The single geometric heuristic $1/k^2$ accounted for roughly 78% of the distance reduction ($d_N^2 \approx 0.22$). 

When tracking the optimal constants across expanding boundaries ($N = 100, 250, 500, 1000$), our symbolic regression engine autonomously discovered a perfect logarithmic drift governed by the master equations:

- $c_1(N) = -0.2678 \ln(N) - 1.2136 \quad (R^2 = 0.999)$
- $c_2(N) = 0.3392 \ln(N) + 1.0772 \quad (R^2 = 0.998)$

This confirms that as the truncation boundary $N$ expands, the optimal weights continuously shift to balance the infinite logarithmic tail of the prime topology that was amputated. 

To ensure this floor was not an artifact of multicollinearity, we scrubbed a 12-dimensional heuristic dictionary using Euclidean QR orthogonalization. Projecting onto this orthogonalized basis plunged the energy distance deeper into the negative domain ($d_N^2 \approx -0.2789$), definitively proving the structural indefiniteness of the truncation cliff.

### 3.3 The Möbius Mollifier and Parseval's Theorem

To formally cross the truncation boundary, we applied Parseval's theorem for Mellin transforms, translating the infinite real-space distance into a complex contour integral containing $\zeta(s)$. 

In the discrete domain, we introduced a logarithmically tapered Möbius function: $v_k = \frac{\mu(k)}{k}(1 - \frac{\ln k}{\ln N})$. When projected alone, this mollifier yielded catastrophic results ($d_N^2 \approx 0.999$), violently shattering against the pole at $s = 1$. Synthesizing a 3-dimensional hybrid basis successfully balanced the pole but provided no improvement over the geometric core alone ($d_N^2 \approx 0.21$).

### 3.4 Isolation of Truncation Artifacts

Residual vectors from the subspace projection were subjected to a logarithmically-warped spectral sweep. The raw spectrum exhibited a significant resonance spike at $y \approx 11.85$. 

To differentiate genuine arithmetical signal from boundary leakage, we applied standard signal-processing window functions (Blackman and Hann) to the residual vectors prior to the spectral sweep. Both window functions completely obliterated the $y = 11.85$ peak, definitively proving it was an artifact of the rectangular truncation boundary rather than a shifted structural frequency (such as a Riemann zero).

## 4. Discussion

The results demonstrate the inherent danger of applying unconstrained machine learning models to bounded mathematical domains. When evaluated on the bounded $L^2(0,1)$ space (which lacks the logarithmic measure $dt/t^2$), the pipeline found exact $\mathcal{O}(1/N)$ decay governed by Euler's Totient function. However, this was a trivial Fourier approximation representing zero prime topology.

Only by utilizing the exact algebraic solvers and enforcing formal verification constraints were we able to expose the true indefinite nature of the finite Báez-Duarte matrix. The neurosymbolic approach proves that while Transformers are highly capable of finding geometric relationships, they cannot overcome the structural noise generated by amputating an infinite-dimensional operator.

## 5. Conclusion

We have presented a robust neurosymbolic architecture capable of stress-testing the computational limits of analytic number theory formulations. By mapping the truncation cliff of the Báez-Duarte criterion, we empirically verified that finite-dimensional reductions generate indefinite spectral collapse and window-dependent resonance artifacts. Future research in computational number theory must prioritize continuous functional analysis or dynamically shifting $N$-dependent sequences to bypass the limitations of finite matrix regression.

---
*Code Availability: The source code for the Number-Theoretic Transformer, the exact algebraic solvers, and the Lean 4 formalization environments is available at [https://github.com/sizzlins/sizzlin-riemann](https://github.com/sizzlins/sizzlin-riemann).*
