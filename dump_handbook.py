from typing import Union, List
from pathlib import Path
from os import PathLike
import json


DIR = Path(__file__).parent
TEXTMAP = DIR / 'TextMap'
EXCELBINOUTPUT = DIR / 'ExcelBinOutput'
LANGS = [i.name[7:-5] for i in TEXTMAP.iterdir()]
PROPS = [
	{
		"Name": 4022780027,  # Characters in TextMap
		"filename": "AvatarExcelConfigData.json"
	},
	{
		"Name": 3514848586,  # Weapons in TextMap
		"filename": "WeaponExcelConfigData.json"
	},
	{
		"Name": 626562562,  # Materials in TextMap
		"filename": "MaterialExcelConfigData.json"
	},
	{
		"Name": 2338513143,  # Artifacts Name in TextMap
		"filename": "ReliquaryExcelConfigData.json"
	},
	{
	    "Name": 1897268740,  # Living beings in TextMap
	    "filename": "AnimalDescribeExcelConfigData.json"
	},
	{
		"Name": "Artifact Main Attribution",
		"filename": "ReliquaryMainPropExcelConfigData.json"
	},
	{
		"Name": "Artifact Sub Attribution",
		"filename": "ReliquaryAffixExcelConfigData.json"
	},
	{
		"Name": 3775892005,
		"type": "mobs",
		"filename": "MonsterExcelConfigData.json"
	},
	{
		"Name": "Scene",
		"filename": "DungeonExcelConfigData.json"
	},
	{
		"Name": "NPC",  # NPCs in TextMap,
		"filename": "NpcExcelConfigData.json"
	}
]
ATTR2TXT_MAPPING = {
	'FIGHT_PROP_HP': 2404061249,
	'FIGHT_PROP_ATTACK': 1756301290,
	'FIGHT_PROP_DEFENSE': 1575853882,
	'FIGHT_PROP_SUB_HURT': 3892469682,
	'FIGHT_PROP_HEAL_ADD': 3911103831,
	'FIGHT_PROP_CRITICAL': 1916797986,
	'FIGHT_PROP_ADD_HURT': 2920451417,
	'FIGHT_PROP_HP_PERCENT': 2756497090,
	'FIGHT_PROP_HEALED_ADD': 3392845215,
	'FIGHT_PROP_ICE_SUB_HURT': 2221516638,
	'FIGHT_PROP_ICE_ADD_HURT': 4054347456,
	'FIGHT_PROP_WIND_ADD_HURT': 312842903,
	'FIGHT_PROP_ROCK_SUB_HURT': 3363551926,
	'FIGHT_PROP_ELEC_SUB_HURT': 1580778495,
	'FIGHT_PROP_CRITICAL_HURT': 4137936461,
	'FIGHT_PROP_SPEED_PERCENT': 3552803520,
	'FIGHT_PROP_WIND_SUB_HURT': 675300986,
	'FIGHT_PROP_ROCK_ADD_HURT': 2557985416,
	'FIGHT_PROP_ELEC_ADD_HURT': 3514877774,
	'FIGHT_PROP_FIRE_SUB_HURT': 570007818,
	'FIGHT_PROP_FIRE_ADD_HURT': 999734248,
	'FIGHT_PROP_ATTACK_PERCENT': 2796372974,
	'FIGHT_PROP_GRASS_SUB_HURT': 2809766539,
	'FIGHT_PROP_GRASS_ADD_HURT': 1824382851,
	'FIGHT_PROP_WATER_ADD_HURT': 3619239513,
	'FIGHT_PROP_WATER_SUB_HURT': 1406081734,
	'FIGHT_PROP_DEFENSE_PERCENT': 3076885710,
	'FIGHT_PROP_ELEMENT_MASTERY': 2326066533,
	'FIGHT_PROP_PHYSICAL_ADD_HURT': 3763864883,
	'FIGHT_PROP_PHYSICAL_SUB_HURT': 2073208032,
	'FIGHT_PROP_CHARGE_EFFICIENCY': 1735465728,
	'FIGHT_PROP_SKILL_CD_MINUS_RATIO': 1083556685,
	'FIGHT_PROP_SHIELD_COST_MINUS_RATIO': 195785769
}


def write_json(data: dict, fp: Union[Path, PathLike], mode: str = 'w+', encoding: str = 'utf-8', indent: int = 4, ensure_ascii: bool = False):
	with open(fp, mode=mode, encoding=encoding) as f:
		json.dump(data, fp, indent=indent, ensure_ascii=ensure_ascii)


