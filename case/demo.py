import random
from .hash_num import hash_adset


def add(name, email):
    """
    @api {post} /add 拼接字符串
    @apiGroup 商业化-SSP
    @apiName add
    @apiDescription  拼接字符串
    @apiPermission 张三
    @apiParam {String=张三,李四} name=张三 用户名
    @apiParam {String} email=222@bigo.sg 邮箱
    @apiParamExample {json} 请求示例:
    {
         "name": "张三",
         "email": "222@bigo.sg"
      }
    @apiSuccess (200) {Number} code 服务器码
    @apiSuccess (200) {String} data 造数成功返回相关的数据
    @apiSuccess (200) {String} msg 提示语
    @apiSuccessExample {json} 返回示例:
    {
        "code": 200,
        "msg": "请求成功",
        "data": zhangsan,222@bigo.sg
    }
    """
    sum = name + ',' + email
    print(sum)
    return dict(code=200, data=sum, msg="success")


def randomNum(index: int, numList: list):
    """
    @api {post} /randomNum 随机数
    @apiGroup 秩序
    @apiName randomNum
    @apiDescription 追加随机数
    @apiPermission 李四
    @apiParam {Number=666} index 序号
    @apiParam {Object[]} numList 数据数组
    @apiParam {String=22,333,444} numList.id 这里填写id数据
    @apiParam {String} numList.content 这里填写描述
    @apiParamExample {json} 请求示例：
    {
        "index": 2,
        "numList": [
            {"id":"123","content":"hello"},
            {"id":"456","content":"world"}
        ]
    }
    @apiSuccess (200) {Number} code 服务器码
    @apiSuccess (200) {String} data 造数成功返回相关的数据
    @apiSuccess (200) {String} msg 提示语
    @apiSuccessExample {json} 返回示例:
    {
        "code": 200,
        "msg": "请求成功",
        "data": {}
    }

    """
    for nums in numList:
        nums['id'] = "{}-{}".format(nums['id'], random.randint(1, 10))
    data = {"index": index, "num": numList}
    return dict(code=200, msg="success", data=data)


def msDemo(project_id: str, task_id: str, params: list, task_type: int, user: str):
    """
    @api {post} /msDemo 调用大黄蜂
    @apiGroup Hello-通用
    @apiName msDemo
    @apiDescription 调用大黄蜂
    @apiPermission 王五
    @apiParam {String=9e6f72b0-0fee-4ce2-aeb8-4c9345edc045} project_id 大黄蜂项目id
    @apiParam {String=b57c78fb-449a-42bd-90f5-991f4bed6875} task_id 计划/场景id
    @apiParam {Number=1} task_type 任务类型
    @apiParam {String} user 用户
    @apiParam {Object} params 大黄蜂入参
    @apiParam {Number} params.p1 参数1
    @apiParam {String} params.p2 参数2
    @apiParamExample {json} 请求示例：
    {
    "project_id":"9e6f72b0-0fee-4ce2-aeb8-4c9345edc045",
    "task_id":"b57c78fb-449a-42bd-90f5-991f4bed6875",
    "task_type": 1,
    "user":"test_user",
    "params":{"p1":12,"p2":"eee"}
    }
    @apiSuccess (200) {Number} code 服务器码
    @apiSuccess (200) {String} data 造数成功返回相关的数据
    @apiSuccess (200) {String} msg 提示语
    @apiSuccessExample {json} 返回示例:
    {
        "code": 200,
        "msg": "请求成功",
        "data": {}
    }

    """
    data = {"project_id": project_id, "task_id": task_id, "task_type": task_type, "params": params, "user": user}
    return dict(code=200, msg="success", data=data)


def hashNum(adset_id: int):
    """
    @api {post} /hashNum 外部应用示例
    @apiGroup 商业化-DSP
    @apiName hashNum
    @apiDescription 外部应用示例
    @apiPermission 王五
    @apiParam {Number} adset_id 广告组id
    @apiParamExample {json} 请求示例：
    {
    "adset_id":44387428390149888
    }
    @apiSuccess (200) {Number} code 服务器码
    @apiSuccess (200) {String} data 造数成功返回相关的数据
    @apiSuccess (200) {String} msg 提示语
    @apiSuccessExample {json} 返回示例:
    {
        "code": 200,
        "msg": "请求成功",
        "data": {}
    }

    """
    data = hash_adset(adset_id)
    return dict(code=200, msg="success", data=data)
