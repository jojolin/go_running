# go running
- `pid`: 个人用户id

- `vkey`: 安全校验码，由前后端RSA对称算法生成
  - e.g. `/lecture?id={lectureId}&ts={timestamp}&vkey={vkey}`
    - `vkey=rsa(lecture?id={lectureId}&ts={timestamp}`

- `data`: 由对称算法生成的加密数据，加入时间戳，所有需要保密传输的内容
  - 保密内容包括: `pid`

- `errorCode`: 错误码，前后端反馈错误及异常情况
  - "000000": 正常
  - "000001": 安全校验失败
  - "000002": 请求资源不存在

- 所有请求路径带上`&ts={timestamp}&vkey={vkey}`


## 课程
- /lecture/list
  - [获取课程列表](./lectureList.json)

- /lecture?id={lectureId}
  - [获取课程详细信息](./lecture.json)

- /lecture?id={lectureId}

## 电台配置
- /radioConfig
  - [获取个人电台配置](./radioConfig.json)

```
POST /radioConfig

{"id": "pid"}
```

- /radioConfig/save
  - [保存个人电台配置](./radioConfig.json)

```
POST /radioConfig/save 

{"id": "pid", "voiceTipOn": true, ...}
```

## 歌单
- /diss/new
  - 新建歌单
  - @param: id, 个人id
  - TODO
  
```
POST /diss/new

data=rsa({"id": "pid"})

RESPONSE:
{"dissId": "d134342"}
```

- /diss/save?id={dissId}
  - 保存新建的歌单
  - @param: dissId, 新建歌单id
  - TODO
```
POST /diss/save?id={dissId}

```
data=rsa({"id": "pid"})&diss={...}
```

  
- /diss/list?page={page}&num={num}
  - 获取歌单列表
  - @param: id, 个人id
  - @param: page, 页码
  - @param: num, 数目

```
POST /diss/list

data=rsa({"id": "pid"})
```

- /diss?id={dissId}
  - [获取歌单详细信息](./diss.json)

- /dissLikes

```
POST /dissLikes

data=rsa({"id": "pid"})

RESPONSE:
[Diss]
```

## 歌曲
- /song/list?rate={rate}
  - 获取匹配频率的歌曲列表

- /song?rate={rate}
  - 获取匹配频率的[歌曲](./song.json)
  - @param: rate, 频率

```
POST /song?rate=170

data=rsa({"id": "pid"})

RESPONSE:
{"songId": "4234324", ...}
```

## 语音包资源
- /voice/list
  - 获取语音包列表

```
POST /voice/list

data=rsa({"id": "pid"})

RESPONSE:
[{id: "v1234567", ...}]
```

- /voice?id={id}
  - [获取语音包](./voice.json)
