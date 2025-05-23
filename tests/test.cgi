#!/bin/bash
# filepath: /Users/sjcarnam/GitHub/virtuosoft-dev/dev-pw-app/web/test.cgi

# Output the Content-Type header followed by a blank line
echo -e "Content-Type: text/html\r\n\r\n"

# Output the HTML content
cat <<EOF
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>CGI Test</title>
</head>
<body>
    <h1>CGI Test</h1>
    <p>This is a test of the CGI functionality.</p>
    <p>Current Date and Time: $(date)</p>
    <p>Server Hostname: $(hostname)</p>
</body>
</html>
EOF
