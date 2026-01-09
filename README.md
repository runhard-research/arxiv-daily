# arXiv Daily Papers

_Last updated: 2026-01-09_

---

## Computer Vision
<!-- START:vision -->
_No papers found._
<!-- END:vision -->

## Large Language Models
<!-- START:llm -->
### RelayLLM: Efficient Reasoning via Collaborative Decoding
- **arXiv**: http://arxiv.org/abs/2601.05167v1
- **Summary**:
  - Large Language Models (LLMs) for complex reasoning is often hindered by high computational costs and latency, while resource-efficient Small Language Models (SLMs) typically lack the necessary reasoning capacity.
  - Existing collaborative approaches, such as cascading or routing, operate at a coarse granularity by offloading entire queries to LLMs, resulting in significant computational waste when the SLM is capable of handling the majority of reasoning steps.

### Agent-as-a-Judge
- **arXiv**: http://arxiv.org/abs/2601.05111v1
- **Summary**:
  - LLM-as-a-Judge has revolutionized AI evaluation by leveraging large language models for scalable assessments.
  - However, as evaluands become increasingly complex, specialized, and multi-step, the reliability of LLM-as-a-Judge has become constrained by inherent biases, shallow single-pass reasoning, and the inability to verify assessments against real-world observations.

### Token-Level LLM Collaboration via FusionRoute
- **arXiv**: http://arxiv.org/abs/2601.05106v1
- **Summary**:
  - Large language models (LLMs) exhibit strengths across diverse domains.
  - However, achieving strong performance across these domains with a single general-purpose model typically requires scaling to sizes that are prohibitively expensive to train and deploy.

### Reinforced Efficient Reasoning via Semantically Diverse Exploration
- **arXiv**: http://arxiv.org/abs/2601.05053v1
- **Summary**:
  - Reinforcement learning with verifiable rewards (RLVR) has proven effective in enhancing the reasoning of large language models (LLMs).
  - Monte Carlo Tree Search (MCTS)-based extensions improve upon vanilla RLVR (e.g., GRPO) by providing tree-based reasoning rollouts that enable fine-grained and segment-level credit assignment.

### Hán Dān Xué Bù (Mimicry) or Qīng Chū Yú Lán (Mastery)? A Cognitive Perspective on Reasoning Distillation in Large Language Models
- **arXiv**: http://arxiv.org/abs/2601.05019v1
- **Summary**:
  - Recent Large Reasoning Models trained via reinforcement learning exhibit a "natural" alignment with human cognitive costs.
  - However, we show that the prevailing paradigm of reasoning distillation -- training student models to mimic these traces via Supervised Fine-Tuning (SFT) -- fails to transmit this cognitive structure.

### Text as a Universal Interface for Transferable Personalization
- **arXiv**: http://arxiv.org/abs/2601.04963v1
- **Summary**:
  - We study the problem of personalization in large language models (LLMs).
  - Prior work predominantly represents user preferences as implicit, model-specific vectors or parameters, yielding opaque ``black-box'' profiles that are difficult to interpret and transfer across models and tasks.

### GenProve: Learning to Generate Text with Fine-Grained Provenance
- **arXiv**: http://arxiv.org/abs/2601.04932v1
- **Summary**:
  - Large language models (LLM) often hallucinate, and while adding citations is a common solution, it is frequently insufficient for accountability as users struggle to verify how a cited source supports a generated claim.
  - Existing methods are typically coarse-grained and fail to distinguish between direct quotes and complex reasoning.

<!-- END:llm -->

## Multimodal (MLLM)
<!-- START:mllm -->
### RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation
- **arXiv**: http://arxiv.org/abs/2601.05241v1
- **Summary**:
  - The diversity, quantity, and quality of manipulation data are critical for training effective robot policies.
  - However, due to hardware and physical setup constraints, collecting large-scale real-world manipulation data remains difficult to scale across diverse environments.

### Mechanisms of Prompt-Induced Hallucination in Vision-Language Models
- **arXiv**: http://arxiv.org/abs/2601.05201v1
- **Summary**:
  - Large vision-language models (VLMs) are highly capable, yet often hallucinate by favoring textual prompts over visual evidence.
  - We study this failure mode in a controlled object-counting setting, where the prompt overstates the number of objects in the image (e.g., asking a model to describe four waterlilies when only three are present).

### Vision-Language Introspection: Mitigating Overconfident Hallucinations in MLLMs via Interpretable Bi-Causal Steering
- **arXiv**: http://arxiv.org/abs/2601.05159v1
- **Summary**:
  - Object hallucination critically undermines the reliability of Multimodal Large Language Models, often stemming from a fundamental failure in cognitive introspection, where models blindly trust linguistic priors over specific visual evidence.
  - Existing mitigations remain limited: contrastive decoding approaches operate superficially without rectifying internal semantic misalignments, while current latent steering methods rely on static vectors that lack instance-specific precision.

### A Lightweight and Explainable Vision-Language Framework for Crop Disease Visual Question Answering
- **arXiv**: http://arxiv.org/abs/2601.05143v1
- **Summary**:
  - Visual question answering for crop disease analysis requires accurate visual understanding and reliable language generation.
  - This work presents a lightweight vision-language framework for crop and disease identification from leaf images.

