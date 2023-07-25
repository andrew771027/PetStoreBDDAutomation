#!/bin/sh
# Test

# Report

# behave -f allure_behave.formatter:AllureFormatter -o {allure_report_folder} {path_to_feature_file}
behave --junit
rm reports/*.*
behave tests/features --format allure_behave.formatter:AllureFormatter -o reports -f pretty
allure serve reports

# Seagger
wget https://petstore.swagger.io/v2/swagger.json -O /docs/swagger.json
