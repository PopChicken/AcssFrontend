"""主窗口"""
import sys
import asyncio

from qasync import QEventLoop

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QComboBox, QTableWidget


class MainWindow:
    """窗体类 保存窗体与空间
    """
    def __init__(self, window: QWidget, loop: QEventLoop) -> None:
        self.window = window
        self.loop = loop
        self.username_input: QLineEdit = window.userName  # 用户名输入框
        self.password_input: QLineEdit = window.password  # 密码输入框
        self.user_state_label: QLabel = window.userState  # 登陆状态标签
        self.user_role_label: QLabel = window.userIdentity  # 用户身份标签
        self.login_button: QPushButton = window.loginBtn  # 登录按钮
        self.register_button: QPushButton = window.registBtn  # 注册按钮
        self.logout_button: QPushButton = window.logoutBtn  # 退出登录按钮
        self.charge_mode_box: QComboBox = window.chargeMode  # 充电模式选框
        self.battery_capacity_input: QLineEdit = window.batteryCapacity  # 电池容量输入框
        self.require_amount_input: QLineEdit = window.electricityReq  # 请求电量输入框
        self.submit_request_button: QPushButton = window.chargeReqBtn  # 请求充电按钮
        self.edit_request_button: QPushButton = window.rewriteBtn  # 修改充电请求按钮
        self.end_request_button: QPushButton = window.endChargeBtn  # 结束/取消充电按钮
        self.order_detail_table: QTableWidget = window.infoTable  # 详单表格
        self.query_orders_button: QPushButton = window.searchBtn  # 查询详单按钮
        self.time_label: QLabel = window.time  # 当前时间标签
        self.status_label: QLabel = window.presentState  # 当前充电状态标签
        self.queue_position_label: QLabel = window.presentQueue  # 当前队列位置标签
        self.request_id_label: QLabel = window.queueNum  # 充电请求ID标签


mainwindow: MainWindow = None


def create_window() -> MainWindow:
    """创建主窗体

    Returns:
        MainWindow: 包含控件与窗体的数据类
    """
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    ui_file = QFile("user/mainwindow.ui")
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open ui file: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)

    global mainwindow
    mainwindow = MainWindow(window, loop)
    return mainwindow


def run_mainwindow() -> int:
    """运行主窗体直到主窗体被关闭

    Returns:
        int: 执行返回值
    """

    mainwindow.window.show()

    with mainwindow.loop:
        return mainwindow.loop.run_forever()
