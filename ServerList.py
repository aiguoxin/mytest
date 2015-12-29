__author__ = 'chengmingwang'


# define resource const
RESOURCE_10_221 = "10.221"
RESOURCE_10_121 = "10.121"
RESOURCE_10_153 = "10.153"
RESOURCE_10_11 = "10.11"
RESOURCE_10_10 = "10.10"
RESOURCE_TEST_DEV = "test-dev"
RESOURCE_PURE_TEST = "pure-test"
RESOURCE_TEST_DEPLOY = 'test-deploy'
RESOURCE_DATA = {
    RESOURCE_10_221: [
        ('../src/main/resources/shanghai_config.properties', '/data/video/config.properties'),
        ('../src/main/resources/log4j.xml', '/usr/local/jetty/resources/log4j.xml'),
        ('../src/main/resources/jvm.option', '/data/video/jvm.option'),
        ('../src/main/resources/ipdata.dat', '/data/video/ipdata.dat'),
        ('../src/main/resources/kernel_service_code_dict.json', '/data/video/kernel_service_code_dict.json'),
        ('../src/main/resources/kernel_service_code_dict_tw.json', '/data/video/kernel_service_code_dict_tw.json'),
        # ('../src/main/resources/security_code.json','/data/video/security_code.json')
    ],
    RESOURCE_10_121: [
        ('../src/main/resources/shanghai_config.properties', '/data/video/config.properties'),
        ('../src/main/resources/log4j.xml', '/usr/local/jetty/resources/log4j.xml'),
        ('../src/main/resources/jvm.option', '/data/video/jvm.option'),
        ('../src/main/resources/ipdata.dat', '/data/video/ipdata.dat'),
        ('../src/main/resources/kernel_service_code_dict.json', '/data/video/kernel_service_code_dict.json'),
        ('../src/main/resources/kernel_service_code_dict_tw.json', '/data/video/kernel_service_code_dict_tw.json'),
        # ('../src/main/resources/security_code.json','/data/video/security_code.json')
    ],
    RESOURCE_10_153: [
        ('../src/main/resources/jiyang_config.properties', '/data/video/config.properties'),
        ('../src/main/resources/log4j.xml', '/usr/local/jetty/resources/log4j.xml'),
        ('../src/main/resources/jvm.option', '/data/video/jvm.option'),
        ('../src/main/resources/ipdata.dat', '/data/video/ipdata.dat'),
        ('../src/main/resources/kernel_service_code_dict.json', '/data/video/kernel_service_code_dict.json'),
        ('../src/main/resources/security_code.json', '/data/video/security_code.json'),
        # ('../src/main/resources/kernel_service_code_dict_tw.json','/data/video/kernel_service_code_dict_tw.json'),
    ],
    RESOURCE_10_11: [
        ('../src/main/resources/beijing_liantong_config.properties', '/data/video/config.properties'),
        ('../src/main/resources/log4j.xml', '/usr/local/jetty/resources/log4j.xml'),
        ('../src/main/resources/jvm.option', '/data/video/jvm.option'),
        ('../src/main/resources/ipdata.dat', '/data/video/ipdata.dat'),
        ('../src/main/resources/kernel_service_code_dict.json', '/data/video/kernel_service_code_dict.json'),
        ('../src/main/resources/kernel_service_code_dict_tw.json', '/data/video/kernel_service_code_dict_tw.json'),
        # ('../src/main/resources/security_code.json','/data/video/security_code.json')
    ],
    RESOURCE_10_10: [
        ('../src/main/resources/beijing_dianxin_config.properties', '/data/video/config.properties'),
        ('../src/main/resources/log4j.xml', '/usr/local/jetty/resources/log4j.xml'),
        ('../src/main/resources/jvm.option', '/data/video/jvm.option'),
        ('../src/main/resources/ipdata.dat', '/data/video/ipdata.dat'),
        ('../src/main/resources/kernel_service_code_dict.json', '/data/video/kernel_service_code_dict.json'),
        ('../src/main/resources/kernel_service_code_dict_tw.json', '/data/video/kernel_service_code_dict_tw.json'),
        # ('../src/main/resources/security_code.json','/data/video/security_code.json')
    ],
    RESOURCE_TEST_DEV: [
        ('../src/main/resources/test_dev_config.properties', '/data/video/config.properties'),
        ('../src/main/resources/log4j.xml', '/usr/local/jetty/resources/log4j.xml'),
        ('../src/main/resources/jvm.option', '/data/video/jvm.option'),
        ('../src/main/resources/ipdata.dat', '/data/video/ipdata.dat'),
        ('../src/main/resources/kernel_service_code_dict_tw.json', '/data/video/kernel_service_code_dict_tw.json'),
        ('../src/main/resources/kernel_service_code_dict.json', '/data/video/kernel_service_code_dict.json'),
        # ('../src/main/resources/security_code.json','/data/video/security_code.json')
    ],
    RESOURCE_TEST_DEPLOY: [
        ('../src/main/resources/beijing_dianxin_config.properties', '/data/video/config.properties'),
        ('../src/main/resources/log4j.xml', '/usr/local/jetty/resources/log4j.xml'),
        ('../src/main/resources/jvm.option', '/data/video/jvm.option'),
        ('../src/main/resources/ipdata.dat', '/data/video/ipdata.dat'),
        ('../src/main/resources/kernel_service_code_dict_tw.json', '/data/video/kernel_service_code_dict_tw.json'),
        ('../src/main/resources/kernel_service_code_dict.json', '/data/video/kernel_service_code_dict.json'),
        # ('../src/main/resources/security_code.json','/data/video/security_code.json')
    ],
    RESOURCE_PURE_TEST: [
        ('../src/main/resources/pure_test.properties', '/data/video/config.properties'),
        ('../src/main/resources/log4j.xml', '/usr/local/jetty/resources/log4j.xml'),
        ('../src/main/resources/jvm.option', '/data/video/jvm.option'),
        ('../src/main/resources/ipdata.dat', '/data/video/ipdata.dat'),
        ('../src/main/resources/kernel_service_code_dict.json', '/data/video/kernel_service_code_dict.json'),
        ('../src/main/resources/kernel_service_code_dict_tw.json', '/data/video/kernel_service_code_dict_tw.json'),
        # ('../src/main/resources/security_code.json','/data/video/security_code.json')
    ]
    # 'dev-prod':[
    # ('../src/main/resources/dev_prod_config.properties','/data/video/config.properties'),
    # ('../src/main/resources/log4j.xml','/usr/local/jetty/resources/log4j.xml'),
    # ('../src/main/resources/jvm.option','/data/video/jvm.option')
    # ]
}


