echo "svn up ---------------------"
svndir="/home/kl/svn2"
svn up 1300_编码

find ./1300_编码/ -name '*.~sql' |xargs rm -rf

if [ -n "$(svn st 1300_编码| grep '?')" ]; then
echo "svn add code ---------------------"
svn add $(svn st 1300_编码 | grep '?' | awk '{print $2}')
fi

if [ -n "$(svn st 1300_编码 | grep -v test.txt)" ]; then
echo "svn commmit code ---------------------"
svn commit 1300_编码 -m "dongjian $(date +%Y%m%d)" > commit.log
fi

date_str=$(date +%Y%m%d)
if [ -n "$1" ]; then
    date_str=$1
    echo "date_str------$date_str----------------"
fi
mantis=$2
echo "remark------${mantis}----------------"
echo "register excel create ---------------------"
module_type=$3
python3 /mnt/c/Users/pactera/lc_python/vs_code/commit_register.py "${date_str}" "${mantis}" "${module_type}"
#python3 /mnt/c/Users/pactera/lc_python/vs_code/commit_register.py $1 $2 $3 

if [ -n "$(svn st 1300_编码| grep '?')" ]; then
echo "svn add excel---------------------"
svn add $(svn st 1300_编码 | grep '?' | awk '{print $2}')
fi

if [ -n "$(svn st 1300_编码 | grep -v test.txt)" ]; then
echo "svn commmit excel ---------------------"
svn commit 1300_编码 -m "dongjian $(date +%Y%m%d) register"
fi

