filename = './neko.txt.mecab'

sentences = []
morphs = []
with open(filename, encoding="utf-8",mode='r') as f:
  for line in f:  # 1行ずつ読込
    if line != 'EOS\n':  # 文末以外：形態素解析情報を辞書型に格納して形態素リストに追加
      fields = line.split('\t') #list
      if len(fields) != 2 or fields[0] == '':  # 文頭以外の空白と改行文字はスキップ
        continue
      else:
        attr =  fields[1].split(',')
        morph = {'surface': fields[0], 'base': attr[6], 'pos': attr[0], 'pos1': attr[1]}
        morphs.append(morph)
    else:  # 文末が来た時に形態素リストを文リストに追加（1文追加する）
      sentences.append(morphs)
      morphs = []


ans=set()
for sentence in sentences:
    for morph in sentence:
        if morph['pos']=='動詞':
            ans.add(morph['base'])

print(f'動詞の表層系の種類：{len(ans)}\n')
print('---sample---')
for v in list(ans)[:10]:
    print(v)

