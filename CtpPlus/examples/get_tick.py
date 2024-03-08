# encoding:utf-8

from multiprocessing import Process, Queue
from CtpPlus.CTP.MdApi import run_tick_engine
from CtpPlus.CTP.FutureAccount import get_simulate_account


def print_tick(md_queue):
    while True:
        if not md_queue.empty():
            print(md_queue.get(block=False))


if __name__ == '__main__':
    # 账户配置
    subscribe_list = [b'rb2410']
    future_account = get_simulate_account(
        investor_id='179939',                   # SimNow账户
        password='jfy9601194415',                     # SimNow账户密码
        subscribe_list=subscribe_list,  # 合约列表
        server_name='电信1'                      # 电信1、电信2、移动、TEST
    )

    # 共享队列
    share_queue = Queue(maxsize=100)

    # 行情进程
    md_process = Process(target=run_tick_engine, args=(future_account, [share_queue]))
    # 交易进程
    print_process = Process(target=print_tick, args=(share_queue,))

    #
    md_process.start()
    print_process.start()

    #
    md_process.join()
    print_process.join()
