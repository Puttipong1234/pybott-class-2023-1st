from settrade_v2 import Investor

investor = Investor(app_id="gZOMQIXaGK2fmQ40",                               
                app_secret="AP0SQNpqgIobNh2l23jGPYaHs/16PzDtR0Mc/2rkGHle", 
                broker_id="SANDBOX",
                app_code="SANDBOX",
                is_auto_queue = False)

deri = investor.Derivatives(account_no="Pybott-D")

print(deri.get_portfolios())

print(deri.get_account_info())