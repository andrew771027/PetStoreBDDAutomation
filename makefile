# Test

# Report

# behave -f allure_behave.formatter:AllureFormatter -o {allure_report_folder} {path_to_feature_file}
behave --junit
behave --format allure_behave.formatter:AllureFormatter -o reports -f pretty

allure serve reports