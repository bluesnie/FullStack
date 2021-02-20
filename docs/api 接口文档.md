###### datetime:2021/2/20 17:29
###### author:nzb

## 实时动态数据

- **url**： `/app/dynamic_chart/dynamic_chart_data/`

- **method**：`GET`

- **成功**：
    ```json
        {
            "code": 10000,
            "results": [
                1,
                17,
                8
            ],
            "errMsg": ""
        }
    ```

## 最新 100 条动态数据

- **url**： `/app/dynamic_chart/`

- **method**：`GET`

- **参数说明**：

| 字段 | 类型 | 是否必须  | 描述  | 说明  |
| ------------ | ------------ | ------------ | ------------ | --------------- |
| offset |  int      | 是   |  偏移量     |   |
| limit |  int      | 是   |  数量，`默认：100，最大：200`     |   |

- **成功**：
    ```json
        {
            "count": 627,  // 总数量
            "next": "http://127.0.0.1:8000/app/dynamic_chart/?limit=100&offset=100", // 下页链接
            "previous": null, // 上一页链接
            "results": [ // 结果数组
                {
                    "id": 1,
                    "content": 6
                },
                {
                    "id": 2,
                    "content": 1
                },
                {
                    "id": 3,
                    "content": 19
                }
            ]
        }
    ```

## 保存当前数据

- **url**： `/app/dynamic_chart/`

- **method**：`POST`

- **参数说明**：

| 字段 | 类型 | 是否必须  | 描述  | 说明  |
| ------------ | ------------ | ------------ | ------------ | --------------- |
| data |  array      | 是   |  数据数组     |   |

- **成功**：
    ```json
        {
          "code": 10000,
          "errMsg": ''
        }
    ```
    
- **失败**：
    ```json
        {
          "code": 40000,
          "errMsg": '无数据可保存'
        }
    ```

## 实时数据 url
- `http://127.0.0.1:8000/app/dynamic_chart/dynamic_chart_template1/`

## 100 数据 url
- `http://127.0.0.1:8000/app/dynamic_chart/dynamic_chart_template2/`