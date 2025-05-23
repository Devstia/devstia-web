#!/bin/bash
# filepath: /Users/sjcarnam/GitHub/virtuosoft-dev/dev-pw-app/web/test.cgi

# Output the Content-Type header and the separator
# Use -n to suppress echo's default trailing newline
# Use -e to interpret \r\n sequences
echo -n -e "Content-Type: text/html\r\n\r\n"

# Start HTML output
cat <<EOF
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>CGI GET Parameters Test</title>
</head>
<body>
    <h1>CGI GET Parameters Test</h1>
EOF

# Check if QUERY_STRING is set and not empty
if [ -n "$QUERY_STRING" ]; then
    echo "<h2>Raw Query String:</h2>"
    echo "<pre>${QUERY_STRING}</pre>" # Display raw query string

    echo "<h2>Parsed Parameters:</h2>"
    echo "<ul>"

    # Simple parsing: replace '&' with newline, then loop through 'key=value'
    # This is a basic parser and might not handle URL encoding perfectly
    echo "$QUERY_STRING" | tr '&' '\n' | while IFS='=' read -r key value; do
        # Basic URL decoding for common characters (optional, can be expanded)
        # For more robust decoding, external tools like 'urlencode' or languages like Perl/Python are better
        decoded_key=$(echo -e "${key//%/\\x}")
        decoded_value=$(echo -e "${value//%/\\x}")
        echo "<li><strong>${decoded_key}</strong>: ${decoded_value}</li>"
    done

    echo "</ul>"
else
    echo "<p>No GET parameters (QUERY_STRING) found.</p>"
fi

# End HTML output
cat <<EOF
</body>
</html>
EOF
