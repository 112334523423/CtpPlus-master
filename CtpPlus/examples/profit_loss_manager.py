# encoding:utf-8

# CtpPlus量化投资开源框架
# 微信公众号：CtpPlus
# 官网：http://algo.plus

from multiprocessing import Process, Queue
from CtpPlus.CTP.MdApi import run_tick_engine
from CtpPlus.CTP.TraderApi import run_traderapi
from CtpPlus.CTP.FutureAccount import FutureAccount, get_simulate_account

if __name__ == '__main__':

    # 止盈止损参数
    pl_parameter = {
        'StrategyID': 9,
        'ProfitLossParameter': {
            b'rb2010': {'0': [2], '1': [2]},   # '0'代表止盈, '1'代表止损
            b'ni2007': {'0': [20], '1': [20]},   # '0'代表止盈, '1'代表止损
        },
    }

    # 账户配置
    subscribe_list = []
    for instrument_id in pl_parameter['ProfitLossParameter']:
        subscribe_list.append(instrument_id)
    future_account = get_simulate_account(
        investor_id='',                         # SimNow账户
        password='',                            # SimNow账户密码
        subscribe_list=subscribe_list,  # 合约列表
        server_name='TEST'                    # 电信1、电信2、移动、TEST
    )

    # 共享队列
    share_queue = Queue(maxsize=100)
    share_queue.put(pl_parameter)

    # 行情进程
    md_process = Process(target=run_tick_engine, args=(future_account, [share_queue]))
    # 交易进程
    trader_process = Process(target=run_traderapi, args=(future_account, share_queue))

    #
    md_process.start()
    trader_process.start()

    #
    md_process.join()
    trader_process.join()
