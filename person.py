#!/usr/bin/env python3
# @File: person.py
# --coding:utf-8--
# @Author:Schopenhauerzhang@icloud.com(Schopenhauerzhang@gmail.com)
# @license:Copyright Schopenhauerzhang@icloud.com All rights Reserved.  
# @Time: 2019-09-23 15:00

from google.protobuf import json_format
from py_protobuf.protobuf import person_pb2

import json


def get_protobuf_data():
	"""
	生成protobuf data
	Returns:
		bytes-like object
	"""
	try:
		person = person_pb2.Person()
		person.id = 123
		person.name = "abc"
		p_res = person.SerializeToString()
	except Exception:
		print("get_protobuf_data error: fail, please check your code")
		raise Exception("get_protobuf_data error: fail, please check your code")
	return p_res


def protobuf2json_or_dict(is_json = True):
	"""
	将protobuf data转为json
	Args:
		is_json: bool ,True Returns json / False Returns dict

	Returns:
		dict/json string
	"""
	try:
		persons = person_pb2.Person()
		persons.ParseFromString(get_protobuf_data())
		
		if is_json is True:
			result = json_format.MessageToJson(persons)
			result = json.loads(result)
		else:
			result = json_format.MessageToJson(persons)
	except Exception:
		print("protobuf2json_or_dict error: fail, please check your code")
		raise Exception("protobuf2json_or_dict error: fail, please check your code")
	
	return result

def extension_cni(is_json = false):
	"""
	将protobuf data转为json,todo k8s cni plugins
	Args:
		is_json: bool ,True Returns json / False Returns dict

	Returns:
		dict/json string
	"""
	try:
		persons = person_pb2.Person()
		persons.ParseFromString(get_protobuf_data())
		
		if is_json is True:
			result = json_format.MessageToJson(persons)
			result = json.loads(result)
		else:
			result = json_format.MessageToJson(persons)
	except Exception:
		print("protobuf2json_or_dict error: fail, please check your code")
		raise Exception("protobuf2json_or_dict error: fail, please check your code")
	
	return result

def extension_k8s(is_json = false):
	"""
	将protobuf data转为json,todo k8s  plugins
	Args:
		is_json: bool ,True Returns json / False Returns dict

	Returns:
		dict/json string
	"""
	try:
		if is_json is True:
			result = json_format.MessageToJson(persons)
			result = json.loads(result)
		else:
			result = json_format.MessageToJson(persons)
	except Exception:
		raise Exception("protobuf2json_or_dict error: fail, please check your code")
	
	return result


def extension_client_go(is_json = false):
	"""
	将protobuf data转为json,todo k8s cni plugins
	Args:
		is_json: bool ,True Returns json / False Returns dict

	Returns:
		dict/json string
	"""
	try:
		if is_json is True:
			result = json_format.MessageToJson(persons)
			result = json.loads(result)
		else:
			result = json_format.MessageToJson(persons)
	except Exception:
		raise Exception("protobuf2json_or_dict error: fail, please check your code")
	
	return result

def extension_week(is_json = false):
	"""
	将protobuf data转为json,todo week plugins
	Args:
		is_json: bool ,True Returns json / False Returns dict

	Returns:
		dict/json string
	"""
	try:
		result = json_format.MessageToJson(persons)
	except Exception:
		raise Exception("protobuf2json_or_dict error: fail, please check your code")
	
	return result
	
