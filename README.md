# AwemeSDK

> 联系微信gameids获取token、host
>

## ChangeLog

2021-04-04 更新:

    - 新增接口 `用户开播查询`
    - 新增接口 `用户星图信息`
    - 新增接口 `用户粉丝列表`
    - 新增接口 `用户关注列表`
    - 新增接口 `用户带货口碑`
    - 新增接口 `用户视频精简版`
    - 新增接口 `用户信息精简版`
    - 新增接口 `视频详情精简版`
    - 新增接口 `视频无水印地址`
    - 新增接口 `商品详情详细版(有销量)`
    - 新增接口 `直播间随机推荐`
    - 新增接口 `直播间在线观众`
    - 新增接口 `直播间正在介绍商品`
    - 新增接口 `全站带货榜`
    - 新增接口 `全站音浪榜`
    - 新增接口 `直播榜`
    - 新增接口 `音乐榜-热歌榜`
    - 新增接口 `音乐榜-原创榜`
    - 新增接口 `音乐榜-飙升榜`
    - 新增接口 `搜索直播`
    - 新增接口 `搜索商品`
    - 新增接口 `搜索话题`
    - 新增接口 `搜索音乐`
    - 新增接口 `搜索地点`
    - 新增接口 `首页推荐`

## 调用示例

```python

from douyin import AwemeSDK

token = '你的密钥'
host  = '主机地址'  
              
# 初始化SDK实例
sdk   = AwemeSDK(token,host)


# 0.用户详情-详细版
user_info = sdk.get_user_info('100000004548')

# 1.用户详情-精简版
user_detail = sdk.get_user_detail('MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4')

# 2.用户作品-详细版 ，一次返回10条视频，可翻页
user_videos = sdk.get_user_videos('100000004548')

# 3.用户作品-精简版，一次返回10条视频，可翻页
user_posts = sdk.get_user_posts('100000004548')

# 4.用户喜欢视频，一次返回10条视频，可翻页
user_favourites = sdk.get_user_favourites('100000004548')

# 5.视频评论，一次返回10条视频，可翻页
video_comments = sdk.get_video_comments('6849103450475711752') 

# 6.关键词搜索视频
users = sdk.search_users('热巴')


```

## 所有接口请看文件`douyin.py`代码注释
 