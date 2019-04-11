# RESTful服务器：http://host:port/api

## 所有用户角色及其权限：

`root`
```
除了最自己删、改、查。拥有一切权限（只要存在该功能）。
```

`admin`
```
除了对于root用户的一切操作，对同等级角色的删除与更改。拥有一切权限，具体如下：
    用户：
        1、获取非root用户列表（含过滤）。
        2、创建用户（可创建admin/stuff两种角色的用户）。
        3、删除stuff用户。
        4、更新stuff和自己的资料。
        5、查看非root用户的详情信息。
    图书：
        1、获取图书列表（含过滤）。
        2、增加图书。
        3、下架图书。
        4、更新图书信息。
        5、查看图书详情信息。
    书种：
        1、获取书种（含过滤）。
        2、增加书种。
        3、删除书种（前提是无图书引用该书种）。
    索引：
        1、查看引用某书种的所有书籍。
        2、解除所有书籍对某书种的引用（之后可以删除）。
        3、查看与某用户相关的所有销售记录。
        4、查看与某图书有关的所有销售记录。
        5、查看与某VIP有关的所有销售记录。
    销售记录：
        1、获取所有销售记录。
        2、增加销售记录（即售书）。
    VIP：
        1、获取VIP列表（含过滤）。
        2、创建VIP。
        3、删除某VIP。
```

`stuff`
```
普通员工的权限，具体如下：
    用户：
        1、获取角色为stuff用户列表（含过滤）。
        2、更新自己的资料(包括密码)。
        5、查看角色为stuff用户的详情信息。
    图书：
        1、获取图书列表（含过滤）。
        2、查看图书详情信息。
    书种：
        1、获取书种（含过滤）。
        2、增加书种。
    索引：
        1、查看引用某书种的所有书籍。
        2、查看与某用户相关的所有销售记录。
        3、查看与某图书有关的所有销售记录。
        4、查看与某VIP有关的所有销售记录。
    销售记录：
        1、增加销售记录（即售书）。
    VIP：
        1、获取VIP列表（含过滤）。
        2、创建VIP。
        4、删除某VIP。
```

## 所有接口地址及其简略：
  
