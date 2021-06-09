import requests
import pandas as pd

import json



"""   To display the single loan   """

def display_values(res,loan_id):
        
        data = res.json()

        response = data["response"]
        
        loan_list =[]

       
        

        for i in response['Results']:
               
              
                    
                    result = dict((k, i[k]) for k in ['custom_field_5819', 'custom_field_5820', 'custom_field_5821'
                                                                 ,'custom_field_5822', 'custom_field_5823', 'custom_field_5824',
                                                                 'custom_field_6985','custom_field_7079', 'custom_field_7080',
                                                                 'custom_field_7099','custom_field_7100', 'custom_field_7101',  
                                                                 'custom_field_7102','custom_field_7103', 'custom_field_7104',
                                                                 'custom_field_7106','custom_field_8548']
                                        if k in i)

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
                        
                        field_5819 = i['custom_field_5819']
                   
                    else:
                        
                        field_5819 = ''
                   
                      

                    if key_5820 in result.keys():
                        
                        field_5820 = i['custom_field_5820']
                   
                    else:
                        
                        field_5820 = ''
                    
                      

                    if key_5821 in result.keys():
                      
                       field_5821 = i['custom_field_5821']
                    
                    else:
                        
                        field_5821 = ''
                    
                    

                    if key_5822 in result.keys():
                       
                        field_5822 = i['custom_field_5822']
                    
                    else:
                        
                        field_5822 = ''
                    
                    

                    if key_5823 in result.keys():
                        
                        field_5823 = i['custom_field_5823']
                    
                    else:
                        
                        field_5823 = ''
                     

                    if key_5824 in result.keys():
                        
                        field_5824 = i['custom_field_5824']
                    
                    else:
                        
                        field_5824 = ''
                    
                    if key_6985 in result.keys():
                        
                        field_6985 = i['custom_field_6985']
                   
                    else:
                        
                        field_6985 = ''
                   
                    if key_7079 in result.keys():
                        
                        field_7079 = i['custom_field_7079']
                   
                    else:
                        
                        field_7079 = ''

                    if key_7080 in result.keys():
                        
                        field_7080 = i['custom_field_7080']
                   
                    else:
                        
                        field_7080 = ''
                    
                    if key_7099 in result.keys():
                      
                       field_7099 = i['custom_field_7099']
                    
                    else:
                        
                        field_7099 = ''

                    if key_7100 in result.keys():
                       
                        field_7100 = i['custom_field_7100']
                    
                    else:
                        
                        field_7100 = ''
                    
                    

                    if key_7101 in result.keys():
                        
                        field_7101 = i['custom_field_7101']
                    
                    else:
                        
                        field_7101 = ''
                       

                    if key_7102 in result.keys():
                      
                       field_7102 = i['custom_field_7102']
                    
                    else:
                        
                        field_7102 = ''
                    
                    

                    if key_7103 in result.keys():
                       
                        field_7103 = i['custom_field_7103']
                    
                    else:
                        
                        field_7103 = ''
                    
                    

                    if key_7104 in result.keys():
                        
                        field_7104 = i['custom_field_7104']
                    
                    else:
                        
                        field_7104 = ''
                     

                    if key_7106 in result.keys():
                        
                        field_7106 = i['custom_field_7106']
                    
                    else:
                        
                        field_7106 = ''

                    if key_8548 in result.keys():
                        
                        field_8548 = i['custom_field_8548']
                    
                    else:
                        
                        field_8548 = ''
                       
                        loan_list.append([
                                i['loan_id'],
                                i['loan_product_id'],
                                i['borrower_id'],

                                i['loan_application_id'],
                                i['loan_disbursed_by_id'],
                                i['loan_principal_amount'],
                                i['loan_released_date'],
                                i['loan_interest_method'],
                                i['loan_interest_type'],
                                i['loan_interest_period'],
                                i['loan_interest'],
                                i['loan_duration_period'],
                                i['loan_duration'],
                                i['loan_payment_scheme_id'],
                                i['loan_num_of_repayments'],
                                i['loan_decimal_places'],
                                i['loan_interest_start_date'],
                                i['loan_fees_pro_rata'],
                                i['loan_do_not_adjust_remaining_pro_rata'],
                                i['loan_first_repayment_pro_rata'],
                                i['loan_first_repayment_date'],
                                i['first_repayment_amount'],
                                i['last_repayment_amount'],
                                i['loan_override_maturity_date'],
                                i['override_each_repayment_amount'],
                                i['loan_interest_each_repayment_pro_rata'],
                                i['loan_interest_schedule'],
                                i['loan_principal_schedule'],
                                i['loan_balloon_repayment_amount'],
                                i['automatic_payments'],
                                i['payment_posting_period'],
                                i['total_amount_due'],
                                i['balance_amount'],
                                i['due_date'],
                                i['total_paid'],
                                i['child_status_id'],
                                i['loan_fee_schedule_3951'],
                                i['loan_fee_id_3951'],
                                i['loan_fee_schedule_4734'],
                                i['loan_fee_id_4734'],
                                i['loan_fee_schedule_4727'],
                                i['loan_fee_id_4727'],
                                i['loan_fee_schedule_4726'],
                                i['loan_fee_id_4726'],

                                i['loan_fee_schedule_4725'],
                                i['loan_fee_id_4725'],
                                i['loan_fee_schedule_4724'],
                                i['loan_fee_id_4724'],
                                i['loan_fee_schedule_4611'],
                                i['loan_fee_id_4611'],
                                i['loan_fee_schedule_4197'],
                                i['loan_fee_id_4197'],
                                i['loan_fee_schedule_4196'],
                                i['loan_fee_id_4196'],
                                i['loan_fee_schedule_4195'],
                                i['loan_fee_id_4195'],
                                i['loan_fee_schedule_4194'],
                                i['loan_fee_id_4194'],
                                i['loan_fee_schedule_4735'],
                                i['loan_fee_id_4735'],
                                i['loan_override_sys_gen_penalty'],
                                i['loan_manual_penalty_amount'],
                                i['loan_status_id'],
                                i['loan_title'],
                                i['loan_description'],
                                
                                i['borrower_country'],
                                i['borrower_fullname'],
                                i['borrower_firstname'],
                                i['borrower_lastname'],
                                i['borrower_business_name'],
                                i['borrower_unique_number'],
                                i['borrower_gender'],
                                i['borrower_title'],
                                i['borrower_mobile'],
                                i['borrower_email'],
                                i['borrower_dob'],
                                i['borrower_address'],
                                i['borrower_city'],
                                i['borrower_province'],
                                i['borrower_zipcode'],
                                i['borrower_landline'],
                                i['borrower_working_status'],
                                i['borrower_credit_score'],
                                i['borrower_description'],
                                i['borrower_access_ids'],
                                i['borrower_photo'],
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

                    loan_df.to_csv('data/single_loan_'+str(loan_id)+'.csv',index=None)

  
def main():

    public_key = 12815

    branch = 15735

    loan_id = 1428102

    
    API_BASE_URL = f'https://api-main.loandisk.com/{public_key}/{branch}/loan/{loan_id}'

    header = {
        'content-type': 'application/json',
        'Authorization': 'Fn5eHUrSX6vD6ckykekD52NyamrfpR4gHBYgDk8f',
    }

    
    try:
        
        res = requests.get(API_BASE_URL,headers = header)
           
        display_values(res,loan_id)
       

    except requests.exceptions.HTTPError as e:
        print('Unable to retrieve values.')
        print(e.response.text)
 
