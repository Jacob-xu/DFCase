def add(a, b):
    """
    @api {post} /add 两数相加
    @apiGroup 商业化
    @apiName add
    @apiDescription  两数求和，返回计算结果
    @apiPermission fang
    @apiParam {String=7777,9999} a=77777    数字类型
    @apiParam {String=667777} b=9999   数字类型
    @apiParamExample {json} 请求示例:
    {
         "a": "111",
         "b": "9999"
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
    sum = a+b
    return dict(code=0, data=sum, msg="success")