# AutoQA – Web Automation Testing Framework

**AutoQA** is a lightweight and modular test automation framework built using **Python**, **Selenium WebDriver**, and **PyTest**.  
It automates key Quality Assurance (QA) tasks such as login validation, UI navigation, and product visibility testing using the [saucedemo.com](https://www.saucedemo.com) demo site.

---

## Features

- Automated login flow testing
- UI navigation and logout checks
- Product view interaction
- Clear and modular test structure
- Easy to extend and maintain

---

## Technologies Used

- Python 3.12
- Selenium WebDriver
- PyTest

---

## Project Structure

```
testing-portfolio/
│
├── tests/
│   ├── test_login.py        # Validates login functionality
│   ├── test_navigation.py   # Checks menu and logout flow
│   └── test_search.py       # Opens a product detail page
│
├── conftest.py              # Shared setup/teardown for WebDriver
├── requirements.txt         # Project dependencies
└── README.md
```

---

## Installation

1. Clone this repository or download the ZIP:

```bash
git clone https://github.com/yourusername/AutoQA.git
cd AutoQA
```

2. Install dependencies (Python 3.12 recommended):

```bash
pip install -r requirements.txt
```

3. Ensure [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) is installed and added to your system PATH.

---

## Running Tests

```bash
pytest
```

All tests will open Chrome, execute actions, and close the browser automatically.

---

## Test Target

All tests interact with the demo website:  
[https://www.saucedemo.com](https://www.saucedemo.com)

Use test credentials like:

- Username: `standard_user`
- Password: `secret_sauce`

---

## Author

**Khurrum Arif**  
[KhurrumArif02@gmail.com](mailto:KhurrumArif02@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/khurrum-arif-uol) | [GitHub](https://github.com/KhurrumA)


