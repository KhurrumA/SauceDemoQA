# SauceDemoQA

**SauceDemoQA** is a robust, modular, and scalable test automation framework for browser-based UI testing.  
It uses **Python**, **Selenium WebDriver**, and **PyTest**, and is built around the **Page Object Model** for clean test logic separation.

This project runs automated tests against the demo e-commerce site:  
[https://www.saucedemo.com](https://www.saucedemo.com)

---

## 🚀 Features

- Page Object Model (POM) for clean, reusable page interactions
- Parametrized login tests with valid and invalid credentials
- Negative test handling (empty form, locked user, wrong password)
- HTML report generation using `pytest-html`
- Automatic screenshot capture on test failures


---

## Setup & Installation

1. Clone the repo or unzip the project:
```bash
cd autoqa-advanced
pip install -r requirements.txt
```

2. Ensure ChromeDriver is installed.

---

## Running the Tests

```bash
pytest --html=report.html
```

- Test output will appear in the terminal
- HTML report will be generated as `report.html`
- Screenshots (on failures) go into `/screenshots/`

---

## Credentials for Testing

Use SauceDemo-provided test users:
```
Username: standard_user
Password: secret_sauce
```

---

## Example Screenshot on Failure

On any test failure, a full-page screenshot is saved automatically to help you debug.

---

## Author

**Khurrum Arif**  
[KhurrumArif02@gmail.com](mailto:KhurrumArif02@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/khurrum-arif-uol) | [GitHub](https://github.com/KhurrumA)


