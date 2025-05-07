import requests
from bs4 import BeautifulSoup
import re
import os
url="https://github.com/PX4/PX4-Autopilot/issues/19665"


def create_markdown_file(path, filename, content):
    # 检查路径是否存在，不存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    # 拼接完整文件路径
    file_path = os.path.join(path, filename + '.md')
    # 创建并写入文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Markdown file created and saved at: {file_path}")


def get_clean_content(parent_tag,target_class,header_class):
    final_text = ""
    # 遍历父标签的所有子元素并提取文本
    for element in parent_tag.children:
        if element.name and ' '.join(element.get('class', [])) == target_class:
            # 处理 class 为 'Box Box--condensed my-2' 的 div

            box_text = ""

            # 查找Box-header f6的div并处理其文本
            for child in element.find_all('div', class_=header_class):
                box_text += f'/*{child.get_text(strip=True)}*/'

            # 获取该Box下除去Box-header f6部分的文本
            other_text = element.get_text(separator=' ', strip=True)
            other_text = re.sub(r'\s+', ' ', other_text)
            # 移除已处理的 Box-header f6 的文本，避免重复
            for child in element.find_all('div', class_=header_class):
                header_text = child.get_text(strip=False)
                header_text= re.sub(r'\s+', ' ', header_text)
                other_text= re.sub(r'\s+', ' ', other_text)
                other_text = other_text.replace(header_text[1:], '')
            # 将剩余文本添加到结果中
            box_text += other_text.strip()

            # 将完整的 Box 内容包裹在 ```
            final_text += f'\n```cpp \n {box_text}\n```'
        elif element.name == 'pre' and ' '.join(element.get('class', [])) == 'notranslate':
            box_text=get_clean_content(element,target_class,header_class)
            final_text += f'\n```bash \n {box_text}\n```'
        elif element.name == 'ol' or element.name == 'ul':
            # 处理 ol 或 ul 列表中的 li 元素
            for i, li in enumerate(element.find_all('li', recursive=False)):
                if element.name == 'ol':
                    # 对于 ol 列表，使用数字标号
                    list_counter = i + 1
                    if(element.get('start')!=None):
                        list_counter+=(int(element.get('start'))-1)
                    final_text += f'{list_counter}.'+get_clean_content(li,target_class,header_class)+'\n'
                elif element.name == 'ul':
                    # 对于 ul 列表，使用符号标号
                    final_text += f'- '+get_clean_content(li,target_class,header_class)+'\n'
        elif element.name=='li':
            break
        elif element.name is None:
            # 如果是纯文本节点，直接添加
            final_text += element
        else:
            # 处理除 'Box Box--condensed my-2' 外的其他元素
            final_text += get_clean_content(element,target_class,header_class)

    # 处理文本：将#替换为\#，将连续空格替换为一个空格
    final_text = re.sub(r'#', r'\#', final_text)  # 替换#为\#
    final_text = re.sub(r'\n+', '  \n', final_text)  # 替换多个连续换行为一个<br>
    return final_text

