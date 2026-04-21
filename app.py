from flask import Flask, render_template, request
import requests

app = Flask(__name__)

uzbek_names = {
    1: "Fotiha surasi",
    2: "Baqara surasi",
    3: "Oli Imron surasi",
    4: "Niso surasi",
    5: "Moida surasi",
    6: "An'om surasi",
    7: "A'rof surasi",
    8: "Anfol surasi",
    9: "Tavba surasi",
    10: "Yunus surasi",
    11: "Hud surasi",
    12: "Yusuf surasi",
    13: "Ra'd surasi",
    14: "Ibrohim surasi",
    15: "Hijr surasi",
    16: "Nahl surasi",
    17: "Isro surasi",
    18: "Kahf surasi",
    19: "Maryam surasi",
    20: "Toha surasi",
    21: "Anbiyo surasi",
    22: "Hajj surasi",
    23: "Mo‘minun surasi",
    24: "Nur surasi",
    25: "Furqon surasi",
    26: "Shuaro surasi",
    27: "Namli surasi",
    28: "Qasas surasi",
    29: "Ankabut surasi",
    30: "Rum surasi",
    31: "Luqmon surasi",
    32: "Sajda surasi",
    33: "Ahzob surasi",
    34: "Saba surasi",
    35: "Fatir surasi",
    36: "Yosin surasi",
    37: "Soffat surasi",
    38: "Sod surasi",
    39: "Zumar surasi",
    40: "G‘ofir surasi",
    41: "Fussilat surasi",
    42: "Shuro surasi",
    43: "Zuxruf surasi",
    44: "Duxon surasi",
    45: "Josiya surasi",
    46: "Ahqof surasi",
    47: "Muhammad surasi",
    48: "Fath surasi",
    49: "Hujurot surasi",
    50: "Qof surasi",
    51: "Zoriyot surasi",
    52: "Tur surasi",
    53: "Najm surasi",
    54: "Qamar surasi",
    55: "Rahmon surasi",
    56: "Voqia surasi",
    57: "Hadid surasi",
    58: "Mujodala surasi",
    59: "Hashr surasi",
    60: "Mumtahana surasi",
    61: "Soff surasi",
    62: "Jum'a surasi",
    63: "Munofiqun surasi",
    64: "Tag‘obun surasi",
    65: "Taloq surasi",
    66: "Tahrim surasi",
    67: "Mulk surasi",
    68: "Qalam surasi",
    69: "Haqqa surasi",
    70: "Maorij surasi",
    71: "Nuh surasi",
    72: "Jinn surasi",
    73: "Muzzammil surasi",
    74: "Muddassir surasi",
    75: "Qiyomat surasi",
    76: "Insan surasi",
    77: "Mursalat surasi",
    78: "Naba surasi",
    79: "Nozi'at surasi",
    80: "Abasa surasi",
    81: "Takvir surasi",
    82: "Infitor surasi",
    83: "Mutoffifun surasi",
    84: "Inshiqoq surasi",
    85: "Buruj surasi",
    86: "Toriq surasi",
    87: "A'lo surasi",
    88: "G‘oshiyya surasi",
    89: "Fajr surasi",
    90: "Balad surasi",
    91: "Shams surasi",
    92: "Layl surasi",
    93: "Zuho surasi",
    94: "Sharh surasi",
    95: "Tin surasi",
    96: "Alaq surasi",
    97: "Qadr surasi",
    98: "Bayyina surasi",
    99: "Zalzala surasi",
    100: "Odiyat surasi",
    101: "Qori'a surasi",
    102: "Takosur surasi",
    103: "Asr surasi",
    104: "Humaza surasi",
    105: "Fil surasi",
    106: "Quraysh surasi",
    107: "Ma’un surasi",
    108: "Kavsar surasi",
    109: "Kofirun surasi",
    110: "Nasr surasi",
    111: "Masad surasi",
    112: "Ixlos surasi",
    113: "Falaq surasi",
    114: "Nos surasi"
}

