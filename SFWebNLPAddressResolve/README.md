# 逆向顺丰官网地址智能识别api
- [顺丰官网](https://www.sf-express.com/chn/sc)

## 背景
- 想找一个可以自动把省市区，人名，手机号，地址解析成结构化数据的api
- 免费！免费！免费！ （重要的事情说三遍）
- 使用简单，最好是http请求方式调用

## 免责声明
只做技术讨论，不可用于非法用途，后果自负！

## 接口地址
```text
https://www.sf-express.com/sf-service-core-web/service/nlp/address/mainlandChina/resolve?lang=sc&region=cn&translate=sc
```

## 分析过程
- 最初只需要在顺丰官网登录后，获取到自己账号的cookie就可以调用。

- 2024年8月初的时候发现调不通了，于是去官网验证，发现改版了，增加了api签名等参数，于是开始逆向。

## 逆向结论
接口增加了一系列参数

- appid: 跟顺丰的端(手机，网页，其他等)有关，与appSecret成对出现，且固定
- appSecret: 与appid成对出现，固定
- timestamp: 毫秒时间戳
- nonce: 6位随机字符串
- sign: md5(appId+appSecret+body+nonce+timestamp), 此处的算法通过看前端代码得知，日后可能变化
- body: body体中的参数不需要紧凑型，参与sign计算的时候需要变为紧凑型