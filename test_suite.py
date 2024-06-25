import pytest

if __name__ == "__main__":
    pytest.main([
        '-v',  # verbose mode
        '--html=reports/test_suite_report.html',  # HTML report file
        'test_cases/test_sign_up.py',
        'test_cases/test_login.py',
        'test_cases/test_cart.py',
        'test_cases/test_checkout.py'
        'test_cases/test_logout.py'
    ])