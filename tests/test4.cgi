#!/bin/bash
# filepath: /Users/sjcarnam/GitHub/virtuosoft-dev/dev-pw-app/web/test4.cgi

# IMPORTANT: No Content-Type header or blank line needed for SSI includes.
# Just output the partial HTML directly.

echo "<p>This is partial HTML content included from <strong>test4.cgi</strong>.</p>"

if [ -n "$QUERY_STRING" ]; then
    echo "<p>The query string passed to test4.cgi was: <code>$QUERY_STRING</code></p>"
else
    echo "<p>No query string was passed to test4.cgi.</p>"
fi
