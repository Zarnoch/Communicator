"""HTML resources for test result file"""

HEADER = """
<html>
    <head>
        <title>
            Test Report
        </title>
        <style type="text/css">
        .test-result-table {
            border: 1px solid black;
            width: 800px;
        }
        .test-result-table-header-cell {
            border-bottom: 1px solid black;
            background-color: silver;
        }
        .test-result-step-command-cell {
            border-bottom: 1px solid gray;
        }
        .test-result-step-description-cell {
            border-bottom: 1px solid gray;
        }
        .test-result-step-result-cell-ok {
            border-bottom: 1px solid gray;
            background-color: green;
        }
        .test-result-step-result-cell-failure {
            border-bottom: 1px solid gray;
            background-color: red;
        }
        </style>
    </head>
    <body>
        <h1 class="test-results-header">
            Test Report
        </h1>

        <table class="test-result-table" cellspacing="0">
            <thead>
                <tr>
                    <td class="test-result-table-header-cell">
                        Test Case
                    </td>
                    <td class="test-result-table-header-cell">
                        Description
                    </td>
                    <td class="test-result-table-header-cell">
                        Result
                    </td>
                </tr>
            </thead>
            <tbody>
"""

ROW_TEMPLATE_PASS = """
                <tr class="test-result-step-row test-result-step-row-altone">
                    <td class="test-result-step-command-cell">
                        {test_name}
                    </td>
                    <td class="test-result-step-description-cell">
                        {description}
                    </td>
                    <td class="test-result-step-result-cell-ok">
                        OK
                    </td>
                </tr>
"""

ROW_TEMPLATE_FAIL = """
                <tr class="test-result-step-row test-result-step-row-alttwo">
                    <td class="test-result-step-command-cell">
                        {test_name}
                    </td>
                    <td class="test-result-step-description-cell">
                        {description}
                    </td>
                    <td class="test-result-step-result-cell-failure">
                        FAILURE
                    </td>
                </tr>
"""

FOOTER = """
            </tbody>
        </table>
    </body>
</html>
"""
