import logging

from test_junkie.reporter.html_reporter import ReportTemplate
from test_junkie.runner import Runner

from src.page.html_reporter.CustomReporter import CustomReporter
from src.page.utils.Constants import Transversal
from src.test.suites.RestfulBookerSuite import RestfulBooker

report_template = ReportTemplate()
report_template.__class__.get_body_template = CustomReporter.get_custom_monkey_html_template
runner = None
if Transversal.ENV == "QA":
    runner = Runner(
        suites=[
            RestfulBooker
        ],
        html_report=f"reports/{Transversal.NAME_REPORT}",
        monitor_resources=True
    )

runner.run(test_multithreading_limit=1,
           suite_multithreading_limit=24)
