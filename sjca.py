import requests
import json
import pprint
import os

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import sys,time

os.system('clear')



def not_ready():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print_one_by_one("~ The switch you selected has not enabled restapi yet. Please try again. ~\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print()

def invalid_choice():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print_one_by_one("      ~ Invalid Choice. Please try again. Thank you! ~\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print()

def print_one_by_one(text):
    sys.stdout.write("\r " + " " * 60 + "\r")
    sys.stdout.flush()
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


payload = {}
headers = {
    'Authorization': 'Basic cmVzdGFwaV9yOjEyMzQ1Njc4OTBAQXNkZmdoamtsOw==',
    'Accept': 'application/json',
    'Content-Type': 'application/xml'
}


def switch_sjca_sw1_2(url_get_cfg, url_get_int, sw_name):
    # payload = {}
    # headers = {
    #     'Authorization': 'Basic cmVzdGFwaV9yOjEyMzQ1Njc4OTBAQXNkZmdoamtsOw==',
    #     'Accept': 'application/json',
    #     'Content-Type': 'application/xml'
    # }

    response_get_cfg = requests.request("GET", url_get_cfg, verify=False, headers=headers, data=payload)
    response_get_cfg_dict = response_get_cfg.json()

    response_get_int = requests.request("GET", url_get_int, verify=False, headers=headers, data=payload)
    response_get_int_dict = response_get_int.json()

    #print(type(response))            #<class 'requests.models.Response'>
    #print(type(response_dict))       #<class 'dict'>
    # print(type(response.text))          #<class 'str'>
    # print(type(response.json()))        #<class 'dict'>
    # print(type(response.json))          #<class 'method'>
    # print(type(response.content))       #<class 'bytes'>

    while True:
        interface_choice = input("""\nPlease choose which interface you want to check: \n
          0:    ae0             15:   ae15
          1:    ae1             16:   ae16
          2:    ae2             17:   ae17
          3:    ae3             18:   ae18
          4:    ae4             19:   ae19
          5:    ae5             20:   ae20
          6:    ae6             21:   ae21
          7:    ae7             22:   ae22
          8:    ae8             23:   ae23
          9:    ae9             24:   ae24
          10:   ae10            25:   ae25
          11:   ae11            34:   xe-0/0/34
          12:   ae12            35:   xe-0/0/35
          13:   ae13            36:   xe-0/0/36
          14:   ae14            37:   xe-0/0/37
                    
          Q:    Quit\n       
                Your choice: """)

        if interface_choice == '0':
            interface_name = 'ae0'
        elif interface_choice == '1':
            interface_name = 'ae1'
        elif interface_choice == '2':
            interface_name = 'ae2'
        elif interface_choice == '3':
            interface_name = 'ae3'
        elif interface_choice == '4':
            interface_name = 'ae4'
        elif interface_choice == '5':
            interface_name = 'ae5'
        elif interface_choice == '6':
            interface_name = 'ae6'
        elif interface_choice == '7':
            interface_name = 'ae7'
        elif interface_choice == '8':
            interface_name = 'ae8'
        elif interface_choice == '9':
            interface_name = 'ae9'
        elif interface_choice == '10':
            interface_name = 'ae10'
        elif interface_choice == '11':
            interface_name = 'ae11'
        elif interface_choice == '12':
            interface_name = 'ae12'
        elif interface_choice == '13':
            interface_name = 'ae13'
        elif interface_choice == '14':
            interface_name = 'ae14'
        elif interface_choice == '15':
            interface_name = 'ae15'
        elif interface_choice == '16':
            interface_name = 'ae16'
        elif interface_choice == '17':
            interface_name = 'ae17'
        elif interface_choice == '18':
            interface_name = 'ae18'
        elif interface_choice == '19':
            interface_name = 'ae19'
        elif interface_choice == '20':
            interface_name = 'ae20'
        elif interface_choice == '21':
            interface_name = 'ae21'
        elif interface_choice == '22':
            interface_name = 'ae22'
        elif interface_choice == '23':
            interface_name = 'ae23'
        elif interface_choice == '24':
            interface_name = 'ae24'
        elif interface_choice == '25':
            interface_name = 'ae25'
        elif interface_choice == '34':
            interface_name = 'xe-0/0/34'
        elif interface_choice == '35':
            interface_name = 'xe-0/0/35'
        elif interface_choice == '36':
            interface_name = 'xe-0/0/36'
        elif interface_choice == '37':
            interface_name = 'xe-0/0/37'
        elif interface_choice.lower() == 'q':
            os._exit(0)
        else:
            invalid_choice()
            continue

        int_ids_get_cfg = len(response_get_cfg_dict['configuration']['interfaces'][
                                  'interface'])  # to figure out how many interfaces this switch has, data type is list
        for int_id_get_cfg in range(int_ids_get_cfg):  # if_id is the index of the list
            if (response_get_cfg_dict['configuration']['interfaces']['interface'])[int_id_get_cfg][
                'name'] == interface_name:  # retrieve interface_id(index of the lost) from interface_name
                interface_id_get_cfg = int_id_get_cfg

        int_ids_get_int = len(response_get_int_dict['interface-information'][0]['physical-interface'])
        for int_id_get_int in range(int_ids_get_int):
            if (response_get_int_dict['interface-information'][0]['physical-interface'])[int_id_get_int]['name'][0][
                "data"] == interface_name:
                interface_id_get_int = int_id_get_int

        os.system('clear')

        print("~" * 80)
        int_dsc = response_get_cfg_dict['configuration']['interfaces']['interface'][interface_id_get_cfg]['description']
        int_mtu = \
        response_get_int_dict['interface-information'][0]['physical-interface'][interface_id_get_int]['mtu'][0][
            'data']
        print_one_by_one(
            f"Interface: '{interface_name}' \nDescription: '{int_dsc}' \nMTU: '{int_mtu}'\nOn switch '{sw_name}' has the following VLAN members: \n")
        print_one_by_one("~" * 80)
        print()
        pprint.pprint(
            response_get_cfg_dict['configuration']['interfaces']['interface'][interface_id_get_cfg]['unit'][0][
                'family'][
                'ethernet-switching']['vlan']['members'])
        print("~" * 80)


def switch_sjca_sw3_4(url_get_cfg, url_get_int, sw_name):
    # payload = {}
    # headers = {
    #     'Authorization': 'Basic cmVzdGFwaV9yOjEyMzQ1Njc4OTBAQXNkZmdoamtsOw==',
    #     'Accept': 'application/json',
    #     'Content-Type': 'application/xml'
    # }

    response_get_cfg = requests.request("GET", url_get_cfg, verify=False, headers=headers, data=payload)
    response_get_cfg_dict = response_get_cfg.json()

    response_get_int = requests.request("GET", url_get_int, verify=False, headers=headers, data=payload)
    response_get_int_dict = response_get_int.json()

    while True:
        interface_choice = input("""\nPlease choose which interface you want to check: \n
          0:    ae0             9:   ae9
          1:    ae1             10:   ae10
          2:    ae2             11:   ae11
          3:    ae3             12:   ae12
          4:    ae4             13:   ae13
          5:    ae5             14:   ae14
          6:    ae6             15:   ae15
          7:    ae7             16:   ae16
          8:    ae8             17:   ae17

          Q:    Quit\n       
                Your choice: """)

        if interface_choice == '0':
            interface_name = 'ae0'
        elif interface_choice == '1':
            interface_name = 'ae1'
        elif interface_choice == '2':
            interface_name = 'ae2'
        elif interface_choice == '3':
            interface_name = 'ae3'
        elif interface_choice == '4':
            interface_name = 'ae4'
        elif interface_choice == '5':
            interface_name = 'ae5'
        elif interface_choice == '6':
            interface_name = 'ae6'
        elif interface_choice == '7':
            interface_name = 'ae7'
        elif interface_choice == '8':
            interface_name = 'ae8'
        elif interface_choice == '9':
            interface_name = 'ae9'
        elif interface_choice == '10':
            interface_name = 'ae10'
        elif interface_choice == '11':
            interface_name = 'ae11'
        elif interface_choice == '12':
            interface_name = 'ae12'
        elif interface_choice == '13':
            interface_name = 'ae13'
        elif interface_choice == '14':
            interface_name = 'ae14'
        elif interface_choice == '15':
            interface_name = 'ae15'
        elif interface_choice == '16':
            interface_name = 'ae16'
        elif interface_choice == '17':
            interface_name = 'ae17'
        elif interface_choice.lower() == 'q':
            os._exit(0)
        else:
            invalid_choice()
            continue

        int_ids_get_cfg = len(response_get_cfg_dict['configuration']['interfaces'][
                                  'interface'])  # to figure out how many interfaces this switch has, data type is list
        for int_id_get_cfg in range(int_ids_get_cfg):  # if_id is the index of the list
            if (response_get_cfg_dict['configuration']['interfaces']['interface'])[int_id_get_cfg][
                'name'] == interface_name:  # retrieve interface_id(index of the lost) from interface_name
                interface_id_get_cfg = int_id_get_cfg

        int_ids_get_int = len(response_get_int_dict['interface-information'][0]['physical-interface'])
        for int_id_get_int in range(int_ids_get_int):
            if (response_get_int_dict['interface-information'][0]['physical-interface'])[int_id_get_int]['name'][0][
                "data"] == interface_name:
                interface_id_get_int = int_id_get_int

        os.system('clear')

        print("~" * 80)
        int_dsc = response_get_cfg_dict['configuration']['interfaces']['interface'][interface_id_get_cfg]['description']
        int_mtu = \
            response_get_int_dict['interface-information'][0]['physical-interface'][interface_id_get_int]['mtu'][0][
                'data']
        print_one_by_one(
            f"Interface: '{interface_name}' \nDescription: '{int_dsc}' \nMTU: '{int_mtu}'\nOn switch '{sw_name}' has the following VLAN members: \n")
        print_one_by_one("~" * 80)
        print()
        pprint.pprint(
            response_get_cfg_dict['configuration']['interfaces']['interface'][interface_id_get_cfg]['unit'][0][
                'family'][
                'ethernet-switching']['vlan']['members'])
        print("~" * 80)

def switch_sjca_sw5_6(url_get_cfg, url_get_int, sw_name):
    # payload = {}
    # headers = {
    #     'Authorization': 'Basic cmVzdGFwaV9yOjEyMzQ1Njc4OTBAQXNkZmdoamtsOw==',
    #     'Accept': 'application/json',
    #     'Content-Type': 'application/xml'
    # }

    response_get_cfg = requests.request("GET", url_get_cfg, verify=False, headers=headers, data=payload)
    response_get_cfg_dict = response_get_cfg.json()

    response_get_int = requests.request("GET", url_get_int, verify=False, headers=headers, data=payload)
    response_get_int_dict = response_get_int.json()

    while True:
        interface_choice = input("""\nPlease choose which interface you want to check: \n
          0:    xe-0/0/0            
          1:    xe-0/0/1           

          Q:    Quit\n       
                Your choice: """)

        if interface_choice == '0':
            interface_name = 'xe-0/0/0'
        elif interface_choice == '1':
            interface_name = 'xe-0/0/1'
        elif interface_choice.lower() == 'q':
            os._exit(0)
        else:
            invalid_choice()
            continue

        int_ids_get_cfg = len(response_get_cfg_dict['configuration']['interfaces'][
                                  'interface'])  # to figure out how many interfaces this switch has, data type is list
        for int_id_get_cfg in range(int_ids_get_cfg):  # if_id is the index of the list
            if (response_get_cfg_dict['configuration']['interfaces']['interface'])[int_id_get_cfg][
                'name'] == interface_name:  # retrieve interface_id(index of the lost) from interface_name
                interface_id_get_cfg = int_id_get_cfg

        int_ids_get_int = len(response_get_int_dict['interface-information'][0]['physical-interface'])
        for int_id_get_int in range(int_ids_get_int):
            if (response_get_int_dict['interface-information'][0]['physical-interface'])[int_id_get_int]['name'][0][
                "data"] == interface_name:
                interface_id_get_int = int_id_get_int

        os.system('clear')

        print("~" * 80)
        int_dsc = response_get_cfg_dict['configuration']['interfaces']['interface'][interface_id_get_cfg]['description']
        int_mtu = \
            response_get_int_dict['interface-information'][0]['physical-interface'][interface_id_get_int]['mtu'][0][
                'data']
        print_one_by_one(
            f"Interface: '{interface_name}' \nDescription: '{int_dsc}' \nMTU: '{int_mtu}'\nOn switch '{sw_name}' has the following VLAN members: \n")
        print_one_by_one("~" * 80)
        print()
        pprint.pprint(
            response_get_cfg_dict['configuration']['interfaces']['interface'][interface_id_get_cfg]['unit'][0][
                'family'][
                'ethernet-switching']['vlan']['members'])
        print("~" * 80)

def switch_sjca_sw7_8(url_get_cfg, url_get_int, sw_name):
    # payload = {}
    # headers = {
    #     'Authorization': 'Basic cmVzdGFwaV9yOjEyMzQ1Njc4OTBAQXNkZmdoamtsOw==',
    #     'Accept': 'application/json',
    #     'Content-Type': 'application/xml'
    # }

    response_get_cfg = requests.request("GET", url_get_cfg, verify=False, headers=headers, data=payload)
    response_get_cfg_dict = response_get_cfg.json()

    response_get_int = requests.request("GET", url_get_int, verify=False, headers=headers, data=payload)
    response_get_int_dict = response_get_int.json()

    while True:
        interface_choice = input("""\nPlease choose which interface you want to check: \n
          1:    ae1             
          2:    ae2             

          Q:    Quit\n       
                Your choice: """)

        if interface_choice == '1':
            interface_name = 'ae1'
        elif interface_choice == '2':
            interface_name = 'ae2'
        elif interface_choice.lower() == 'q':
            os._exit(0)
        else:
            invalid_choice()
            continue

        int_ids_get_cfg = len(response_get_cfg_dict['configuration']['interfaces'][
                                  'interface'])  # to figure out how many interfaces this switch has, data type is list
        for int_id_get_cfg in range(int_ids_get_cfg):  # if_id is the index of the list
            if (response_get_cfg_dict['configuration']['interfaces']['interface'])[int_id_get_cfg][
                'name'] == interface_name:  # retrieve interface_id(index of the lost) from interface_name
                interface_id_get_cfg = int_id_get_cfg

        int_ids_get_int = len(response_get_int_dict['interface-information'][0]['physical-interface'])
        for int_id_get_int in range(int_ids_get_int):
            if (response_get_int_dict['interface-information'][0]['physical-interface'])[int_id_get_int]['name'][0][
                "data"] == interface_name:
                interface_id_get_int = int_id_get_int

        os.system('clear')

        print("~" * 80)
        int_dsc = response_get_cfg_dict['configuration']['interfaces']['interface'][interface_id_get_cfg]['description']
        int_mtu = \
            response_get_int_dict['interface-information'][0]['physical-interface'][interface_id_get_int]['mtu'][0][
                'data']
        print_one_by_one(
            f"Interface: '{interface_name}' \nDescription: '{int_dsc}' \nMTU: '{int_mtu}'\nOn switch '{sw_name}' has the following VLAN members: \n")
        print_one_by_one("~" * 80)
        print()
        pprint.pprint(
            response_get_cfg_dict['configuration']['interfaces']['interface'][interface_id_get_cfg]['unit'][0][
                'family'][
                'ethernet-switching']['vlan']['members'])
        print("~" * 80)

def sjca():
    while True:
        sw_choice = input ("""\nPlease choose which switch you want to check: \n
              1:  leaf-access01.corp.sjca
              2:  leaf-access02.corp.sjca
              3:  leaf-access03.corp.sjca
              4:  leaf-access04.corp.sjca
              5:  leaf-access05.corp.sjca
              6:  leaf-access06.corp.sjca:
              7:  leaf-access07.corp.sjca
              8:  leaf-access08.corp.sjca\n       
          Your choice: """)
        if sw_choice == '1':
          url_get_cfg = "http://172.19.195.27:3000/rpc/get-configuration"
          url_get_int = "http://172.19.195.27:3000/rpc/get-interface-information"
          sw_name = 'leaf-access01.corp.sjca'
          switch_sjca_sw1_2(url_get_cfg, url_get_int, sw_name)

        elif sw_choice == '2':
          url_get_cfg = "http://172.19.195.28:3000/rpc/get-configuration"
          url_get_int = "http://172.19.195.28:3000/rpc/get-interface-information"
          sw_name = 'leaf-access02.corp.sjca'
          switch_sjca_sw1_2(url_get_cfg, url_get_int, sw_name)

        elif sw_choice == '3':
          url_get_cfg = "http://172.19.195.48:3000/rpc/get-configuration"
          url_get_int = "http://172.19.195.48:3000/rpc/get-interface-information"
          sw_name = 'leaf-access03.corp.sjca'
          switch_sjca_sw3_4(url_get_cfg, url_get_int, sw_name)

        elif sw_choice == '4':
          url_get_cfg = "http://172.19.195.49:3000/rpc/get-configuration"
          url_get_int = "http://172.19.195.49:3000/rpc/get-interface-information"
          sw_name = 'leaf-access04.corp.sjca'
          switch_sjca_sw3_4(url_get_cfg, url_get_int, sw_name)

        elif sw_choice == '5':
          url_get_cfg = "http://172.19.195.52:3000/rpc/get-configuration"
          url_get_int = "http://172.19.195.52:3000/rpc/get-interface-information"
          sw_name = 'leaf-access05.corp.sjca'
          switch_sjca_sw5_6(url_get_cfg, url_get_int, sw_name)

        elif sw_choice == '6':
          url_get_cfg = "http://172.19.195.53:3000/rpc/get-configuration"
          url_get_int = "http://172.19.195.53:3000/rpc/get-interface-information"
          sw_name = 'leaf-access06.corp.sjca'
          switch_sjca_sw5_6(url_get_cfg, url_get_int, sw_name)

        elif sw_choice == '7':
          url_get_cfg = "http://172.19.195.58:3000/rpc/get-configuration"
          url_get_int = "http://172.19.195.58:3000/rpc/get-interface-information"
          sw_name = 'leaf-access07.corp.sjca'
          switch_sjca_sw7_8(url_get_cfg, url_get_int, sw_name)

        elif sw_choice == '8':
          url_get_cfg = "http://172.19.195.59:3000/rpc/get-configuration"
          url_get_int = "http://172.19.195.59:3000/rpc/get-interface-information"
          sw_name = 'leaf-access08.corp.sjca'
          switch_sjca_sw7_8(url_get_cfg, url_get_int, sw_name)

        # elif sw_choice == '5' or sw_choice == '6':
        #     not_ready()

        else:
          invalid_choice()