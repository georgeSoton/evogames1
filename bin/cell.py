coop_cost = 1
coop_benefit = 2

class cell:
	colour = 0,0,0
	default_payoff = 0
	payoff_dict = {}
	name = ""
	def payoff_against(rivalname):
		if rivalname in payoff_dict:
			return payoff_dict[rivalname]
		else:
			return default_payoff

class defector(cell):
	def __init__(self):
		self.colour = 255,0,0
		self.name = "defector"
		self.payoff_dict["defector"] = 0
		self.payoff_dict["cooperator"] = coop_benefit
