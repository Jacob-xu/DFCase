import random


def add(name, email):
    """
    @api {post} /add 拼接字符串
    @apiGroup 商业化
    @apiName add
    @apiDescription  拼接字符串
    @apiPermission 张三
    @apiParam {String=zhangsan,lisi} name=zhangsan 用户名
    @apiParam {String=222@bigo.com} email=222@bigo.sg 邮箱
    @apiParamExample {json} 请求示例:
    {
         "name": "zhangsan",
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
    return dict(code=0, data=sum, msg="success")


def randomNum(numList: list):
    """
    @api {post} /randomNum 随机数
    @apiGroup 秩序
    @apiName randomNum
    @apiDescription 追加随机数
    @apiPermission 李四
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
        "code": 200,
        "msg": "请求成功",
        "data": {}
    }

    """
    for nums in numList:
        nums['id'] = "{}-{}".format(nums['id'], random.randint(1, 10))
    return dict(code=0, msg="success", data=numList)