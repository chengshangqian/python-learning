# 作者：成尚谦
# 日期：2021年11月6日
# 功能描述：将命令行中输入json数据的以约定的分割符号split_symbol分割key后合并为json字符串
import sys
import json

# 分割标识符号
split_symbol = "-"


# 处理命令行输出的参数
def handler(input_params: dict):
    json_nodes = parse_to_json_nodes(input_params)
    root_level = 1
    root_parent_path = ""
    json_string = merge_to_json_string(json_nodes, root_level, root_parent_path)
    print({"data": {"output": json_string}})


# 初始化为json节点：按照路径作为节点在字典中的key
def parse_to_json_nodes(input_params: dict):
    json_nodes = {}
    for path, value in input_params.items():
        keys = path.split(split_symbol)
        length = len(keys)
        node_path = ""
        for i in range(0, length):
            level = i + 1
            level_nodes_key = "level_" + str(level) + "_nodes"
            level_nodes = {}
            if level_nodes_key in json_nodes:
                level_nodes = json_nodes[level_nodes_key]
            else:
                json_nodes[level_nodes_key] = level_nodes
            node_key = keys[i]
            if level == 1:
                node_path = node_key
            else:
                node_path += split_symbol + node_key
            node_value = {}
            if level == length:
                node_value = value
            node = {"path": node_path, "key": node_key, "value": node_value}
            level_nodes[node_path] = node
    return json_nodes


# 查找指定层级和父路径的json节点集合
def filter_json_nodes(json_nodes: dict, level: int, parent_path: str):
    level_nodes = json_nodes["level_" + str(level) + "_nodes"]
    nodes = {}
    for path, node in level_nodes.items():
        if level == 1 and path == node["key"]:
            nodes[path] = node
        elif path.startswith(parent_path + split_symbol):
            nodes[path] = node
    return nodes


# 将指定层级和父路径的json节点集合合并为json字符串
def merge_to_json_string(json_nodes: dict, level: int, parent_path: str):
    current_level_nodes = filter_json_nodes(json_nodes, level, parent_path)
    json_string = "{"
    count = 0
    for path, node in current_level_nodes.items():
        if count > 0:
            json_string += ", "
        json_string += "\"" + node["key"] + "\": "
        value = node["value"]
        value_type = type(value)
        if dict == value_type:
            child_level = level + 1
            json_string += merge_to_json_string(json_nodes, child_level, path)
        else:
            json_string += parse_to_string_value(value)
        count += 1
    json_string += "}"
    return json_string


# 将json值初始化为字符类型值
def parse_to_string_value(value):
    value_type = type(value)
    if int == value_type or float == value_type:
        return str(value)
    elif bool == value_type:
        return str(value).lower()
    else:
        return "\"" + str(value) + "\""


if __name__ == '__main__':
    try:
        # idea中增加命令参数进行测试：
        # {\"user-name-first.Name\":\"Cheng\",\"user-name-last.Name\":\"Shangqian\",\"user-age\":32,\"marry\":true}
        # 本地测试输入
        # input_data = {"user-name-first.Name":"Cheng","user-name-last.Name":"Shangqian","user-age":32,"account":"1007919"}
        # 异常测试 result = 1 / 0
        input_data = json.loads(sys.argv[1])
        handler(input_data)
    except Exception as err:
        print({"data": {"error_msg": str(err)}})
        raise err
