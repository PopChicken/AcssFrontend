"""程序入口"""
import sys
import asyncio

sys.path.append('.')

import qasync

import mainwindow
import api

from toast import QToaster
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import QTimer


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


@qasync.asyncSlot()
async def on_checklist_clicked():
    try:
        data = await api.query_order_detail()
    except api.ApiError as e:
        QToaster.showMessage(window.window, str(e))
        return
    for i in range(0, len(data)):
        window.order_detail_table.setRowCount(i + 1)
        window.order_detail_table.setItem(i, 0, QTableWidgetItem(data[i]['order_id']))
        window.order_detail_table.setItem(i, 1, QTableWidgetItem(data[i]['create_time']))
        window.order_detail_table.setItem(i, 2, QTableWidgetItem(data[i]['pile_id']))
        window.order_detail_table.setItem(i, 3, QTableWidgetItem(data[i]['charged_amount']))
        window.order_detail_table.setItem(i, 4, QTableWidgetItem(str(data[i]['charged_time'])))
        window.order_detail_table.setItem(i, 5, QTableWidgetItem(data[i]['begin_time']))
        window.order_detail_table.setItem(i, 6, QTableWidgetItem(data[i]['end_time']))
        window.order_detail_table.setItem(i, 7, QTableWidgetItem(data[i]['charging_cost']))
        window.order_detail_table.setItem(i, 8, QTableWidgetItem(data[i]['service_cost']))
        window.order_detail_table.setItem(i, 9, QTableWidgetItem(data[i]['total_cost']))
    QToaster.showMessage(window.window, "查询成功")


@qasync.asyncSlot()
async def preview_callback():
    pass


if __name__ == "__main__":
    window = mainwindow.create_window()
    window.login_button.clicked.connect(on_login_clicked)
    window.logout_button.clicked.connect(on_logout_clicked)
    window.register_button.clicked.connect(on_register_clicked)
    window.query_orders_button.clicked.connect(on_checklist_clicked)
    # TODO 在这里注册其它按钮的slot函数
    timer = QTimer()
    timer.timeout.connect(preview_callback)
    timer.start(1000)
    sys.exit(mainwindow.run_mainwindow())
