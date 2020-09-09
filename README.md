## 课程
- /lecture/list
  - [获取课程列表](./lectureList.json)

- /lecture?id={lectureId}
  - [获取课程详细信息](./lecture.json)

## 电台配置
- /radioConfig?id={id}
  - [个人电台配置](./radioConfig.json)

- /radioConfig/save?id={id}
  - 保存个人电台配置

## 歌单
- /diss/new?id={id}
  - @param: id, 个人id
  - 新建歌单
  - TODO
  
```
GET /diss/new?id=p1234567

{"dissId": "d134342"}
```

- /diss/save?id={dissId}
  - TODO
```
POST /diss/save?id={dissId}

```
  
- /diss/list?id={id}&page={page}&num={num}
  - 获取歌单列表
  - @param: id, 个人id
  - @param: page, 页码
  - @param: num, 数目

- /diss?id={dissId}
  - [获取歌单详细信息](./diss.json)


## 语音包资源
- /voice/list
  - 获取语音包列表

- /voice?id={id}
  - [获取语音包](./voice.json)
