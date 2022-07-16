class WizCoinException(Exception):
	""" The WizCoin module raises this when the module is misused."""
	pass

class WizCoin:
	def __init__(self, galleons, sickles, knuts):
		""" Create a new WizCoin object with galleons, sickles, and knuts. """
		self.galleons = galleons
		self.sickles = sickles
		self.knuts = knuts
		# NOTE: __init__ methid NEVER have a return statement

	@property
	def galleons(self):
		""" Return the number of galleon coins in this object """
		return self._galleons
	
	@galleons.setter
	def galleons(self, value):
		if not isinstance(value, int):
			raise WizCoinException('galleons attr must be set to an int, not a ' + value.__class__.__qualname__)
		if value < 0:
			raise WizCoinException('galleons attr must be a positive int, not ' + value.__class__.__qualname__)	
		self._galleons = value	

	@property
	def total(self):
		""" Total value (in knuts) of all the coins in the WizCoin object. """ 
		return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

	# Note that there is no setter or deleter method for detail

	def __repr__(self):
		"""Returns a string of an expression that re-creates this object."""
		return f'{self.__class__.__qualname__}({self.galleons}, {self.sickles}, {self.knuts})'

	def __str__(self):
		"""Returns a human-readable string representation of this object."""
		return f'{self.galleons}g, {self.sickles}s, {self.knuts}k'

	def __add__(self, other):
		""" Adds the coin amounts in two WizCoin object together. """
		if not isinstance(other, WizCoin):
			return NotImplemented

		return WizCoin(other.galleons + self.galleons, other.sickles + self.sickles, other.knuts + self.knuts)

	def __mul__(self, other):
		""" Multiplies the coin amounts by a non-negative integer. """
		if not isinstance(other, int):
			return NotImplemented
		if other < 0:
			# Multiplying by a negative int results in negative
			# amounts of coins, which is invalid.
			raise WizCoinException('cannot multiply with negative integers')

		return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)