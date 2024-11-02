function execute_submit() {
    local workspaceFolder=$1  # /path/to/atcoder
    local fileDirname=$2  # /path/to/atcoder/<ContestName>/<Level>  [e.g. /path/to/atcoder/abc001/a]
    local fileBasename=$3  # <FileName> [e.g. main.py]

    # activate virtualenv
    . ${workspaceFolder}/.venv/bin/activate

    local _ATCODER_URL=$(python ${workspaceFolder}/tools/_get_url.py ${fileDirname})

    cd ${fileDirname}
    oj submit \
        ${_ATCODER_URL} \
        ${fileDirname}/${fileBasename} \
        --guess-python-interpreter pypy \
        -y
}

execute_submit $1 $2 $3
