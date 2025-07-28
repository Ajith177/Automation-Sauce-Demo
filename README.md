🔐 SauceDemo Login Automation (Python + Selenium)
This project automates the login functionality of the Sauce Demo website using Python and Selenium WebDriver.

It serves as a foundational test suite and will be expanded to cover more scenarios as development progresses.

🚀 Tech Stack
Language: Python 3.x

Automation Tool: Selenium WebDriver

Test Framework: PyTest

Browser: Chrome

Version Control: GitHub

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

1) Clone the repository

     git clone https://github.com/Ajith177/Automation-Sauce-Demo.git
     cd Automation-Sauce-Demo


2) Install dependencies
     pip install -r requirements.txt


3) Run all test cases
     pytest test_suite.py -v


🧠 Upcoming Features......................................


✅ Cross-browser testing support

✅ Jenkins Pipeline Integration

✅ Checkout flow automation

