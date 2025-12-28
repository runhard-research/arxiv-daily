# arXiv Daily Papers

_Last updated: 2025-12-28_

---

## Computer Vision
<!-- START:vision -->
_No papers found._
<!-- END:vision -->

## Large Language Models
<!-- START:llm -->
### ReaSeq: Unleashing World Knowledge via Reasoning for Sequential Modeling
- **arXiv**: http://arxiv.org/abs/2512.21257v1
- **Summary**:
  - Industrial recommender systems face two fundamental limitations under the log-driven paradigm: (1) knowledge poverty in ID-based item representations that causes brittle interest modeling under data sparsity, and (2) systemic blindness to beyond-log user interests that constrains model performance within platform boundaries.
  - These limitations stem from an over-reliance on shallow interaction statistics and close-looped feedback while neglecting the rich world knowledge about product semantics and cross-domain behavioral patterns that Large Language Models have learned from vast corpora.

### Rethinking Supervised Fine-Tuning: Emphasizing Key Answer Tokens for Improved LLM Accuracy
- **arXiv**: http://arxiv.org/abs/2512.21017v1
- **Summary**:
  - With the rapid advancement of Large Language Models (LLMs), the Chain-of-Thought (CoT) component has become significant for complex reasoning tasks.
  - However, in conventional Supervised Fine-Tuning (SFT), the model could allocate disproportionately more attention to CoT sequences with excessive length.

### Automatic Replication of LLM Mistakes in Medical Conversations
- **arXiv**: http://arxiv.org/abs/2512.20983v1
- **Summary**:
  - Large language models (LLMs) are increasingly evaluated in clinical settings using multi-dimensional rubrics which quantify reasoning quality, safety, and patient-centeredness.
  - Yet, replicating specific mistakes in other LLM models is not straightforward and often requires manual effort.

### Reflection Pretraining Enables Token-Level Self-Correction in Biological Sequence Models
- **arXiv**: http://arxiv.org/abs/2512.20954v1
- **Summary**:
  - Chain-of-Thought (CoT) prompting has significantly advanced task-solving capabilities in natural language processing with large language models.
  - Unlike standard prompting, CoT encourages the model to generate intermediate reasoning steps, non-answer tokens, that help guide the model toward more accurate final outputs.

### Where Did This Sentence Come From? Tracing Provenance in LLM Reasoning Distillation
- **arXiv**: http://arxiv.org/abs/2512.20908v1
- **Summary**:
  - Reasoning distillation has attracted increasing attention.
  - It typically leverages a large teacher model to generate reasoning paths, which are then used to fine-tune a student model so that it mimics the teacher's behavior in training contexts.

### MediEval: A Unified Medical Benchmark for Patient-Contextual and Knowledge-Grounded Reasoning in LLMs
- **arXiv**: http://arxiv.org/abs/2512.20822v1
- **Summary**:
  - Large Language Models (LLMs) are increasingly applied to medicine, yet their adoption is limited by concerns over reliability and safety.
  - Existing evaluations either test factual medical knowledge in isolation or assess patient-level reasoning without verifying correctness, leaving a critical gap.

### Semantic Deception: When Reasoning Models Can't Compute an Addition
- **arXiv**: http://arxiv.org/abs/2512.20812v1
- **Summary**:
  - Large language models (LLMs) are increasingly used in situations where human values are at stake, such as decision-making tasks that involve reasoning when performed by humans.
  - We investigate the so-called reasoning capabilities of LLMs over novel symbolic representations by introducing an experimental framework that tests their ability to process and manipulate unfamiliar symbols.

<!-- END:llm -->

## Multimodal (MLLM)
<!-- START:mllm -->
### Beyond Memorization: A Multi-Modal Ordinal Regression Benchmark to Expose Popularity Bias in Vision-Language Models
- **arXiv**: http://arxiv.org/abs/2512.21337v1
- **Summary**:
  - We expose a significant popularity bias in state-of-the-art vision-language models (VLMs), which achieve up to 34% higher accuracy on famous buildings compared to ordinary ones, indicating a reliance on memorization over generalizable understanding.
  - To systematically investigate this, we introduce the largest open benchmark for this task: the YearGuessr dataset, a collection of 55,546 building images with multi-modal attributes from 157 countries, annotated with continuous ordinal labels of their construction year (1001-2024), GPS data, and page-view counts as a proxy for popularity.

### Leveraging Lightweight Entity Extraction for Scalable Event-Based Image Retrieval
- **arXiv**: http://arxiv.org/abs/2512.21221v1
- **Summary**:
  - Retrieving images from natural language descriptions is a core task at the intersection of computer vision and natural language processing, with wide-ranging applications in search engines, media archiving, and digital content management.
  - However, real-world image-text retrieval remains challenging due to vague or context-dependent queries, linguistic variability, and the need for scalable solutions.

### RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic
- **arXiv**: http://arxiv.org/abs/2512.21220v1
- **Summary**:
  - Embodied agents powered by vision-language models (VLMs) are increasingly capable of executing complex real-world tasks, yet they remain vulnerable to hazardous instructions that may trigger unsafe behaviors.
  - Runtime safety guardrails, which intercept hazardous actions during task execution, offer a promising solution due to their flexibility.

### Latent Implicit Visual Reasoning
- **arXiv**: http://arxiv.org/abs/2512.21218v1
- **Summary**:
  - While Large Multimodal Models (LMMs) have made significant progress, they remain largely text-centric, relying on language as their core reasoning modality.
  - As a result, they are limited in their ability to handle reasoning tasks that are predominantly visual.

### VisRes Bench: On Evaluating the Visual Reasoning Capabilities of VLMs
- **arXiv**: http://arxiv.org/abs/2512.21194v1
- **Summary**:
  - Vision-Language Models (VLMs) have achieved remarkable progress across tasks such as visual question answering and image captioning.
  - Yet, the extent to which these models perform visual reasoning as opposed to relying on linguistic priors remains unclear.

### MarineEval: Assessing the Marine Intelligence of Vision-Language Models
- **arXiv**: http://arxiv.org/abs/2512.21126v1
- **Summary**:
  - We have witnessed promising progress led by large language models (LLMs) and further vision language models (VLMs) in handling various queries as a general-purpose assistant.
  - VLMs, as a bridge to connect the visual world and language corpus, receive both visual content and various text-only user instructions to generate corresponding responses.

<!-- END:mllm -->

## Vision + Robotics
<!-- START:vision_ro -->
### Fast SAM2 with Text-Driven Token Pruning
- **arXiv**: http://arxiv.org/abs/2512.21333v1
- **Summary**:
  - Segment Anything Model 2 (SAM2), a vision foundation model has significantly advanced in prompt-driven video object segmentation, yet their practical deployment remains limited by the high computational and memory cost of processing dense visual tokens across time.
  - The SAM2 pipelines typically propagate all visual tokens produced by the image encoder through downstream temporal reasoning modules, regardless of their relevance to the target object, resulting in reduced scalability due to quadratic memory attention overhead.

### ACD: Direct Conditional Control for Video Diffusion Models via Attention Supervision
- **arXiv**: http://arxiv.org/abs/2512.21268v1
- **Summary**:
  - Controllability is a fundamental requirement in video synthesis, where accurate alignment with conditioning signals is essential.
  - Existing classifier-free guidance methods typically achieve conditioning indirectly by modeling the joint distribution of data and conditions, which often results in limited controllability over the specified conditions.

### LookPlanGraph: Embodied Instruction Following Method with VLM Graph Augmentation
- **arXiv**: http://arxiv.org/abs/2512.21243v1
- **Summary**:
  - Methods that use Large Language Models (LLM) as planners for embodied instruction following tasks have become widespread.
  - To successfully complete tasks, the LLM must be grounded in the environment in which the robot operates.

### RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic
- **arXiv**: http://arxiv.org/abs/2512.21220v1
- **Summary**:
  - Embodied agents powered by vision-language models (VLMs) are increasingly capable of executing complex real-world tasks, yet they remain vulnerable to hazardous instructions that may trigger unsafe behaviors.
  - Runtime safety guardrails, which intercept hazardous actions during task execution, offer a promising solution due to their flexibility.

### Latent Implicit Visual Reasoning
- **arXiv**: http://arxiv.org/abs/2512.21218v1
- **Summary**:
  - While Large Multimodal Models (LMMs) have made significant progress, they remain largely text-centric, relying on language as their core reasoning modality.
  - As a result, they are limited in their ability to handle reasoning tasks that are predominantly visual.

### VisRes Bench: On Evaluating the Visual Reasoning Capabilities of VLMs
- **arXiv**: http://arxiv.org/abs/2512.21194v1
- **Summary**:
  - Vision-Language Models (VLMs) have achieved remarkable progress across tasks such as visual question answering and image captioning.
  - Yet, the extent to which these models perform visual reasoning as opposed to relying on linguistic priors remains unclear.

### ORCA: Object Recognition and Comprehension for Archiving Marine Species
- **arXiv**: http://arxiv.org/abs/2512.21150v1
- **Summary**:
  - Marine visual understanding is essential for monitoring and protecting marine ecosystems, enabling automatic and scalable biological surveys.
  - However, progress is hindered by limited training data and the lack of a systematic task formulation that aligns domain-specific marine challenges with well-defined computer vision tasks, thereby limiting effective model application.

### MarineEval: Assessing the Marine Intelligence of Vision-Language Models
- **arXiv**: http://arxiv.org/abs/2512.21126v1
- **Summary**:
  - We have witnessed promising progress led by large language models (LLMs) and further vision language models (VLMs) in handling various queries as a general-purpose assistant.
  - VLMs, as a bridge to connect the visual world and language corpus, receive both visual content and various text-only user instructions to generate corresponding responses.

<!-- END:vision_ro -->
