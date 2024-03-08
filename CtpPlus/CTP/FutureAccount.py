# encoding:utf-8

import os

BASE_LOCATION = "./log"
MD_LOCATION = BASE_LOCATION
TD_LOCATION = BASE_LOCATION

SIMULATE_SERVER = {
    '电信1': {'BrokerID': 9999, 'TDServer': "180.168.146.187:10201", 'MDServer': '180.168.146.187:10211', 'AppID': 'simnow_client_test', 'AuthCode': '0000000000000000'},
    '电信2': {'BrokerID': 9999, 'TDServer': "180.168.146.187:10202", 'MDServer': '180.168.146.187:10212', 'AppID': 'simnow_client_test', 'AuthCode': '0000000000000000'},
    '移动': {'BrokerID': 9999, 'TDServer': "218.202.237.33:10203", 'MDServer': '218.202.237.33:10213', 'AppID': 'simnow_client_test', 'AuthCode': '0000000000000000'},
    'TEST': {'BrokerID': 9999, 'TDServer': "180.168.146.187:10130", 'MDServer': '180.168.146.187:10131', 'AppID': 'simnow_client_test', 'AuthCode': '0000000000000000'},
    'N视界': {'BrokerID': 10010, 'TDServer': "210.14.72.12:4600", 'MDServer': '210.14.72.12:4602', 'AppID': '', 'AuthCode': ''},
}


class FutureAccount:
    def __init__(self, broker_id, server_dict, reserve_server_dict, investor_id, password, app_id, auth_code, subscribe_list, md_flow_path=MD_LOCATION, td_flow_path=TD_LOCATION):
        self.broker_id = broker_id  # 期货公司BrokerID
        self.server_dict = server_dict  # 登录的服务器地址
        self.reserve_server_dict = reserve_server_dict  # 备用服务器地址
        self.investor_id = investor_id  # 账户
        self.password = password  # 密码
        self.app_id = app_id  # 认证使用AppID
        self.auth_code = auth_code  # 认证使用授权码
        self.subscribe_list = subscribe_list  # 订阅合约列表[]
        self.md_flow_path = md_flow_path  # MdApi流文件存储地址，默认MD_LOCATION
        self.td_flow_path = td_flow_path  # TraderApi流文件存储地址，默认TD_LOCATION


def get_simulate_account(investor_id, password, subscribe_list=None, server_name='电信1', md_flow_path=MD_LOCATION, td_flow_path=TD_LOCATION):
    if server_name not in SIMULATE_SERVER.keys():
        print(f'{server_name}不在可选列表[电信1, 电信2, 移动, TEST]中，默认使用电信1。')
        server_name = '电信1'

    if subscribe_list is None:
        subscribe_list = []

    investor_id = investor_id if isinstance(investor_id, bytes) else investor_id.encode(encoding='utf-8')
    password = password if isinstance(password, bytes) else password.encode(encoding='utf-8')
    return FutureAccount(
        broker_id=SIMULATE_SERVER[server_name]['BrokerID'],  # 期货公司BrokerID
        server_dict=SIMULATE_SERVER[server_name],  # TDServer为交易服务器，MDServer为行情服务器。服务器地址格式为"ip:port。"
        reserve_server_dict={},
        investor_id=investor_id,  # 账户
        password=password,  # 密码
        app_id=SIMULATE_SERVER[server_name]['AppID'],  # 认证使用AppID
        auth_code=SIMULATE_SERVER[server_name]['AuthCode'],  # 认证使用授权码
        subscribe_list=subscribe_list,  # 订阅合约列表
        md_flow_path=md_flow_path,  # MdApi流文件存储地址，默认MD_LOCATION
        td_flow_path=td_flow_path  # TraderApi流文件存储地址，默认TD_LOCATION
    )
