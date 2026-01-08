# arXiv Daily Papers

_Last updated: 2026-01-08_

---

## Computer Vision
<!-- START:vision -->
_No papers found._
<!-- END:vision -->

## Large Language Models
<!-- START:llm -->
### All That Glisters Is Not Gold: A Benchmark for Reference-Free Counterfactual Financial Misinformation Detection
- **arXiv**: http://arxiv.org/abs/2601.04160v1
- **Summary**:
  - We introduce RFC Bench, a benchmark for evaluating large language models on financial misinformation under realistic news.
  - RFC Bench operates at the paragraph level and captures the contextual complexity of financial news where meaning emerges from dispersed cues.

### KDCM: Reducing Hallucination in LLMs through Explicit Reasoning Structures
- **arXiv**: http://arxiv.org/abs/2601.04086v1
- **Summary**:
  - To mitigate hallucinations in large language models (LLMs), we propose a framework that focuses on errors induced by prompts.
  - Our method extends a chain-style knowledge distillation approach by incorporating a programmable module that guides knowledge graph exploration.

### Modular Prompt Optimization: Optimizing Structured Prompts with Section-Local Textual Gradients
- **arXiv**: http://arxiv.org/abs/2601.04055v1
- **Summary**:
  - Prompt quality plays a central role in controlling the behavior, reliability, and reasoning performance of large language models (LLMs), particularly for smaller open-source instruction-tuned models that depend heavily on explicit structure.
  - While recent work has explored automatic prompt optimization using textual gradients and self-refinement, most existing methods treat prompts as monolithic blocks of text, making it difficult to localize errors, preserve critical instructions, or prevent uncontrolled prompt growth.

### Benchmark^2: Systematic Evaluation of LLM Benchmarks
- **arXiv**: http://arxiv.org/abs/2601.03986v1
- **Summary**:
  - The rapid proliferation of benchmarks for evaluating large language models (LLMs) has created an urgent need for systematic methods to assess benchmark quality itself.
  - We propose Benchmark^2, a comprehensive framework comprising three complementary metrics: (1) Cross-Benchmark Ranking Consistency, measuring whether a benchmark produces model rankings aligned with peer benchmarks; (2) Discriminability Score, quantifying a benchmark's ability to differentiate between models; and (3) Capability Alignment Deviation, identifying problematic instances where stronger models fail but weaker models succeed within the same model family.

### Large-Scale Aspect-Based Sentiment Analysis with Reasoning-Infused LLMs
- **arXiv**: http://arxiv.org/abs/2601.03940v1
- **Summary**:
  - We introduce Arctic-ABSA, a collection of powerful models for real-life aspect-based sentiment analysis (ABSA).
  - Our models are tailored to commercial needs, trained on a large corpus of public data alongside carefully generated synthetic data, resulting in a dataset 20 times larger than SemEval14.

### Adaptive-Boundary-Clipping GRPO: Ensuring Bounded Ratios for Stable and Generalizable Training
- **arXiv**: http://arxiv.org/abs/2601.03895v1
- **Summary**:
  - Group Relative Policy Optimization (GRPO) has emerged as a popular algorithm for reinforcement learning with large language models (LLMs).
  - However, upon analyzing its clipping mechanism, we argue that it is suboptimal in certain scenarios.

<!-- END:llm -->

## Multimodal (MLLM)
<!-- START:mllm -->
### Scanner-Induced Domain Shifts Undermine the Robustness of Pathology Foundation Models
- **arXiv**: http://arxiv.org/abs/2601.04163v1
- **Summary**:
  - Pathology foundation models (PFMs) have become central to computational pathology, aiming to offer general encoders for feature extraction from whole-slide images (WSIs).
  - Despite strong benchmark performance, PFM robustness to real-world technical domain shifts, such as variability from whole-slide scanner devices, remains poorly understood.

### Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning
- **arXiv**: http://arxiv.org/abs/2601.04153v1
- **Summary**:
  - Direct Preference Optimization (DPO) has recently improved Text-to-Video (T2V) generation by enhancing visual fidelity and text alignment.
  - However, current methods rely on non-differentiable preference signals from human annotations or learned reward models.

### GeoReason: Aligning Thinking And Answering In Remote Sensing Vision-Language Models Via Logical Consistency Reinforcement Learning
- **arXiv**: http://arxiv.org/abs/2601.04118v1
- **Summary**:
  - The evolution of Remote Sensing Vision-Language Models(RS-VLMs) emphasizes the importance of transitioning from perception-centric recognition toward high-level deductive reasoning to enhance cognitive reliability in complex spatial tasks.
  - However, current models often suffer from logical hallucinations, where correct answers are derived from flawed reasoning chains or rely on positional shortcuts rather than spatial logic.

### CLAP: Contrastive Latent Action Pretraining for Learning Vision-Language-Action Models from Human Videos
- **arXiv**: http://arxiv.org/abs/2601.04061v1
- **Summary**:
  - Generalist Vision-Language-Action models are currently hindered by the scarcity of robotic data compared to the abundance of human video demonstrations.
  - Existing Latent Action Models attempt to leverage video data but often suffer from visual entanglement, capturing noise rather than manipulation skills.

