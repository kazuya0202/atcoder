# AtCoder

## Links

- [AtCoder](https://atcoder.jp/home)
- [AtCoder Problems / ichiya_x](https://kenkoooo.com/atcoder/#/table/ichiya_x)

## Usage

### Requirements

- atcoder-tools
- online-judge-tools

```shell
pip install atcoder-tools online-judge-tools
```

### Download problems

```shell
sh tools/download_problem.sh <CONTEST_ID>
# e.g. sh download_problem.sh abc326
```

### Download problems sequentially

- before executing below command, edit variables (`start`, `end`) in `tools/seq_download_problem.py`

```shell
python tools/seq_download_problems.py
```

### Write a program

```shell
CONTEST_ID/<PROBLEM_LEVEL>/main.py
# e.g. abc326/A/main.py
```

### Test

```shell
sh tools/test_problem.sh <FILE_PATH>
# e.g. sh test_problem.sh abc326/A/main.py
```

### Submit

- [manual] Copy and paste on AtCoder webpage.
