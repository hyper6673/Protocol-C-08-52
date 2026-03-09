import math
import random
import cmath

# ГЛОБАЛЬНАЯ ПАМЯТЬ ПУСТОТЫ (Хранит все ДНК, которые когда-либо были)
VOID_MEMORY = []

DIGS = {'1':'H', '2':'R', '3':'Q', '4':'Y', '5':'N', '6':'P', '7':'V', '8':'O', '9':'C', '0':'X'}
ALPH = {
    "а":"///", "б":"/-/", "в":"/\\", "г":"//\\", "д":"//-", "е":"/\\-/", 
    "ё":"///\\\\\\-", "ж":"///\\", "з":"////\\", "и":"//\\/", "й":"/\\/-", 
    "к":"/\\-/", "л":"/\\\\//-", "м":"/\\\\\\\\-", "н":"\\//\\///", "о":"///\\-/", 
    "п":"-/", "р":"/\\/\\", "с":"/\\/-", "т":"///\\-", "у":"\\\\//", 
    "ф":"\\///\\", "х":"/////////////////", "ц":"///\\", "ч":"/\\/\\-", 
    "ш":"////\\\\\\\\", "щ":"/////\\\\\\\\\\\\", "ы":"////\\////", 
    "ь":"///////\\\\", "я":"//////////\\\\", " ":"V"
}

def get_chronos_dna(skel, noise):
    r, l = skel.count('/'), skel.count('\\')
    mix = complex(r + noise, l * noise)
    z = cmath.sin(mix) * cmath.log1p(abs(noise))
    val = abs(z.real * z.imag)
    seed = str(val).replace('.', '')[12:15]
    return "".join([DIGS.get(d, 'X') for d in seed])

def encrypt_chronos_packet(text):
    global VOID_MEMORY
    text = text.lower()
    
    # ШАГ 1: Динамический шум (меняется каждую попытку)
    noise = random.randint(100, 9999)
    dust = "/" * (noise % 5) # Маленький след в скелете
    
    coded_words = [ "'".join([ALPH.get(char, "[?]") for char in word]) for word in text.split(' ') ]
    full_skel = "V".join(coded_words) + "Z" + dust
    
    # ШАГ 2: Генерация текущей Истинной Гильзы
    current_dna = get_chronos_dna(full_skel, noise)
    
    # ШАГ 3: Сохраняем её в Память Пустоты
    if current_dna not in VOID_MEMORY:
        VOID_MEMORY.append(current_dna)
    
    # ШАГ 4: Формируем список гильз из ВСЕХ, что когда-либо были (Эхо прошлого)
    # Если памяти мало, добавим чуть-чуть рандома для маскировки
    shells = list(VOID_MEMORY) 
    
    # Если это первая попытка, добавим пару фейков для блефа
    while len(shells) < 4:
        fake = ''.join(random.choices(list(DIGS.values()), k=3))
        if fake not in shells: shells.append(fake)
        
    random.shuffle(shells)
    return full_skel, ", ".join(shells), len(shells)

# --- ИНТЕРФЕЙС ЭХО-ЗАМКА ---
print("⌛ C-08-52 CHRONOS ECHOS: ПАМЯТЬ АКТИВИРОВАНА")
while True:
    msg = input("\n📝 Введи текст (один и тот же несколько раз!): ")
    if msg == 'exit': break
    
    skel, shells, count = encrypt_chronos_packet(msg)
    print(f"\n🦴 СКЕЛЕТ: {skel}")
    print(f"🎯 ГИЛЬЗЫ (ТЕПЕРЬ ТАКЖЕ ИЗ ПРОШЛОГО): {shells}")
    print(f"🧩 ВСЕГО ВАРИАНТОВ В ПУСТОТЕ: {len(VOID_MEMORY)}")
