import openai
import time

def use_openai_api(words,api_key):
    openai.api_key = api_key
    # openai.base_url = url
    openai.base_url = 'https://api.nbchat.site/v1/'
    response = openai.chat.completions.create(
        model="gpt-4o",  # 确认使用 GPT-4o 模型
        messages=[
            {"role": "user", "content": words}
        ]
    )
    #print(response)
    return response

def total_counts(tokens_in_now,tokens_out_now,cost_now,response):
    #print(response)
    tokens_in_now=int(response.usage.prompt_tokens)
    tokens_out_now=int(response.usage.completion_tokens)
    price_in=0.01/1000
    price_out=0.03/1000
    cost_now+=(price_in*tokens_in_now+price_out*tokens_out_now)
    current_time = time.strftime('%Y年%m月%d日%H点%M分', time.localtime())
    print(f'当前时刻为{current_time},本次任务共消耗了：输入{tokens_in_now}个token，输出{tokens_out_now}个token，当前总计{cost_now}美元')
    with open("token_and_cost.txt","a",encoding='utf-8') as f:
        f.write(f'当前时刻为{current_time},本次任务共消耗了：输入{tokens_in_now}个token，输出{tokens_out_now}个token，当前总计{cost_now}美元'+'\n'*2)
    f.close()

def save_answer(response,save_path):
    answer=response.choices[0].message.content
    with open(save_path,'a',encoding='utf-8') as f:
        f.write(answer)
        f.write('\n')
    f.close()

def read_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

tokens_in_now=0
tokens_out_now=0
cost_now=0

path='./markdown/new/issue'
# urls=[21634, 20826, 20793, 20477, 20374,
#       20260, 19667, 19665, 19348, 19233,
#       19155, 19134, 18750, 18576, 18574,
#       18573, 18385, 18306, 18060, 18014,#20
#       17831, 17769, 17746, 17380, 17323,
#       17244, 17237, 17220, 17192, 17006,
#       16843, 16813, 16715, 16670, 16586,
#       16390, 16305, 16299, 16278, 16230,#40
#       16129, 16122, 16113, 15922, 15826,
#       15667, 15628, 15501, 15417, 15410,
#       15409, 15408, 15347, 15211, 15042,
#       15037, 14947, 14903, 14840, 14824,#60
#       14802, 14736, 14730, 14718, 14717,
#       14671, 14670, 14649, 14612, 14600,
#       14588, 14579, 14566, 14527, 14479,
#       14456, 14442, 14440, 14439, 14354,#80
#       14303, 14300, 14281, 14260, 14206,
#       14200, 14189, 14157, 14150, 14101,
#       14075, 14011, 13956, 13946, 13752,
#       13751, 13732, 13724, 13688, 13533,#100
#       13471, 13455, 13415, 13377, 13374,
#       13329, 13313, 13309, 13292, 13280,
#       13244, 13180, 13148, 13116, 13055,
#       13012, 12980, 12955, 12932, 12919,#120
#       12879, 12833, 12813, 12761, 12758,
#       12692, 12637, 12517, 12240, 12221,
#       12193, 12190, 12171, 12071, 12029,
#       12006, 11945, 11942, 11929, 11901,#140
#       11899, 11880, 11860, 11847, 11832,
#       11794, 11778, 11750, 11716, 11685,
#       11646, 11551, 11492, 11433, 11408,
#       11386, 11364, 11282, 11238, 11226,#160
#       11198, 11118, 11110, 11006, 10999,
#       10972, 10767, 10693, 10686, 10655,
#       10593, 10571, 10471, 10457, 10412,
#       10092, 9867, 9841, 9768, 9554,#180
#       9513, 9025, 8828, 8303, 8255,
#       7755, 7746, 7457, 7051, 6783,
#       6669, 6282, 6184, 6172, 5887,
#       5465, 5317, 3795, 3117, 500]#200

urls=[21686, 21674, 21672, 21654, 21650, 21625, 21607, 21601, 21600, 21588, 21575, 21544, 21518, 21496, 21494, 21481, 21471, 21441, 21430, 21401, 21393, 21370, 21327, 21278, 21242, 21184, 21167, 21102, 21072, 21062, 21043, 20900, 20881, 20834, 20820, 20783, 20765, 20762, 20743, 20731, 20708, 20693, 20677, 20668, 20634, 20609, 20555, 20519, 20503, 20465, 20410, 20395, 20345, 20334, 20311, 20211, 20159, 20158, 20134, 20130, 20126, 20091, 19998, 19969, 19917, 19901, 19890, 19859, 19853, 19852, 19831, 19797, 19788, 19770, 19760, 19756, 18595, 18271, 18082, 17911, 17442, 17417, 16601, 16445, 16235, 16057, 15612, 15595, 15527, 15466, 15069, 15065, 14909, 14904, 14888, 14838, 14659, 14274, 14251, 14243, 14232, 14223, 14161, 14133, 13962, 13952, 13892, 13856, 13793, 13754, 13731, 13682, 13675, 13654, 13508, 13467, 13231, 13147, 13087, 13030, 13010, 13001, 12900, 12855, 12626, 12471, 12338, 12307, 12251, 12241, 12201, 11875, 11751, 11452, 11220, 10775, 10678, 10627, 10489, 10296, 10099, 9716, 9200]

startnum=0
example_content=read_document('./markdown/issue15628.md')
example_output=read_document('./issue15628.md')
api_key=""
for i in range(startnum,len(urls)):
    doc_content=read_document(path+str(urls[i])+'.md')
    words = f"""
    This is a markdown document about bug reports in the open-source flight control system software PX4 Autopilot for drones:\n\n{doc_content}\n\n
    Be sure to extract the report time and commit version of PX4 AutoPilot from it. If the commit version of PX4 AutoPilot is not mentioned, please fill in the content 'not mentioned' here, and Extract the information of the following content in the following format:
    Environment where the bug occurred:
        Hardware environment:
        Software environment:
        Report time:
        PX4 Autopilot commit version:
    Steps for bug reproduction:
        Step 1:
        Step 2:
        ...
        Step n:
    Observed behavior by the user:
        Behavior after step 1:
        Behavior after step 2:
        ...
        Behavior after step n:
    Expected behavior:
        Expected behavior 1:
        Expected behavior 2:
        ...
        Expected behavior n:
    Additional information provided by the user for bug investigation:
        Actions taken by the user (if the user actively investigated the bug)
        URL of the flight log provided by the user
        ...
    Communication between developers or other personnel and the user:
        Suggestion 1 provided by developers or other personnel:
        Result of the operation after the user adopted suggestion 1:
        Suggestion 2 provided by developers or other personnel:
        Result of the operation after the user adopted suggestion 2:
        ...
        Suggestion n provided by developers or other personnel:
        Result of the operation after the user adopted suggestion n:
    \n\n 
    Here is an example for you:
    For document:\n\n{example_content}\n\n
    The output should be following:\n\n{example_output}\n\n
    """
    response=use_openai_api(words,api_key)
    answer=response.choices[0].message.content
    save_answer(response,'./new_answer/issue'+str(urls[i])+'.md')
    print('Issue'+str(urls[i])+'.md'+'done! This is No.'+str(i))
# #total_counts(tokens_in_now,tokens_out_now,cost_now,response)
# #save_answer(response)
# response=use_openai_api(words,api_key)
# answer=response.choices[0].message.content
# print(answer)