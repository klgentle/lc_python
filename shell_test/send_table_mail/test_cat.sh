f="test.html"

func () {
    local f_content=$(cat ${f})
    
    echo ${f_content}
}

func
