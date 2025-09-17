---
marp: true
size: 4:3
paginate: true
title: HW2 – Grading Rubric (Individual Project)
---

# HW2 Grading (Individual Project) Rubric  

- Total: **25 points**  
- Each assignment: **5 points**  
- No partial points (all-or-nothing per assignment)  
- This rubric is **only for individual projects**  

---

## 📘 Assignment 1 (5 pts)

> Notice!
>
> - It's critically important to understand the scope, requirements, and expectations of the projects.  
> - Students must visit me if anything is unclear or need help.  
> - Earning 5 points in this assignment means you understand how to start, make progress, and finalize the projects successfully.  

---

**Understand project success**

- [x] Downloaded individual project documents from Canvas  
- [x] Read and understood rubrics & requirements  
- [x] Reviewed GitHub PDFs (Projects + Requirements)  
- [x] Understood how to use Git/GitHub  
  - Visit me if you need help

**Points:** __5__ / 5  

---

## 📘 Assignment 2 (5 pts)

**Write requirements**

- [x] Decided AI option  
option 2
- [x] Defined features (problem, importance, solution)  
  - List features here:  
    1. Question Dataset

      * Problem: USMLE questions are not easily available in a structured, machine-readable format.
      * Importance: A standardized dataset is necessary for consistent and fair evaluation of AI models.
      * Solution: Scrape and store the official Step 1 Free 120 questions, including correct answers and images.

    2. Model Integration

      * Problem: Different AI models require different APIs and formats for querying.
      * Importance: To benchmark fairly, the system must support multiple AI providers in a unified way.
      * Solution: Build a framework to connect with multiple AI APIs (e.g., OpenAI, Anthropic, Google, etc.) using keys and model IDs.

    3. Evaluation System

      * Problem: There needs to be a way to automatically check if the AI’s answer matches the correct one.
      * Importance: Objective scoring ensures accuracy comparisons across models.
      * Solution: Implement an answer-checking mechanism that compares model responses to correct answers and logs results.

    4. Results Dashboard

      * Problem: Raw outputs from models are difficult to interpret at scale.
      * Importance: Clear visualization helps compare performance quickly.
      * Solution: Display accuracy per model and allow drill-down into individual question/answer logs.


    5. Stretch Features

      * Image Handling – Compare model performance with/without images.
      * Prompt Perturbation – Test model consistency by rephrasing or duplicating questions.
      * Lab Value Expansion – Add extra lab data to test reasoning depth.
      * Comparative Metrics – Track reasoning quality, hallucinations, or consistency beyond accuracy.

---

- [x] Listed requirements to complete features  
  - List requirements here:  
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
- [x] Published on Canvas (individual project page)  
  - Link:[individual project page](https://nku.instructure.com/courses/81924/pages/member-joseph-ampfer-individual-project-page) 

**Points:** __5__ / 5  

---

### Your Individual Project Feature/Requirements Count

It is possible to change the features/requirements if you encounter “unknown unknowns,” with explanation.

1. Number of individual features: ( __6_ )  
2. Number of individual requirements: ( __20_ )  

---

### Your Individual Project Features

- What is the problem?  
See which AI model does best on medical exams. 
- Why is it important?  
As AI use is ever growing, people begin to use it for medical advice. It is crucial to know which one has best medical depth. My case in particular is helpful for medical students studing for their Liscensing exams and knowing which model to use.
- How will you solve it (including the design)? 
 Make an AI benchmark. See features listed above.

---

## 📘 Assignment 3 (5 pts)

**Make schedules**

- [x] Checked course & personal calendar  
- [x] Created milestones  

**Points:** __5__ / 5  

---

### Write your milestones

Make clear when you plan to implement requirements and finish milestones.

### Milestones

* Feature 1: Question Dataset

  * Requirement 1.1: Web scraper to collect USMLE Free 120 questions
  * Requirement 1.2: Store each question, answer choices, and correct answer
  * Requirement 1.3: Capture associated images
  * Requirement 1.4: Ensure uniform format (JSON/CSV)
  * Plan: Implement in Weeks 6–7 for prototype; complete dataset finalized by Week 8

* Feature 2: Model Integration

  * Requirement 2.1: Collect API keys for supported AI providers
  * Requirement 2.2: Create standard interface to send questions and receive answers
  * Requirement 2.3: Support multiple model IDs and endpoints
  * Requirement 2.4: Handle rate limits and API errors gracefully
  * Plan: Baseline integration with one model by Week 7 (prototype), expand to multiple models by Week 9 (Sprint 1 submission)

* Feature 3: Evaluation System

  * Requirement 3.1: Parse AI responses to extract chosen answer
  * Requirement 3.2: Compare extracted answer with correct answer
  * Requirement 3.3: Mark response as correct/incorrect
  * Requirement 3.4: Store raw response for further review
  * Plan: Initial evaluation logic in Week 7 (prototype); complete robust system by Week 9

* Feature 4: Results Dashboard

  * Requirement 4.1: Show % accuracy per model
  * Requirement 4.2: Display per-question logs (question, response, correct answer, score)
  * Requirement 4.3: Include filtering (correct only, incorrect only, by model)
  * Requirement 4.4: Provide basic charts/graphs of results
  * Plan: Build basic dashboard by Weeks 10–11 (MVP); polish with filters/graphs by Weeks 12–14


* Feature 5: Stretch Features

  * Requirement 6.1: Toggle images on/off in prompts
  * Requirement 6.2: Add prompt variation module (rephrasing, duplication)
  * Requirement 6.3: Enable lab value injection in questions
  * Requirement 6.4: Add advanced evaluation metrics (hallucination detection, consistency checks)
  * Plan: Attempt after MVP completion, between Weeks 12–14


If the schedule changes, update your Canvas page with:  

- Actual date finished:  
- Explanation of schedule slip:  

---

## 📘 Assignment 4 (5 pts)

**Prepare to report progress**

- [x] Ready to share progress on Canvas (individual project page)  
  - Link: [canvas](https://nku.instructure.com/courses/81924/pages/member-joseph-ampfer-individual-project-page) 

**Points:** __5__ / 5  

---

## 📘 Assignment 5 (5 pts)

**Share work on GitHub**

- [x] Created project repository (new GitHub ID if needed)  
- [x] Understood GitHub, Markdown, Marp, Hugo  
- [ ] Repo + GitHub.io site created  
  - Repo Link: [benchmark](https://github.com/joseph-ampfer/ai_medical_benchmark)  
  - GitHub.io Link: [io](https://joseph-ampfer.github.io/ai_medical_benchmark/) (It's OK to be empty in the beginning, but there should be a link)  

**Points:** __5__ / 5  

---

# 📊 Total Summary  

| Assignment            | Max Points | Earned Points |
|-----------------------|------------|---------------|
| 1. Understand success | 5          | __5__          |
| 2. Requirements       | 5          | __5__          |
| 3. Schedules          | 5          | __5__          |
| 4. Report progress    | 5          | __5__          |
| 5. GitHub             | 5          | __5__          |
| **Total**             | **25**     | **__25__**      |

---

## 📤 Submission  

Both team leaders and team members must upload this **individual project rubric** as part of the HW2 deliverable on Canvas.
