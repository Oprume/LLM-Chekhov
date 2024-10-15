import re
from collections import Counter

CUT_NOTES = 10
VOCAB = set()

dash = '¬ '
russian_letter = r'[а-яА-ЯёЁ]'
counter = Counter()

def clear_text(texts: list[str] ) -> str:
     # Remove '¬ ' '\n\n', cutting unrelevant text
     text = ''.join(texts[CUT_NOTES:])
     assert len(re.findall('ПРИМЕЧАНИЯ', text)) == 1
     pos = text.find('ПРИМЕЧАНИЯ')
     text = text[:pos]
    # print(f'Removed {len_text - pos} notes symbols')
     return text.replace('\n\n', ' ').replace(dash, '')
     
#Remove least n frequency symbols
def rm_least_symbols(texts = list[str], n=80) -> list[str]:
     least_common = counter.most_common()[:-n-1:-1]
     total_size = sum([i[1] for i in least_common])
     print(f'Removing total {total_size} symbols')
     least_syms = [sym[0] for sym in least_common if not re.search(russian_letter, sym[0])]
     least_syms.append('■')

     VOCAB.update(counter.keys()) #create vocab
     VOCAB.difference_update(least_syms)
     for i, text in enumerate(texts):
          for sym in least_syms:
               text = text.replace(sym, '')
          texts[i] = text

     #print(len(least_common) - len(least_syms))
     return texts


def main():
     print('Starting cleaning text')
     texts = []
     for i in range(1, 9):
          file = f'tom_{i}.txt'
          with open('raw_toms/' + file , encoding='utf-8') as f:
               text = f.readlines()
          text = clear_text(text)
          texts.append(text)
          counter.update(text)

     new_texts = rm_least_symbols(texts)
     for i in range(1, 9):
          file = f'tom_train{i}.txt'
          with open('toms/' + file, mode='w', encoding='utf-8') as f :
              f.write(new_texts[i - 1])
          print(f'File {file} is done' )
     

def unique_symbols(file='toms/tom_train3.txt', n=40):
     #TODO Удалить малоиспользуемые символы или заменить на unknown token
     with open(file, encoding='utf-8') as f:
          text = f.read()
     symbols = set(text)
     c = Counter(text)
     print(c)
     least_common = dict(c.most_common()[:-n-1:-1])
     print(least_common)
     syms = [sym for sym in least_common.keys()]
     freqs = [sym for sym in least_common.values()]
     freq_alpha = [n.isalpha() for n in syms]

     for i in range(n):               
          sym = syms[i]
          match = True if re.search(russian_letter, sym) else False
          freq = freqs[i]
          pos = text.find(sym)
          if i == 8:
               print(repr(text[pos-10: pos+10]))
          print(i, pos, '\t', text[pos-10: pos+10].strip(), '\t', sym, freq, freq_alpha[i], match)


if __name__ == '__main__':

     main()
    # unique_symbols()

