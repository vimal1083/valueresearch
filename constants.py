
from collections import OrderedDict


# FORMAT_A https://bit.ly/2Zrbe45 results_Nxbrl
# FORMAT_B https://bit.ly/2MJoRIp results
# FORMAT_C https://bit.ly/2Ku8yfY results
# FORMAT_D https://bit.ly/2OHNqrR results non banking
# FORMAT_E  non banking
# FORMAT_C https://bit.ly/2Ku8yfY results

format_a_fields = OrderedDict()

format_a_fields["revenue_from_operations"] = "Revenue from operations"
format_a_fields["other_income"] = "Other income"
format_a_fields["total_income"] = "Total Income"
# Expenses
format_a_fields["cost_of_material_consumed"] = "Cost of materials consumed"
format_a_fields["purchase_of_stock_in_trade"] = "Purchases of stock-in-trade"
format_a_fields["changes_in_inventories"] = "Changes in inventories of finished goods"
format_a_fields["employee_benifit_expense"] = "Employee benefits expense"
format_a_fields["finance_cost"] = "Finance costs"
format_a_fields["depreciation_expense"] = "Depreciation and amortisation"
format_a_fields["other_expense"] = "Other expenses"
format_a_fields["total_expense"] = "Total Expenses"
# Tax
format_a_fields["current_tax"] = "Current Tax"
format_a_fields["deferred_tax"] = "Deferred Tax"
format_a_fields["total_tax"] = "Total Tax expense"

format_a_fields["pl_from_continuing_operations"] = "rofit (Loss) for the period from continuing operations"
format_a_fields["pl_from_discontinued_operations"] = "Profit/(loss) from discontinued operations"
format_a_fields["tax_expense_of_discontinued_operations"] = "Tax expense of discontinued operations"


# Total profit or loss, attributable to
format_a_fields["pl_attributable_to_non_controlling_interests"] = "Total profit or loss, attributable to non-controlling interests"
format_a_fields["pl_attributable_to_owners_of_parent"] = "Profit or loss, attributable to owners of parent"


# Total Comprehensive income for the period attributable to
format_a_fields["ci_attributable_to_non_controlling_interests"] = "Total comprehensive income for the period attributable to owners of parent non-controlling interests"
format_a_fields["ci_attributable_to_owners_of_parent"] = "Comprehensive income for the period attributable to owners of parent"

    
# PAT
format_a_fields["pat"] = "Consolidated Net Profit/Loss for the period"
format_a_fields["share_of_pl"] = "Share of profit / (loss) of associates"
format_a_fields["total_comprehensive_income"] = "Total comprehensive income"

# PBT
format_a_fields["pbt"] = "Profit / (Loss) before tax"


# Details of equity share capital
format_a_fields["paid_up_equity_shatre_capital"] = "Paid-up equity share capital"
format_a_fields["face_value"] = "Face Value (in Rs.)"

# Details of debt securities
format_a_fields["paid_up_debt_capital"] = "Paid-up debt capital"
format_a_fields["face_value_of_debt"] = "Face value of debt securities (in Rs.)"
format_a_fields["reserve_excluding_revaluation"] = "Reserve excluding Revaluation Reserves as per balance"
format_a_fields["debenture_redemption_reserve"] = "Debenture redemption reserve"

# Earnings per equity share
format_a_fields["consolidated_basic_eps"] = "Basic EPS for continued and discontinued operations"
format_a_fields["consolidated_diluted_eps"] = "Diluted EPS for continued and discontinued operations"

format_b_fields = OrderedDict()

format_b_fields["IGNORE_THIS"] = "Profit from Operations before Other Income"
format_b_fields["revenue_from_operations"] = "Net Sales/Income from Operation"
format_b_fields["other_income"] = "Other Income"
format_b_fields["total_income"] = "Total Income"

# Expenses
format_b_fields["cost_of_material_consumed"] = "Consumption of Raw Materials"
format_b_fields["purchase_of_stock_in_trade"] = "Purchase of traded goods"
format_b_fields["employee_benifit_expense"] = "Employees Cost"
format_b_fields["depreciation_expense"] = "Depreciation"
format_b_fields["other_expense"] = "Other Expenditure"
format_b_fields["total_expense"] = "Total Expenditure"

# PBT
format_b_fields["pbt"] = "Profit(+)/Loss(-) from Ordinary Activities before tax"
format_b_fields["total_tax"] = "Tax Expense"
# PAT
format_b_fields["pat"] = "Net Profit (+) / Loss (-) for the period"
# Details of equity share capital
format_b_fields["paid_up_equity_shatre_capital"] = "Paid-up Equity Share Capital"
format_b_fields["face_value"] = "Face Value (in Rs.)"

# Earnings per equity share
format_b_fields["consolidated_basic_eps"] = "Basic EPS after Extraordinary items (in Rs.)"
format_b_fields["consolidated_diluted_eps"] = "Diluted EPS after Extraordinary items (in Rs.)"

