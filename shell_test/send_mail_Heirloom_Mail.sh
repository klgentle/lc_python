## Prepare a temporary script that will serve as an editor.

## This script will be passed to ed.
temp_script=$(mktemp)
cat <<'EOF' >>"$temp_script"
1a
Content-Type: text/html
.
$r test.html
w
q
EOF
## Call mailx, and tell it to invoke the editor script
#EDITOR="ed -s $temp_script" heirloom-mailx -S editheaders=1 -s "Subject" klgentle@sina.com <<EOF
EDITOR="ed -s $temp_script" mailx -S editheaders=1 -s "Subject" klgentle@sina.com <<EOF
~e
.
EOF
rm -f "$temp_script"
