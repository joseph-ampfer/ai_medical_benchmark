from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
from typing import List, Dict

class NBMEScraper:
    def __init__(self, headless: bool = False):
        """Initialize the scraper with Chrome webdriver"""
        self.driver = None
        self.questions = []
        self.headless = headless
        
    def setup_driver(self):
        """Set up Chrome webdriver with options"""
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Use webdriver-manager to automatically handle ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        
    def navigate_to_site(self, launch_url: str):
        """Navigate to the NBME launch page and set up the test"""
        print(f"Navigating to {launch_url}")
        self.driver.get(launch_url)
        
        # Wait for page to load
        wait = WebDriverWait(self.driver, 15)
        try:
            # Wait for the page to load by looking for any content
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            time.sleep(3)  # Additional wait for dynamic content
        except Exception as e:
            print(f"Page load timeout: {e}")
            
    def setup_test_options(self) -> bool:
        """Set up test options: select Step 1 All Blocks and Show Correct Answers"""
        try:
            wait = WebDriverWait(self.driver, 15)
            
            print("Setting up test options...")
            
            # Step 1: Select "Step 1 All Blocks" radio button
            # First, let's debug by finding all radio buttons and their labels
            print("Debugging: Looking for radio buttons...")
            try:
                all_radio_buttons = self.driver.find_elements(By.XPATH, "//input[@type='radio']")
                print(f"Found {len(all_radio_buttons)} radio buttons")
                
                for i, radio in enumerate(all_radio_buttons):
                    # Try to find the associated label
                    try:
                        parent_label = radio.find_element(By.XPATH, "./parent::label")
                        label_text = parent_label.text.strip()
                        print(f"Radio {i+1}: '{label_text}'")
                    except:
                        try:
                            # Try to find label by for attribute
                            radio_id = radio.get_attribute('id')
                            if radio_id:
                                label = self.driver.find_element(By.XPATH, f"//label[@for='{radio_id}']")
                                label_text = label.text.strip()
                                print(f"Radio {i+1}: '{label_text}' (found by for attribute)")
                        except:
                            print(f"Radio {i+1}: (label text not found)")
            except Exception as e:
                print(f"Debug error: {e}")
            
            # More specific selectors for "Step 1 All Blocks"
            step1_selectors = [
                # # Most specific - exact text match
                # "//label[text()='Step 1 All Blocks']/input[@type='radio']",
                # # Contains text but more specific
                # "//label[contains(text(), 'Step 1 All Blocks')]/input[@type='radio']",
                # # Alternative: find by value if it has one
                # "//input[@type='radio'][contains(@value, 'all') or contains(@value, 'All')]",
                # Look for radio button with specific ng-model and check the label
                "//input[@type='radio'][following-sibling::text()[contains(., 'All Blocks')] or preceding-sibling::text()[contains(., 'All Blocks')]]"
            ]
            
            step1_selected = False
            for i, selector in enumerate(step1_selectors):
                try:
                    print(f"Trying selector {i+1}: {selector}")
                    radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    
                    # Double-check that we found the right element by checking its label
                    try:
                        parent_label = radio_button.find_element(By.XPATH, "./parent::label")
                        label_text = parent_label.text.strip()
                        print(f"Found radio with label: '{label_text}'")
                        
                        if "All Blocks" in label_text:
                            radio_button.click()
                            print("✅ Selected 'Step 1 All Blocks' option")
                            step1_selected = True
                            break
                        else:
                            print(f"❌ Wrong radio button found: '{label_text}', continuing...")
                            continue
                    except:
                        # If we can't verify the label, click anyway as a fallback
                        radio_button.click()
                        print("✅ Selected radio button (could not verify label)")
                        step1_selected = True
                        break
                        
                except Exception as e:
                    print(f"Selector {i+1} failed: {e}")
                    continue
                    
            if not step1_selected:
                print("⚠️ Could not find Step 1 All Blocks radio button, trying to proceed anyway...")
            
            # Step 2: Check "Show Correct Answers" checkbox
            answer_selectors = [
                "//input[@type='checkbox'][contains(@id, 'answer') or contains(@id, 'correct')]",
                "//label[contains(text(), 'Show Correct Answers')]/../input[@type='checkbox']",
                "//label[contains(text(), 'Afficher les réponses')]/../input[@type='checkbox']",
                "//*[contains(text(), 'Show Correct Answers')]/input[@type='checkbox']",
                "//input[@type='checkbox']"  # Fallback to any checkbox
            ]
            
            answer_selected = False
            for selector in answer_selectors:
                try:
                    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    if not checkbox.is_selected():
                        checkbox.click()
                        print("✅ Enabled 'Show Correct Answers' option")
                    else:
                        print("✅ 'Show Correct Answers' already enabled")
                    answer_selected = True
                    break
                except:
                    continue
                    
            if not answer_selected:
                print("⚠️ Could not find Show Correct Answers checkbox")
            
            # Step 3: Click "Start" button
            start_selectors = [
                "//button[contains(text(), 'Start') or contains(text(), 'Démarrer')]",
                "//input[@type='submit'][contains(@value, 'Start') or contains(@value, 'Démarrer')]",
                "//input[@type='button'][contains(@value, 'Start') or contains(@value, 'Démarrer')]",
                "//*[contains(text(), 'Start') or contains(text(), 'Démarrer')][@role='button']"
            ]
            
            start_clicked = False
            for selector in start_selectors:
                try:
                    start_button = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    start_button.click()
                    print("✅ Clicked 'Start' button")
                    start_clicked = True
                    break
                except:
                    continue
                    
            if not start_clicked:
                print("❌ Could not find or click Start button")
                return False
                
            # Wait for test to load
            time.sleep(5)
            print("✅ Test setup complete, waiting for questions to load...")
            return True
            
        except Exception as e:
            print(f"Error setting up test options: {e}")
            return False
            
    def extract_question_content(self) -> Dict[str, List[str]]:
        """Extract content from elements with class 'NBPara NBMarkup' and potential answers"""
        question_data = {
            "question_parts": [],
            "correct_answers": [],
            "all_content": []
        }
        
        try:
            # Find all elements with the specified class for questions
            elements = self.driver.find_elements(By.CLASS_NAME, "NBExposition.S1")
            
            # If the above doesn't work (spaces in class name), try with CSS selector
            if not elements:
                elements = self.driver.find_elements(By.CSS_SELECTOR, ".NBExposition.S1")
            
            # If still no elements, try finding them separately
            if not elements:
                nb_para_elements = self.driver.find_elements(By.CLASS_NAME, "NBPara")
                elements = [elem for elem in nb_para_elements if "NBMarkup" in elem.get_attribute("class")]
            
            for element in elements:
                text = element.text.strip()
                if text:
                    question_data["question_parts"].append(text)
                    question_data["all_content"].append(text)
            
            # Try to find answer elements (these might have different classes when answers are shown)
            answer_selectors = [
                # ".correct-answer",
                # ".answer-correct", 
                # ".NBAnswer",
                # "[class*='correct']",
                # "[class*='answer']"
                "ol.options li.stContext"
            ]
            
            for selector in answer_selectors:
                try:
                    answer_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for elem in answer_elements:
                        answer_text = elem.text.strip()
                        if answer_text and answer_text not in question_data["all_content"]:
                            # question_data["correct_answers"].append(answer_text)
                            question_data["all_content"].append(answer_text)
                        if elem.get_attribute("class") == "stContext correct":
                            question_data["correct_answers"].append(answer_text)
                except:
                    continue
                    
            print(f"Found {len(question_data['question_parts'])} question parts and {len(question_data['correct_answers'])} answer elements")
            return question_data
            
        except Exception as e:
            print(f"Error extracting question content: {e}")
            return question_data
            
    def click_next_item(self) -> bool:
        """Click the 'Proceed to Next Item' button"""
        try:
            wait = WebDriverWait(self.driver, 10)
            
            # Look for button with text "Proceed to Next Item"
            next_button = None
            
            # Try different selectors for the button
            button_selectors = [
                "//button[contains(text(), 'Proceed to Next Item')]",
                "//input[@value='Proceed to Next Item']",
                "//a[contains(text(), 'Proceed to Next Item')]",
                "//*[contains(text(), 'Proceed to Next Item')]"
            ]
            
            for selector in button_selectors:
                try:
                    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    break
                except:
                    continue
                    
            if next_button:
                print("Clicking 'Proceed to Next Item' button")
                next_button.click()
                time.sleep(2)  # Wait for page to load
                return True
            else:
                print("'Proceed to Next Item' button not found")
                return False
                
        except Exception as e:
            print(f"Error clicking next item button: {e}")
            return False
            
    def scrape_all_questions(self, launch_url: str, max_questions: int = 10) -> List[Dict]:
        """Scrape all available questions from the site"""
        try:
            self.setup_driver()
            self.navigate_to_site(launch_url)
            
            # Set up test options (radio button, checkbox, start button)
            if not self.setup_test_options():
                print("❌ Failed to set up test options. Cannot proceed.")
                return []
            
            question_count = 0
            
            while question_count < max_questions:
                print(f"\n--- Question {question_count + 1} ---")
                
                # Extract question content
                question_data_extracted = self.extract_question_content()
                
                if question_data_extracted["question_parts"]:
                    # Combine all parts into a single question
                    full_question = "\n".join(question_data_extracted["question_parts"])
                    
                    question_data = {
                        "question_number": question_count + 1,
                        "content": full_question,
                        "parts": question_data_extracted["question_parts"],
                        "correct_answers": question_data_extracted["correct_answers"],
                        "all_content": question_data_extracted["all_content"]
                    }
                    
                    self.questions.append(question_data)
                    print(f"Extracted question: {full_question[:100]}...")
                    question_count += 1
                else:
                    print("No question content found on this page")
                
                # Try to go to next question
                if not self.click_next_item():
                    print("Cannot proceed to next item. Scraping complete.")
                    break
                    
                # Small delay between questions
                time.sleep(1)
                
            return self.questions
            
        except Exception as e:
            print(f"Error during scraping: {e}")
            return self.questions
            
        finally:
            if self.driver:
                self.driver.quit()
                
    def save_questions_to_file(self, filename: str = "nbme_questions.json"):
        """Save scraped questions to a JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.questions, f, indent=2, ensure_ascii=False)
            print(f"Questions saved to {filename}")
        except Exception as e:
            print(f"Error saving questions: {e}")
            
    def get_questions_for_benchmark(self) -> List[Dict]:
        """Convert scraped questions to benchmark format"""
        benchmark_questions = []
        
        for i, q in enumerate(self.questions):
            # Use correct answers if available, otherwise leave empty
            answer = ""
            if q.get("correct_answers"):
                answer = " | ".join(q["correct_answers"])
                
            benchmark_questions.append({
                "task": "medical_practice",
                "question": q["content"],
                "answer": answer,
                "source": "NBME Practice",
                "question_id": q["question_number"]
            })
            
        return benchmark_questions

def main():
    """Main function to run the scraper"""
    launch_url = "https://orientation.nbme.org/launch/usmle/stpf1"
    
    print("Starting NBME Question Scraper...")
    print("This will:")
    print("1. Navigate to the NBME launch page")  
    print("2. Select 'Step 1 All Blocks'")
    print("3. Enable 'Show Correct Answers'")
    print("4. Click 'Start' to begin the test")
    print("5. Extract all practice questions")
    print()
    
    scraper = NBMEScraper(headless=False)  # Set to True for headless mode
    
    try:
        # Scrape questions
        questions = scraper.scrape_all_questions(launch_url, max_questions=5)
        
        if questions:
            print(f"\nSuccessfully scraped {len(questions)} questions!")
            
            # Save to file
            scraper.save_questions_to_file()
            
            # Print first question as example
            print("\nFirst question example:")
            print(questions[0]["content"][:200] + "...")
            
            # Get benchmark format
            benchmark_questions = scraper.get_questions_for_benchmark()
            
            # Save benchmark format
            with open("nbme_benchmark.json", 'w', encoding='utf-8') as f:
                json.dump(benchmark_questions, f, indent=2, ensure_ascii=False)
            print("Benchmark format saved to nbme_benchmark.json")
            
        else:
            print("No questions were scraped.")
            
    except Exception as e:
        print(f"Scraping failed: {e}")

if __name__ == "__main__":
    main()
