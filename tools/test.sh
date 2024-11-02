function execute_test() {
    local workspaceFolder=$1  # /path/to/atcoder
    local fileDirname=$2  # /path/to/atcoder/<ContestName>/<Level>  [e.g. /path/to/atcoder/abc001/a]
    local fileBasename=$3  # <FileName> [e.g. main.py]

    # activate virtualenv
    . ${workspaceFolder}/.venv/bin/activate

    cd ${fileDirname}
    oj test \
        -c "python ${fileBasename}" \
        -d "${fileDirname}/test"
}

execute_test $1 $2 $3
