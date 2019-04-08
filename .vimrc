set encoding=utf-8 fileencodings=ucs-bom,utf-8,cp936
" 设置字符编码
set fileencoding=utf-8
set fileencodings=utf-8,gb2312,gb18030,latin1
set termencoding=utf-8
set encoding=utf-8

" 语法高亮
syntax on
" 深色背景
color evening
" 检测文件类型
filetype on
" 根据文件类型加载对应的插件
filetype plugin on

" 显示行号
set number
" 在第64列显示竖线
set cc=64
" 高亮显示当前行
set cursorline

" 设置各种缩进
set tabstop=4
set softtabstop=4
set shiftwidth=4
set autoindent
set smartindent
set cindent
" tab转换为空格
set expandtab

" 将ESC键映射为两次j键
inoremap jj <Esc>

" 自动完成大括号
imap { {<CR>}<Esc>kA<CR>
inoremap ( ()<Esc>i
inoremap [ []<Esc>i
inoremap { {<CR>}<Esc>O
autocmd Syntax html,vim inoremap < <lt>><Esc>i| inoremap > <c-r>=ClosePair('>')<CR>
inoremap ) <c-r>=ClosePair(')')<CR>
inoremap ] <c-r>=ClosePair(']')<CR>
inoremap } <c-r>=CloseBracket()<CR>
inoremap " <c-r>=QuoteDelim('"')<CR>
inoremap ' <c-r>=QuoteDelim("'")<CR>

function ClosePair(char)
 if getline('.')[col('.') - 1] == a:char
 return "\<Right>"
 else
 return a:char
 endif
endf

function CloseBracket()
 if match(getline(line('.') + 1), '\s*}') < 0
 return "\<CR>}"
 else
 return "\<Esc>j0f}a"
 endif
endf

function QuoteDelim(char)
 let line = getline('.')
 let col = col('.')
 if line[col - 2] == "\\"
 "Inserting a quoted quotation mark into the string
 return a:char
 elseif line[col - 1] == a:char
 "Escaping out of the string
 return "\<Right>"
 else
 "Starting a string
 return a:char.a:char."\<Esc>i"
 endif
endf
