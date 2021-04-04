
from deco import register
from api import API

class AwemeSDK:

    def __init__(self,token,host):
        self.host = 'http://{host}'.format(host=host.rstrip('/'))
        self.token = token

    @register(API.UserInfo)
    def get_user_info(self,uid):
        '''
        获取用户信息，详细版本
        :param uid:用户user id,例如：'104255897823'
        '''
        return {
            'uid':uid
        }

    @register(API.UserDetail)
    def get_user_detail(self,uid):
        '''
        获取用户信息，精简版本
        :param uid:用户sec_user_id，例如：'MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4'
        '''
        return {
            'uid':uid
        }

    @register(API.UserLiveInfo)
    def get_user_live_info(self, uid):
        '''
        获取用户直播信息
        :param uid: 用户user id,例如：'104255897823'
        '''
        return {
            'uid': uid
        }

    @register(API.UserLiveStatus)
    def get_user_live_status(self, uid):
        '''
        查询用户是否开播，获取开播的直播间room_id
        :param uid: 用户user id,例如：'104255897823'
        '''
        return {
            'uid': uid
        }

    @register(API.UserStarDetail)
    def get_user_star_detail(self, uid):
        '''
        获取用户星图的达人信息，前提是用户是星图达人
        :param uid: 用户user id,例如：'71606232346'
        '''
        return {
            'uid': uid
        }

    @register(API.UserReputation)
    def get_user_reputation(self, uid):
        '''
        获取用户带货口碑
        :param uid: 用户user id,例如：'74293591101'
        '''
        return {
            'uid': uid
        }

    @register(API.UserPosts)
    def get_user_posts(self, uid, cursor=0):
        '''
        获取用户发布的视频作品,精简版本
        :param uid: 用户user id,例如：'104255897823'
        :param cursor: 翻页游标，根据返回结果的max_cursor进行翻页操作，初始值为0
        '''
        return {
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserVideos)
    def get_user_videos(self, uid, cursor=0):
        '''
        获取用户发布的视频作品,详细版本
        :param uid: 用户user id,例如：'104255897823'
        :param cursor: 翻页游标，根据返回结果的max_cursor进行翻页操作，初始值为0
        '''
        return {
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserFavourites)
    def get_user_favourites(self, uid, cursor=0):
        '''
        获取用户点赞过的视频列表
        :param uid: 用户user id
        :param cursor: 翻页游标，根据返回结果的max_cursor进行翻页操作，初始值为0
        '''
        return {
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserPromotions)
    def get_user_promotions(self, uid, cursor=0):
        '''
        获取用户商品橱窗
        :param uid:用户user id
        :param cursor:翻页游标，默认0
        '''
        return {
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserFollowings)
    def get_user_followings(self, uid, cursor=0):
        '''
        获取用户关注列表
        :param uid:用户user id
        :param cursor:翻页游标，根据结果返回的min_time传入作为下一页翻页参数，初始为0
        '''
        return {
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserFollowers)
    def get_user_followers(self, uid, cursor=0):
        '''
        获取用户关注列表
        :param uid:用户user id
        :param cursor:翻页游标，根据结果返回的min_time传入作为下一页翻页参数，初始为0
        '''
        return {
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.VideoComments)
    def get_video_comments(self, aweme_id, cursor=0):
        '''
        获取视频评论
        :param aweme_id:视频id,如：6849103450475711752
        :param cursor:翻页游标，根据结果返回的cursor传入作为下一页翻页参数，初始为0
        '''
        return {
            'aweme_id': aweme_id,
            'cursor': cursor,
        }

    @register(API.VideoDetail)
    def get_video_detail(self,aweme_id):
        '''
        获取视频详情，详细版本
        :param aweme_id:视频的id
        '''
        return {
            'aweme_id': aweme_id,
        }

    @register(API.VideoInfo)
    def get_video_info(self,aweme_id):
        '''
        获取视频详情，精简版本
        :param aweme_id:视频的id
        '''
        return {
            'aweme_id': aweme_id,
        }

    @register(API.VideoPromotions)
    def get_video_promotions(self, aweme_id):
        '''
        获取某个视频的带货商品信息
        :param aweme_id:视频id
        '''
        return {
            'aweme_id': aweme_id,
        }

    @register(API.VideoCommentReplies)
    def get_video_comment_replies(self, aweme_id,cid,cursor=0):
        '''
        获取视频评论的子评论
        :param aweme_id: 视频id
        :param cid: 评论id
        :param cursor: 子评论列表翻页游标，适用于子评论过多的情况下,根据结果返回的cursor传入作为下一页翻页参数，初始为0

        '''
        return {
            'aweme_id': aweme_id,
            'cid':cid,
            'cursor':cursor
        }

    @register(API.VideoNoMark)
    def get_video_url(self, aweme_id):
        '''
        获取某个视频的无水印视频下载地址
        :param aweme_id:视频id
        '''
        return {
            'aweme_id': aweme_id,
        }

    @register(API.ChallengeDetail)
    def get_challenge_detail(self, challenge_id):
        '''
        获取话题（challenge）详情
        :param challenge_id:话题id
        '''
        return {
            'cid': challenge_id
        }

    @register(API.ChallengeVideos)
    def get_challenge_videos(self, challenge_id,cursor=0):
        '''
        获取话题（challenge）下的视频
        :param challenge_id:话题id
        :param cursor:翻页游标，根据结果返回的cursor进行翻页操作，初始值为0
        '''
        return {
            'cid': challenge_id,
            'cursor':cursor,
        }

    @register(API.PoiDetail)
    def get_poi_detail(self, poi_id):
        '''
        获取地点（poi）详情
        :param poi_id: 地点id
        '''
        return {
            'poi_id': poi_id
        }

    @register(API.PoiVideos)
    def get_poi_videos(self, poi_id,cursor=0):
        '''
        获取地点（poi）下的视频
        :param poi_id: 地点id
        :param cursor: 翻页游标，根据结果返回的cursor进行翻页操作，初始值为0
        '''
        return {
            'poi_id': poi_id,
            'cursor':cursor
        }

    @register(API.PromotionsVideosFeed)
    def get_promotion_videos_feed(self, page=1):
        '''
        带货视频推荐流
        :param page:页数索引
        '''
        return {
            'page': page,
        }

    @register(API.PromotionInfo)
    def get_promotion_info(self,promotion_id):
        '''
        获取某样带货商品的信息,精简版本，无销量具体数据
        :param promotion_id: 商品id
        '''
        return {
            'promotion_id': promotion_id,
        }

    @register(API.PromotionDetail)
    def get_promotion_detail(self,promotion_id):
        '''
        获取某样带货商品的信息,详细版本，有销量具体数据
        :param promotion_id: 商品id
        '''
        return {
            'promotion_id': promotion_id,
        }

    @register(API.PromotionSameVideos)
    def get_promotion_same_videos(self, promotion_id):
        '''
        同款商品带货视频推荐
        :param promotion_id:商品id
        '''
        return {
            'promotion_id': promotion_id,
        }

    @register(API.LiveRoomChat)
    def get_liveroom_chat(self,room_id):
        '''
        获取抖音直播间弹幕/进入直播间观众/刷礼物/关注主播 信息
        :param room_id:直播间id
        '''
        return {
            'room_id':room_id
        }

    @register(API.LiveRoomPromotions)
    def get_liveroom_promotions(self,room_id):
        '''
        获取抖音直播间带货商品信息
        :param room_id:直播间id
        '''
        return {
            'room_id':room_id
        }

    @register(API.LiveRoomInfo)
    def get_liveroom_info(self,room_id):
        '''
        获取抖音直播间信息
        :param room_id:直播间id
        '''
        return {
            'room_id':room_id
        }

    @register(API.LiveRoomStatus)
    def get_liveroom_status(self,room_id):
        '''
        查询直播间是否开播
        :param room_id:直播间id
        '''
        return {
            'room_ids':room_id
        }

    @register(API.LiveRoomAudience)
    def get_liveroom_audience(self,room_id):
        '''
        查询直播间在线观众，前200人
        :param room_id:直播间id
        '''
        return {
            'room_ids':room_id
        }

    @register(API.LiveRoomIntro)
    def get_liveroom_intro(self,room_id):
        '''
        查询直播间当前正在介绍的商品详情
        :param room_id:直播间id
        '''
        return {
            'room_ids':room_id
        }

    @register(API.LiveRoomFeed)
    def get_liveroom_feed(self):
        '''
        随机获取直播间
        '''
        return

    @register(API.RealStarBoard)
    def star_board(self):
        '''
        实时明星爱DOU榜
        '''
        return

    @register(API.RealHotBoard)
    def hot_board(self):
        '''
        实时热点榜
        '''
        return

    @register(API.RealGoodsBoard)
    def goods_board(self):
        '''
        实时好物榜
        '''
        return

    @register(API.RealHotVideos)
    def hot_videos(self):
        '''
        最热视频榜单
        '''
        return

    @register(API.RealEcoBoard)
    def eco_board(self):
        '''
        全站带货榜
        '''
        return

    @register(API.RealWaveBoard)
    def wave_board(self):
        '''
        全站音浪榜
        '''
        return

    @register(API.RealLiveBoard)
    def live_board(self):
        '''
        直播榜
        '''
        return

    @register(API.MusicHotBoard)
    def hot_music_board(self):
        '''
        音乐榜-热歌榜
        '''
        return

    @register(API.MusicNewhitBoard)
    def newhit_music_board(self):
        '''
        音乐榜-飙升榜
        '''
        return

    @register(API.MusicOriginalBoard)
    def original_music_board(self):
        '''
        音乐榜-原创榜
        '''
        return

    @register(API.RealBrandBoard)
    def brand_board(self,category_id,start_date=None):
        '''
        实时品牌榜
        :param category_id: 品牌类别id，可以从品牌类别接口获取，一次即可
        :param start_date:开始日期，可用于抓取历史榜单数据，默认空
        '''
        return {
            'cate_id':category_id,
            'start_date':start_date
        }

    @register(API.RealBrandCates)
    def brand_categories(self):
        '''
        品牌类别接口
        '''
        return

    @register(API.RealBrandDetail)
    def brand_detail(self,category_id,brand_id):
        '''
        热榜品牌详情
        :param category_id:品牌类别id，可以从品牌类别接口获取，一次即可
        :param brand_id:品牌id
        '''
        return {
            'category': category_id,
            'brand_id':brand_id
        }

    @register(API.SearchUsers)
    def search_users(self,keyword,cursor=0):
        '''
        关键词搜索用户
        :param keyword:搜索关键词
        :param cursor:翻页游标，初始为0，根据返回的cursor值进行翻页
        '''
        return {
            'keyword': keyword,
            'cursor':cursor
        }

    @register(API.SearchVideos)
    def search_videos(self,keyword,cursor=0):
        '''
        关键词搜索视频
        :param keyword:搜索关键词
        :param cursor:翻页游标，初始为0，根据返回的cursor值进行翻页
        '''
        return {
            'keyword': keyword,
            'cursor':cursor
        }

    @register(API.SearchLives)
    def search_lives(self,keyword,cursor=0):
        '''
        关键词搜索直播
        :param keyword:搜索关键词
        :param cursor:翻页游标，初始为0，根据返回的cursor值进行翻页
        '''
        return {
            'keyword': keyword,
            'cursor':cursor
        }

    @register(API.SearchGoods)
    def search_goods(self,keyword,cursor=0):
        '''
        关键词搜索商品
        :param keyword:搜索关键词
        :param cursor:翻页游标，初始为0，根据返回的cursor值进行翻页
        '''
        return {
            'keyword': keyword,
            'cursor':cursor
        }

    @register(API.SearchChallenges)
    def search_challenges(self, keyword, cursor=0):
        '''
        关键词搜索话题
        :param keyword:搜索关键词
        :param cursor:翻页游标，初始为0，根据返回的cursor值进行翻页
        '''
        return {
            'keyword': keyword,
            'cursor': cursor
        }

    @register(API.SearchMusic)
    def search_music(self, keyword, cursor=0):
        '''
        关键词搜索音乐
        :param keyword:搜索关键词
        :param cursor:翻页游标，初始为0，根据返回的cursor值进行翻页
        '''
        return {
            'keyword': keyword,
            'cursor': cursor
        }

    @register(API.SearchPoi)
    def search_poi(self, keyword, cursor=0):
        '''
        关键词搜索地点
        :param keyword:搜索关键词
        :param cursor:翻页游标，初始为0，根据返回的cursor值进行翻页
        '''
        return {
            'keyword': keyword,
            'cursor': cursor
        }

    @register(API.HomeFeed)
    def home_feed(self):
        '''
        首页推荐
        '''
        return