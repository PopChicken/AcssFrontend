"""程序入口"""
import sys
from typing import Any, Dict, List

sys.path.append('.')
sys.path.append('..')

import qasync

import mainwindow
import api

from PySide6.QtWidgets import QTableWidgetItem
from toast import QToaster


# TODO 仿照该函数编写其它点击事件函数
@qasync.asyncSlot()
async def on_login_clicked():
    try:
        token, is_admin = await api.login(window.username_input.text(), window.password_input.text())
    except api.ApiError as e:
        QToaster.showMessage(window.window, str(e))
        return
    if is_admin == 'USER':
        QToaster.showMessage(window.window, "权限不足 无法登陆")
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
    QToaster.showMessage(window.window, "不允许管理员自行注册")


# 查询全部充电桩状态函数
@qasync.asyncSlot()
async def on_query_piles_stat_clicked() -> List[Dict[str, Any]]:
    try:
        data = await api.query_all_piles_stat()
    except api.ApiError as e:
        QToaster.showMessage(window.window, str(e))
        return
    window.query_pile_state_table.clearContents()
    for i in range(0, len(data)):
        window.query_pile_state_table.setRowCount(i + 1)
        window.query_pile_state_table.setItem(i, 0, QTableWidgetItem(data[i]['pile_id']))
        window.query_pile_state_table.setItem(i, 1, QTableWidgetItem(data[i]['status']))
        window.query_pile_state_table.setItem(i, 2, QTableWidgetItem(str(data[i]['cumulative_usage_times'])))
        window.query_pile_state_table.setItem(i, 3, QTableWidgetItem(str(data[i]['cumulative_charging_time'])))
        window.query_pile_state_table.setItem(i, 4, QTableWidgetItem(str(data[i]['cumulative_charging_amount'])))
    QToaster.showMessage(window.window, "查询成功")


@qasync.asyncSlot()
async def on_check_pile_list_clicked():
    try:
        data = await api.admin_status_report()
    except api.ApiError as e:
        QToaster.showMessage(window.window, str(e))
        return
    window.query_pile_list_table.clearContents()
    for i in range(0, len(data)):
        window.query_pile_list_table.setRowCount(i + 1)
        window.query_pile_list_table.setItem(i, 0, QTableWidgetItem(str(data[i]['pile_id'])))
        window.query_pile_list_table.setItem(i, 1, QTableWidgetItem(str(data[i]['day'])))
        window.query_pile_list_table.setItem(i, 2, QTableWidgetItem(str(data[i]['week'])))
        window.query_pile_list_table.setItem(i, 3, QTableWidgetItem(str(data[i]['month'])))
        window.query_pile_list_table.setItem(i, 4, QTableWidgetItem(str(data[i]['cumulative_usage_times'])))
        window.query_pile_list_table.setItem(i, 5, QTableWidgetItem(str(data[i]['cumulative_charging_time'])))
        window.query_pile_list_table.setItem(i, 6, QTableWidgetItem(str(data[i]['cumulative_charging_amount'])))
        window.query_pile_list_table.setItem(i, 7, QTableWidgetItem(str(data[i]['cumulative_charging_earning'])))
        window.query_pile_list_table.setItem(i, 8, QTableWidgetItem(str(data[i]['cumulative_service_earning'])))
        window.query_pile_list_table.setItem(i, 9, QTableWidgetItem(str(data[i]['cumulative_earning'])))
    QToaster.showMessage(window.window, "已显示报表结果")


@qasync.asyncSlot()
async def on_check_queue_clicked():
    try:
        data = await api.admin_query_queue()
    except api.ApiError as e:
        QToaster.showMessage(window.window, str(e))
        return
    window.query_queue_table.clearContents()
    for i in range(0, len(data)):
        window.query_queue_table.setRowCount(i + 1)
        window.query_queue_table.setItem(i, 0, QTableWidgetItem(str(data[i]['pile_id'])))
        window.query_queue_table.setItem(i, 1, QTableWidgetItem(str(data[i]['username'])))
        window.query_queue_table.setItem(i, 2, QTableWidgetItem(str(data[i]['battery_size'])))
        window.query_queue_table.setItem(i, 3, QTableWidgetItem(str(data[i]['require_amount'])))
        window.query_queue_table.setItem(i, 4, QTableWidgetItem(str(data[i]['waiting_time'])))
    QToaster.showMessage(window.window, "已显示队列结果")


@qasync.asyncSlot()
async def on_update_pile_stat():
    try:
        pile_id = window.pile_number_input.text()
        status_text = window.pile_state_box.currentText()
        if status_text == '运行':
            status = 'RUNNING'
        elif status_text == '关机':
            status = 'SHUTDOWN'
        else:
            status = 'UNAVAILABLE'
        await api.update_pile_stat(pile_id, status)
    except api.ApiError as e:
        QToaster.showMessage(window.window, str(e))
        return
    QToaster.showMessage(window.window, '充电桩状态更新成功')


if __name__ == "__main__":
    window = mainwindow.create_window()
    window.login_button.clicked.connect(on_login_clicked)
    window.register_button.clicked.connect(on_register_clicked)
    # TODO 在这里注册其它按钮的slot函数
    window.query_pile_state_button.clicked.connect(on_query_piles_stat_clicked)
    window.query_pile_list_button.clicked.connect(on_check_pile_list_clicked)
    window.query_queue_button.clicked.connect(on_check_queue_clicked)
    window.update_button.clicked.connect(on_update_pile_stat)
    sys.exit(mainwindow.run_mainwindow())
