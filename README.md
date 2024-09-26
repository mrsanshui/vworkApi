# vworkApi介绍

《vworkApi》是基于PC端的企业微信封装的、REST风格的接口，开发者可通过**HTTP轻松调用**。可进行二次开发，实现微信机器人、群管理等强大的功能！



### 社区版跟专业版的区别？

- 社区版：
  - 麻雀虽小五脏俱全！
  - 不支持长时间运行
  - 不再维护更新
  - 微信版本：4.0.0.6024
  
- 专业版：
  - 功能更加强大、稳定！
  - 支持长时间运行
  - 使用有保障！持续更新迭代
  - 微信版本：4.1.28.6021



> 如果对你有帮助，别吝啬你的小手留个star呗



## 使用教程

> <span style="color: #ff5050">使用前请先安装指定版本的企业微信</span>
>
> 指定版本企业微信安装包：[https://pan.baidu.com/s/1FKlfwVsFLOhAKYlpSWSSMA](https://pan.baidu.com/s/1FKlfwVsFLOhAKYlpSWSSMA)
>
> 提取码：sszs



1. 克隆该项目（<span style="color: #ff5050">请关闭你的杀毒软件，否则可能会误删dll文件</span>）
2. 运行《注入工具(图形界面版).exe》点击启动并注入
3. 注入成功后，即可向 `8989` 端口发送HTTP请求，执行对应操作，请求路径为 `/api`，请求方法为 `POST`
4. 如需监听聊天消息：
   - 开启一个HTTP服务，并且运行在 `9000` 端口上，请求路径为 `/msg`，请求方法为 `POST`
5. 文档地址：https://www.showdoc.com.cn/mrsanshui/9693807382610096



## 更灵活的使用方法（使用命令行注入）

如需更灵活的使用，可使用命令行调用《inject_tool.exe》

命令参数：[inject_tool.exe的全路径] start [DLL的端口号]

示例：`C:\inject_tool.exe start 8989 --my_port=9000`

<span style="color: red">注意：</span>`--my_port` 就是你用来接收消息的端口号，这个参数是可选的，不填的话默认就是9000



## 如何多开？

非常简单！
不论你是使用《图形界面工具注入》、还是《命令行注入》
都只需要输入不同的 `[DLL的端口号]` 即可实现多开

- 第1个号：`C:\inject_tool.exe start 8989`
- 第2个号：`C:\inject_tool.exe start 8990`
- 第3个号：`C:\inject_tool.exe start 8991`
- 以此类推...



## 疑问解答、联系方式

- 交流QQ群：716983832
- 进群解决一切蛇皮问题！



## 声明

**本项目仅供技术研究，请勿用于非法用途，如有任何人凭此做何非法事情，均于作者无关，特此声明。**

