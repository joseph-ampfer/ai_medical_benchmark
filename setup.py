#!/usr/bin/env python3
"""
Setup script to install required dependencies for the NBME scraper
"""

import subprocess
import sys

def install_requirements():
    """Install required packages"""
    try:
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        sys.exit(1)

def main():
    print("🔧 Setting up NBME Practice Question Scraper...")
    install_requirements()
    
    print("\n📝 Setup complete! You can now run the scraper with:")
    print("   python scraper.py")
    
    print("\n⚠️  Note: Make sure you have Chrome browser installed.")
    print("   The scraper will automatically download the appropriate ChromeDriver.")

if __name__ == "__main__":
    main()
