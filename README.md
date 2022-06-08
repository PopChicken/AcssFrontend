# AccsFrontend

智能(A)充电/计费(C)调度(S)系统(S)的前端仓库，基于 PySide6 框架与 Python3.10 开发。

## 开发环境配置

1. 下载安装Python3.10（Windows建议使用微软商店）

2. 克隆项目仓库

3. 在项目根目录执行 `python3.10 -m pip install -r requirements.txt`

4. 使用 `python3.10 main.py` 启动程序

## 调试方法

调试 AcssFrontend 的方法与调试 AcssBackend 的方法一致

1. 使用 Visual Studio Code 打开本项目，并点击右下角 Python 版本切换至 Python3.10

2. 在调试选项中选择 Python 文件 并创建 launch.json

3. 在希望调试的位置添加断点

4. 使用功能键 F5 启动调试

## 代码要求

- 不可以在代码中使用同步阻塞操作，例如 `sleep(1)`；

- 所有阻塞操作均需要使用使用支持 asyncio 的函数，并在函数前添加 await 关键字；

- 使用 await 关键字的函数 def 前需要添加 async 关键字。
