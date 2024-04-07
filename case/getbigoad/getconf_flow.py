import yaml
import time
import sys
import os

sys.path.append(os.getcwd())

yaml_file = os.path.dirname(os.path.abspath(__file__)) + '/conf'
file = open(yaml_file, 'r', encoding="utf-8")
file_data = yaml.load(file.read(), Loader=yaml.FullLoader)


def get_headers():
    headers = file_data.get('config_base').get('headers')
    return headers


def get_body():
    body = file_data.get('config_base').get('body')
    body_attr = file_data.get('config_base').get('body_attr')
    return body, body_attr


def get_country(choose):
    country = file_data.get('config_' + choose).get('country')
    return country


def get_net(choose):
    net = file_data.get('config_' + choose).get('net')
    return net


def get_slot(choose):
    placement_id = file_data.get('config_' + choose).get('placement_id')
    slot = file_data.get('config_' + choose).get('slot')
    strategy_id = file_data.get('config_' + choose).get('strategy_id')
    pkg_name = file_data.get('config_' + choose).get('pkg_name')
    return placement_id, slot, strategy_id, pkg_name


def get_time():
    t = time.time()
    # 请求时间
    now_time = int(t)
    # 展示时间延后1分钟
    impls_ms_time = int(round(t * 1000)) + 60000
    # 点击事件延后2分钟
    clk_ms_time = int(round(t * 1000)) + 120000
    return now_time, impls_ms_time, clk_ms_time


def get_type(choose):
    if choose == 'native_img':
        types = [{'adx_type': 1, 'ad_type': 1, 'floor_price': 1}]
    elif choose == 'native_video':
        types = [{'adx_type': 2, 'ad_type': 1, 'floor_price': 1}]
    elif choose == 'banner':
        types = [{'adx_type': 3, 'ad_type': 2, 'floor_price': 1}]
    else:
        types = [{'adx_type': 1, 'ad_type': 1, 'floor_price': 1}, {'adx_type': 2, 'ad_type': 1, 'floor_price': 1}]
    return types


if __name__ == '__main__':
    get_headers()
