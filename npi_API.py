import json,requests,re,os,sys,csv,time,random
import pandas as pd
from pprint import pprint


file=open(r'NPI.csv','r')
reader=csv.reader(file)
npi=[i[0] for i in reader]  #store list of npi codes in variable named npi



def addressed(libs):
    addr_dat=[]
    for addr in libs['addresses']:
        for field in df_iter:
            try:
                addr_dat.append(addr[field])
            except KeyError:
                addr_dat.append('N/A')
    return addr_dat

def identifiers(lib):
    dat=[]
    id_=lib['identifiers']
    if id_=='':
        return ['N/A']
    else:
        dat.append("{'identifiers': "+''.join(str(id_))+'}')
        return dat[0]

def validate(los):
    for i in range(len(los)):
        if los[i]=='':
            los[i]='N/A'

def basics(lib):
    dat=[]
    for field in basic:
        try:
            dat.append(lib['basic'][field])
        except KeyError:
            dat.append('N/A')
    return dat


def tax(lib):#if primary returns N/A, it is because there is only Other Taxonomies listed
    taxies=lib['taxonomies']
    rest=[]
    dat=[]
    for dic in taxies:
        if dic['primary']==True:
            primary=dic
        elif dic['primary']==False:
            rest.append(dic)
    for i in tax_iter:
        try:
            dat.append(primary[i])
        except (KeyError,UnboundLocalError):
            dat.append('N/A')
    dat.append("{'taxonomies': "+''.join(str(rest))+'}')
    return dat


pd.options.display.max_columns=None

error_npi=['N/A' for i in range(55)]

not_found404=['D/A' for i in range(55)]

tax_iter=['code','desc','license','primary','state']

basic=['authorized_official_credential',
           'authorized_official_first_name',
           'authorized_official_last_name',
           'authorized_official_middle_name',
           'authorized_official_name_prefix',
           'authorized_official_telephone_number',
           'authorized_official_title_or_position',
           'certification_date',
           'credential',
           'deactivation_date',
           'enumeration_date',
           'first_name',
           'gender',
           'last_name',
           'last_updated',
           'middle_name',
           'name',
           'name_prefix',
           'name_suffix',
           'organization_name',
           'organizational_subpart',
           'parent_organization_ein',
           'parent_organization_legal_business_name',
           'reactivation_date',
           'sole_proprietor',
           'status']

df_iter=['country_code',
'country_name',
'address_purpose',
'address_type',
'address_1',
'address_2',
'city',
'state',
'postal_code',
'telephone_number',
'fax_number']
df=[['NPI',
'country_code',
'country_name',
'address_purpose',
'address_type',
'address_1',
'address_2',
'city',
'state',
'postal_code',
'telephone_number',
'fax_number',
'Secondary_country_code',
'Secondary_country_name',
'Secondary_address_purpose',
'Secondary_address_type',
'Secondary_address_1',
'Secondary_address_2',
'Secondary_city',
'Secondary_state',
'Secondary_postal_code',
'Secondary_telephone_number',
'Secondary_fax_number',
'authorized_official_credential',
'authorized_official_first_name',
'authorized_official_last_name',
'authorized_official_middle_name',
'authorized_official_name_prefix',
'authorized_official_telephone_number',
'authorized_official_title_or_position',
'certification_date',
'credential',
'deactivation_date',
'enumeration_date',
'first_name',
'gender',
'last_name',
'last_updated',
'middle_name',
'name',
'name_prefix',
'name_suffix',
'organization_name',
'organizational_subpart',
'parent_organization_ein',
'parent_organization_legal_business_name',
'reactivation_date',
'sole_proprietor',
'status',
'primary_taxonomy_code',
'primary_taxonomy_description',
'primary_taxonomy_license',
'primary_taxonomy',
'primary_state',
'Other_taxonomy_Json',
'Other_Identifiers_Json']]

for idx,i in enumerate(npi):
    if idx%15==0:
        time.sleep(5*random.random())
    if idx%1000==0:
        time.sleep(7+5*random.random())
    if idx%20000==0:
        dfd=pd.DataFrame(df[1:],columns=df[0])
        dfd.to_excel(f'npis\\{idx}final_NPI_API.xlsx')
        
    response=requests.get(f'https://npiregistry.cms.hhs.gov/api/?number={i}&version=2.1')
    data=json.loads(response.text)
    if 'Errors' in data.keys():
        df.append([i]+not_found404)
        continue
    if data['result_count']==0:
        df.append([i]+error_npi)
        continue
    dff=[]
    temp_libs=data['results'][0]
    dff.extend([i]+addressed(temp_libs))
    dff.extend(basics(temp_libs))
    dff.extend(tax(temp_libs))
    dff.append(identifiers(temp_libs))
    validate(dff)
    df.append(dff)
    print(idx,i,str(len(df[idx+1])),str(len(df)))
    if len(dff)!=56:
        pprint(temp_libs)
        print('Should be 22: ',str(len(addressed(temp_libs))))
        pprint(addressed(temp_libs))
        print('Should be 26: ',str(len(basics(temp_libs))))
        pprint(basics(temp_libs))
        print('Should be 6: ',str(len(tax(temp_libs))))
        pprint(tax(temp_libs))

dfd=pd.DataFrame(df[1:],columns=df[0])
dfd.to_excel('final_NPI_API.xlsx')
