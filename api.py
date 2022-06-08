"""API封装"""
from datetime import datetime
from typing import Any, Dict, List, Tuple

import requests


BASE_URL = 'http://127.0.0.1:8000'  # 基础 API URL


class ApiError(BaseException):
    """API返回值为-1时抛出该异常

    服务端抛出错误信息时，raise本异常，
    外侧调用者捕获该异常并决定是否打印异常信息。

    抛出方法：
    ```
    if resp['code'] == -1:
        raise ApiError(resp['message'])
    ```

    处理方法：
    ```
    try:
        some_api()
    except ApiError as e:
        some_toast(str(e))
    ```
    """


async def api_post(path: str, json: Dict) -> Dict[str, Any] | None:
    """_summary_

    Args:
        path (str): BASE_URL 后的相对路径
        json (Dict): 字典，会被转换为JSON字符串置于请求体中

    Raises:
        ApiError: 响应码为-1的异常，包含错误信息

    Returns:
        Dict[str, Any] | None: 响应中的 data 字段，可能为 None
    """


async def api_get(path: str) -> Dict[str, Any] | None:
    """_summary_

    Args:
        path (str): BASE_URL 后的相对路径

    Raises:
        ApiError: 响应码为-1的异常，包含错误信息

    Returns:
        Dict[str, Any] | None: 响应中的 data 字段，可能为 None
    """


async def login(username: str, password: str) -> Dict[str, Any]:
    pass


async def time() -> Tuple[datetime, int]:
    pass


async def register() -> None:
    pass


async def submit_charging_request(charge_mode: str, require_amount: str, battery_size: str) -> None:
    pass


async def edit_charging_request(charge_mode: str, require_amount: str) -> None:
    pass


async def end_charging_request() -> None:
    pass


async def query_order_detail() -> List[Dict[str, Any]]:
    pass


async def preview_queue() -> Dict[str, Any]:
    pass
