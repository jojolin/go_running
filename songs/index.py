# index playlist

import os
from os import path
import shutil
import hashlib
import json

from tinytag import TinyTag
import pdb


def index(root_path):
    index_map = {}
    files_list = []
    for root, dirs, files in os.walk(root_path):
        for dir in dirs:
            for root2, dirs2, files2 in os.walk(path.join(root, dir)):
                for fn in files2:
                    if not fn.endswith('mp3'):
                        continue
                    files_list.append((dir, root2, fn))
    print(f'total musics: {len(files_list)}')
    parsed_root_path = root_path + '_parsed'
    os.makedirs(parsed_root_path, exist_ok=True)
    print(f'create {parsed_root_path}')
    for diss_name, dir, fn in files_list:
        fp = path.join(dir, fn)
        tag = TinyTag.get(fp)
        new_dir = path.join(parsed_root_path, dir)
        os.makedirs(new_dir, exist_ok=True)
        print(f'create {new_dir}')
        md5 = hashlib.md5()
        md5.update("{}{}{}".format(tag.artist, tag.album, tag.title).encode())  # new id with md5(artist, album, title)
        song_id = md5.hexdigest()
        nfp = path.join(new_dir, song_id + '.' + fn.split('.')[1])
        shutil.copyfile(fp, nfp)  # copy to parsed dir
        print(f'copy file {fp} -> {nfp}')
        if diss_name not in index_map:
            index_map[diss_name] = {
                "id": diss_name,
                "category": "跑步",
                "title": diss_name,
                "picUrl": "",
                "rateRange": [0, 0],
                "kind": None,
                "songCount": 0,
                "songs": []
            }
        songs = index_map[diss_name]["songs"]
        singers = []
        # pdb.set_trace()
        for artist in tag.artist.split('&'):
            singers.append({"singerName": artist.strip(), "singerId": ""})
        songs.append({
            "resourcePath": nfp,
            "songId": song_id,
            "songName": tag.title,
            "singer": singers,
            "pic": "",
            "rateRange": [0, 0]
        })
    with open('index.json', 'w', encoding='utf8') as w:
        w.write(json.dumps(index_map, ensure_ascii=False))
    print('save index file to index.json')
    return index_map


def main():
    import sys
    (index(sys.argv[1]))


if __name__ == '__main__':
    main()

''' ref: diss
{
	"id": "123",
	"category": "跑步",
	"title": "Power walking on sunshine",
	"picUrl": "",
	"rateRange": [
		178,
		186
	],
	"kind": "likes",
	"songCount": 2,
	"songs": [
		{
			"songId": "12345",
			"songName": "Better Now",
			"singer": [
				{
					"singerName": "Calvin Harris",
					"singerId": ""
				},
				{
					"singerName": "Dua Lipa",
					"singerId": ""
				}
			],
			"pic": "",
			"rateRange": [
				178,
				186
			]
		},
		{
			"songId": "12534",
			"songName": "Kimberly Evans",
			"singer": [
				{
					"singerName": "Cardi B",
					"singerId": ""
				},
				{
					"singerName": "Bad bunny",
					"singerId": ""
				},
				{
					"singerName": "J Balvin",
					"singerId": ""
				}
			],
			"pic": "",
			"rateRange": [
				178,
				186
			]
		}
	]
}
'''
