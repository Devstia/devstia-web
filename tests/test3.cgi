#!/bin/bash
# filepath: /Users/sjcarnam/GitHub/virtuosoft-dev/dev-pw-app/web/test3.cgi

# IMPORTANT: No Content-Type header or blank line needed for SSI includes.
# Just output the partial HTML directly.

echo "<p>This is partial HTML content included from <strong>test3.cgi</strong>.</p>"
echo "<p>Current time according to test3.cgi: $(date)</p>"
