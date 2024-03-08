1.结构体重复定义（v6.7.2）：
	///查询结算信息确认域
	struct CThostFtdcQrySettlementInfoConfirmField
	{
		///经纪公司代码
		TThostFtdcBrokerIDType	BrokerID;
		///投资者代码
		TThostFtdcInvestorIDType	InvestorID;
		///投资者帐号
		TThostFtdcAccountIDType	AccountID;
		///币种代码
		TThostFtdcCurrencyIDType	CurrencyID;
	};
	
	///装载结算信息
	struct CThostFtdcQrySettlementInfoConfirmField
	{
		///经纪公司代码
		TThostFtdcBrokerIDType	BrokerID;
	};