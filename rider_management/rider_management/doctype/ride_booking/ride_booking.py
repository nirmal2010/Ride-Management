# Copyright (c) 2025, Nirmalrajaa K and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	pass

@frappe.whitelist()
def calc_amount(self, method):
	final_serv_cost = 0
	km_total = 0
	if self.price_per_km:
		km_total = (self.price_per_km * self.estimated_km)
	if self.services:
		for cost in self.services:
			final_serv_cost += cost.amount
				
	total_chargable = final_serv_cost + km_total
	
	self.total_amount = total_chargable