format_c_fields = OrderedDict()


format_c_fields["IGNORE_THIS"] = "Profit from Operations before Other Income" 
format_c_fields["revenue_from_operations"] = "Net Sales/Income from Operation" 
format_c_fields["other_income"] = "Other Income" 
format_c_fields["total_income"] = "Total Income" 
# Expenses
format_c_fields["cost_of_material_consumed"] = "Consumption of Raw Materials" 
format_c_fields["purchase_of_stock_in_trade"] = "Purchase of traded goods" 
format_c_fields["employee_benifit_expense"] = "Employees Cost" 
format_c_fields["depreciation_expense"] = "Depreciation" 
format_c_fields["other_expense"] = "Other Expenditure" 
format_c_fields["total_expense"] = "Total Expenditure" 
# PBT
format_c_fields["pbt"] = "Profit(+)/Loss(-) from Ordinary Activities before tax" 
format_c_fields["total_tax"] = "Tax Expense" 
# PAT
format_c_fields["pat"] = "Consolidated Net Profit (+) / Loss (-) for the period" 

# Details of equity share capital
format_c_fields["paid_up_equity_shatre_capital"] = "Paid-up Equity Share Capital" 
format_c_fields["face_value"] = "Face Value (in Rs.)" 
# Earnings per equity share
format_c_fields["consolidated_basic_eps"] = "Basic EPS after Extraordinary items (in Rs.)" 
format_c_fields["consolidated_diluted_eps"] = "Diluted EPS after Extraordinary items (in Rs.)" 


format_d_fields = OrderedDict()

format_d_fields["other_income"] = "Other Income" 
format_d_fields["total_income"] = "Total Income" 
# Expenses
format_d_fields["employee_benifit_expense"] = "Employees cost" 
format_d_fields["other_expense"] = "Other Operating Expenses (Any item exceeding 10% of the total expenses relating to continuing operations to be shown separately)" 
format_d_fields["total_expense"] = "Total Expenditure excluding provisions and contingencies" 
# PBT
format_d_fields["pbt"] = "Profit(+) / Loss(-) from Ordinary Activities before tax" 
format_d_fields["total_tax"] = "Tax Expense" 
# PAT
format_d_fields["pat"] = "Consolidated Net Profit (+) / Loss (-) for the period" 

# Details of equity share capital
format_d_fields["paid_up_equity_shatre_capital"] = "Paid-up Equity Share Capital (in Rs.)" 
format_d_fields["face_value"] = "Face Value (in Rs.)" 
# Earnings per equity share
format_d_fields["consolidated_basic_eps"] = "Basic EPS after Extraordinary items (in Rs.)" 
format_d_fields["consolidated_diluted_eps"] = "Diluted EPS after Extraordinary items (in Rs.)" 
# BANK FIELDS
format_d_fields["india_holding_percentage"] = "Percentage of shares Held by Government of India" 
format_d_fields["npa_percentage"] = "% of Gross/Net NPA" 
format_d_fields["provisions_and_contingencies"] = "Provisions (other than tax) and contingencies" 
format_d_fields["interest_earned"] ="Interest Earned" 
format_d_fields["discount_on_advances"] ="Interest/Discount on Advances/Bills" 
format_d_fields["income_on_investments"] ="Income on Investments" 
format_d_fields["capital_adequacy_ratio"] = "Capital Adequacy Ratio"



format_e_fields = OrderedDict()

format_e_fields["other_income"] = "Other Income" 
format_e_fields["total_income"] = "Total Income" 
# Expenses
format_e_fields["employee_benifit_expense"] = "Employees cost" 
format_e_fields["other_expense"] = "Other Operating Expenses (Any item exceeding 10% of the total expenses relating to continuing operations to be shown separately)" 
format_e_fields["total_expense"] = "Total Expenditure excluding provisions and contingencies" 
# PBT
format_e_fields["pbt"] = "Profit(+) / Loss(-) from Ordinary Activities before tax" 
format_e_fields["total_tax"] = "Tax Expense" 
# PAT
format_e_fields["pat"] = "Net Profit (+) / Loss (-) for the period" 

# Details of equity share capital
format_e_fields["paid_up_equity_shatre_capital"] = "Paid-up Equity Share Capital (in Rs.)" 
format_e_fields["face_value"] = "Face Value (in Rs.)" 
# Earnings per equity share
format_e_fields["consolidated_basic_eps"] = "Basic EPS after Extraordinary items (in Rs.)" 
format_e_fields["consolidated_diluted_eps"] = "Diluted EPS after Extraordinary items (in Rs.)" 
# BANK FIELDS
format_e_fields["india_holding_percentage"] = "Percentage of shares Held by Government of India" 
format_e_fields["npa_percentage"] = "% of Gross/Net NPA" 
format_e_fields["provisions_and_contingencies"] = "Provisions (other than tax) and contingencies" 
format_e_fields["interest_earned"] ="Interest Earned" 
format_e_fields["discount_on_advances"] ="Interest/Discount on Advances/Bills" 
format_e_fields["income_on_investments"] ="Income on Investments" 
format_e_fields["capital_adequacy_ratio"] = "Capital Adequacy Ratio"




