# encoding:utf-8

from CtpPlus.CTP.MdApi import run_mdrecorder
from CtpPlus.CTP.FutureAccount import FutureAccount, get_simulate_account


if __name__ == '__main__':
    # 账户配置
    instrument_id_list = [b'rb2010']  # 需要订阅的合约列表
    future_account = get_simulate_account(
        investor_id=b'',  # SimNow账户
        password=b'',  # SimNow账户密码
        subscribe_list=instrument_id_list,  # 合约列表
        server_name='TEST'  # 电信1、电信2、移动、TEST
    )

    #
    run_mdrecorder(future_account)
