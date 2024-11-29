import yaml
import os
import sys

config_path = os.path.join(os.path.dirname(__file__), 'configs.yaml')

# 读取配置文件
try:
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
except FileNotFoundError:
    print(f"Error: The configuration file {config_path} does not exist.")
    sys.exit(1)
except yaml.YAMLError as e:
    print(f"Error parsing YAML file: {e}")
    sys.exit(1)

# 运营商常量
TELECOM = "telecom"  # 电信
CMCC = "cmcc"  # 移动
UNICOM = "unicom"  # 联通

# 获取配置
user_account = config['user_account']
operator = config['operator']
user_password = config['user_password']

# 验证运营商是否合法
valid_operators = [TELECOM, CMCC, UNICOM]
if operator not in valid_operators:
    print(f"Error: Invalid operator '{operator}'. Must be one of {valid_operators}.")
    sys.exit(1)

print("Configuration loaded successfully.")
