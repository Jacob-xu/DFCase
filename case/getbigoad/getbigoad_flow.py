import requests
import time
import random
from . import getconf_flow

requests.packages.urllib3.disable_warnings()


def GetBigoAdUserChoose(choose_slot, choose_country, choose_type, gaid, impl, click, attr, mappedIae):
    headers = getconf_flow.get_headers()
    body, body_attr = getconf_flow.get_body()

    placement_id, slot, strategy_id, pkg_name = getconf_flow.get_slot(choose_slot)
    types = getconf_flow.get_type(choose_type)
    country = getconf_flow.get_country(choose_country)
    net = getconf_flow.get_net(choose_country)

    body['ori']['placement_id'] = placement_id
    body['ori']['slot'] = slot
    body['ori']['pkg_name'] = pkg_name
    body['ori']['country'] = country
    body['ori']['gaid'] = gaid
    body['ori']['net'] = net
    body['types'] = types

    url = "http://builtin-proxy.basic.bigo.inner/flags?addr=202.168.108.109:20098/BigoAdService/GetBigoAd"
    payload = body

    try:
        response = requests.request("POST", url, headers=headers, json=payload)
        result = response.json()
    except:
        print('=' * 10)
        print('Gateway服务有误')

    if result["msg"] == 'success':
        AnalyResult(result, gaid, impl, click, attr, mappedIae)
    else:
        result = "无广告"
        print(result)
    return result


def AnalyResult(result, gaid, impl, click, attr, mappedIae):
    source_json = {
        'ad_id': '',
        'adset_id': '',
        'series_id': '',
        'account_id': '',
        'land_url': '',
        'tgt_pkg_name': '',
        'sid': '',
        'logid': '',
        'bigo_tracker_impl': '',
        'bigo_tracker_click': '',
        'other_tracker_impl': '',
        'other_tracker_click': '',
        'vast': '',
        'banner': '',
        'impl': '',
        'click': '',
        'attr': ''
    }
    try:
        ad_id = result['data']['ad_id']
        adset_id = result['data']['adset_id']
        series_id = result['data']['series_id']
        account_id = result['data']['account_id']
        land_url = result['data']['land_url']
        tgt_pkg_name = result['data']['tgt_pkg_name']
        sid = result['data']['sid']
        logid = result['logid']
        getadsource = True
        print('=' * 10)
        print("sid:", sid)
        print("ad_id:", ad_id)
        print("adset_id:", adset_id)
        print("series_id:", series_id)
        print("account_id:", account_id)
        print("land_url:", land_url)
        print("tgt_pkg_name:", tgt_pkg_name)
        print("logid:", logid)
    except:
        getadsource = False
        print('=' * 10)
        print("AnalyResult Error")

    # 广告类型判断
    try:
        adx_type = result['data']['adx_type']
        if adx_type == 'ADX_NATIVE':
            # print(adx_type)
            pass
        elif adx_type == 'ADX_VIDEO':
            # print(adx_type)
            vast = result['data']['video']['data']
            print('=' * 10)
            print("vast:", vast)
        elif adx_type == 'ADX_BANNER':
            # print(adx_type)
            banner = result['data']['display']['data']
            print('=' * 10)
            print("banner:", banner)
    except:
        print('=' * 10)
        print("GetAdxType Error")

    try:
        # 获取曝光追踪链
        track_impls_third_list = result['data']['track_impls_third']
        other_tracker_impl = []
        for i in (0, len(track_impls_third_list) - 1):
            if track_impls_third_list[i]['name'] == 'bigo_tracker_impl':
                bigo_tracker_impl = track_impls_third_list[i]['value']
            else:
                other_tracker_impl.append(track_impls_third_list[i]['value'])

        print('=' * 10)
        print("展示追踪链:", bigo_tracker_impl)

        # 获取点击追踪链
        track_clicks_third_list = result['data']['track_clicks_third']
        other_tracker_click = []
        for i in (0, len(track_clicks_third_list) - 1):
            if track_clicks_third_list[i]['name'] == 'bigo_tracker':
                bigo_tracker_click = track_clicks_third_list[i]['value']
            else:
                other_tracker_click.append(track_clicks_third_list[i]['value'])

        print('=' * 10)
        print("点击追踪链:", bigo_tracker_click)

    except:
        print('=' * 10)
        print("GetTacker Error")

    if getadsource:
        source_json['gaid'] = gaid
        source_json['ad_id'] = ad_id
        source_json['adset_id'] = adset_id
        source_json['series_id'] = series_id
        source_json['account_id'] = account_id
        source_json['land_url'] = land_url
        source_json['tgt_pkg_name'] = tgt_pkg_name
        source_json['sid'] = sid
        source_json['logid'] = logid
        source_json['bigo_tracker_impl'] = bigo_tracker_impl
        source_json['bigo_tracker_click'] = bigo_tracker_click
        source_json['other_tracker_impl'] = other_tracker_impl
        source_json['other_tracker_click'] = other_tracker_click
        source_json['impl'] = impl
        source_json['click'] = click
        source_json['attr'] = attr
        source_json['mappedIae'] = mappedIae
        try:
            source_json['vast'] = vast
        except:
            pass
        try:
            source_json['banner'] = banner
        except:
            pass

        if impl or click == 'True':
            SendTracker(source_json)
        if attr == True:
            Attribution(source_json, mappedIae)

    return source_json


