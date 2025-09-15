# NBME Practice Questions Web Scraper

This scraper extracts practice questions from the NBME orientation website. It automatically handles the complete setup workflow:

1. **Launch Page Setup** - Goes to `https://orientation.nbme.org/launch/usmle/stpf1`
2. **Test Configuration** - Selects "Step 1 All Blocks" and "Show Correct Answers" 
3. **Question Extraction** - Navigates through questions and extracts content with answers

## 🚀 Quick Start

### 1. Install Dependencies

First, install the required packages:

```bash
pip install selenium webdriver-manager
```

Or install all dependencies at once:
```bash
pip install -r requirements.txt
```

### 2. Run the Scraper

```bash
python scraper.py
```

### 3. View Results

The scraper will create two output files:
- `nbme_questions.json` - Raw scraped questions with all parts
- `nbme_benchmark.json` - Questions formatted for benchmark testing

## 📋 How It Works

The scraper follows a complete automated workflow:

1. **Opens Chrome browser** (automatically downloads ChromeDriver if needed)
2. **Navigates to launch page** - Goes to `https://orientation.nbme.org/launch/usmle/stpf1`
3. **Configures test options**:
   - Selects "Step 1 All Blocks" radio button
   - Enables "Show Correct Answers" checkbox 
   - Clicks "Start" button to begin test
4. **Extracts question content** - Finds elements with class `NBPara NBMarkup`
5. **Captures correct answers** - Extracts answer elements when available
6. **Navigates between questions** - Clicks "Proceed to Next Item" button
7. **Saves results** - Outputs questions in JSON format with answers included

## 🔧 Configuration Options

### Headless Mode
To run without opening a browser window:

```python
scraper = NBMEScraper(headless=True)
```

### Limit Number of Questions
Change the maximum number of questions to scrape:

```python
questions = scraper.scrape_all_questions(url, max_questions=10)
```

## 📁 Output Format

### Raw Questions (`nbme_questions.json`)
```json
[
  {
    "question_number": 1,
    "content": "Full question text with all parts combined",
    "parts": [
      "Question part 1",
      "Question part 2", 
      "Answer choices..."
    ],
    "correct_answers": [
      "The correct answer explanation",
      "Answer choice: A"
    ],
    "all_content": [
      "All extracted content including questions and answers"
    ]
  }
]
```

### Benchmark Format (`nbme_benchmark.json`)
```json
[
  {
    "task": "medical_practice", 
    "question": "Full question text",
    "answer": "Correct answer extracted from site | Alternative answer",
    "source": "NBME Practice",
    "question_id": 1
  }
]
```

## 🔍 Troubleshooting

### Common Issues

1. **Chrome not found**
   - Make sure Google Chrome is installed on your system
   - The scraper will automatically download ChromeDriver

2. **Selenium import error**
   ```
   pip install selenium webdriver-manager
   ```

3. **Page doesn't load**
   - Check your internet connection
   - The NBME site might be temporarily unavailable
   - Try increasing wait times in the script

4. **Can't find question elements**
   - The website might have changed its structure
   - Check if the class names are still `NBPara NBMarkup`
   - Look at the browser console for errors

### Debugging Mode

To see what's happening, run with the browser visible:
```python
scraper = NBMEScraper(headless=False)
```

## 📊 Integration with Benchmark System

The scraped questions can be integrated with your existing benchmark system in `main.py`:

```python
import json
from main import evaluate_model

# Load scraped questions
with open('nbme_benchmark.json', 'r') as f:
    nbme_questions = json.load(f)

# Add answers manually or through another process
for q in nbme_questions:
    q['answer'] = "Your answer here"  # Fill in correct answers

# Run evaluation
results = evaluate_model("gpt-4o-mini", nbme_questions[:5])
print(f"Accuracy: {results['accuracy']*100:.1f}%")
```

## ⚠️ Important Notes

- **Ethical Use**: Only use this scraper for educational purposes
- **Rate Limiting**: The scraper includes delays to be respectful to the server
- **Terms of Service**: Make sure you comply with NBME's terms of service
- **Automatic Answer Extraction**: The scraper now automatically extracts correct answers when "Show Correct Answers" is enabled
- **Complete Workflow**: The scraper handles the entire process from launch page to question extraction

## 🛠️ Customization

### Modify Question Extraction
To extract different elements, modify the `extract_question_content()` method:

```python
# Look for different class names
elements = self.driver.find_elements(By.CLASS_NAME, "your-class-here")

# Use different CSS selectors
elements = self.driver.find_elements(By.CSS_SELECTOR, ".your-selector")
```

### Change Navigation Logic
To modify how the scraper moves between questions, update the `click_next_item()` method:

```python
# Look for different button text
"//button[contains(text(), 'Your Button Text')]"
```

## 📝 Example Output

When you run the scraper, you'll see output like:

```
Starting NBME Question Scraper...
This will:
1. Navigate to the NBME launch page
2. Select 'Step 1 All Blocks'
3. Enable 'Show Correct Answers'
4. Click 'Start' to begin the test
5. Extract all practice questions

Navigating to https://orientation.nbme.org/launch/usmle/stpf1
Setting up test options...
✅ Selected 'Step 1 All Blocks' option
✅ Enabled 'Show Correct Answers' option
✅ Clicked 'Start' button
✅ Test setup complete, waiting for questions to load...

--- Question 1 ---
Found 3 question parts and 2 answer elements
Extracted question: A 25-year-old man presents with chest pain...
Clicking 'Proceed to Next Item' button

--- Question 2 ---
Found 2 question parts and 1 answer elements
Extracted question: A 45-year-old woman has a history of...
Clicking 'Proceed to Next Item' button

Successfully scraped 15 questions!
Questions saved to nbme_questions.json
Benchmark format saved to nbme_benchmark.json
```