### VERSE: Visual Embedding Reduction and Space Exploration. Clustering-Guided Insights for Training Data Enhancement in Visually-Rich Document Understanding
- **arXiv**: http://arxiv.org/abs/2601.05125v1
- **Summary**:
  - This work introduces VERSE, a methodology for analyzing and improving Vision-Language Models applied to Visually-rich Document Understanding by exploring their visual embedding space.
  - VERSE enables the visualization of latent representations, supporting the assessment of model feasibility.

<!-- END:mllm -->

## Vision + Robotics
<!-- START:vision_ro -->
### QNeRF: Neural Radiance Fields on a Simulated Gate-Based Quantum Computer
- **arXiv**: http://arxiv.org/abs/2601.05250v1
- **Summary**:
  - Recently, Quantum Visual Fields (QVFs) have shown promising improvements in model compactness and convergence speed for learning the provided 2D or 3D signals.
  - Meanwhile, novel-view synthesis has seen major advances with Neural Radiance Fields (NeRFs), where models learn a compact representation from 2D images to render 3D scenes, albeit at the cost of larger models and intensive training.

### LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model
- **arXiv**: http://arxiv.org/abs/2601.05248v1
- **Summary**:
  - Vision-Language-Action (VLA) models have recently demonstrated strong generalization capabilities in robotic manipulation.
  - Some existing VLA approaches attempt to improve action accuracy by explicitly generating linguistic reasoning traces or future visual observations before action execution.

### Pixel-Perfect Visual Geometry Estimation
- **arXiv**: http://arxiv.org/abs/2601.05246v1
- **Summary**:
  - Recovering clean and accurate geometry from images is essential for robotics and augmented reality.
  - However, existing geometry foundation models still suffer severely from flying pixels and the loss of fine details.

### RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation
- **arXiv**: http://arxiv.org/abs/2601.05241v1
- **Summary**:
  - The diversity, quantity, and quality of manipulation data are critical for training effective robot policies.
  - However, due to hardware and physical setup constraints, collecting large-scale real-world manipulation data remains difficult to scale across diverse environments.

### Mechanisms of Prompt-Induced Hallucination in Vision-Language Models
- **arXiv**: http://arxiv.org/abs/2601.05201v1
- **Summary**:
  - Large vision-language models (VLMs) are highly capable, yet often hallucinate by favoring textual prompts over visual evidence.
  - We study this failure mode in a controlled object-counting setting, where the prompt overstates the number of objects in the image (e.g., asking a model to describe four waterlilies when only three are present).

### Vision-Language Introspection: Mitigating Overconfident Hallucinations in MLLMs via Interpretable Bi-Causal Steering
- **arXiv**: http://arxiv.org/abs/2601.05159v1
- **Summary**:
  - Object hallucination critically undermines the reliability of Multimodal Large Language Models, often stemming from a fundamental failure in cognitive introspection, where models blindly trust linguistic priors over specific visual evidence.
  - Existing mitigations remain limited: contrastive decoding approaches operate superficially without rectifying internal semantic misalignments, while current latent steering methods rely on static vectors that lack instance-specific precision.

### A Lightweight and Explainable Vision-Language Framework for Crop Disease Visual Question Answering
- **arXiv**: http://arxiv.org/abs/2601.05143v1
- **Summary**:
  - Visual question answering for crop disease analysis requires accurate visual understanding and reliable language generation.
  - This work presents a lightweight vision-language framework for crop and disease identification from leaf images.

### VERSE: Visual Embedding Reduction and Space Exploration. Clustering-Guided Insights for Training Data Enhancement in Visually-Rich Document Understanding
- **arXiv**: http://arxiv.org/abs/2601.05125v1
- **Summary**:
  - This work introduces VERSE, a methodology for analyzing and improving Vision-Language Models applied to Visually-rich Document Understanding by exploring their visual embedding space.
  - VERSE enables the visualization of latent representations, supporting the assessment of model feasibility.

### UniLiPs: Unified LiDAR Pseudo-Labeling with Geometry-Grounded Dynamic Scene Decomposition
- **arXiv**: http://arxiv.org/abs/2601.05105v1
- **Summary**:
  - Unlabeled LiDAR logs, in autonomous driving applications, are inherently a gold mine of dense 3D geometry hiding in plain sight - yet they are almost useless without human labels, highlighting a dominant cost barrier for autonomous-perception research.
  - In this work we tackle this bottleneck by leveraging temporal-geometric consistency across LiDAR sweeps to lift and fuse cues from text and 2D vision foundation models directly into 3D, without any manual input.

### From Understanding to Engagement: Personalized pharmacy Video Clips via Vision Language Models (VLMs)
- **arXiv**: http://arxiv.org/abs/2601.05059v1
- **Summary**:
  - Vision Language Models (VLMs) are poised to revolutionize the digital transformation of pharmacyceutical industry by enabling intelligent, scalable, and automated multi-modality content processing.
  - Traditional manual annotation of heterogeneous data modalities (text, images, video, audio, and web links), is prone to inconsistencies, quality degradation, and inefficiencies in content utilization.

<!-- END:vision_ro -->
