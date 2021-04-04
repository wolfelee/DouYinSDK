#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @author     :   xstatus
    @time       :   2021/4/4 15:52
    @email      :   xstatus@126.com
    @wechat     :   gameids
    @project    :   DouYinSDK -> demo样例.py
    @IDE        :   PyCharm
    @describe   :   测试样例
"""

if __name__ == '__main__':

    #导入sdk
    from douyin import AwemeSDK

    #添加微信gameids获取token和host
    HOST    = '主机地址'
    TOKEN   = '你的密钥'

    #初始化sdk实例,传入token和host
    sdk = AwemeSDK(token=TOKEN,host=HOST)

    #样例：查询用户信息
    user_info = sdk.get_user_info(uid='104255897823')

    #返回数据样例：
    '''
{
    "app": "douyin",
    "code": 200,
    "data": {
        "extra": {
            "fatal_item_ids": [],
            "logid": "202104041556240102040491065FA54EBF",
            "now": 1617522984000
        },
        "log_pb": {
            "impr_id": "202104041556240102040491065FA54EBF"
        },
        "status_code": 0,
        "user": {
            "apple_account": 0,
            "avatar_168x168": {
                "height": 720,
                "uri": "30ed2000aad26be101cad",
                "url_list": [
                    "https://p26.douyinpic.com/30ed2000aad26be101cad~tplv-dy-shrink:188:188.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=true&sh=188_188&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p6.douyinpic.com/img/30ed2000aad26be101cad~c5_168x168.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p9.douyinpic.com/img/30ed2000aad26be101cad~c5_168x168.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p11.douyinpic.com/img/30ed2000aad26be101cad~c5_168x168.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p6.douyinpic.com/img/30ed2000aad26be101cad~c5_168x168.jpeg?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF"
                ],
                "width": 720
            },
            "avatar_300x300": {
                "height": 720,
                "uri": "30ed2000aad26be101cad",
                "url_list": [
                    "https://p3.douyinpic.com/30ed2000aad26be101cad~tplv-dy-shrink:188:188.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=true&sh=188_188&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p3.douyinpic.com/img/30ed2000aad26be101cad~c5_300x300.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p9.douyinpic.com/img/30ed2000aad26be101cad~c5_300x300.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p6.douyinpic.com/img/30ed2000aad26be101cad~c5_300x300.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p3.douyinpic.com/img/30ed2000aad26be101cad~c5_300x300.jpeg?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF"
                ],
                "width": 720
            },
            "avatar_larger": {
                "height": 720,
                "uri": "30ed2000aad26be101cad",
                "url_list": [
                    "https://p29.douyinpic.com/aweme/1080x1080/30ed2000aad26be101cad.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p9.douyinpic.com/aweme/1080x1080/30ed2000aad26be101cad.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p3.douyinpic.com/aweme/1080x1080/30ed2000aad26be101cad.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p29.douyinpic.com/aweme/1080x1080/30ed2000aad26be101cad.jpeg?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF"
                ],
                "width": 720
            },
            "avatar_medium": {
                "height": 720,
                "uri": "30ed2000aad26be101cad",
                "url_list": [
                    "https://p3.douyinpic.com/30ed2000aad26be101cad~tplv-dy-shrink:188:188.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=true&sh=188_188&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p9.douyinpic.com/aweme/720x720/30ed2000aad26be101cad.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p6.douyinpic.com/aweme/720x720/30ed2000aad26be101cad.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p29.douyinpic.com/aweme/720x720/30ed2000aad26be101cad.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p9.douyinpic.com/aweme/720x720/30ed2000aad26be101cad.jpeg?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF"
                ],
                "width": 720
            },
            "avatar_thumb": {
                "height": 720,
                "uri": "30ed2000aad26be101cad",
                "url_list": [
                    "https://p6.douyinpic.com/30ed2000aad26be101cad~tplv-dy-shrink:188:188.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=true&sh=188_188&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p29.douyinpic.com/aweme/100x100/30ed2000aad26be101cad.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p26.douyinpic.com/aweme/100x100/30ed2000aad26be101cad.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p11.douyinpic.com/aweme/100x100/30ed2000aad26be101cad.webp?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF",
                    "https://p29.douyinpic.com/aweme/100x100/30ed2000aad26be101cad.jpeg?from=2956013662&s=PackSourceEnum_USER_PROFILE&se=false&sh=&sc=avatar&l=202104041556240102040491065FA54EBF"
                ],
                "width": 720
            },
            "aweme_count": 2766,
            "birthday": "",
            "birthday_hide_level": 0,
            "can_show_group_card": 1,
            "city": "武汉",
            "commerce_info": {
                "challenge_list": null,
                "head_image_list": null,
                "offline_info_list": [],
                "smart_phone_list": null,
                "task_list": null
            },
            "commerce_user_info": {
                "ad_revenue_rits": null,
                "has_ads_entry": false
            },
            "commerce_user_level": 0,
            "country": "中国",
            "cover_colour": "#03B837A2",
            "cover_url": [
                {
                    "uri": "31ad1000254caa51a0258",
                    "url_list": [
                        "https://p26.douyinpic.com/31ad1000254caa51a0258~tplv-dy-shrink:750:422.jpeg?from=2480802190&s=profile&se=true&sh=750_422&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p5-ipv6.douyinpic.com/obj/31ad1000254caa51a0258?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p29.douyinpic.com/obj/31ad1000254caa51a0258?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p26.douyinpic.com/obj/31ad1000254caa51a0258?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF"
                    ]
                },
                {
                    "uri": "c8510002be9a3a61aad2",
                    "url_list": [
                        "https://p3.douyinpic.com/c8510002be9a3a61aad2~tplv-dy-shrink:750:422.jpeg?from=2480802190&s=profile&se=true&sh=750_422&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p5-ipv6.douyinpic.com/obj/c8510002be9a3a61aad2?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p11.douyinpic.com/obj/c8510002be9a3a61aad2?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p9.douyinpic.com/obj/c8510002be9a3a61aad2?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF"
                    ]
                }
            ],
            "custom_verify": "",
            "district": "洪山",
            "dongtai_count": 2766,
            "enable_wish": false,
            "enterprise_user_info": "{\"commerce_info\":{\"offline_info_list\":[],\"challenge_list\":null,\"task_list\":null,\"head_image_list\":null,\"smart_phone_list\":null},\"homepage_bottom_toast\":null,\"permissions\":[{\"Id\":3,\"Key\":\"ItemShop\",\"Name\":\"视频电商\",\"AppId\":1128,\"Status\":1,\"Extra\":null,\"Customization\":null,\"Parent\":0,\"Actions\":null},{\"Id\":4,\"Key\":\"LiveShop\",\"Name\":\"直播电商\",\"AppId\":1128,\"Status\":1,\"Extra\":null,\"Customization\":null,\"Parent\":0,\"Actions\":null},{\"Id\":5,\"Key\":\"UserShop\",\"Name\":\"个人橱窗\",\"AppId\":1128,\"Status\":1,\"Extra\":null,\"Customization\":null,\"Parent\":0,\"Actions\":null}]}",
            "enterprise_verify_reason": "人民日报官方账号",
            "favoriting_count": 74,
            "follow_status": 0,
            "follower_count": 125737299,
            "follower_request_status": 0,
            "follower_status": 0,
            "followers_detail": [
                {
                    "app_name": "aweme",
                    "apple_id": "1142110895",
                    "download_url": "https://d.douyin.com/JsvN/",
                    "fans_count": 125737299,
                    "icon": "http://p3.pstatp.com/origin/50ec00079b64de2050dc",
                    "name": "抖音",
                    "open_url": "snssdk1128://user/profile/104255897823?",
                    "package_name": "com.ss.android.ugc.aweme"
                },
                {
                    "app_name": "news_article",
                    "apple_id": "529092160",
                    "download_url": "https://d.toutiao.com/YjjY/",
                    "fans_count": 0,
                    "icon": "http://p3.pstatp.com/origin/50ed00079a1b6b8d1fb1",
                    "name": "头条",
                    "open_url": "snssdk143://profile?uid=0",
                    "package_name": "com.ss.android.article.news"
                },
                {
                    "app_name": "live_stream",
                    "apple_id": "1086047750",
                    "download_url": "http://d.huoshanzhibo.com/eFvB/",
                    "fans_count": 0,
                    "icon": "http://p3.pstatp.com/origin/2ea5c000abe106154adef",
                    "name": "抖音火山版",
                    "open_url": "snssdk1112://profile?id=0",
                    "package_name": "com.ss.android.ugc.live"
                }
            ],
            "following_count": 20,
            "forward_count": 0,
            "gender": 0,
            "ins_id": "",
            "is_activity_user": false,
            "is_block": false,
            "is_blocked": false,
            "is_effect_artist": false,
            "is_gov_media_vip": true,
            "is_mix_user": false,
            "is_star": false,
            "iso_country_code": "",
            "life_story_block": {
                "life_story_block": false
            },
            "live_commerce": true,
            "location": "武汉",
            "message_chat_entry": true,
            "mplatform_followers_count": 125737299,
            "nickname": "人民日报",
            "original_musician": {
                "digg_count": 0,
                "music_count": 0,
                "music_used_count": 0
            },
            "profile_tab_type": 0,
            "province": "湖北",
            "r_fans_group_info": {},
            "recommend_reason_relation": "",
            "recommend_user_reason_source": 0,
            "room_id": 0,
            "school_name": "",
            "sec_uid": "MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4",
            "secret": 0,
            "share_info": {
                "bool_persist": 1,
                "share_desc": "在抖音，记录美好生活！",
                "share_image_url": {
                    "url_list": null
                },
                "share_qrcode_url": {
                    "uri": "b6fd001f6ba9684c2724",
                    "url_list": [
                        "https://p3.douyinpic.com/obj/b6fd001f6ba9684c2724",
                        "https://p29.douyinpic.com/obj/b6fd001f6ba9684c2724",
                        "https://p6.douyinpic.com/obj/b6fd001f6ba9684c2724"
                    ]
                },
                "share_title": "快来加入抖音，让你发现最有趣的我！",
                "share_url": "www.iesdouyin.com/share/user/104255897823?iid=MS4wLjABAAAAs5exbTqGrfTM_AtW7VsqCDwrxMxqqNPBxJsKoO5_q4piEbON1-VKZz0eOjHcUao1&with_sec_did=1&sec_uid=MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4&did=MS4wLjABAAAAn11YiGPWUp0sFaBehPrcbq4gdFsoxdHru5B53SojlP1vXy2-Ty5x3m8TyDw5yrG3",
                "share_weibo_desc": "在抖音，记录美好生活！"
            },
            "shop_micro_app": "",
            "short_id": "0",
            "show_favorite_list": true,
            "signature": "参与、沟通、记录时代。",
            "signature_display_lines": 0,
            "signature_language": "zh",
            "sync_to_toutiao": 0,
            "tab_settings": {
                "private_tab": {
                    "private_tab_style": 1,
                    "show_private_tab": false
                }
            },
            "total_favorited": 6238761782,
            "twitter_id": "",
            "twitter_name": "",
            "uid": "104255897823",
            "unique_id": "rmrbxmt",
            "urge_detail": {
                "user_urged": 0
            },
            "user_not_see": 0,
            "user_not_show": 1,
            "verification_type": 0,
            "video_cover": {},
            "video_icon": {
                "height": 720,
                "uri": "",
                "url_list": [],
                "width": 720
            },
            "watch_status": false,
            "white_cover_url": [
                {
                    "uri": "31ad1000254caa51a0258",
                    "url_list": [
                        "https://p26.douyinpic.com/31ad1000254caa51a0258~tplv-dy-shrink:750:422.jpeg?from=2480802190&s=profile&se=true&sh=750_422&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p5-ipv6.douyinpic.com/obj/31ad1000254caa51a0258?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p29.douyinpic.com/obj/31ad1000254caa51a0258?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p26.douyinpic.com/obj/31ad1000254caa51a0258?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF"
                    ]
                },
                {
                    "uri": "318f1000413827e122102",
                    "url_list": [
                        "https://p26.douyinpic.com/318f1000413827e122102~tplv-dy-shrink:750:422.jpeg?from=2480802190&s=profile&se=true&sh=750_422&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p26.douyinpic.com/obj/318f1000413827e122102?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p9.douyinpic.com/obj/318f1000413827e122102?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF",
                        "https://p3.douyinpic.com/obj/318f1000413827e122102?from=2480802190&s=profile&se=false&sh=&sc=cover&l=202104041556240102040491065FA54EBF"
                    ]
                }
            ],
            "with_commerce_enterprise_tab_entry": false,
            "with_commerce_entry": true,
            "with_fusion_shop_entry": false,
            "with_new_goods": false,
            "youtube_channel_id": "",
            "youtube_channel_title": ""
        }
    },
    "msg": "success"
}
'''



