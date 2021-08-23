class Atm(object):
  def __init__(self,cardNumber,pinNumber,company):
    self.cardNumber=cardNumber
    self.pinNumber=pinNumber

  def start(self):
    print("CashWithdrawl")

  def stop(self):
    print("BalanceEnquiry")

hdfc = Atm(123,456,"paypal")
hdfc.start()
hdfc.stop()