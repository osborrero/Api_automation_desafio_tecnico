from test_junkie.reporter.html_reporter import ReportTemplate
from test_junkie.runner import Runner

from src.page.html_reporter.CustomReporter import CustomReporter
from src.test.suites.RestfulBookerSuite import RestfulBooker


runner = Runner(

    suites=[RestfulBooker],
    html_report="reports/report_yape.html",
    monitor_resources=True
)
aggregator = runner.run(test_multithreading_limit=1, suite_multithreading_limit=10)