`/session` *[登录、注销](#session)*

`/accounts` *[获取用户、新增用户](#accounts)*
`/accounts/<account_id>` *[用户删、改、查](#accounts-1)*

`/books` *[获取图书、新增图书](#books)*
`/books/<book_id>` *[图书删、改、查](#books-1)*

`/vips` *[获取VIP、新增VIP](#vips)*
`/vips/<vip_id>` *[VIP删除](#vips-1)*

`/types` *[获取书种、新增书种](#types)*
`/types/<book_type_id>` *[书种删除](#types-1)*

`/sales_records` *[获取销售记录、添加销售记录](#sales_records)*

`/references/book2type/<book_type_id>` *[解除图书对书种的索引、获取某书种的所有图书](#book2type)*
`/references/record2account/<account_id>` *[获取某用户的售书记录](#record2account)*
`/references/record2book/<book_id>` *[获取某图书的销售记录](#record2book)*
`/references/record2vip/<vip_id>` *[获取某VIP的购买记录](#record2vip)*


## 详情说明
<font color=blue>写在前面</font>

    1、越权请求会得到如下统一response
    {
      "message": "You don't have the permission to access the requested resource. It is either read-protected or not readable by the server."
    }
    
    2、除了get方法，其他方法的请求结果都有'success'字段。可以根据该字段判断请求是否成功，再根据其余的message或者token/id获得其他信息。
    
    3、如果form-data缺少某必要字段，会出现如下格式提示（下面是未填写密码）
    {
      "message": {
        "password": "This is password"
      }
    }

### /session <span id="session">登录、注销</span> 

#### post: 登录
##### form-data
```
username: root
password: password
```
##### response
```
{
  "id": "56ebb6ee159ce145f818193b",
  "message": "No message",
  "success": 1,
  "token": "0wnCLKVPFG5x2eW8"
}
```

#### delete: 登出
##### headers
```
token: 0wnCLKVPFG5x2eW8
```
<font color=red>注：如无特别说明，以下所有请求除了要求的form-data或param以外，还要必须提供key为\'token'值为\'XXXX'的header键值对。根据RESTful的等幂性，此字段提供身份验证。</font>
##### response
```
{
  "message": "No message",
  "success": 1
}
```

### /accounts <span id="accounts">获取用户、新增用户</span> 

#### post 新增用户
##### form-data
```
username: skyduy
nickname: YuJun
password: secret
confirm: secret
role: 1 (其中0为员工，1为超级管理员)
```
##### response(post /accounts)
```
{
  "id": "56ed05cb159ce12c74a634f5",
  "message": "No message",
  "success": 1,
  "token": "kdqdxwJowiraNP3D"
}
```

#### get 获取所有用户
##### param(可选，此时表示过滤：nickname或者username)，当有param时：
```
/accounts?username=skyduy&&nickname=YuJun
```
##### response(get /accounts)
```
{
  "accounts": [
    {
      "id": "56ed05cb159ce12c74a634f5",
      "nickname": "YuJun",
      "role": "stuff"
    },
    {
      "id": "56ed073d159ce12b0c442de8",
      "nickname": "张三",
      "role": "stuff"
    },
    {
      "id": "56ed0805159ce100546b669e",
      "nickname": "张三",
      "role": "admin"
    }
  ]
}
```
### /accounts/account_id:str <span id="accounts-1">用户删、改、查</span> 

#### get 查看用户详情信息
##### response(get /accounts/56ed0805159ce100546b669e)
```
{
  "created": "Sat, 19 Mar 2016 16:04:21 -0000",
  "description": "",
  "id": "56ed0805159ce100546b669e",
  "nickname": "张三",
  "role": "admin",
  "username": "yangjing1"
}
```


#### put 查看用户详情信息
##### form-data
```
nickname: '员工of张三'
new_password: 2 （填写该框表示要修改密码，可选）
confirm: 2 （填写该框表示要修改密码，可选）
old_password: 1 （填写该框表示要修改密码，可选）
des: 'new_des' (可选)
```

##### response(put /accounts/56ed073d159ce12b0c442de8)
```
{
  "id": "56ed073d159ce12b0c442de8",
  "message": "user's profile update successfully!",
  "success": 1
}
```


#### delete 删除用户
##### response(delete /accounts/56ed073d159ce12b0c442de8)
```
{
  "message": "No message",
  "success": 1
}
```

### /books <span id="books">获取图书、新增图书</span> 

#### post 获取图书列表（含过滤）
##### form-data
```
name: 海贼王
count: 100
price: 20.5
des: 可为空
```
##### response(post /books)
```
{
  "id": "56ed0c06159ce147ec4131dc",
  "message": "No message",
  "success": 1
}
```
#### get 获取图书列表（含过滤）
##### response(get /books)
```
{
  "books": [
    {
      "id": "56ed0c06159ce147ec4131dc",
      "name": "海贼王",
      "price": 20.5,
      "sales": 0
    },
    {
      "id": "56ed0c66159ce147ec4131dd",
      "name": "金瓶梅",
      "price": 58,
      "sales": 0
    }
  ]
}
```
### /books/book_id:str <span id="books-1">图书删、改、查</span> 

#### get 查看图书详情信息
##### response(get /books/56ed0c66159ce147ec4131dd)
```
{
  "description": "张三喜欢的故事",
  "id": "56ed0c66159ce147ec4131dd",
  "name": "金瓶梅",
  "price": 58,
  "remaining": 100,
  "sales": 0,
  "type": []
}
```
#### put 更新图书信息
##### form-data
```
delta: -20
price: 100
des = '张三超级喜欢的故事，被他买掉了20本，因此升价为100元'(可选)
type_id = 'type_id1'（根据种类id添加一个种类，若不存在id忽略）
type_id = 'type_id2'（表示一次性添加两个种类）
```
##### response(put /books/56ed0c66159ce147ec4131dd)
```
{
  "id": "56ed0c66159ce147ec4131dd",
  "message": "No message",
  "success": 1
}
```
#### delete 下架某图书
##### response(delete /books/56ed0c66159ce147ec4131dd)
```
{
  "message": "No message",
  "success": 1
}
```

### /vips <span id="vips">获取VIP、新增VIP</span> 

#### post 新增VIP
##### form-data
```
username: vip1
nickname: 我是大V
phone: 1233457 （可选最长15）
```
##### response (post /vips)
```
{
  "id": "56ed0ec2159ce1266c62acae",
  "message": "No message",
  "success": 1
}
```
#### get 获取VIP列表（含过滤）
```
{
  "vips": [
    {
      "id": "56ed0ec2159ce1266c62acae",
      "nickname": "我是大V",
      "phone": "1233457",
      "username": "vip1"
    },
    {
      "id": "56ed0ed7159ce1266c62acaf",
      "nickname": "我也是大V",
      "phone": "12345678901",
      "username": "vip2"
    }
  ]
}
```

### /vips/vip_id:str <span id="vips-1">VIP删除。</span> 

#### delete 查看某VIP详情信息
##### response (delete /vips/56ed0ec2159ce1266c62acae)
```
{
  "message": "No message",
  "success": 1
}
```

### /types <span id="types">获取书种、新增书种。</span> 

#### post 新增书种
##### form-data
```
name: 动漫
```
##### response (post /types)
```
{
  "id": "56ed0f92159ce1266c62acb0",
  "message": "No message",
  "success": 1
}
```

#### get 获取书种列表（含过滤）
##### response(get /types)
```
{
  "books_types": [
    {
      "id": "56ed0f92159ce1266c62acb0",
      "name": "动漫"
    },
    {
      "id": "56ed0f9d159ce1266c62acb1",
      "name": "热血"
    },
    {
      "id": "56ed0fa1159ce1266c62acb2",
      "name": "后宫"
    }
  ]
}
```

### /types/book_type_id:str <span id="types-1">书种删除。</span> 

#### delete 查看某书籍详情信息
#### response(delete /types/56ed0f9d159ce1266c62acb1)
```
{
  "message": "No message",
  "success": 1
}
```

### /sales_records 获取销售记录、添加销售记录
#### post 销售图书
##### form-data
```
count: 1
seller_id: 56ed05cb159ce12c74a634f5
book_id: 56ed0c06159ce147ec4131dc
purchaser_id:56ed0ed7159ce1266c62acaf (可选)
```
##### response (post /sales_records)
```
{
  "id": "56ed10f1159ce1266c62acb3",
  "message": "No message",
  "success": 1
}
```

#### get 获取销售记录列表
##### response (get /sales_records)
```
{
  "sales_records": [
    {
      "book": {
        "id": "56ed0c06159ce147ec4131dc",
        "name": "海贼王",
        "price": 20.5,
        "sales": 3
      },
      "count": 1,
      "id": "56ed10f1159ce1266c62acb3",
      "price": 16.400000000000002,
      "purchaser": {
        "id": "56ed0ed7159ce1266c62acaf",
        "nickname": "我也是大V",
        "phone": "12345678901",
        "username": "vip2"
      },
      "sale_time": "Sat, 19 Mar 2016 16:42:25 -0000",
      "seller": {
        "id": "56ed05cb159ce12c74a634f5",
        "nickname": "YuJun",
        "role": "stuff"
      }
    },
    {
      "book": {
        "id": "56ed0c06159ce147ec4131dc",
        "name": "海贼王",
        "price": 20.5,
        "sales": 3
      },
      "count": 2,
      "id": "56ed11b2159ce101a8f49bdb",
      "price": 20.5,
      "purchaser": {
        "id": null,
        "nickname": null,
        "phone": null,
        "username": null
      },
      "sale_time": "Sat, 19 Mar 2016 16:45:38 -0000",
      "seller": {
        "id": "56ed05cb159ce12c74a634f5",
        "nickname": "YuJun",
        "role": "stuff"
      }
    }
  ]
}
```

### /references/book2type/book_type_id:str <span id="book2type">解除图书对书种的索引、获取某书种的所有图书。</span> 

#### get 获取某书种所有图书
##### response (get /references/book2type/56ed140a159ce139bca7ad1a)
```
{
  "books": [
    {
      "id": "56ed0c06159ce147ec4131dc",
      "name": "海贼王",
      "price": 20,
      "sales": 3
    }
  ]
}
```
#### delete 解除图书对书种的索引
##### response (delete /references/book2type/56ed140a159ce139bca7ad1a)
```
{
  "message": "No message",
  "success": 1
}
```

### /references/record2account/account_id:str <span id="record2account">获取某用户的售书记录。</span> 

#### get 获取某用户售书记录
##### response (get /references/record2account/56ed05cb159ce12c74a634f5)
```
{
  "sales_records": [
    {
      "book": {
        "id": "56ed0c06159ce147ec4131dc",
        "name": "海贼王",
        "price": 20,
        "sales": 3
      },
      "count": 1,
      "id": "56ed10f1159ce1266c62acb3",
      "price": 16.400000000000002,
      "purchaser": {
        "id": "56ed0ed7159ce1266c62acaf",
        "nickname": "我也是大V",
        "phone": "12345678901",
        "username": "vip2"
      },
      "sale_time": "Sat, 19 Mar 2016 16:42:25 -0000",
      "seller": {
        "id": "56ed05cb159ce12c74a634f5",
        "nickname": "YuJun",
        "role": "stuff"
      }
    },
    {
      "book": {
        "id": "56ed0c06159ce147ec4131dc",
        "name": "海贼王",
        "price": 20,
        "sales": 3
      },
      "count": 2,
      "id": "56ed11b2159ce101a8f49bdb",
      "price": 20.5,
      "purchaser": {
        "id": null,
        "nickname": null,
        "phone": null,
        "username": null
      },
      "sale_time": "Sat, 19 Mar 2016 16:45:38 -0000",
      "seller": {
        "id": "56ed05cb159ce12c74a634f5",
        "nickname": "YuJun",
        "role": "stuff"
      }
    }
  ]
}
```

### /references/record2book/book_id:str <span id="record2book">获取某图书的销售记录。</span> 

#### get 获取某图书的销售记录
##### response (get /references/record2book/56ed0c06159ce147ec4131dc)
```
{
  "sales_records": [
    {
      "book": {
        "id": "56ed0c06159ce147ec4131dc",
        "name": "海贼王",
        "price": 20,
        "sales": 3
      },
      "count": 1,
      "id": "56ed10f1159ce1266c62acb3",
      "price": 16.400000000000002,
      "purchaser": {
        "id": "56ed0ed7159ce1266c62acaf",
        "nickname": "我也是大V",
        "phone": "12345678901",
        "username": "vip2"
      },
      "sale_time": "Sat, 19 Mar 2016 16:42:25 -0000",
      "seller": {
        "id": "56ed05cb159ce12c74a634f5",
        "nickname": "YuJun",
        "role": "stuff"
      }
    },
    {
      "book": {
        "id": "56ed0c06159ce147ec4131dc",
        "name": "海贼王",
        "price": 20,
        "sales": 3
      },
      "count": 2,
      "id": "56ed11b2159ce101a8f49bdb",
      "price": 20.5,
      "purchaser": {
        "id": null,
        "nickname": null,
        "phone": null,
        "username": null
      },
      "sale_time": "Sat, 19 Mar 2016 16:45:38 -0000",
      "seller": {
        "id": "56ed05cb159ce12c74a634f5",
        "nickname": "YuJun",
        "role": "stuff"
      }
    }
  ]
}
```

### /references/record2vip/vip_id:str <span id="record2vip">获取某VIP的购买记录。</span> 

#### get 获取某VIP的购买记录
##### response(get /references/record2vip/56ed0ed7159ce1266c62acaf)
```
{
  "sales_records": [
    {
      "book": {
        "id": "56ed0c06159ce147ec4131dc",
        "name": "海贼王",
        "price": 20,
        "sales": 3
      },
      "count": 1,
      "id": "56ed10f1159ce1266c62acb3",
      "price": 16.400000000000002,
      "purchaser": {
        "id": "56ed0ed7159ce1266c62acaf",
        "nickname": "我也是大V",
        "phone": "12345678901",
        "username": "vip2"
      },
      "sale_time": "Sat, 19 Mar 2016 16:42:25 -0000",
      "seller": {
        "id": "56ed05cb159ce12c74a634f5",
        "nickname": "YuJun",
        "role": "stuff"
      }
    }
  ]
}
```
