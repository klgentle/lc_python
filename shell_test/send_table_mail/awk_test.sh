ls -l | awk 'BEGIN{getline;print"--------------------------------------------------------"}
{printf("|%010d\t%-3s\t%2s\t%-5s\t%-s\n",$5,$6,$7,$8,$9)}
END{print"---------------------------------------------------------"}' > printf.csv
