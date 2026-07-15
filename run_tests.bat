@echo off
rem 1. Run the tests and collect results
py -m pytest --alluredir=reports/allure-results

rem 2. Use 'call' so control returns to this script afterward - converts results to html
call allure generate reports/allure-results -o reports/allure-report --clean

rem 3. Use 'call' to open the final HTML report on briwser
call allure open reports/allure-report
