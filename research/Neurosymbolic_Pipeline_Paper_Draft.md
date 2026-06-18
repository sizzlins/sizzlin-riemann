# A Neurosymbolic Pipeline for Mapping Finite-Dimensional Limits in Analytic Number Theory

**Author:** Muhammad Akhiel al Syahbana  
**Affiliation:** Department of Informatics, Universitas Tanjungpura  

---

## Abstract

We present a neurosymbolic pipeline designed to investigate the finite-dimensional truncation limits of infinite-dimensional Hilbert space operators, specifically applied to the Nyman-Beurling and Báez-Duarte formulations. Our architecture integrates deep reinforcement learning (PyTorch) with exact algebraic solvers (SciPy, mpmath) and formal verification environments (Lean 4). We demonstrate that finite truncations of the Báez-Duarte measure generate structural noise and indefinite spectral collapse, which standard neural networks misinterpret as trivial solutions when trained without domain-specific prime topology metrics. By projecting onto orthogonal subspaces and performing logarithmically-warped spectral sweeps, we empirically isolate and verify these truncation artifacts. This pipeline highlights the structural limitations of applying bounded computational models to unbounded analytic number theory problems and provides a robust framework for experimental mathematics.

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

### 2.4 Use of Large Language Models

To accelerate the implementation of the pipeline, Large Language Models (LLMs) were utilized strictly as coding assistants. The human author served as the principal systems architect—defining the mathematical goals, curating the logic flow, and vetting all algorithmic outputs—while LLMs were prompted to generate boilerplate syntax for PyTorch and Lean 4 integrations.

## 3. Results

### 3.1 Indefinite Spectral Collapse

When analyzing the exact Vasyunin matrices at finite truncation scales ($N \geq 250$), the system exhibited catastrophic structural failure. The optimization returned negative distances ($d_N^2 < 0$). Spectral decomposition of the matrices revealed the presence of negative eigenvalues (e.g., $\lambda_{\min} \approx -78.85$). This confirms empirically that the finite truncation of the infinite Báez-Duarte operator is fundamentally indefinite. 

### 3.2 Subspace Projection and the Geometric Core

By bypassing raw matrix inversion and projecting the solution onto classical number-theoretic basis vectors (Galerkin projection), we discovered an absolute asymptotic distance floor. The single geometric heuristic $1/k^2$ accounted for roughly 78% of the distance reduction. Expanding the subspace to 12 dimensions using heavily correlated heuristics (such as the divisor function $d(k)/k^2$ and the von Mangoldt function $\Lambda(k)/k^2$) provided negligible improvement, solidifying the $d_N^2 \approx 0.21$ truncation boundary.

### 3.3 Isolation of Truncation Artifacts

Residual vectors from the subspace projection were subjected to a logarithmically-warped spectral sweep. The raw spectrum exhibited a significant resonance spike at $y \approx 11.85$. 

To differentiate genuine arithmetical signal from boundary leakage, we applied standard signal-processing window functions (Blackman and Hann) to the residual vectors prior to the spectral sweep. Both window functions completely obliterated the $y = 11.85$ peak, definitively proving it was an artifact of the rectangular truncation boundary rather than a shifted structural frequency (such as a Riemann zero).

## 4. Discussion

The results demonstrate the inherent danger of applying unconstrained machine learning models to bounded mathematical domains. When evaluated on the bounded $L^2(0,1)$ space (which lacks the logarithmic measure $dt/t^2$), the pipeline found exact $\mathcal{O}(1/N)$ decay governed by Euler's Totient function. However, this was a trivial Fourier approximation representing zero prime topology.

Only by utilizing the exact algebraic solvers and enforcing formal verification constraints were we able to expose the true indefinite nature of the finite Báez-Duarte matrix. The neurosymbolic approach proves that while Transformers are highly capable of finding geometric relationships, they cannot overcome the structural noise generated by amputating an infinite-dimensional operator.

## 5. Conclusion

We have presented a robust neurosymbolic architecture capable of stress-testing the computational limits of analytic number theory formulations. By mapping the truncation cliff of the Báez-Duarte criterion, we empirically verified that finite-dimensional reductions generate indefinite spectral collapse and window-dependent resonance artifacts. Future research in computational number theory must prioritize continuous functional analysis or dynamically shifting $N$-dependent sequences to bypass the limitations of finite matrix regression.

---
*Code Availability: The source code for the Number-Theoretic Transformer, the exact algebraic solvers, and the Lean 4 formalization environments is available at [https://github.com/sizzlins/sizzlin-riemann](https://github.com/sizzlins/sizzlin-riemann).*
