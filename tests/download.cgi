#!/bin/bash
# filepath: /Users/sjcarnam/GitHub/virtuosoft-dev/dev-pw-app/web/download.cgi

# Output the headers to trigger a file download
echo -e "Content-Type: text/html"
echo -e "Content-Disposition: attachment; filename=\"download.htm\""
echo ""

# Output the HTML content
cat <<EOF
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Download Test</title>
</head>
<body>
    <h1>Download Test</h1>
    <p>This file is being downloaded as "test.htm".</p>
</body>
</html>
EOF
