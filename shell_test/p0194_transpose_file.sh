awk '
{
    for (i = 1; i <= NF; i++) {
        if(NR == 1) {
            s[i] = $i;
        } else {
            s[i] = s[i] " " $i;
        }
    }
}
END {
    for (i = 1; s[i] != ""; i++) {
        print s[i];
    }
}' transpose.txt

# NR: a variable indicating the number of records (i.e. current line number) that's accumulated across multiple files read. FNR is similar to NR, but is reset for each file read. Since we only need to deal with one file in this question, either is fine to use.
# NF: a variable indicating the number of fields (i.e. number of "columns") on an input line.
