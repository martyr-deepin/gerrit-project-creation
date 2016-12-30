# deepin git项目创建工具

因为在创建gerrit项目需要对gitlab、github（开源项目）做同步，所以创建项目的同时也需要对gitlab、github初始化。人生苦短，使用此工具能多续 1s。

## 续法
填充配置
```shell
cp config.ini_example config.ini
vim config.ini
```

```shell
./new -h
usage: new [-h] [-t TYPE] [-g GIT] name

positional arguments:
  name                  project name

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  project type [public | private | web]
  -g GIT, --git GIT     choose one or multi target, [gerrit | github |
                        gitlab], eg: github,gitlab
```
