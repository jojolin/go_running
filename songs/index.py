# index playlist

import os
from os import path
import shutil
import hashlib
import json

from tinytag import TinyTag
import pdb


def index(root_path):
    # pdb.set_trace()
    index_map = {}
    files_list = []
    for root, dirs, files in os.walk(root_path):
        for dir in dirs:
            for root2, dirs2, files2 in os.walk(path.join(root, dir)):
                for fn in files2:
                    rate = 0
                    if fn.endswith('png'):
                        files_list.append((dir, root2, fn, rate))
                    if fn.endswith('mp3'):
                        print(fn)
                        rate_string = ''.join(fn[fn.find('（') : fn.find('）')]).strip('（')
                        if not rate_string == '':
                            rate = int(rate_string)
                        files_list.append((dir, root2, fn, rate))
    print(f'total musics: {len(files_list)}')
    parsed_root_path = root_path + '_parsed'
    os.makedirs(parsed_root_path, exist_ok=True)
    print(f'create {parsed_root_path}')
    for diss_name, dir, fn, rate in files_list:
        fp = path.join(dir, fn)
        new_dir = path.join(parsed_root_path, dir)
        os.makedirs(new_dir, exist_ok=True)
        print(f'create {new_dir}')
        if fn.endswith('png'):
            nfp = path.join(new_dir, fn)
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
            index_map[diss_name]["picUrl"] = nfp
            continue

        tag = TinyTag.get(fp)
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
        for artist in tag.artist.split('&'):
            singers.append({"singerName": artist.strip(), "singerId": ""})
        # set song rateRage, with (-5, +5)
        rate_low, rate_high = rate - 5, rate + 5
        songs.append({
            "playUrl": nfp,
            "songId": song_id,
            "songName": tag.title,
            "singer": singers,
            "pic": "",
            "rateRange": [rate_low, rate_high]
        })
        index_map[diss_name]["songCount"] += 1
        # set diss rateRange
        if index_map[diss_name]["rateRange"][0] == 0 or \
                rate_low < index_map[diss_name]["rateRange"][0]:
            index_map[diss_name]["rateRange"][0] = rate_low
        if index_map[diss_name]["rateRange"][1] == 0 or \
                rate_high > index_map[diss_name]["rateRange"][1]:
            index_map[diss_name]["rateRange"][1] = rate_high

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
