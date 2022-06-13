"""程序入口"""
import sys

sys.path.append('.')

import qasync

import mainwindow
import api

from toast import QToaster


# TODO 仿照该函数编写其它点击事件函数
@qasync.asyncSlot()
async def on_login_clicked():
    try:
        token, is_admin = await api.login(window.username_input.text(), window.password_input.text())
    except api.ApiError as e:
        QToaster.showMessage(window.window, str(e))
        return
    api.TOKEN = token
    if is_admin:
        role = 'ADMIN'
    else:
        role = 'USER'
    window.user_role_label.setText(role)
    window.user_state_label.setText('已登陆')
    QToaster.showMessage(window.window, "登陆成功")


@qasync.asyncSlot()
async def on_register_clicked():
    try:
        await api.register(window.username_input.text(), window.password_input.text())
    except api.ApiError as e:
        QToaster.showMessage(window.window, str(e))
        return
    QToaster.showMessage(window.window, "注册成功")



@qasync.asyncSlot()
async def on_logout_clicked():
    api.TOKEN = ''
    window.user_role_label.setText('无')
    window.user_state_label.setText('未登陆')
    QToaster.showMessage(window.window, "成功注销")


if __name__ == "__main__":
    window = mainwindow.create_window()
    window.login_button.clicked.connect(on_login_clicked)
    window.logout_button.clicked.connect(on_logout_clicked)
    window.register_button.clicked.connect(on_register_clicked)
    # TODO 在这里注册其它按钮的slot函数
    sys.exit(mainwindow.run_mainwindow())
