import time
import requests
from openpyxl import Workbook

# 招聘信息 API
liepin_url = 'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job'
# 用于预检的消息头
pre_headers = {
  'Access-Control-Request-Headers': 'content-type,x-client-type,x-fscp-bi-stat,x-fscp-fe-version,x-fscp-std-info,x-fscp-trace-id,x-fscp-version,x-requested-with,x-xsrf-token',
  'Access-Control-Request-Method': 'POST',
  'Host': 'apic.liepin.com',
  'Origin': 'https://www.liepin.com'
}
# 简化后的消息头
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
  # 约定请求体为 JSON 格式数据
  'Content-Type': 'application/json;charset=UTF-8;',
  # 应对猎聘网反爬机制
  'X-Client-Type': 'web',
  'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/"}',
  'X-Fscp-Fe-Version': '2d1b05d',
  'X-Fscp-Std-Info': '{"client_id": "40108"}',
  'X-Fscp-Trace-Id': '0dfb583c-b594-47f1-a378-279593aa7038',
  'X-Fscp-Version': '1.1',
  'X-Requested-With': 'XMLHttpRequest',
  'X-XSRF-TOKEN': 'HRS0v6agSYqtxqIlpbvx2g'
}
# 建立会话，保持与服务期间通信状态

# 获取数据
def get_data():
  # 用于保存招聘信息，初始状态下为空
  jobs = []
  # 重复 20 次，每次获取一页招聘信息
  for i in range(10):
    # 构造请求体，每次循环获取第 i+1 页数据
    payload = {
      "data": {
        "mainSearchPcConditionForm": {
          "city": "410",
          "dq": "410",
          "pubTime": "",
          "currentPage": i,
          "pageSize": 40,
          "key": "python",
          "suggestTag": "",
          "workYearCode": "",
          "compId": "",
          "compName": "",
          "compTag": "",
          "industry": "",
          "salary": "",
          "jobKind": "",
          "compScale": "",
          "compKind": "",
          "compStage": "",
          "eduLevel": "",
          "otherCity": ""

        }
      }
    }
    # 向 liepin_url 发送带 headers 消息头、payload 请求体的请求
    res = requests.post(liepin_url, headers=headers, json=payload)

    # 若响应异常，则打印响应状态码，跳出本次循环
    if res.status_code != 200:
      print(res.status_code)
      break
    # 若数据异常，则打印异常信息，跳出本次循环
    if res.json()['flag'] != 1:
      print(res.json()['msg'])
      break

    ans=res.json()

    # 能运行到这里，说明响应正常、数据正常，遍历每条招聘信息
    job_card_list = ans['data']['data']['jobCardList']
    for job_card in job_card_list:
      jobs.append([
        job_card['job']['title'],  # 职位名
        job_card['job']['dq'],  # 地区
        job_card['job']['salary'],  # 薪资范围
        calc_annual_salary(job_card['job']['salary']),  # 年薪
        #job_card['job']['requireEduLevel'],  # 学历要求
        #job_card['job']['requireWorkYears'],  # 经验要求
        job_card['comp']['compName'],  # 公司名
      ])
    # 爬取一页数据后暂停一秒，防止被封
    time.sleep(1)

  # 20 页数据处理结束，返回所有招聘信息
  return jobs


# 由薪资范围计算年薪
def calc_annual_salary(salary_str):
  # 若薪资面议，则将该职位年薪记录为“面议”
  if '面议' in salary_str:
    return '面议'
  # 否则计算年薪
  else:
    # 若指定发放多少个月薪水，即薪水范围形如：11k·15薪、11-20k·15薪
    if '薪' in salary_str:
      # 将薪资范围分割为「月薪范围」、「月数」两部分
      salary_range, salary_times_str = salary_str.split('k·')
      salary_times = int(salary_times_str.strip('薪'))  # 丢弃末尾「薪」字
    # 未指定发放多少个月薪水，即薪水范围形如：11k、11-20k
    else:
      salary_range = salary_str.strip('k')  # 丢弃末尾「k」字
      salary_times = 12  # 默认发放 12 个月薪水
    # 若薪资不固定，则计算平均值
    if '-' in salary_range:
      salary_min_str, salary_max_str = salary_range.split('-')  # 分割薪资范围
      salary_min = int(salary_min_str)  # 最低月薪
      salary_max = int(salary_max_str)  # 最高月薪
      salary = (salary_min + salary_max) / 2  # 平均月薪
    # 否则以给定月薪作为最终月薪
    else:
      salary = int(salary_range)
    # 返回年薪计算结果
    return salary * salary_times * 1000


# 存储数据
def save_data(jobs):
  count = 0  # 非面议岗位总数
  total = 0  # 非面议岗位年薪总和
  wb = Workbook()  # 新建工作簿
  sheet = wb.active  # 选择默认的工作表
  sheet.title = 'python职位信息'  # 给工作表重命名

  # 写入表头
  sheet.append(['职位名', '地区', '薪资范围', '年薪', '学历要求', '经验要求', '公司名'])
  # 遍历招聘信息
  for job in jobs:
    # 若该岗位薪资非面议
    if job[3] != '面议':
      count += 1  # 非面议岗位总数加 1
      total += job[3]  # 累计非面议岗位年薪
    # 将该岗位信息写入工作表
    sheet.append(job)

  # 打印平均年薪，并保留 2 位小数
  print('Python 相关职位平均年薪是 {} 元'.format(round(total / count, 2)))
  # 保存文件
  wb.save('猎聘职位信息表.xlsx')


# 调用 get_data() 函数爬取 20 页招聘信息
jobs = get_data()
# 保存数据，并打印平均年薪
save_data(jobs)