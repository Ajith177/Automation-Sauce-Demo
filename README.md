🔐 SauceDemo Login Automation (Python + Selenium)

This project automates the login functionality of the [Sauce Demo](https://www.saucedemo.com/) website using Python and Selenium WebDriver.

It's a foundational test suite that will be expanded to cover more scenarios as development progresses.

---
🚀 Tech Stack

- Language: Python 3.x  
- Automation Tool: Selenium WebDriver  
- Test Framework: pytest  
- Browser: Chrome 
- Version Control: GitHub  

---

📁 Project Structure

Automation-Sauce-Demo/
│
├── Sauce-demo/                 # Main source folder (contains modules)
│   ├── Login/                  # Login-related page and test classes
│   └── Swag_Labs/              # Main test cases including cart functionality
│
├── __pycache__/                # Python cache (ignore in versioning)
│
├── conftest.py                 # PyTest fixtures for setup and teardown
├── test_suite.py               # Entry point to run grouped tests
└── README.md                   # Project documentation


🧪 How to Run Tests


1) Clone the repo
   *) git clone https://github.com/Ajith177/Automation-Sauce-Demo.git
   *)cd Automation-Sauce-Demo

2) Install dependencies
   *) pip install -r requirements.txt

3) Run all test cases
   *)pytest test_suite.py -v

   
🧠 Upcoming Features................................

*) Cross-browser testing support
*) Jenkins Pipeline Integration
*) Checkout flow automation



