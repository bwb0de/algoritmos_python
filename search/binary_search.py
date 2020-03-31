#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# license: AGPL-3.0 
#
# Código extraído do módulo 'cli_tools', repositório python_modules
#

def return_bisect_lists(input_list):
	"""Divide uma lista e retorna uma tupla com o termo central e as metades direita e esquerda
	
	Arguments:
		input_list {list} -- lista a ser dividida
	
	Returns:
		{tuple} -- tupla contendo (fatia_esquerda, termo_central, fatia_direita)
		{string|int|float} -- se a lista for unitária retorna o elemento
		{NoneType} -- retorna None se a lista de entrada for vazia
	"""

	assert isinstance(input_list, list)

	input_size = len(input_list) 
	
	if input_size == 1:	return input_list[0]
	elif input_size == 0: return None

	left_side = input_list[:input_size//2]
	middle_element = input_list[input_size//2]
	right_side = input_list[(input_size//2)+1:]

	return left_side, middle_element, right_side



def bisect_search(search_value, input_list):
	"""Realiza pesquisa binária na lista de entrada e retorna True se o elemento existir
	
	Arguments:
		search_value {string|int|float} -- item a ser pesquisado
		input_list {list} -- a lista de entrada precisa conter elementos de um mesmo tipo
	
	Returns:
		{bool} -- retorna True se existir, False se não
	"""

	assert isinstance(search_value, (str, int, float))
	assert isinstance(input_list, list)

	input_size = len(input_list) 

	if input_list == []:
		return False
	elif input_size == 1:
		middle_element = return_bisect_lists(input_list)
		if search_value == middle_element: return True
		else:return False
	else:
		left_side, middle_element, right_side = return_bisect_lists(input_list)
		try:
			if search_value == middle_element: return True
			elif search_value < middle_element: return bisect_search(search_value, left_side)
			else: return bisect_search(search_value, right_side)	
		except TypeError:
			return False


def return_bisect_lists_idx(input_list, slice_ref, current_mid_idx=0):
	"""Retorna uma tupla com os índices de referencia para dividi-lá em termo central, fatias direita e esquerda
	
	Arguments:
		input_list {list} -- lista de entrada
		slice_ref {tuple} -- tupla contendo o index de início e fim da fatia
	
	Keyword Arguments:
		current_mid_idx {int} -- valor do índice para o termo do meio (default: {0})
	
	Returns:
		{tuple} -- retorna uma tupla com os indices da fatia esquerda, termo dentral e fatia direita
		{int} -- retorna um inteiro quando a lista é unitária
		{NoneType} -- retorna None se a lista estiver vazia
	"""

	assert isinstance(input_list, list)
	assert isinstance(slice_ref, (list, tuple))
	assert isinstance(current_mid_idx, int)
	
	init_idx, end_idx = slice_ref
	sliced_list = input_list[init_idx:end_idx]
	new_mid_idx = (init_idx + end_idx)//2 

	input_size = len(sliced_list) 
	
	if input_size == 1:	return new_mid_idx 
	elif input_size == 0: return None

	new_mid_idx = (init_idx + end_idx)//2 
	left_side_slice_idx = (init_idx, new_mid_idx)
	right_side_slice_idx = ((new_mid_idx)+1, end_idx) 

	return left_side_slice_idx, new_mid_idx, right_side_slice_idx



def bisect_search_idx(search_value, input_list, slice_ref, current_mid_idx=0):
	"""Retorna a posição do elemento pesquisado na lista fornecida, se não existir, retorna Falso
	
	Arguments:
		search_value {int|str|float} -- termo/elemento a ser pesquisado
		input_list {list} -- a lista de entrada precisa conter elementos de um mesmo tipo
		slice_ref {tuple} -- tupla contendo os indices de referência inicial e final da fatia
	
	Keyword Arguments:
		current_mid_idx {int} -- posição do termo central (default: {0})
	
	Returns:
		{int} -- retorna a posição do elemento na lista, se ele existir
		{bool} -- retorna False se o elemento não existir
	"""

	assert isinstance(search_value, (str, int, float)), "O argumento 'search_value' pode ser do tipo string, inteiro ou float"
	assert isinstance(input_list, list), "O argumento 'input_list' deve ser do tipo lista"
	assert isinstance(slice_ref, (tuple, list)), "O argumento 'slice_ref', deve ser uma tupla ou lista"
	assert isinstance(current_mid_idx, int), "O argumento 'current_mid_idx' deve ser um número inteiro"

	init_idx, end_idx = slice_ref
	sliced_list = input_list[init_idx:end_idx]
	sliced_list_size = len(sliced_list)

	if sliced_list == []:
		return False
	elif sliced_list_size == 1:
		new_mid_idx = return_bisect_lists_idx(input_list, slice_ref=slice_ref, current_mid_idx=current_mid_idx)
		if search_value == input_list[new_mid_idx]: return new_mid_idx
		else: return False
	else:
		left_side_slice_idx, new_mid_idx, right_side_slice_idx = return_bisect_lists_idx(input_list, slice_ref, current_mid_idx)
		try:
			if search_value == input_list[new_mid_idx]: 
				return new_mid_idx
			elif search_value < input_list[new_mid_idx]:
				return bisect_search_idx(search_value, input_list, slice_ref=left_side_slice_idx, current_mid_idx=new_mid_idx)
			else:
				return bisect_search_idx(search_value, input_list, slice_ref=right_side_slice_idx, current_mid_idx=new_mid_idx)	
		except TypeError:
			return False