machine_list = {
    "beijing":[
        "10.10.12.24",
        "10.10.12.25",
        "10.10.12.15",
        "10.10.12.16",
        "10.10.13.61",
        "10.10.13.62",
        "10.10.13.63",
        "10.10.13.64",
        "10.10.13.185",
        "10.10.13.186",
        "10.10.13.187",
        "10.10.13.188",
        "10.10.13.189",
        "10.10.13.190",
        "10.10.13.191",
        "10.10.13.192",
        "10.10.13.193",
        "10.10.13.194",
        "10.11.78.4",
        "10.11.78.5",
        "10.11.78.6",
        "10.11.78.7",
        "10.11.78.8",
        "10.11.78.9",
        "10.11.78.10",
        "10.11.78.11",
        "10.11.78.12",
        "10.11.78.13"
    ],
    "shanghai":[
        "10.221.74.83",
        "10.221.74.84",
        "10.221.74.85",
        "10.221.74.86",
        "10.121.50.90",
        "10.121.50.91",
        "10.121.50.92",
        "10.121.50.94",
        "10.121.50.95",
        "10.121.50.110",
        "10.121.50.126",
        "10.121.50.134",
        "10.221.75.40",
        "10.221.75.41",
        "10.221.75.42",
        "10.221.75.43",
        "10.221.75.44",
        "10.221.75.45",
        "10.221.75.46",
        "10.221.75.47",
        "10.221.75.48",
        "10.221.75.49",
        "10.221.75.39",
        "10.221.74.62",
        "10.221.74.63",
        "10.221.74.64",
        "10.221.74.65",
        "10.221.74.164",
        "10.221.74.165",
        "10.221.74.166",
        "10.221.74.167",
        "10.221.74.168",
        "10.221.74.169",
        "10.221.74.170",
        "10.221.74.200",
        "10.221.74.202",
        "10.221.74.207",
        "10.221.74.208",
        "10.221.74.209",
        "10.221.74.210",
        "10.221.74.211",
        "10.221.74.212",
        "10.221.74.213",
        "10.121.85.31",
        "10.121.85.32",
        "10.121.85.33",
        "10.121.85.34",
        "10.121.85.35",
        "10.121.85.36",
        "10.121.85.37",
        "10.121.85.38",
        "10.121.85.39",
        "10.121.85.40",
        "10.121.85.41",
        "10.121.85.42",
        "10.121.85.43",
        "10.121.85.44",
        "10.121.85.45",
        "10.121.85.51",
        "10.121.85.53",
        "10.121.85.54",
        "10.121.85.100",
        "10.121.85.55",
        "10.221.75.52",
        "10.221.75.53",
        "10.221.75.54",
        "10.221.75.55",
        "10.221.75.56",
    ],
    "jiyang":[
        "10.153.107.217",
        "10.153.107.237",
        "10.153.107.130",
        "10.153.107.131",
        "10.153.110.89",
        "10.153.110.90",
        "10.153.110.91",
        "10.153.110.92",
        "10.153.110.93",
        "10.153.110.94",
        "10.153.74.149",
        "10.153.74.151",
        "10.153.74.157",
        "10.153.110.133",
        "10.153.110.134",
        "10.153.110.135",
        "10.153.110.136",
        "10.153.110.137",
        "10.153.110.138",
        "10.153.110.139",
        # "10.153.74.224"    for zabbix
        "10.153.108.44",
        "10.153.108.45",
        "10.153.108.46",
        "10.153.108.47",
        "10.153.108.48",
        "10.153.108.49",
        "10.153.108.50",
        "10.153.108.51",
        "10.153.108.52",
        "10.153.108.53",
        "10.153.108.54",
        "10.153.108.55",
        "10.153.108.56",
        "10.153.108.57",
        "10.153.108.58",
        "10.153.108.59",
        "10.153.108.87",
        "10.153.108.88",
        "10.153.108.104",
        "10.153.108.105",
        "10.153.108.106",
        "10.153.108.107",
        "10.153.108.108",
        "10.153.108.118",
        "10.153.108.119",
        "10.153.108.120",
        "10.153.108.121",
        "10.153.108.122",
        "10.153.108.123",
        "10.153.108.124",
        "10.153.108.125",
        "10.153.108.126",
        "10.153.108.127",
        "10.153.108.128",
        "10.153.108.184",
        "10.153.108.185",
        "10.153.108.186",
        "10.153.108.187",
        "10.153.108.188",
        "10.153.108.189",
        "10.153.110.146",
        "10.153.110.147",
        "10.153.110.148",
        "10.153.110.149",
        "10.153.110.150",
    ],
    #"dev-prod":[
    #    "10.121.76.195"
    #],
    #"dev-test":[
    #    "10.121.85.15"
    #]
    "test-dev":[
        "10.10.189.160"
    ],
    "test-deploy":[
        "10.153.122.140",
        "10.153.122.139",
    ],
    "pure-test":[
        "10.15.211.193"
    ]
}

def host_resource_group(area, host):
    if area in RESOURCE_DATA:
        return area
    else:
        ip_items = host.split(".")
        ip_area_key = '.'.join(ip_items[:2])
        return ip_area_key