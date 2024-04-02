def hash_adset(adset_id):
    FLAGS_dsp_ad_abtest_hash_seed = 0x1234

    adset_id = int(adset_id)
    num = adset_id >> 15
    hash_num = num ^ (num >> 3) ^ (num >> 1)
    slot = (hash_num ^ FLAGS_dsp_ad_abtest_hash_seed) % 100
    print("该广告组hash值:", slot)
    return slot
