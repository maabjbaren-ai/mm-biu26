# Product Requirement Document (PRD)
## Project Name: Cross-Lingual Vector Disruption Simulator (Broken Phone)
**Group ID:** mm-biu26  
---

### 1. Introduction & Background
This system is an AI-driven, multi-agent evaluation platform built to simulate and measure semantic degradation across chained translations (English to French to Hebrew to English). Powered by advanced LLM Orchestration, the system acts as a practical experimentation of the Broken Phone phenomenon within a multi-dimensional semantic vector space. 

### 2. Objectives & Value Proposition
* Theoretical Proof: To demonstrate how successive LLM trajectories ("The Forest of Infinite Paths") deviate from the original semantic node as the context undergoes multiple iterations.
* Technical Execution: Deploying a Level 4 Orchestrator architecture that dynamically coordinates functional translation Skills and conducts algorithmic vector distance metrics.
* Managerial Control: Shifting the technical operational paradigm from hardcoded API logic (Rule-Based) into structural prompt-driven agent execution.

### 3. Core System Components & Architecture
The system consists of 4 structural layers mimicking an advanced enterprise AI infrastructure:
1. LLM Core (The Brain): Main processing hub executing translations and dynamic actions.
2. Orchestrator Agent (The Manager): An autonomous system that controls workflow execution, manages internal state, and passes data between nodes sequentially.
3. Custom Skill Wrappers (The Costumes):
   * Skill_EN_FR: Configured System Prompt specialized in English-to-French translation.
   * Skill_FR_HE: Configured System Prompt specialized in French-to-Hebrew translation.
   * Skill_HE_EN: Configured System Prompt specialized in Hebrew-to-English translation.
4. Vector Evaluation Tool (The Guardrail): A native Python tool utilizing word embeddings and vector distance mathematical formulas to gauge absolute cosine similarity or Euclidean distance between the initial Input and final Output.

### 4. Functional Requirements
* Autonomous Pipeline: The user inputs a single English string. The Orchestrator must process the loop end-to-end without mid-process human intervention.
* Skill State Management: The Orchestrator must successfully swap the system contexts via structured sub-directories inside .claude/skills/ without overlapping system cache.
* Mathematical Assessment: The system must compute and output a definitive numerical drift score (Vector Distance Matrix).

### 5. Non-Functional Requirements
* Auditability & Logging: Complete storage of intermediate outputs at every step of the translation chain inside localized markdown files for verification.
* Prompt Caching Compliance: Structure variables efficiently at the start of sessions to optimize execution costs.
