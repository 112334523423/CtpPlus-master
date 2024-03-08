# encoding:utf-8

from time import sleep, perf_counter as timer
from CtpPlus.CTP.TraderApiBase import TraderApiBase
from CtpPlus.CTP.FutureAccount import FutureAccount
from CtpPlus.CTP.ApiStruct import *
from CtpPlus.CTP.ApiConst import *
from CtpPlus.utils.base_field import to_bytes, to_str


class QueryInstrumentHelper(TraderApiBase):
    def __init__(self, broker_id, td_server, investor_id, password, app_id, auth_code, md_queue=None, flow_path='', private_resume_type=2, public_resume_type=2):
        super(QueryInstrumentHelper, self).__init__()
        self.subscribe_list = []

    def query_instrumrent(self):
        qry_instrument_field = QryInstrumentField()
        self.ReqQryInstrument(qry_instrument_field)

    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        if not pRspInfo or pRspInfo['ErrorID'] == 0:
            if pInstrument and pInstrument['ProductClass'] == ProductClass_Futures:
                self.subscribe_list.append(pInstrument['InstrumentID'])

            self.status += bIsLast

    def Join(self):
        while True:
            if self.status == 0:
                self.query_instrumrent()
                self.status = 1
            elif self.status == 2:
                return self.subscribe_list
            sleep(1)


def run_query_instrument(account):
    if isinstance(account, FutureAccount):
        trader_engine = QueryInstrumentHelper(
            account.broker_id,
            account.server_dict['TDServer'],
            account.investor_id,
            account.password,
            account.app_id,
            account.auth_code,
            None,
            account.td_flow_path
        )
        return trader_engine.Join()
