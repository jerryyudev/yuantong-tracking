import subprocess
import json
import datetime
import warnings

# 忽略 DeprecationWarning 警告
warnings.simplefilter("ignore", category=DeprecationWarning)

def query_yuantong_tracking_with_curl(tracking_number):
    # 构造 curl 命令
    curl_command = [
        "curl",
        f"https://alayn.baidu.com/express/appdetail/pc_express?query_from_srcid=51150&tokenV2=ahA5WvCaFBtOyLiezn67h%2FRQ9Up5udU28fM49Z274jfSoPPZQe7FyMT%2BAQFuh9p0&com=yuantong&nu={tracking_number}&qid=b3556ac0000507fc&cb=jsonp_1737105594825_35885",
        "-H", "Accept: */*",
        "-H", "Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "-H", "Connection: keep-alive",
        "-H", "Cookie: PSTM=1705066961; BIDUPSID=1F6975F965D32D3F99F05F3E76C74890; BAIDUID=08BA526609E899CF90DADE182720BAED:SL=0:NR=10:FG=1; BDUSS=RUd1ZDR29FeDRnSC0xOWJIanlvSW9oTFgySk9Vb0lwZmNMbC1iSVM2QWJqbDFtRVFBQUFBJCQAAAAAAQAAAAEAAABntqkMzuXOrL~VvOQ2NjY2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABsBNmYbATZmdV; BDUSS_BFESS=RUd1ZDR29FeDRnSC0xOWJIanlvSW9oTFgySk9Vb0lwZmNMbC1iSVM2QWJqbDFtRVFBQUFBJCQAAAAAAQAAAAEAAABntqkMzuXOrL~VvOQ2NjY2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABsBNmYbATZmdV; MCITY=-131%3A; H_WISE_SIDS=61027_60853_61502_61612_61685_61684_61736_61781_61787; H_WISE_SIDS_BFESS=61027_60853_61502_61612_61685_61684_61736_61781_61787; H_PS_PSSID=61027_60853_61684_61736_61781_61787_61824_61804_61859_61896; BAIDUID_BFESS=08BA526609E899CF90DADE182720BAED:SL=0:NR=10:FG=1; BA_HECTOR=al04a4al0k21a021ahah8g8h2r0kdp1jojk231v; ZFY=hcMLc4mLWvItyPHvtLbC61A0j22SCmqxtLmlIbb3xbI:C; __bid_n=187f00c8e1892963b64437; ab_sr=1.0.1_NTY2MWRhZDg0NTQxYzY0YTI4NjU4NmI2MjQxZjcwNTc0MGExMGRiZmUzMzRhOWI4ZmFmZDk1MTExNTIwZmE1ZjM4NDZmZTI4YWRjZjIzM2M5MmQ4MGU0ODZkYWRlNWU4YjFhOWZjNTExYmUyYmE4OTlkZDE4YTJlMTEzZDhlNmRlM2I1ZjNhMGExMDIwMTdmYTg0ZTIwOGE3Y2E1ZjMxNjI2YjFlN2YwYTg0YjIwZTk2MGE2OGQ2YjdlNjliMTZiMGI4M2Q2OTI3MWZmNDc4NjJjODE1MGY2ODVmMGUzYTM3ZDY1MmU3M2NlZmNkOTI4MzI0OWVlNDZiNzE4MTViOQ==; RT=\"z=1&dm=baidu.com&si=0e51c6f8-77b8-41c2-8a35-884a3b021d01&ss=m60hbrrw&sl=9&tt=d52&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=22g6&ul=3c0q&hd=3c0z\""
    ]

    try:
        # 执行 curl 命令，并捕获输出
        result = subprocess.run(
            curl_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # 确保输出是字符串
            encoding="utf-8"  # 指定解码方式为 utf-8
        )
        
        if result.returncode == 0:
            # 提取并解析 JSON 数据
            json_data = result.stdout.split('jsonp_1737105594825_35885(')[-1][:-1]  # 去掉前后多余的部分
            data = json.loads(json_data)

            # 提取快递信息
            context = data.get("data", {}).get("context", [])
            formatted_context = []

            for entry in context:
                # 转换时间
                time = datetime.datetime.fromtimestamp(entry["time"]).strftime('%Y-%m-%d %H:%M:%S')
                formatted_context.append({
                    "time": time,
                    "desc": entry["desc"]
                })
            
            return formatted_context
        else:
            return {"error": result.stderr}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # 输入快递单号
    tracking_number = input("请输入圆通快递单号: ")

    # 查询快递信息
    result = query_yuantong_tracking_with_curl(tracking_number)

    # 打印格式化结果
    if isinstance(result, list):
        for entry in result:
            print(f"时间: {entry['time']}，描述: {entry['desc']}")
    else:
        print(result)
