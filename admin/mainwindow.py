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

        self.query_queue_button: QPushButton = window.queueBtn  # 查询排队情况按钮
        self.query_queue_table: QTableWidget = window.queueTable  # 查询排队情况表格

        self.query_pile_state_button: QPushButton = window.pileStateBtn  # 查询充电桩状态按钮
        self.query_pile_state_table: QTableWidget = window.pileStateTable  # 查询充电桩状态表格

        self.query_pile_list_button: QPushButton = window.pileListBtn  # 查询充电桩报表按钮
        self.query_pile_list_table: QTableWidget = window.pileListTable  # 查询充电桩报表表格

        # 修改充电桩状态
        self.pile_number_input: QLineEdit = window.pileNum  # 充电桩编号
        self.pile_state_box: QComboBox = window.switchState  # 充电模式选框
        self.update_button: QPushButton = window.updateBtn  # 更新按钮



mainwindow: MainWindow = None


def create_window() -> MainWindow:
    """创建主窗体

    Returns:
        MainWindow: 包含控件与窗体的数据类
    """
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    ui_file = QFile("admin/mainwindow.ui")
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
