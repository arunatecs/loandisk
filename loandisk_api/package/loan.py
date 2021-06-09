import requests

import json
import pandas as pd


"""   To display list of loan values         """

def display_values(res):
        
        data = res.json()
        
        response = data["response"]
        
        loan_list =[]
        
      
        
        counter =0

        for i in response['Results']:
               
                while(counter < len(i)):
                    
                    result = dict((k, i[counter][k]) for k in ['custom_field_5819', 'custom_field_5820', 'custom_field_5821'
                                                                 ,'custom_field_5822', 'custom_field_5823', 'custom_field_5824',
                                                                 'custom_field_6985','custom_field_7079', 'custom_field_7080',
                                                                 'custom_field_7099','custom_field_7100', 'custom_field_7101',  
                                                                 'custom_field_7102','custom_field_7103', 'custom_field_7104',
                                                                 'custom_field_7106','custom_field_8548']
                                        if k in i[counter])

                    key_5819 = 'custom_field_5819'   
                    key_5820 = 'custom_field_5820'
                    key_5821 = 'custom_field_5821' 
                    key_5822 = 'custom_field_5822'
                    key_5823 = 'custom_field_5823'
                    key_5824 = 'custom_field_5824'  
                    key_6985 = 'custom_field_6985'
                    key_7079 = 'custom_field_7079'      
                    key_7080 = 'custom_field_7080'
                    key_7099 = 'custom_field_7099'
                    key_7100 = 'custom_field_7100' 
                    key_7101 = 'custom_field_7101'
                    key_7102 = 'custom_field_7102' 
                    key_7103 = 'custom_field_7103'
                    key_7104 = 'custom_field_7104'
                    key_7106 = 'custom_field_7106'
                    key_8548 = 'custom_field_8548'   
   

                    if key_5819 in result.keys():
                        
                        field_5819 = i[counter]['custom_field_5819']
                   
                    else:
                        
                        field_5819 = ''
                   
                      

                    if key_5820 in result.keys():
                        
                        field_5820 = i[counter]['custom_field_5820']
                   
                    else:
                        
                        field_5820 = ''
                    
                      

                    if key_5821 in result.keys():
                      
                       field_5821 = i[counter]['custom_field_5821']
                    
                    else:
                        
                        field_5821 = ''
                    
                    

                    if key_5822 in result.keys():
                       
                        field_5822 = i[counter]['custom_field_5822']
                    
                    else:
                        
                        field_5822 = ''
                    
                    

                    if key_5823 in result.keys():
                        
                        field_5823 = i[counter]['custom_field_5823']
                    
                    else:
                        
                        field_5823 = ''
                     

                    if key_5824 in result.keys():
                        
                        field_5824 = i[counter]['custom_field_5824']
                    
                    else:
                        
                        field_5824 = ''
                    
                    if key_6985 in result.keys():
                        
                        field_6985 = i[counter]['custom_field_6985']
                   
                    else:
                        
                        field_6985 = ''
                   
                    if key_7079 in result.keys():
                        
                        field_7079 = i[counter]['custom_field_7079']
                   
                    else:
                        
                        field_7079 = ''

                    if key_7080 in result.keys():
                        
                        field_7080 = i[counter]['custom_field_7080']
                   
                    else:
                        
                        field_7080 = ''
                    
                    if key_7099 in result.keys():
                      
                       field_7099 = i[counter]['custom_field_7099']
                    
                    else:
                        
                        field_7099 = ''

                    if key_7100 in result.keys():
                       
                        field_7100 = i[counter]['custom_field_7100']
                    
                    else:
                        
                        field_7100 = ''
                    
                    

                    if key_7101 in result.keys():
                        
                        field_7101 = i[counter]['custom_field_7101']
                    
                    else:
                        
                        field_7101 = ''
                       

                    if key_7102 in result.keys():
                      
                       field_7102 = i[counter]['custom_field_7102']
                    
                    else:
                        
                        field_7102 = ''
                    
                    

                    if key_7103 in result.keys():
                       
                        field_7103 = i[counter]['custom_field_7103']
                    
                    else:
                        
                        field_7103 = ''
                    
                    

                    if key_7104 in result.keys():
                        
                        field_7104 = i[counter]['custom_field_7104']
                    
                    else:
                        
                        field_7104 = ''
                     

                    if key_7106 in result.keys():
                        
                        field_7106 = i[counter]['custom_field_7106']
                    
                    else:
                        
                        field_7106 = ''

                    if key_8548 in result.keys():
                        
                        field_8548 = i[counter]['custom_field_8548']
                    
                    else:
                        
                        field_8548 = ''
                       
                        loan_list.append([
                                i[counter]['loan_id'],
                                i[counter]['loan_product_id'],
                                i[counter]['borrower_id'],

                                i[counter]['loan_application_id'],
                                i[counter]['loan_disbursed_by_id'],
                                i[counter]['loan_principal_amount'],
                                i[counter]['loan_released_date'],
                                i[counter]['loan_interest_method'],
                                i[counter]['loan_interest_type'],
                                i[counter]['loan_interest_period'],
                                i[counter]['loan_interest'],
                                i[counter]['loan_duration_period'],
                                i[counter]['loan_duration'],
                                i[counter]['loan_payment_scheme_id'],
                                i[counter]['loan_num_of_repayments'],
                                i[counter]['loan_decimal_places'],
                                i[counter]['loan_interest_start_date'],
                                i[counter]['loan_fees_pro_rata'],
                                i[counter]['loan_do_not_adjust_remaining_pro_rata'],
                                i[counter]['loan_first_repayment_pro_rata'],
                                i[counter]['loan_first_repayment_date'],
                                i[counter]['first_repayment_amount'],
                                i[counter]['last_repayment_amount'],
                                i[counter]['loan_override_maturity_date'],
                                i[counter]['override_each_repayment_amount'],
                                i[counter]['loan_interest_each_repayment_pro_rata'],
                                i[counter]['loan_interest_schedule'],
                                i[counter]['loan_principal_schedule'],
                                i[counter]['loan_balloon_repayment_amount'],
                                i[counter]['automatic_payments'],
                                i[counter]['payment_posting_period'],
                                i[counter]['total_amount_due'],
                                i[counter]['balance_amount'],
                                i[counter]['due_date'],
                                i[counter]['total_paid'],
                                i[counter]['child_status_id'],
                                i[counter]['loan_fee_schedule_3951'],
                                i[counter]['loan_fee_id_3951'],
                                i[counter]['loan_fee_schedule_4734'],
                                i[counter]['loan_fee_id_4734'],
                                i[counter]['loan_fee_schedule_4727'],
                                i[counter]['loan_fee_id_4727'],
                                i[counter]['loan_fee_schedule_4726'],
                                i[counter]['loan_fee_id_4726'],

                                i[counter]['loan_fee_schedule_4725'],
                                i[counter]['loan_fee_id_4725'],
                                i[counter]['loan_fee_schedule_4724'],
                                i[counter]['loan_fee_id_4724'],
                                i[counter]['loan_fee_schedule_4611'],
                                i[counter]['loan_fee_id_4611'],
                                i[counter]['loan_fee_schedule_4197'],
                                i[counter]['loan_fee_id_4197'],
                                i[counter]['loan_fee_schedule_4196'],
                                i[counter]['loan_fee_id_4196'],
                                i[counter]['loan_fee_schedule_4195'],
                                i[counter]['loan_fee_id_4195'],
                                i[counter]['loan_fee_schedule_4194'],
                                i[counter]['loan_fee_id_4194'],
                                i[counter]['loan_fee_schedule_4735'],
                                i[counter]['loan_fee_id_4735'],
                                i[counter]['loan_override_sys_gen_penalty'],
                                i[counter]['loan_manual_penalty_amount'],
                                i[counter]['loan_status_id'],
                                i[counter]['loan_title'],
                                i[counter]['loan_description'],
                                
                                i[counter]['borrower_country'],
                                i[counter]['borrower_fullname'],
                                i[counter]['borrower_firstname'],
                                i[counter]['borrower_lastname'],
                                i[counter]['borrower_business_name'],
                                i[counter]['borrower_unique_number'],
                                i[counter]['borrower_gender'],
                                i[counter]['borrower_title'],
                                i[counter]['borrower_mobile'],
                                i[counter]['borrower_email'],
                                i[counter]['borrower_dob'],
                                i[counter]['borrower_address'],
                                i[counter]['borrower_city'],
                                i[counter]['borrower_province'],
                                i[counter]['borrower_zipcode'],
                                i[counter]['borrower_landline'],
                                i[counter]['borrower_working_status'],
                                i[counter]['borrower_credit_score'],
                                i[counter]['borrower_description'],
                                i[counter]['borrower_access_ids'],
                                i[counter]['borrower_photo'],
                                field_5819,
                                field_5820,
                                field_5821,
                                field_5822,
                                field_5823,
                                field_5824,
                                field_6985,
                                field_7079,
                                field_7080,
                                field_7099,
                                field_7100,
                                field_7101,
                                field_7102,
                                field_7103,
                                field_7104,
                                field_7106,
                                field_8548,
                                

                            ])
                            
                   
                        
                    counter +=  1
                    
                    loan_df = pd.DataFrame(data=loan_list, columns=['loan_id','loan_product_id','borrower_id','loan_application_id', 'loan_disbursed_by_id' , 
                                            'loan_principal_amount' , 'loan_released_date' , 'loan_interest_method' , 
                                            'loan_interest_type' , 'loan_interest_period' , 'loan_interest' , 'loan_duration_period' ,
                                            'loan_duration' , 'loan_payment_scheme_id' , 'loan_num_of_repayments' , 'loan_decimal_places' , 
                                            'loan_interest_start_date' , 'loan_fees_pro_rata' , 'loan_do_not_adjust_remaining_pro_rata' , 
                                            'loan_first_repayment_pro_rata' , 'loan_first_repayment_date' , 'first_repayment_amount' , 
                                            'last_repayment_amount' , 'loan_override_maturity_date' , 'override_each_repayment_amount' , 
                                            'loan_interest_each_repayment_pro_rata' , 'loan_interest_schedule' , 'loan_principal_schedule' ,
                                            'loan_balloon_repayment_amount' , 'automatic_payments' , 'payment_posting_period' ,
                                            'total_amount_due' , 'balance_amount' , 'due_date' , 'total_paid' , 'child_status_id' ,
                                            'loan_fee_schedule_3951' , 'loan_fee_id_3951' , 'loan_fee_schedule_4734' , 'loan_fee_id_4734' 
                                            ,'loan_fee_schedule_4727' , 'loan_fee_id_4727' , 'loan_fee_schedule_4726' , 'loan_fee_id_4726' ,
                                            'loan_fee_schedule_4725' , 'loan_fee_id_4725' , 'loan_fee_schedule_4724' , 'loan_fee_id_4724' , 
                                            'loan_fee_schedule_4611' , 'loan_fee_id_4611' , 'loan_fee_schedule_4197' , 'loan_fee_id_4197' ,
                                            'loan_fee_schedule_4196' , 'loan_fee_id_4196' , 'loan_fee_schedule_4195' , 'loan_fee_id_4195' ,
                                            'loan_fee_schedule_4194' , 'loan_fee_id_4194' , 'loan_fee_schedule_4735' , 'loan_fee_id_4735' , 
                                            'loan_override_sys_gen_penalty' , 'loan_manual_penalty_amount' , 'loan_status_id' , 'loan_title' ,
                                            'loan_description' ,    'borrower_country' , 'borrower_fullname' , 'borrower_firstname' ,
                                            'borrower_lastname' , 'borrower_business_name' , 'borrower_unique_number' , 'borrower_gender' ,
                                            'borrower_title' , 'borrower_mobile' , 'borrower_email' , 'borrower_dob' , 'borrower_address' ,
                                            'borrower_city' , 'borrower_province' , 'borrower_zipcode' , 'borrower_landline' , 
                                            'borrower_working_status' , 'borrower_credit_score' , 'borrower_description' , 'borrower_access_ids' ,
                                            'borrower_photo' , "custom_field_5819" , "custom_field_5820" , 'custom_field_5821' , 'custom_field_5822' ,
                                            'custom_field_5823' , 'custom_field_5824' ,"custom_field_6985" , "custom_field_7079" , 
                                            'custom_field_7080' , 'custom_field_7099' ,"custom_field_7100" , "custom_field_7101" ,
                                            'custom_field_7102' , 'custom_field_7103' ,'custom_field_7104' , 'custom_field_7106' ,
                                            'custom_field_8548',
                                            
                                            ])

                    loan_df.to_csv('data/loan.csv',index=None)
    
def main():

    public_key = 12815

    branch = 15735 

    
    
    
    API_BASE_URL = f'https://api-main.loandisk.com/{public_key}/{branch}/loan/from/1/count/50'

    header = {
        'content-type': 'application/json',
        'Authorization': 'Fn5eHUrSX6vD6ckykekD52NyamrfpR4gHBYgDk8f',
    }

    
    try:
        
        res = requests.get(API_BASE_URL,headers = header)
        
        display_values(res)
    

    except requests.exceptions.HTTPError as e:
        print('Unable to retrieve values.')
        print(e.response.text)