def read_json(fp: Union[Path, PathLike], mode: str = 'r', encoding: str = 'utf-8') -> Union[dict, list]:
	with open(fp, mode=mode, encoding=encoding) as f:
		return json.load(f)


class TextMap:
	def __init__(self, fp: Union[Path, PathLike], encoding: str = 'utf-8'):
		with open(fp, encoding=encoding) as textmap_file:
			self.textmap = json.load(textmap_file)
		self.keys = self.textmap.keys()
	
	def id2text(self, id_: Union[str, int]) -> str:
		if isinstance(id_, str):
			if id_.isdigit():
				id_ = id_
			id_ = None
		else:
			id_ = str(id_)
		return self.textmap.get(id_) if id_ in self.keys else None


def artattr_chk(artattr: dict) -> bool:
	for i in artattr:
		if i in 'PropDepotId/PropType/AffixName/DepotId/PropValue/UpgradeWeight'.split('/'):
			return True
	return False


def formatter(title: Union[int, str], format_data: List[dict], textmap: TextMap, skip_none: bool = True) -> str:
	global mobs_desc
	if isinstance(title, int):
		title = textmap.id2text(title)
	lines = []
	for data_ in format_data:
		if "MonsterName" in data_:  # Mobs
			if not (mobs_desc:=None):
				mobs_desc = {
					j["Id"]: j["NameTextMapHash"]
					for j in read_json(EXCELBINOUTPUT / 'MonsterDescribeExcelConfigData.json')
				}
			if "DescribeId" not in data_:
				continue
			text = textmap.id2text(mobs_desc.get(data_["DescribeId"]))
		elif artattr_chk(data_):  # Artifacts
			if "PropType" not in data_:
				continue
			proptype = data_["PropType"]
			if "PropValue" in data_:
				if proptype.endswith(('PERCENT', 'EFFICIENCY', 'HURT', 'CRITICAL', 'RATIO')) or 'HEAL' in proptype:
					value = str(round(data_.get('PropValue') * 100, ndigits=1)) + '%'
				else:
					value = round(data_.get('PropValue'))
			else:
				value = ''
			attr = textmap.id2text(ATTR2TXT_MAPPING.get(proptype))
			attr = attr if attr else ""
			text = (attr + f'+{value}') if value != '' else attr
		else:
			text = textmap.id2text(data_["NameTextMapHash"])
		if skip_none and text in [None, '+', '']:
			continue
		
		id_ = data_.get('SceneId')  if "SceneId" in data_ else data_.get('Id') 
		lines.append(f'{id_}: {text}')
	return f'=== {title} ===\n' + \
		'\n'.join(lines) + '\n' +'#' * 20
	

if __name__ == '__main__':
	from argparse import ArgumentParser
	from time import strftime
	
	PROPS_DATA = [
		{
			"Name": i.get("Name"),
			"data": read_json(EXCELBINOUTPUT / i.get('filename'))
		}
		for i in PROPS
	]
	parser = ArgumentParser(description="Genshin Impact PS™ Handbook Generator")
	parser.add_argument(
		'--lang', '-L', dest='lang', 
		action='append', default=['all'], 
		help='Languages in the list: all / ' + ' / '.join(LANGS)
	)
	parser.add_argument(
		'--skip-none', '-S', dest='skip',
		action='store', default=True,
		help='Whether to skip ID with empty name'
	)
	args = parser.parse_args()

	for l in args.lang:
		if l == 'all':
			continue
		if l not in LANGS:
			print(f'Invalid Language Code: {l}')
			exit()
	task_lang = []
	task_lang = LANGS if 'all' in args.lang else args.lang
	
	for lang in task_lang:
		print(f'[{lang}] Opening TextMap[{lang}] ...')
		tm = TextMap(TEXTMAP / f'TextMap{lang}.json')
		print(f'[{lang}] Formatting Lines ...')
		categories = [
			formatter(
				title=p.get("Name"),
				format_data=p.get('data'),
				textmap=tm,
				skip_none=args.skip
			) 
			for p in PROPS_DATA
		]
		print(f'[{lang}] Writting HandBook ...')
		with open(DIR / f'Handbook_{lang}.txt', 'w+', encoding='utf-8') as handbook:
			handbook.write(
			    '==> Genshin Impact PS™ Handbook <==\nGenerated in ' + strftime("%Y-%m-%d %H:%M:%S") + '\n\n' + \
			    'You can search === for categories' + '\n\n')
			handbook.write('\n\n'.join(categories))
		
	print('These handbook were generated successfully:' + ' '.join(args.lang))
	