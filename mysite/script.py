import random
import calendar
import pandas as pd
from datetime import datetime


def get_filter_date_data(year, month):
    months_dict = dict((month, index) for index, month in enumerate(calendar.month_abbr) if month)
    month_data = str(months_dict[month]) if len(str(months_dict[month])) == 2 else ('0'+str(months_dict[month]))
    filter_date_data = str(year)+'-'+month_data+'-'+'10'
    return filter_date_data


finalDataFrame = pd.DataFrame()

for i in range(30) :
        insurer_code = '115'
        user_id = {'90' : random.choices(['1', '401', '662'])[0],
                   '102': random.choices(['848'])[0],
                   '103': random.choices(['', '2', '662'])[0],
                   '108': random.choices(['401', '662'])[0],
                   '115': random.choices(['', '1', '79', '662', '852'])[0],
                   '144': random.choices(['1', '662'])[0],
                   '146': random.choices(['1', '662', '802', '852'])[0],
                   '148': random.choices(['1'])[0],
                   '149': random.choices(['1', '662'])[0],
        }
        lob = random.choices(['CRG', 'SFSP'])[0]
        filetype = random.choices(['POLICY', 'CLAIM', 'OCCUPANCY'])[0]
        year =  random.choices(['2019', '2020', '2021', '2022'])[0]
        month = random.choices(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])[0]
        version = random.choices(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])[0]
        filename = f'{insurer_code}_{lob}_{filetype}_{month}_{year}.dat'
        is_no_business = random.choices(['0', '1'])[0]

        
        if version == '0' :
                docfile = f'documents/{insurer_code}_{lob}_{filetype}_{month}_{year}.dat'
        else :
                docfile = f'documents/{insurer_code}_{lob}_{filetype}_{month}_{year}_{version}.dat'
        
        if is_no_business == '1' :
                filename = f'{insurer_code}_NO_BUSINESS_{month}_{year}.dat'
                docfile = f'documents/{filename}'
        
        
        data = {'id' : random.choices(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])[0],
                'docfile' : docfile,
                'filename' : filename,
                'prevalidation_status' : random.choices(['Failed', 'Not applicable', 'Passed', 'Pending'])[0],
                'prevalidation' : random.choices(['Failed', 'Not applicable', 'Passed', 'Pending'])[0],
                'intertable_validation' : random.choices(['Failed', 'Not applicable', 'Passed', 'Pending'])[0],
                'fieldlevel_validation' : random.choices(['Not applicable', 'Pending'])[0],
                'status': random.choices(['Success'])[0],
                'prevalidation_check_error': random.choices(['No error', 'Passed'])[0],
                'prevalidation_error': random.choices(['No error', 'Field-level Validation Success', 'Field-level Validation Failed', '',])[0],
                'intertable_validation_error': random.choices(['No error', 'Inter-Table Validation Failed', 'Inter-Table Validation Partially Success', 'Inter-Table Validation Passed'])[0],
                'fieldlevel_validation_error': random.choices(['No error'])[0],
                'filetype': random.choices(['Policy'])[0],
                'segment': random.choices(['Cargo'])[0],
                'lob': random.choices(['Marine'])[0],
                'months': month.capitalize(),
                'years': year,
                'control_amount': '0',
                'control_number': '0',
                'is_no_business': is_no_business,
                'created_at': datetime.now(),
                'updated_at': datetime.now(),
                'insurer_code': insurer_code,
                'file_status': random.choices(['FAIL REQUEST', 'FAILURE', 'NO BUSINESS', 'PROCESSING', 'FAIL REQUEST APPROVED', 'PARTIALLY SUCCESS', 'SUCCESS', 'RECEIVED'])[0],
                'failed_reason': '',
                'failure_records': '0',
                'success_records': '0',
                'processed_records': '0',
                'processed_on': datetime.now(),
                'version': version,
                'filter_date': get_filter_date_data(year, month.capitalize()),
                'user_id': user_id[insurer_code],
                'fp_starttime': '',
                'fp_endtime': '',
                'fp_status': '',
                'is_failrequest': random.choices(['0', '1'])[0],
                'is_relaxed': random.choices(['0', '1'])[0],
                'is_reuploaded': random.choices(['0', '1'])[0],
                'deleted_at': '',
                'is_deleted': random.choices(['0', '1'])[0],
                'password': '',
                'last_login': '',
                'address': '',
                'mobile_number': '',
                'telephone_number': '',
                'fax_number': '',
                'user_role': '',
                'sent_welcome_email': '',
                'date_of_birth': '',
                'date_of_joining': '',
                'username': '',
                'email': '',
                'first_name': '',
                'is_active': '',
                'is_superuser': '',
                'is_staff': '',
                'is_download': '',
                'is_upload': '',
                'is_create_user': '',
                'is_suspended': '',
                'is_summary_file': '',
                'is_create_admin': '',
                'is_login_status': '',
                'is_district': '',
                'is_office': '',
                'is_summary_file_status': '',
                'is_add_special_user': '',
                'created_on': '',
                'changed_password_date': '',
                'created_by_id': '',
        }

        finalDataFrame = finalDataFrame.append(data, ignore_index=True)

finalDataFrame.to_csv('Data.csv', index=False)