# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
from CtpPlus.CTP.MdApi import run_bar_engine
from CtpPlus.CTP.FutureAccount import get_simulate_account


def print_bar(md_queue):
    while True:
        if not md_queue.empty():
            print(md_queue.get(block=False))


if __name__ == '__main__':
    # 账户
    future_account = get_simulate_account(
        investor_id='',  # 账户
        password='',  # 密码
        server_name='TEST',  # 电信1、电信2、移动、TEST、N视界
        subscribe_list=[b'IC2404'],  # 合约列表
    )

    # future_account = FutureAccount(
    #     broker_id='',  # 期货公司BrokerID
    #     server_dict={'TDServer': "ip:port", 'MDServer': 'ip:port'},  # TDServer为交易服务器，MDServer为行情服务器。服务器地址格式为"ip:port。"
    #     reserve_server_dict={},  # 备用服务器地址
    #     investor_id='',  # 账户
    #     password='',  # 密码
    #     app_id='simnow_client_test',  # 认证使用AppID
    #     auth_code='0000000000000000',  # 认证使用授权码
    #     subscribe_list=[],  # 订阅合约列表
    #     md_flow_path='./log',  # MdApi流文件存储地址，默认MD_LOCATION
    #     td_flow_path='./log',  # TraderApi流文件存储地址，默认TD_LOCATION
    # )

    # 共享队列
    share_queue = Queue(maxsize=100)

    # 行情进程
    md_process = Process(target=run_bar_engine, args=(future_account, [share_queue]))
    # 交易进程
    print_process = Process(target=print_bar, args=(share_queue,))

    md_process.start()
    print_process.start()

    md_process.join()
    print_process.join()
