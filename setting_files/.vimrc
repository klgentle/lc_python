set encoding=utf-8 fileencodings=ucs-bom,utf-8,cp936
" 设置字符编码
set fileencoding=utf-8
set fileencodings=utf-8,gb2312,gb18030,latin1
set termencoding=utf-8
set encoding=utf-8
set fileformat=unix

" 语法高亮
syntax on
" 深色背景
""color evening
" 检测文件类型
filetype on
" 根据文件类型加载对应的插件
filetype plugin on

" 显示行号
set number
" 在第80列显示竖线
set cc=80
" 高亮显示当前行
set cursorline

" 设置各种缩进
set tabstop=4
set softtabstop=4
set shiftwidth=4
""set autoindent
set smartindent
""set cindent
" tab转换为空格
set expandtab

" 将ESC键映射为两次j键
inoremap jj <Esc>

inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {}<ESC>i
inoremap ' ''<ESC>i
inoremap " ""<ESC>i
