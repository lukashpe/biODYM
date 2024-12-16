"""
Created on 16.12.2024

@author: lhoppe
"""

"""
File biODYM_export

Contains export options for biODYM

standard abbreviation: bix


"""

import pandas as pd
import xlsxwriter

# Export values of all flows and stocks to Excel for all elements
def export_xlsx(Dyn_MFA_System, MyYears, ModelClassification):
    flow_labels = []
    for flow in Dyn_MFA_System.FlowDict:
        flow_labels.append(Dyn_MFA_System.FlowDict[flow].Name)
    flow_labels
    
    stock_labels = []
    for stock in Dyn_MFA_System.StockDict:
        stock_labels.append(Dyn_MFA_System.StockDict[stock].Name)
    stock_labels
    
    writer = pd.ExcelWriter('Case_study_results.xlsx', engine='xlsxwriter')
    for element in ModelClassification['Element'].Items:
        flows_Values = []
        for flow in Dyn_MFA_System.FlowDict:
            flows_Values.append(Dyn_MFA_System.FlowDict[flow].Values[:, ModelClassification['Element'].Items.index(element)])
        df_flows = pd.DataFrame(flows_Values).T
        df_flows.columns = flow_labels
        df_flows['Years'] = MyYears
        df_flows.set_index('Years', inplace=True, drop=True)
    
    
        stock_Values = []
        for stock in Dyn_MFA_System.StockDict:
            stock_Values.append(Dyn_MFA_System.StockDict[stock].Values[:, ModelClassification['Element'].Items.index(element)])
        df_stock = pd.DataFrame(stock_Values).T
        df_stock.columns = stock_labels
        df_stock['Years'] = MyYears
        df_stock.set_index('Years', inplace=True, drop=True)
    
    
    
        df_flows.to_excel(writer, sheet_name= f'FlowDict_{element}')
        df_stock.to_excel(writer, sheet_name= f'StockDict_{element}')
    
    
    writer.close()