### FocusUI: Efficient UI Grounding via Position-Preserving Visual Token Selection
- **arXiv**: http://arxiv.org/abs/2601.03928v1
- **Summary**:
  - Vision-Language Models (VLMs) have shown remarkable performance in User Interface (UI) grounding tasks, driven by their ability to process increasingly high-resolution screenshots.
  - However, screenshots are tokenized into thousands of visual tokens (e.g., about 4700 for 2K resolution), incurring significant computational overhead and diluting attention.

<!-- END:mllm -->

## Vision + Robotics
<!-- START:vision_ro -->
### Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning
- **arXiv**: http://arxiv.org/abs/2601.04153v1
- **Summary**:
  - Direct Preference Optimization (DPO) has recently improved Text-to-Video (T2V) generation by enhancing visual fidelity and text alignment.
  - However, current methods rely on non-differentiable preference signals from human annotations or learned reward models.

### CLAP: Contrastive Latent Action Pretraining for Learning Vision-Language-Action Models from Human Videos
- **arXiv**: http://arxiv.org/abs/2601.04061v1
- **Summary**:
  - Generalist Vision-Language-Action models are currently hindered by the scarcity of robotic data compared to the abundance of human video demonstrations.
  - Existing Latent Action Models attempt to leverage video data but often suffer from visual entanglement, capturing noise rather than manipulation skills.

### Stable Language Guidance for Vision-Language-Action Models
- **arXiv**: http://arxiv.org/abs/2601.04052v1
- **Summary**:
  - Vision-Language-Action (VLA) models have demonstrated impressive capabilities in generalized robotic control; however, they remain notoriously brittle to linguistic perturbations.
  - We identify a critical ``modality collapse'' phenomenon where strong visual priors overwhelm sparse linguistic signals, causing agents to overfit to specific instruction phrasings while ignoring the underlying semantic intent.

### CoINS: Counterfactual Interactive Navigation via Skill-Aware VLM
- **arXiv**: http://arxiv.org/abs/2601.03956v1
- **Summary**:
  - Recent Vision-Language Models (VLMs) have demonstrated significant potential in robotic planning.
  - However, they typically function as semantic reasoners, lacking an intrinsic understanding of the specific robot's physical capabilities.

### ResTok: Learning Hierarchical Residuals in 1D Visual Tokenizers for Autoregressive Image Generation
- **arXiv**: http://arxiv.org/abs/2601.03955v1
- **Summary**:
  - Existing 1D visual tokenizers for autoregressive (AR) generation largely follow the design principles of language modeling, as they are built directly upon transformers whose priors originate in language, yielding single-hierarchy latent tokens and treating visual data as flat sequential token streams.
  - However, this language-like formulation overlooks key properties of vision, particularly the hierarchical and residual network designs that have long been essential for convergence and efficiency in visual models.

### FocusUI: Efficient UI Grounding via Position-Preserving Visual Token Selection
- **arXiv**: http://arxiv.org/abs/2601.03928v1
- **Summary**:
  - Vision-Language Models (VLMs) have shown remarkable performance in User Interface (UI) grounding tasks, driven by their ability to process increasingly high-resolution screenshots.
  - However, screenshots are tokenized into thousands of visual tokens (e.g., about 4700 for 2K resolution), incurring significant computational overhead and diluting attention.

### An Event-Based Opto-Tactile Skin
- **arXiv**: http://arxiv.org/abs/2601.03907v1
- **Summary**:
  - This paper presents a neuromorphic, event-driven tactile sensing system for soft, large-area skin, based on the Dynamic Vision Sensors (DVS) integrated with a flexible silicone optical waveguide skin.
  - Instead of repetitively scanning embedded photoreceivers, this design uses a stereo vision setup comprising two DVS cameras looking sideways through the skin.

### A Comparative Study of 3D Model Acquisition Methods for Synthetic Data Generation of Agricultural Products
- **arXiv**: http://arxiv.org/abs/2601.03784v1
- **Summary**:
  - In the manufacturing industry, computer vision systems based on artificial intelligence (AI) are widely used to reduce costs and increase production.
  - Training these AI models requires a large amount of training data that is costly to acquire and annotate, especially in high-variance, low-volume manufacturing environments.

### PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation
- **arXiv**: http://arxiv.org/abs/2601.03782v1
- **Summary**:
  - Humans anticipate, from a glance and a contemplated action of their bodies, how the 3D world will respond, a capability that is equally vital for robotic manipulation.
  - We introduce PointWorld, a large pre-trained 3D world model that unifies state and action in a shared 3D space as 3D point flows: given one or few RGB-D images and a sequence of low-level robot action commands, PointWorld forecasts per-pixel displacements in 3D that respond to the given actions.

<!-- END:vision_ro -->
