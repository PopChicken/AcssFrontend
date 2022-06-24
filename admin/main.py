"""程序入口"""
import sys
from typing import Any, Dict, List

sys.path.append('.')
sys.path.append('..')

import qasync

import mainwindow
import api


# TODO 仿照该函数编写其它点击事件函数
@qasync.asyncSlot()
async def on_login_clicked():
    pass

# 查询全部充电桩状态函数
async def query_all_piles_stat() -> List[Dict[str, Any]]:
    data = await api_get('/admin/query_all_piles_stat')
    return data

if __name__ == "__main__":
    window = mainwindow.create_window()
    window.login_button.clicked.connect(on_login_clicked)
    # TODO 在这里注册其它按钮的slot函数
    window.query_pile_state_button.clicked.connect(query_all_piles_stat)
    sys.exit(mainwindow.run_mainwindow())