def get_md_of_url(url):
    #使用requests库获取HTML内容
    response = requests.get(url)
    response.raise_for_status()  # 如果请求失败，会抛出异常
    html_content = response.text
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    result="# Basic Information:"

    # 查找title
    # 查找第一个class为指定值的h1标签
    class_name = 'gh-header-title mb-2 lh-condensed f1 mr-0 flex-auto wb-break-word'  # 替换为你想要的class值
    title_tag = soup.find('h1', class_=class_name)
    if title_tag:
        result+="\n### Title: "+title_tag.text.replace('\n',' ')
    else:
        print('title ERROR')

    #查找issue status
    class_name='State State--merged d-flex flex-items-center'
    status_tag=soup.find('span',class_=class_name)
    if status_tag:
        result+="\n### Issue status: "+status_tag.text.replace('\n',' ').replace(' ','')
    else:
        print('status ERROR')

    # 查找author+issue open time+fixed by
    class_name='author text-bold Link--secondary'
    author_tag= soup.find('a',class_=class_name)
    relative_time_tag=author_tag.find_next_sibling('relative-time')
    fixed_by_tag=relative_time_tag.find_next_sibling('span').find('a')
    if author_tag:
        result+="\n### Author: "+author_tag.text.replace('\n',' ')
    else:
        print('Author ERROR')
    if relative_time_tag:
        result+='\n### Issue open time: '+relative_time_tag.text.replace('\n',' ')
    else:
        print('open time ERROR')
    if fixed_by_tag:
        result+='\n### Fixed by: '+fixed_by_tag.text.replace('\n',' ')

    class_name = 'gh-header-title mb-2 lh-condensed f1 mr-0 flex-auto wb-break-word'  # 替换为你想要的class值
    a_tag = soup.find_next('a', class_='author Link--primary text-bold css-overflow-wrap-anywhere ')


    # 查找report部分所有内容
    result+="\n# Report"
    whole_block_tag=soup.find('div',class_='js-discussion ml-0 pl-0 ml-md-6 pl-md-3')
    report_tag=soup.find('div',class_='ml-n3 timeline-comment unminimized-comment comment previewable-edit js-task-list-container js-comment timeline-comment--caret')
    report_author_tag=report_tag.find('a',class_='author Link--primary text-bold css-overflow-wrap-anywhere')
    report_time_tag=report_tag.parent.find('relative-time')
    report_content_tag=report_tag.find('td',class_='d-block comment-body markdown-body js-comment-body')
    if report_author_tag:
        result+="\n### Report author: "+report_author_tag.text.replace('\n',' ')
    else:
        print('Report author ERROR')
    if report_time_tag:
        result+="\n### Report Time: "+report_time_tag.text.replace('\n',' ')
    else:
        print('Report Time ERROR')
    if report_content_tag:
        result+="\n### Report Content: "+get_clean_content(report_content_tag,'Box Box--condensed my-2','Box-header f6')
    else:
        print('Report Content ERROR')

    #查找comment部分所有内容
    result+="\n# Comment"
    comment_list=whole_block_tag.find_all('div',class_='ml-n3 timeline-comment unminimized-comment comment previewable-edit js-task-list-container js-comment timeline-comment--caret')
    for i in range(1,len(comment_list)):
        result += "\n## Comment" + str(i)
        comment_author_tag=comment_list[i].find('a',class_='author Link--primary text-bold css-overflow-wrap-anywhere')
        comment_time_tag=comment_author_tag.parent.parent.find('relative-time')
        comment_content_tag=comment_list[i].find('td',class_='d-block comment-body markdown-body js-comment-body')
        if comment_author_tag:
            result += "\n### Comment author: " + comment_author_tag.text.replace('\n', ' ')
        else:
            print('Comment author'+str(i)+'ERROR')
        if comment_time_tag:
            result += "\n### Comment Time: " + comment_time_tag.text.replace('\n', ' ')
        else:
            print('Comment time'+str(i)+'ERROR')
        if comment_content_tag:
            result+="\n### Comment Content: "+get_clean_content(comment_content_tag,'Box Box--condensed my-2','Box-header f6')
        else:
            print('Comment content'+str(i)+'ERROR')
    return result

startnum=91
path='./markdown/new'
urls=[21686, 21674, 21672, 21654, 21650, 21625, 21607, 21601, 21600, 21588, 21575, 21544, 21518, 21496, 21494, 21481, 21471, 21441, 21430, 21401, 21393, 21370, 21327, 21278, 21242, 21184, 21167, 21102, 21072, 21062, 21043, 20900, 20881, 20834, 20820, 20783, 20765, 20762, 20743, 20731, 20708, 20693, 20677, 20668, 20634, 20609, 20555, 20519, 20503, 20465, 20410, 20395, 20345, 20334, 20311, 20211, 20159, 20158, 20134, 20130, 20126, 20091, 19998, 19969, 19917, 19901, 19890, 19859, 19853, 19852, 19831, 19797, 19788, 19770, 19760, 19756, 18595, 18271, 18082, 17911, 17442, 17417, 16601, 16445, 16235, 16057, 15612, 15595, 15527, 15466, 15069, 15065, 14909, 14904, 14888, 14838, 14659, 14274, 14251, 14243, 14232, 14223, 14161, 14133, 13962, 13952, 13892, 13856, 13793, 13754, 13731, 13682, 13675, 13654, 13508, 13467, 13231, 13147, 13087, 13030, 13010, 13001, 12900, 12855, 12626, 12471, 12338, 12307, 12251, 12241, 12201, 11875, 11751, 11452, 11220, 10775, 10678, 10627, 10489, 10296, 10099, 9716, 9200]
for i in range(startnum,len(urls)):
    text=get_md_of_url("https://github.com/PX4/PX4-Autopilot/issues/"+str(urls[i]))
    if text=='':
        print('ERROR in issue '+str(urls[i]))
    else:
        create_markdown_file(path,"issue"+str(urls[i]),text)
    print("Now No."+str(i)+" is done!")