format_f_fields = OrderedDict()


format_f_fields["IGNORE_THIS"] = "Profit from Operations before Other Income" 
format_f_fields["revenue_from_operations"] = "Net Sales/Income from Operation" 
format_f_fields["other_income"] = "Other Income" 
# Expenses
format_f_fields["cost_of_material_consumed"] = "Consumption of Raw Materials" 
format_f_fields["purchase_of_stock_in_trade"] = "Purchase of traded goods" 
format_f_fields["employee_benifit_expense"] = "Employees Cost" 
format_f_fields["depreciation_expense"] = "Depreciation" 
format_f_fields["other_expense"] = "Other Expenditure" 
format_f_fields["total_expense"] = "Total Expenditure" 
# PBT
format_f_fields["pbt"] = "Profit(+)/Loss(-) from Ordinary Activities before tax" 
format_f_fields["total_tax"] = "Tax Expense" 
# PAT
format_f_fields["pat"] = "Net Profit (+) / Loss (-) for the period" 

# Details of equity share capital
format_f_fields["paid_up_equity_shatre_capital"] = "Paid-up Equity Share Capital" 
format_f_fields["face_value"] = "Face Value (in Rs.)" 
# Earnings per equity share
format_f_fields["consolidated_basic_eps"] = "Basic EPS after Extraordinary items (in Rs.)" 
format_f_fields["consolidated_diluted_eps"] = "Diluted EPS after Extraordinary items (in Rs.)" 



field_mappinng = {
    
    "FORMAT_A": {
        "XPath": "body > table  > tr > td > table  > tr > td:nth-child(2) > table  > tr > td:nth-child(1) > table  > tr > td > table  > tr:nth-child({0})",
        "fields": format_a_fields
    },
    "FORMAT_B": {
        "XPath": "body > table  > tr > td > table  > tr > td:nth-child(2)  > table  > tr > td > table  > tr > td > table  > tr:nth-child({0})",
        "fields" : format_b_fields
        
    },
    "FORMAT_C": {
        "XPath": "body > table  > tr > td > table  > tr > td:nth-child(2)  > table  > tr > td > table  > tr > td > table  > tr:nth-child({0})",
        "fields" :format_c_fields
    },
    "FORMAT_D": {
        "XPath": "body > table  > tr > td > table  > tr > td:nth-child(2)  > table  > tr > td > table  > tr > td > table  > tr:nth-child({0})",
        "fields" : format_d_fields
    },
   "FORMAT_E": {
       "XPath": "body > table  > tr > td > table  > tr > td:nth-child(2)  > table  > tr > td > table  > tr > td > table  > tr:nth-child({0})",
        "fields" : format_e_fields
    },
    "FORMAT_F": {
        "XPath": "body > table  > tr > td > table  > tr > td:nth-child(2)  > table  > tr > td > table  > tr > td > table  > tr:nth-child({0})",
        "fields" :format_f_fields
    }
}

format_identifier_mapping = OrderedDict()
format_identifier_mapping["FORMAT_A"] = {
        "should_have": [
            "Non Banking",
            "Profit (Loss) for the period from continuing operations",
            "Revenue from operations",
            "Total profit or loss, attributable to",
            "Earnings per equity share for continuing operations",
            "Net movement in regulatory deferral account balances related to profit or loss and the related deferred tax movement",
        ]
    }
format_identifier_mapping["FORMAT_B"] = {
        "should_have": [
            "Non Banking",
            "Net Sales/Income from Operations",
            "Increase/Decrease in Stock in trade and work in progress"
        ]
    }
format_identifier_mapping["FORMAT_F"] = {
        "should_have": [
            "Non Banking",
            "Net Sales/Income from Operation",
            "Increase/Decrease in Stock in trade and work in progress"
        ],
        "should_not_have":[
            "Total Income"
        ]
    }

format_identifier_mapping["FORMAT_C"] = {
        "should_have": [
            "Non Banking",
            "Net Sales/Income from Operation",
            "Increase/Decrease in Stock in trade and work in progress"
        ]
    }

format_identifier_mapping["FORMAT_E"] = {
        "should_have": [
            "Percentage of shares Held by Government of India",
            "Total Expenditure excluding provisions and contingencies"
        ],
        "should_not_have":[
            "Consolidated Net Profit (+) / Loss (-) for the period"
        ]
    }

format_identifier_mapping["FORMAT_D"] = {
        "should_have": [
            "Percentage of shares Held by Government of India",
            "Total Expenditure excluding provisions and contingencies"
        ]
    }


