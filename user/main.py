"""程序入口"""
import sys

import qasync
import mainwindow


# TODO 仿照该函数编写其它点击事件函数
@qasync.asyncSlot()
async def on_login_clicked():
    pass


if __name__ == "__main__":
    window = mainwindow.create_window()
    window.login_button.clicked.connect(on_login_clicked)
    # TODO 在这里注册其它按钮的slot函数
    sys.exit(mainwindow.run_mainwindow())
