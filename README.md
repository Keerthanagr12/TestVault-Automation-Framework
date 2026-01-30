# TestVault - Microservices Test Automation Framework

[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-green)](https://playwright.dev)
[![Pytest](https://img.shields.io/badge/Pytest-7.4%2B-blue)](https://pytest.org)
[![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

## 🎯 Overview

TestVault is a production-ready **microservices test automation framework** designed to test distributed systems with comprehensive API testing, integration testing, contract testing, and performance testing capabilities.

**Perfect for testing:**
- RESTful APIs and Microservices
- Cross-service integrations
- Distributed system workflows
- API contracts and communication
- Performance baselines and load testing

---

## ✨ Key Features

✅ **Comprehensive API Testing**
- RESTful API endpoint testing
- Request/Response validation
- Header and authentication testing
- Error handling and status code validation

✅ **Integration Testing**
- End-to-end workflow testing
- Multi-service orchestration
- Database assertions
- State management validation

✅ **Contract Testing**
- Service communication contracts (Pact)
- API schema validation
- Request/Response consistency

✅ **Performance Testing**
- API response time validation
- Throughput testing
- Load testing baseline

✅ **Enterprise Features**
- Beautiful HTML reports with metrics
- Test coverage analysis
- CI/CD integration (GitHub Actions)
- Docker containerization
- Allure reporting
- Test data management

---

## 🏗️ Project Structure

```
TestVault-Automation-Framework/
├── tests/
│   ├── api/                          # API endpoint tests
│   │   ├── test_user_service.py
│   │   ├── test_product_service.py
│   │   ├── test_order_service.py
│   │   └── test_payment_service.py
│   ├── integration/                  # Cross-service workflow tests
│   │   ├── test_checkout_flow.py
│   │   ├── test_order_fulfillment.py
│   │   └── test_user_onboarding.py
│   ├── contract/                     # Service contract tests
│   │   ├── test_user_product_contract.py
│   │   └── test_product_order_contract.py
│   └── performance/                  # Performance baseline tests
│       └── test_api_performance.py
├── framework/
│   ├── api_client.py                 # Reusable API client with retry logic
│   ├── base_test.py                  # Base test class with setup/teardown
│   ├── fixtures.py                   # Pytest fixtures for test setup
│   ├── database.py                   # Database operations and seeding
│   ├── assertions.py                 # Custom assertion library
│   └── logger.py                     # Logging configuration
├── config/
│   ├── config.yaml                   # Environment configuration
│   ├── test_data.json                # Test data templates
│   └── endpoints.json                # API endpoint definitions
├── pages/
│   ├── user_api_page.py              # User service API methods
│   ├── product_api_page.py           # Product service API methods
│   └── order_api_page.py             # Order service API methods
├── reports/                          # Generated test reports
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── .github/workflows/
│   ├── api_tests.yml
│   ├── integration_tests.yml
│   └── contract_tests.yml
├── conftest.py                       # Pytest configuration and global fixtures
├── requirements.txt                  # Python dependencies
├── pytest.ini                        # Pytest settings
└── README.md                         # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip (Python package manager)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Keerthanagr12/TestVault-Automation-Framework.git
cd TestVault-Automation-Framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. **Update `config/config.yaml`** with your API endpoints:
```yaml
base_url: "https://api.example.com"
api:
  user_service: "https://api.example.com/users"
  product_service: "https://api.example.com/products"
  order_service: "https://api.example.com/orders"

authentication:
  type: "Bearer"
  token: "your_api_token"

timeout: 10
retry_count: 3
```

2. **Update `config/test_data.json`** with test credentials and data

3. **Update `config/endpoints.json`** with your API endpoints

---

## 📝 Running Tests

### Run All Tests
```bash
pytest -v
```

### Run Specific Test Category
```bash
# API tests only
pytest tests/api/ -v

# Integration tests only
pytest tests/integration/ -v

# Contract tests only
pytest tests/contract/ -v

# Performance tests only
pytest tests/performance/ -v
```

### Run with Reporting
```bash
# Generate HTML report
pytest --html=reports/report.html --self-contained-html

# Generate with coverage
pytest --cov=framework --cov-report=html

# Generate Allure report
pytest --allure-features
```

### Run with Filters
```bash
# Run only smoke tests
pytest -m smoke -v

# Run only critical tests
pytest -m critical -v

# Run excluding slow tests
pytest -m "not slow" -v
```

---

## 🔧 Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|----------|
| **Language** | Python 3.10+ | Test automation |
| **API Testing** | Playwright (Python) | Modern browser automation + API testing |
| **Test Framework** | Pytest | Test orchestration and reporting |
| **HTTP Client** | Requests/aiohttp | RESTful API calls |
| **Contract Testing** | Pact | Service contract validation |
| **Test Data** | Factory Boy + Faker | Realistic test data generation |
| **Assertions** | Pytest + Custom | Clear, readable assertions |
| **Reporting** | Allure Reports | Beautiful test metrics |
| **CI/CD** | GitHub Actions | Automated test execution |
| **Container** | Docker | Test environment isolation |
| **Code Quality** | Pylint + Black | Code style and quality |

---

## 📊 Test Coverage Matrix

| Service | Functional | Integration | Contract | Performance |
|---------|-----------|-------------|----------|----------|
| User Service | ✅ | ✅ | ✅ | ✅ |
| Product Service | ✅ | ✅ | ✅ | ✅ |
| Order Service | ✅ | ✅ | ✅ | ✅ |
| Payment Service | ✅ | ✅ | ✅ | ✅ |

---

## 🔄 CI/CD Integration

Tests automatically run on:
- ✅ Pull Requests
- ✅ Pushes to main branch
- ✅ Scheduled nightly runs
- ✅ Manual trigger via GitHub Actions

View workflows in `.github/workflows/`

---

## 📈 Test Metrics & Reporting

- **HTML Reports** with detailed test results
- **Coverage Reports** showing code coverage %
- **Allure Reports** with history and trends
- **Test Duration** tracking
- **Failure Analysis** with screenshots and logs

---

## 🐳 Docker Support

```bash
# Build Docker image
docker build -t testvault:latest .

# Run tests in container
docker run --rm testvault:latest pytest -v

# Run with docker-compose
docker-compose up
```

---

## 🔐 Best Practices Implemented

✅ **Page Object Model** - Maintainable and reusable test code
✅ **DRY Principle** - No code repetition
✅ **Clear Naming** - Self-documenting test cases
✅ **Proper Logging** - Detailed execution logs
✅ **Error Handling** - Comprehensive try-catch blocks
✅ **Test Data Management** - Isolated, reproducible data
✅ **Atomic Tests** - Independent, non-flaky tests
✅ **CI/CD Ready** - Automated execution pipelines

---

## 📚 Writing Tests

### Example: API Test

```python
from framework.base_test import BaseTest
from pages.user_api_page import UserAPIPage

class TestUserService(BaseTest):
    """User Service API Tests"""

    def setup_method(self):
        """Setup before each test"""
        super().setup_method()
        self.user_api = UserAPIPage(self.api_client)

    def test_create_user_success(self):
        """Test successful user creation"""
        payload = {
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User"
        }
        response = self.user_api.create_user(payload)
        
        assert response.status_code == 201
        assert response.json()["id"] is not None
        assert response.json()["email"] == "test@example.com"

    def test_get_user_not_found(self):
        """Test getting non-existent user"""
        response = self.user_api.get_user(user_id=99999)
        
        assert response.status_code == 404
```

### Example: Integration Test

```python
class TestCheckoutFlow(BaseTest):
    """End-to-End Checkout Workflow Tests"""

    def test_complete_checkout_flow(self):
        """Test complete order creation to payment"""
        # Step 1: Create user
        user = self.user_api.create_user({...})
        
        # Step 2: Create product
        product = self.product_api.create_product({...})
        
        # Step 3: Create order
        order = self.order_api.create_order({
            "user_id": user["id"],
            "items": [{"product_id": product["id"], "qty": 1}]
        })
        
        # Step 4: Process payment
        payment = self.payment_api.process_payment({
            "order_id": order["id"],
            "amount": order["total"]
        })
        
        # Assertions
        assert order["status"] == "completed"
        assert payment["status"] == "success"
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and add tests
4. Run tests: `pytest`
5. Commit with clear messages: `git commit -m "Add feature X"`
6. Push to your fork: `git push origin feature/your-feature`
7. Create a Pull Request

---

## 📋 Test Plan & Coverage

Detailed test plan available in [TEST_PLAN.md](TEST_PLAN.md)

### Coverage Goals
- **API Tests**: 100% endpoint coverage
- **Integration Tests**: All critical user workflows
- **Contract Tests**: All service communications
- **Performance Tests**: Baseline metrics established

---

## 🐛 Troubleshooting

### Common Issues

**Q: Tests fail with "Connection refused"**
- A: Ensure your API server is running and endpoints in config are correct

**Q: Flaky tests (inconsistent failures)**
- A: Check timeouts, add explicit waits, verify test data isolation

**Q: Report generation fails**
- A: Install allure: `pip install allure-pytest`

---

## 📞 Support & Documentation

- 📖 [Pytest Documentation](https://docs.pytest.org/)
- 🎭 [Playwright Documentation](https://playwright.dev/)
- 📝 [Pact Documentation](https://docs.pact.foundation/)
- 📊 [Allure Reports](https://docs.qameta.io/allure/)

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 👤 Author

**Keerthanagr12**
- GitHub: [@Keerthanagr12](https://github.com/Keerthanagr12)
- Portfolio: Check my other QA automation projects

---

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

---

**Last Updated**: January 2026
**Version**: 1.0.0
**Status**: Production Ready ✅