def Attribution(source_json, mappedIae):
    t = time.time()
    now_time = int(t)

    headers = getconf_flow.get_headers()
    body, body_attr = getconf_flow.get_body()

    body_attr['adId'] = source_json['account_id']
    body_attr['adsetId'] = source_json['adset_id']
    body_attr['appId'] = source_json['tgt_pkg_name']
    body_attr['appName'] = source_json['tgt_pkg_name']
    body_attr['campaignId'] = source_json['series_id']
    body_attr['clickTs'] = now_time
    body_attr['gaid'] = source_json['gaid']
    body_attr['gpReferrerInstallTs'] = now_time + 1
    body_attr['mappedIae'] = mappedIae
    body_attr['requestTimestamp'] = now_time + 2
    body_attr['sid'] = source_json['sid']

    url = 'http://202.168.108.109:8013/attribution/apply'
    payload = body_attr
    time.sleep(3)
    response = requests.request("POST", url, headers=headers, json=payload)
    if response.json()["msg"] == "success":
        print('=' * 10)
        print("归因成功")
    else:
        print('=' * 10)
        print("归因失败")


def SendTracker(source_json):
    impl = source_json['impl']
    click = source_json['click']
    bigo_tracker_impl = source_json['bigo_tracker_impl']
    bigo_tracker_click = source_json['bigo_tracker_click']

    if impl:
        impl_delay = random.randint(1, 5)
        time.sleep(impl_delay)
        print("展示延迟:", impl_delay)
        response_impls = requests.request("GET", bigo_tracker_impl, verify=False)
        print('=' * 10)
        print("展示追踪链请求结果:", response_impls.json())
    if click:
        click_delay = random.randint(1, 5)
        time.sleep(click_delay)
        print("点击延迟:", click_delay)
        response_click = requests.request("GET", bigo_tracker_click, verify=False)
        print('=' * 10)
        print("点击追踪链请求结果:", response_click.json())

# if __name__ == '__main__':
#     username = sys.argv[1]
#     choose_slot = sys.argv[2]
#     choose_country = sys.argv[3]
#     choose_type = sys.argv[4]
#     try:
#         gaid = sys.argv[5]
#     except:
#         gaid = 'test_gaid'
#     try:
#         impl = sys.argv[6]
#     except:
#         impl = True
#     try:
#         click = sys.argv[7]
#     except:
#         click = True
#     try:
#         attr = sys.argv[8]
#     except:
#         attr = False
#     try:
#         mappedIae = sys.argv[9]
#     except:
#         mappedIae = 'app_install'
#
#     UserChoose(username, choose_slot, choose_country, choose_type, gaid, impl, click, attr, mappedIae)
#     # UserChoose('yuanxu', 'base_slot', 4, 'native_img', 'test12311', True, True, False, 'app_install')
#     GetBigoAd(username)
#     # GetBigoAd('yuanxu')