@app.route('/')
def index():
    query = request.args.get('q', '').lower()
    res = requests.get("http://api.alquran.cloud/v1/surah")
    surahs = res.json()["data"]

    # ✅ Sajda oyati bor suralar ro'yxati
    sajda_surah_numbers = {7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96}

    # ✅ Sura nomlariga o'zbekcha nom va sajda belgisi qo‘shamiz
    for sura in surahs:
        sura['uzbek'] = uzbek_names.get(sura['number'], '')
        sura['has_sajda'] = sura['number'] in sajda_surah_numbers

    # ✅ Qidiruv bo‘lsa, filtrlaymiz
    if query:
        surahs = [s for s in surahs if
                  query in s['englishName'].lower() or
                  query in s['name'] or
                  query in s['uzbek'].lower()]

    return render_template("index.html", surahs=surahs, query=query)


sura_names_uz = {
    1: "Fotiha", 2: "Baqara", 3: "Oli Imron", 4: "Niso", 5: "Moida",
    6: "An’om", 7: "A’rof", 8: "Anfol", 9: "Tavba", 10: "Yunus",
    11: "Hud", 12: "Yusuf", 13: "Ra’d", 14: "Ibrohim", 15: "Hijr",
    16: "Nahl", 17: "Isro", 18: "Kahf", 19: "Maryam", 20: "Toha",
    21: "Anbiyo", 22: "Haj", 23: "Mo‘minun", 24: "Nur", 25: "Furqon",
    26: "Shuaro", 27: "Namli", 28: "Qasas", 29: "Ankabut", 30: "Rum",
    31: "Luqmon", 32: "Sajda", 33: "Ahzob", 34: "Saba", 35: "Fatir",
    36: "Yosin", 37: "Soffat", 38: "Sod", 39: "Zumar", 40: "G‘ofir",
    41: "Fussilat", 42: "Sho‘ro", 43: "Zuxruf", 44: "Duxon", 45: "Josiya",
    46: "Ahqof", 47: "Muhammad", 48: "Fath", 49: "Hujurot", 50: "Qof",
    51: "Zoriyot", 52: "Tur", 53: "Najm", 54: "Qamar", 55: "Rahmon",
    56: "Voqea", 57: "Hadid", 58: "Mujodala", 59: "Hashr", 60: "Mumtahina",
    61: "Soff", 62: "Juma", 63: "Munofiqun", 64: "Tag‘obun", 65: "Taloq",
    66: "Tahrim", 67: "Mulk", 68: "Qalam", 69: "Haqqa", 70: "Maorij",
    71: "Nuh", 72: "Jinn", 73: "Muzzammil", 74: "Muddassir", 75: "Qiyomat",
    76: "Insan", 77: "Mursalat", 78: "Naba", 79: "Nozi’at", 80: "Abasa",
    81: "Takvir", 82: "Infitor", 83: "Mutoffifun", 84: "Inshiqoq", 85: "Buruj",
    86: "Toriq", 87: "A’lo", 88: "G‘oshiya", 89: "Fajr", 90: "Balad",
    91: "Shams", 92: "Layl", 93: "Zuho", 94: "Sharh", 95: "Tin",
    96: "Alaq", 97: "Qadr", 98: "Bayyina", 99: "Zalzala", 100: "Odiya",
    101: "Qori’a", 102: "Takosur", 103: "Asr", 104: "Humaza", 105: "Fil",
    106: "Quraysh", 107: "Ma’un", 108: "Kavsar", 109: "Kofirun", 110: "Nasr",
    111: "Masad", 112: "Ixlos", 113: "Falaq", 114: "Nos"
}

@app.route('/sura/<int:number>')
def view_sura(number):
    res = requests.get(f"http://api.alquran.cloud/v1/surah/{number}/ar.alafasy")
    sura = res.json()["data"]
    audio_url = f"https://cdn.islamic.network/quran/audio-surah/128/ar.alafasy/{number}.mp3"
    uzbek_name = sura_names_uz.get(number, sura["englishName"])
    return render_template("sura.html", sura=sura, audio_url=audio_url, uzbek_name=uzbek_name)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
