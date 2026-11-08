# FastAPI 系统教程：从基础入门到项目部署

面向已经具备 Python 基础、刚开始学习后端开发的读者。本仓库保存专栏文章、可运行示例和自制配图，按先理解请求，再编写接口，最后完成项目的顺序持续更新（更新时间不定）。

目前已整理**基础篇第 01 篇**。

## 从哪里开始

1. 阅读[第 01 篇：开始之前，API、HTTP 与 FastAPI 到底是什么](<notes/basics/01-开始之前：API、HTTP 与 FastAPI 到底是什么.md>)。
2. 对照[本篇示例代码](code/article01/main.py)理解路由注册、按分类与编号查找笔记，以及 JSON 响应。
3. 按下方步骤在本机启动服务，亲自观察请求和响应。

本篇的笔记数据保存在 Python 字典中。程序重启会恢复初始数据；它不是持久化存储，也没有用户认证。

## 运行第 01 篇示例

以下命令适用于 Windows PowerShell。已验证的环境是 Python 3.13.5、FastAPI 0.115.0、Uvicorn 0.30.6。请在仓库根目录执行：

```powershell
cd code/article01
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install fastapi==0.115.0 uvicorn==0.30.6
.\.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
```

最后一条命令会持续运行。保持这个终端打开，再打开第二个 PowerShell 窗口执行：

```powershell
curl.exe --http1.1 -i -H "Accept: application/json" http://127.0.0.1:8000/notes/basics/01
```

预期状态码为 `200`，响应正文为：

```json
{"id":"01","title":"开始之前"}
```

请求不存在的编号可观察 `404`：

```powershell
curl.exe --http1.1 -i http://127.0.0.1:8000/notes/basics/99
```

结束服务时，在运行 Uvicorn 的终端按 `Ctrl+C`。请求和响应的逐项解释见第 01 篇正文。

## 仓库结构

```text
assets/             文章配图
code/article01/     第 01 篇示例代码
notes/basics/       基础篇文章
```

## 当前状态

本仓库仍在逐篇写作中，文章和示例会随着学习与验证继续修订。欢迎通过 GitHub Issue 指出运行问题或概念错误，并附上复现步骤、Python 版本和实际输出。

## 许可证

 MIT。转载或再分发时，请保留版权声明和许可证文本。
