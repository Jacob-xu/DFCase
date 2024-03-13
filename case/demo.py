import random


def add(a, b):
    """
    @api {post} /add 两数相加
    @apiGroup 商业化
    @apiName add
    @apiDescription  两数求和，返回计算结果
    @apiPermission test
    @apiParam {String=111,222} a=111    第一个请求参数
    @apiParam {String=333} b=333   第二个请求参数
    @apiParamExample {json} 请求示例:
    {
         "a": "111",
         "b": "333"
      }
    @apiSuccess (200) {Number} code 服务器码
    @apiSuccess (200) {String} data 造数成功返回相关的数据
    @apiSuccess (200) {String} msg 提示语
    @apiSuccessExample {json} 返回示例:
    {
        "code": 0,
        "msg": "请求成功",
        "data": 12
    }
    """
    sum = a + b
    return dict(code=0, data=sum, msg="success")


def randomNum(numList: list):
    """
    @api {post} /randomNum 随机数
    @apiGroup 秩序
    @apiName randomNum
    @apiDescription 追加随机数
    @apiPermission test2
    @apiParam {Object[]} numList 数据数组
    @apiParam {String} numList.id 这里填写id数据
    @apiParam {String} numList.content 这里填写描述
    @apiParamExample {json} 请求示例：
    {
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
        "code": 0,
        "msg": "请求成功",
        "data": {}
    }

    """
    for nums in numList:
        nums['id'] = "{}-{}".format(nums['id'], random.randint(1, 10))
    return dict(code=0, msg="success", data=numList)
