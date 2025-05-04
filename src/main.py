import pandas as pd
import os
import glob
from datetime import datetime

folder_path = 'src/data/raw'

readyData = 'src/data/ready'

excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print(f'Não há nenhum arquivo *xlsx disponível')
else:
    dfs = []
    
    for arquivos in excel_files:
        try:
            df_temp = pd.read_excel(arquivos)
            
            file_name = os.path.basename(arquivos)
            if 'brasil' in file_name.lower():
                df_temp['location'] = 'br'
            elif 'france' in file_name.lower():
                df_temp['location'] = 'fr'
            elif 'italian' in file_name.lower():
                df_temp['location'] = 'it'
            else:
                print('não foi encontrado nenhum arquivo com os seguintes paises br, fr e it') 
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')
            
            df_temp['data_da_venda'] = (
                pd.to_datetime(df_temp['sale_date'], format='%m%d%y')
                    .dt.strftime('%d-%m-%y')
            )
           
            df_temp.pop('sale_date')
            
            df_temp['FileName'] = file_name
            
            print(df_temp)
            
            dfs.append(df_temp)
            
        except Exception as e:
            print(f'Error ao ler o arquivo, Erro {e}')
    if dfs:
        result = pd.concat(dfs, ignore_index=True)
    
        output_file = os.path.join(readyData, 'clean.xlsx')
        
        writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
        
        result.to_excel(writer, index=False)
        
        writer._save()
    else:
        print('Nenhum dado precisa ser salvo')