---
marp: true
size: 4:3
paginate: true
title: Week 1 Report (Individual Project)
---

---

# AI Medical Benchmark

---

# Option 2 for AI

---

# Features
    1. Question Dataset

      * Problem: USMLE questions are not easily available in a structured, machine-readable format.
      * Importance: A standardized dataset is necessary for consistent and fair evaluation of AI models.
      * Solution: Scrape and store the official Step 1 Free 120 questions, including correct answers and images.

---

    2. Model Integration

      * Problem: Different AI models require different APIs and formats for querying.
      * Importance: To benchmark fairly, the system must support multiple AI providers in a unified way.
      * Solution: Build a framework to connect with multiple AI APIs (e.g., OpenAI, Anthropic, Google, etc.) using keys and model IDs.

---

    3. Evaluation System

      * Problem: There needs to be a way to automatically check if the AI’s answer matches the correct one.
      * Importance: Objective scoring ensures accuracy comparisons across models.
      * Solution: Implement an answer-checking mechanism that compares model responses to correct answers and logs results.

---

    4. Results Dashboard

      * Problem: Raw outputs from models are difficult to interpret at scale.
      * Importance: Clear visualization helps compare performance quickly.
      * Solution: Display accuracy per model and allow drill-down into individual question/answer logs.

---

    5. Stretch Features

      * Image Handling – Compare model performance with/without images.
      * Prompt Perturbation – Test model consistency by rephrasing or duplicating questions.
      * Lab Value Expansion – Add extra lab data to test reasoning depth.
      * Comparative Metrics – Track reasoning quality, hallucinations, or consistency beyond accuracy.

--- 

    1. For Question Dataset

      * Web scraper to collect official USMLE Step 1 free 120 questions
      * Store each question, answer choices, and correct answer
      * Capture any associated images
      * Ensure uniform format (e.g., JSON, CSV)

    2. For Model Integration

      * Collect API keys for supported AI providers
      * Create a standard interface to send questions and receive answers
      * Support different model IDs and endpoints
      * Handle rate limits and API errors gracefully

    3. For Evaluation System

      * Parse AI responses to extract the model’s chosen answer
      * Compare extracted answer with correct answer
      * Mark response as correct/incorrect
      * Store raw response for further review

    4. For Results Dashboard

      * Show % accuracy for each model
      * Display per-question logs (question, AI response, correct answer, score)
      * Include filtering (e.g., correct only, incorrect only, by model)
      * Provide basic charts/graphs of results

    5. For Stretch Features

      * Implement option to toggle images on/off in prompts
      * Add a "prompt variation" module (rephrasing, duplication)
      * Enable injection of lab values into questions
      * Add advanced evaluation metrics (hallucination detection, consistency checks)


---

- What is the problem?  
See which AI model does best on medical exams. 
- Why is it important?  
As AI use is ever growing, people begin to use it for medical advice. It is crucial to know which one has best medical depth. My case in particular is helpful for medical students studing for their Liscensing exams and knowing which model to use.
- How will you solve it (including the design)? 
 Make an AI benchmark. See features listed above.

# Requirements

**Core User Stories:**
- As a researcher, I want to access a standardized dataset of USMLE questions so that I can fairly evaluate AI models.
- As a developer, I want to integrate multiple AI providers through a unified interface so that I can test different models consistently.
- As an evaluator, I want automated answer checking so that I can objectively score AI responses at scale.
- As a medical educator, I want a results dashboard so that I can quickly compare AI model performance across questions.
- As a student, I want to see which AI model performs best on medical licensing exams so that I can choose the most reliable study assistant.

**Stretch User Stories:**
- As a researcher, I want to test models with and without images so that I can measure visual reasoning capabilities.
- As a developer, I want to test prompt variations so that I can evaluate model consistency and robustness.
- As a clinician, I want models tested with additional lab values so that I can assess deeper medical reasoning skills.
