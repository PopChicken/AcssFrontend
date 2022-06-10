# AccsFrontend

智能(A)充电/计费(C)调度(S)系统(S)的前端仓库，基于 PySide6 框架与 Python3.10 开发。

## 开发环境配置

1. 下载安装 Python3.10（Windows 建议使用微软商店）

2. 克隆项目仓库

3. 在项目根目录执行 `python3.10 -m pip install -r requirements.txt`

4. 使用 `python3.10 admin/main.py` 与 `python3.10 user/main.py` 分别启动用户客户端与管理员客户端程序

---

## 调试方法

调试 AcssFrontend 的方法与调试 AcssBackend 的方法一致

1. 使用 Visual Studio Code 打开本项目，并点击右下角 Python 版本切换至 Python3.10

2. 在调试选项中选择 Python 文件 并创建 launch.json

3. 在希望调试的位置添加断点

4. 使用功能键 F5 启动调试

---

## 代码要求

- 不可以在代码中使用同步阻塞操作，例如 `sleep(1)`；

- 所有阻塞操作均需要使用使用支持 asyncio 的函数，并在函数前添加 await 关键字；

- 使用 await 关键字的函数 def 前需要添加 async 关键字。

---

## 基本代码逻辑说明

### 程序入口模块

`main.py`

这里执行一些基本初始化操作，并且定义按钮点击事件的响应函数，并将它们绑定到 Qt 控件上。

- Qt 以阻塞的方式调用 Python 函数，所以直接在函数中执行网络IO是不可行的（等待响应的过程用户界面会失去响应），所以这里使用 `qasync` 模块兼容了 Python 的异步框架 `asyncio`。通过这种方法，所有阻塞操作全部可以使用异步方式调用，这样就不会阻塞用户界面了。异步调用示例如下：

```python
import api
import qasync


@qasync.asyncSlot()
async def on_login_clicked():
    try:
        kwargs = await api.login('jinuo', 'i-hate-bupt')
    except ApiError as e:
        some_toast(str(e)).show()
    token = kwargs['token']
    is_admin = kwargs['is_admin']
    # rest codes
```

- 响应函数调用 API 模块提供的函数以与服务端进行交互。捕获 `ApiError` 并显示提示框，若未发生异常则从返回值中获取服务器返回的数据，并对用户界面进行相应的更新。

---

### 主窗口模块

`mainwindow.py`

该模块负责加载窗口，并保存控件的 Python 对象。显然这样的写法不是最佳实践，我没有花时间找到加载UI文件并继承 QWidget 类的方法（又不是不能用）。

---

### API 模块

`api.py`

所有对网络的调用全部在 API 模块内完成。

- API 模块内的 `api_post` 与 `api_get` 两个函数封装了 requests 库的 get 与 post 操作。这两个函数需要能够自动在其中添加 `Authorization` 请求头。

  `api_post` 与 `api_get` 中使用 requests 模块时，需要捕获网络 IO 异常（如超时），并且使用 `raise ApiError("网络异常") from e` 将相关异常以 `ApiError` 异常的类型抛出。

  `api_post` 与 `api_get` 在获取到响应时，需要判断 `code` 是否为 0，为 -1 时需要抛出 `ApiError(response['message'])` 异常。

- API 模块除 `api_post` 与 `api_get` 的函数与 开放 API 文档 内的接口一一对应，需要调用 `api_post` 与 `api_get` 对服务端发起请求。

  这些函数不需要捕获 `ApiError` 异常，对异常的捕获应该发生在 API 模块的调用者处，以决定是否要反馈到用户界面中（Toast）。

  调用者捕获到 `ApiError` 异常时，仅需要使用 `str(e)` 即可获取到异常的文本信息，也就是服务端响应中的 message 字段

- 异步：所有函数均为异步函数，调用异步函数时需要添加 `await` 关键字。
