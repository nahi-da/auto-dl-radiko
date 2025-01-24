# 番組名をここに
PROGRAM_NAME = "有吉弘行のSUNDAY NIGHT DREAMER"


class CustomBaseException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.args = args

class InvalidStationId(CustomBaseException):
    def __str__(self):
        return (
            f"\"{self.args[0]}\" はSTATION_MAPに登録されていません。"
        )

class NoSelectedInBrowser(CustomBaseException):
    def __str__(self):
        return (
            f"番組が選択されませんでした。"
        )

class CanceledInDialog(CustomBaseException):
    def __str__(self):
        return (
            f"キャンセルされました。"
        )

class NoInputInDialog(CustomBaseException):
    def __str__(self):
        return (
            f"URLがダイアログに入力されませんでした。"
        )

class InvalidURL(CustomBaseException):
    def __str__(self):
        return (
            f"\"{self.args[0]}\" URLが不正です。"
        )

class DownloadError(CustomBaseException):
    def __str__(self):
        return (
            f"ダウンロードに失敗しました。"
        )

class ProgramNotFound(CustomBaseException):
    def __str__(self):
        return (
            f"番組が見つかりませんでした。"
        )

VERSION_MAP = {
    # Accroding to  https:#radiko.jp/#!/info/2558
    "7.0.0": { "sdk": "24", "builds": ["NBD92Q", "NBD92N", "NBD92G", "NBD92F", "NBD92E", "NBD92D", "NBD91Z", "NBD91Y", "NBD91X", "NBD91U", "N5D91L", "NBD91P", "NRD91K", "NRD91N", "NBD90Z", "NBD90X", "NBD90W", "NRD91D", "NRD90U", "NRD90T", "NRD90S", "NRD90R", "NRD90M"] },
    "7.1.0": { "sdk": "25", "builds": ["NDE63X", "NDE63V", "NDE63U", "NDE63P", "NDE63L", "NDE63H"] },
    "7.1.1": { "sdk": "25", "builds": ["N9F27M", "NGI77B", "N6F27M", "N4F27P", "N9F27L", "NGI55D", "N4F27O", "N8I11B", "N9F27H", "N6F27I", "N4F27K", "N9F27F", "N6F27H", "N4F27I", "N9F27C", "N6F27E", "N4F27E", "N6F27C", "N4F27B", "N6F26Y", "NOF27D", "N4F26X", "N4F26U", "N6F26U", "NUF26N", "NOF27C", "NOF27B", "N4F26T", "NMF27D", "NMF26X", "NOF26W", "NOF26V", "N6F26R", "NUF26K", "N4F26Q", "N4F26O", "N6F26Q", "N4F26M", "N4F26J", "N4F26I", "NMF26V", "NMF26U", "NMF26R", "NMF26Q", "NMF26O", "NMF26J", "NMF26H", "NMF26F"] },
    "7.1.2": { "sdk": "25", "builds": ["N2G48H", "NZH54D", "NKG47S", "NHG47Q", "NJH47F", "N2G48C", "NZH54B", "NKG47M", "NJH47D", "NHG47O", "N2G48B", "N2G47Z", "NJH47B", "NJH34C", "NKG47L", "NHG47N", "N2G47X", "N2G47W", "NHG47L", "N2G47T", "N2G47R", "N2G47O", "NHG47K", "N2G47J", "N2G47H", "N2G47F", "N2G47E", "N2G47D"] },
    "8.0.0": { "sdk": "26", "builds": ["5650811", "5796467", "5948681", "6107732", "6127070"] },
    "8.1.0": { "sdk": "27", "builds": ["5794017", "6107733", "6037697"] },
    "9.0.0": { "sdk": "28", "builds": ["5948683", "5794013", "6127072"] },
    "10.0.0": { "sdk": "29", "builds": ["5933585", "6969601", "7023426" , "7070703"] },
    "11.0.0": { "sdk":"30" , "builds": ["RP1A.201005.006", "RQ1A.201205.011", "RQ1A.210105.002"]},
    "12.0.0": { "sdk": "31" , "builds": ["SD1A.210817.015.A4", "SD1A.210817.019.B1", "SD1A.210817.037", "SQ1D.220105.007"]},
    "13.0.0": { "sdk": "33" , "builds": ["TQ3C.230805.001.B2", "TQ3A.230805.001.A2", "TQ3A.230705.001.A1", "TQ2B.230505.005.A1", "TQ2A.230505.002", "TQ2A.230405.003.E1"]},
}

MODEL_LIST = ["SC-02H", "SCV33", "SM-G935F", "SM-G935X", "SM-G935W8", "SM-G935K", "SM-G935L", "SM-G935S", "SAMSUNG-SM-G935A", "SM-G935VC", "SM-G9350", "SM-G935P", "SM-G935T", "SM-G935U", "SM-G935R4", "SM-G935V", "SC-02J", "SCV36", "SM-G950F", "SM-G950N", "SM-G950W", "SM-G9500", "SM-G9508", "SM-G950U", "SM-G950U1", "SM-G892A", "SM-G892U", "SC-03J", "SCV35", "SM-G955F", "SM-G955N", "SM-G955W", "SM-G9550", "SM-G955U", "SM-G955U1", "SM-G960F", "SM-G960N", "SM-G9600", "SM-G9608", "SM-G960W", "SM-G960U", "SM-G960U1", "SM-G965F", "SM-G965N", "SM-G9650", "SM-G965W", "SM-G965U", "SM-G965U1"
    # Samsung galaxy s7+
    , "SC-01J", "SCV34", "SM-N930F", "SM-N930X", "SM-N930K", "SM-N930L", "SM-N930S", "SM-N930R7", "SAMSUNG-SM-N930A", "SM-N930W8", "SM-N9300", "SGH-N037", "SM-N930R6", "SM-N930P", "SM-N930VL", "SM-N930T", "SM-N930U", "SM-N930R4", "SM-N930V", "SC-01K", "SCV37", "SM-N950F", "SM-N950N", "SM-N950XN", "SM-N950U", "SM-N9500", "SM-N9508", "SM-N950W", "SM-N950U1"
    # samsung galaxy note
    , "WX06K", "404KC", "503KC", "602KC", "KYV32", "E6782", "KYL22", "WX04K", "KYV36", "KYL21", "302KC", "KYV36", "KYV42", "KYV37", "C5155", "SKT01", "KYY24", "KYV35", "KYV41", "E6715", "KYY21", "KYY22", "KYY23", "KYV31", "KYV34", "KYV38", "WX10K", "KYL23", "KYV39", "KYV40"
    # KYOCERA
    , "C6902", "C6903", "C6906", "C6916", "C6943", "L39h", "L39t", "L39u", "SO-01F", "SOL23", "D5503", "M51w", "SO-02F", "D6502", "D6503", "D6543", "SO-03F", "SGP511", "SGP512", "SGP521", "SGP551", "SGP561", "SO-05F", "SOT21", "D6563", "401SO", "D6603", "D6616", "D6643", "D6646", "D6653", "SO-01G", "SOL26", "D6603", "D5803", "D5833", "SO-02G", "D5803", "D6633", "D6683", "SGP611", "SGP612", "SGP621", "SGP641", "E6553", "E6533", "D6708", "402SO", "SO-03G", "SOV31", "SGP712", "SGP771", "SO-05G", "SOT31", "E6508", "501SO", "E6603", "E6653", "SO-01H", "SOV32", "E5803", "E5823", "SO-02H", "E6853", "E6883", "SO-03H", "E6833", "E6633", "E6683", "C6502", "C6503", "C6506", "L35h", "SOL25", "C5306", "C5502", "C5503", "601SO", "F8331", "F8332", "SO-01J", "SOV34", "G8141", "G8142", "G8188", "SO-04J", "701SO", "G8341", "G8342", "G8343", "SO-01K", "SOV36", "G8441", "SO-02K", "602SO", "G8231", "G8232", "SO-03J", "SOV35"
    # sony xperia z series
    , "605SH", "SH-03J", "SHV39", "701SH", "SH-M06"
    # sharp
    , "101F", "201F", "202F", "301F", "IS12F", "F-03D", "F-03E", "M01", "M305", "M357", "M555", "M555", "F-11D", "F-06E", "EM01F", "F-05E", "FJT21", "F-01D", "FAR70B", "FAR7", "F-04E", "F-02E", "F-10D", "F-05D", "FJL22", "ISW11F", "ISW13F", "FJL21", "F-074", "F-07D"
    # fujitu arrows
    , "G9FPL", "GWKK3", "GHL1X", "G0DZQ", "G82U8", "GP4BC", "GE2AE", "GVU6C", "GQML3", "GX7AS", "GB62Z", "G1AZG", "GLUOG", "G8VOU", "GB7N6", "G9S9B16", "G1F8F", "G4S1M", "GD1YQ", "GTT9Q"
    # pixel
]

APP_VERSION = ["8.0.11", "8.0.10", "8.0.9", "8.0.7", "8.0.6", "8.0.5", "8.0.4", "8.0.3", "8.0.2"]

AUTHKEY = 'bcd151073c03b352e1ef2fd66c32209da9ca0afa'

COORDINATES = {
    "北海道": [43.064615, 141.346807],
    "青森": [40.824308, 140.739998],
    "岩手": [39.703619, 141.152684],
    "宮城": [38.268837, 140.8721],
    "秋田": [39.718614, 140.102364],
    "山形": [38.240436, 140.363633],
    "福島": [37.750299, 140.467551],
    "茨城": [36.341811, 140.446793],
    "栃木": [36.565725, 139.883565],
    "群馬": [36.390668, 139.060406],
    "埼玉": [35.856999, 139.648849],
    "千葉": [35.605057, 140.123306],
    "東京": [35.689488, 139.691706],
    "神奈川": [35.447507, 139.642345],
    "新潟": [37.902552, 139.023095],
    "富山": [36.695291, 137.211338],
    "石川": [36.594682, 136.625573],
    "福井": [36.065178, 136.221527],
    "山梨": [35.664158, 138.568449],
    "長野": [36.651299, 138.180956],
    "岐阜": [35.391227, 136.722291],
    "静岡": [34.97712, 138.383084],
    "愛知": [35.180188, 136.906565],
    "三重": [34.730283, 136.508588],
    "滋賀": [35.004531, 135.86859],
    "京都": [35.021247, 135.755597],
    "大阪": [34.686297, 135.519661],
    "兵庫": [34.691269, 135.183071],
    "奈良": [34.685334, 135.832742],
    "和歌山": [34.225987, 135.167509],
    "鳥取": [35.503891, 134.237736],
    "島根": [35.472295, 133.0505],
    "岡山": [34.661751, 133.934406],
    "広島": [34.39656, 132.459622],
    "山口": [34.185956, 131.470649],
    "徳島": [34.065718, 134.55936],
    "香川": [34.340149, 134.043444],
    "愛媛": [33.841624, 132.765681],
    "高知": [33.559706, 133.531079],
    "福岡": [33.606576, 130.418297],
    "佐賀": [33.249442, 130.299794],
    "長崎": [32.744839, 129.873756],
    "熊本": [32.789827, 130.741667],
    "大分": [33.238172, 131.612619],
    "宮崎": [31.911096, 131.423893],
    "鹿児島": [31.560146, 130.557978],
    "沖縄": [26.2124, 127.680932]
}

DEFAULT_AREA = "岩手"

STATION_MAP = {
    'HBC': {'name': 'ＨＢＣラジオ', 'area': ['JP1']},
    'STV': {'name': 'ＳＴＶラジオ', 'area': ['JP1']},
    'AIR-G': {'name': "AIR-G'（FM北海道）", 'area': ['JP1']},
    'NORTHWAVE': {'name': 'FM NORTH WAVE', 'area': ['JP1']}, 
    'RAB': {'name': 'ＲＡＢ青森放送', 'area': ['JP2']}, 
    'AFB': {'name': 'エフエム青森', 'area': ['JP2']}, 
    'IBC': {'name': 'IBCラジオ', 'area': ['JP3']}, 
    'FMI': {'name': 'エフエム岩手', 'area': ['JP3']}, 
    'TBC': {'name': 'TBCラジオ', 'area': ['JP4']}, 
    'DATEFM': {'name': 'Date fm（エフエム仙台）', 'area': ['JP4']}, 
    'ABS': {'name': 'ABS秋田放送', 'area': ['JP5']}, 
    'AFM': {'name': 'エフエム秋田', 'area': ['JP5']}, 
    'YBC': {'name': 'YBC山形放送', 'area': ['JP6']}, 
    'RFM': {'name': 'Rhythm Station エフエム山形', 'area': ['JP6']},
    'RFC': {'name': 'RFCラジオ福島', 'area': ['JP7']},
    'FMF': {'name': 'ふくしまFM', 'area': ['JP7']},
    'JOIK': {'name': 'NHKラジオ第1（札幌）', 'area': ['JP1']},
    'JOHK': {'name': 'NHKラジオ第1（仙台）', 'area': ['JP2', 'JP3', 'JP4', 'JP5', 'JP6', 'JP7']}, 
    'TBS': {'name': 'TBSラジオ', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14']},
    'QRR': {'name': '文化放送', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14']},
    'LFR': {'name': 'ニッポン放送', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14']},
    'INT': {'name': 'interfm', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14']},
    'FMT': {'name': 'TOKYO FM', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14']},
    'FMJ': {'name': 'J-WAVE', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14']},
    'JORF': {'name': 'ラジオ日本', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14']},
    'BAYFM78': {'name': 'bayfm78', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14']},
    'NACK5': {'name': 'NACK5', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14']},
    'YFM': {'name': 'ＦＭヨコハマ', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14']},
    'IBS': {'name': 'LuckyFM 茨城放送', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14']},
    'CRT': {'name': 'CRT栃木放送', 'area': ['JP9']}, 'RADIOBERRY': {'name': 'RADIO BERRY', 'area': ['JP9']},
    'FMGUNMA': {'name': 'FM GUNMA', 'area': ['JP10']},
    'JOAK': {'name': 'NHKラジオ第1（東京）', 'area': ['JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14', 'JP15', 'JP19', 'JP20']},
    'BSN': {'name': 'ＢＳＮラジオ', 'area': ['JP15']},
    'FMNIIGATA': {'name': 'FM NIIGATA', 'area': ['JP15']},
    'KNB': {'name': 'ＫＮＢラジオ', 'area': ['JP16']},
    'FMTOYAMA': {'name': 'ＦＭとやま', 'area': ['JP16']},
    'MRO': {'name': 'MROラジ オ', 'area': ['JP17']},
    'HELLOFIVE': {'name': 'エフエム石川', 'area': ['JP17']},
    'FBC': {'name': 'FBCラジオ', 'area': ['JP18']},
    'FMFUKUI': {'name': 'FM福井', 'area': ['JP18']},
    'YBS': {'name': 'YBSラジオ', 'area': ['JP19']},
    'FM-FUJI': {'name': 'FM FUJI', 'area': ['JP19']},
    'SBC': {'name': 'SBCラジオ', 'area': ['JP20']},
    'FMN': {'name': 'ＦＭ長野', 'area': ['JP20']},
    'JOCK': {'name': 'NHKラジオ第1（名古屋）', 'area': ['JP16', 'JP17', 'JP18', 'JP21', 'JP22', 'JP23', 'JP24']},
    'CBC': {'name': 'CBCラジオ', 'area': ['JP21', 'JP23', 'JP24']},
    'TOKAIRADIO': {'name': 'TOKAI RADIO', 'area': ['JP21', 'JP23', 'JP24']},
    'GBS': {'name': 'ぎふ チャン', 'area': ['JP21', 'JP23', 'JP24']},
    'ZIP-FM': {'name': 'ZIP-FM', 'area': ['JP21', 'JP23', 'JP24']},
    'FMAICHI': {'name': 'FM AICHI', 'area': ['JP21', 'JP23', 'JP24']},
    'FMGIFU': {'name': 'ＦＭ ＧＩＦＵ', 'area': ['JP21']},
    'SBS': {'name': 'SBSラジオ', 'area': ['JP22']},
    'K-MIX': {'name': 'K-MIX', 'area': ['JP22']},
    'FMMIE': {'name': 'レディオキューブ ＦＭ三重', 'area': ['JP24']},
    'ABC': {'name': 'ABCラジオ', 'area': ['JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30']},
    'MBS': {'name': 'MBSラジオ', 'area': ['JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30']},
    'OBC': {'name': 'OBCラジオ大阪', 'area': ['JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30']},
    'CCL': {'name': 'FM COCOLO', 'area': ['JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30']},
    '802': {'name': 'FM802', 'area': ['JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30']},
    'FMO': {'name': 'FM大阪', 'area': ['JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30']},
    'CRK': {'name': 'ラジオ関西', 'area': ['JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30']},
    'KISSFMKOBE': {'name': 'Kiss FM KOBE', 'area': ['JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30']},
    'E-RADIO': {'name': 'e-radio FM滋賀', 'area': ['JP25']},
    'KBS': {'name': 'KBS京都ラジオ', 'area': ['JP25', 'JP26', 'JP27']},
    'ALPHA-STATION': {'name': 'α-STATION FM KYOTO', 'area': ['JP25', 'JP26', 'JP27', 'JP29']},
    'WBS': {'name': 'wbs和歌山放送', 'area': ['JP30']},
    'JOBK': {'name': 'NHKラジオ第1（大阪）', 'area': ['JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30']},
    'BSS': {'name': 'BSSラジオ', 'area': ['JP31', 'JP32']},
    'FM-SANIN': {'name': 'エフエム山陰', 'area': ['JP31', 'JP32']},
    'RSK': {'name': 'ＲＳＫラジオ', 'area': ['JP33']},
    'FM-OKAYAMA': {'name': 'ＦＭ岡山', 'area': ['JP33']},
    'RCC': {'name': 'RCCラジオ', 'area': ['JP34']},
    'HFM': {'name': '広島FM', 'area': ['JP34']},
    'KRY': {'name': 'ＫＲＹ山口放送', 'area': ['JP35']},
    'FMY': {'name': 'エフエム山口', 'area': ['JP35']},
    'JRT': {'name': 'ＪＲＴ四国 放送', 'area': ['JP36']},
    'FM807': {'name': 'FM徳島', 'area': ['JP36']},
    'RNC': {'name': 'RNC西日本放送', 'area': ['JP37']},
    'FMKAGAWA': {'name': 'FM香川', 'area': ['JP37']},
    'RNB': {'name': 'RNB南海放送', 'area': ['JP38']},
    'JOEU-FM': {'name': 'FM愛媛', 'area': ['JP38']},
    'RKC': {'name': 'RKC高知放送', 'area': ['JP39']},
    'HI-SIX': {'name': 'エフエム高知', 'area': ['JP39']},
    'JOFK': {'name': 'NHKラジオ第1（広島）', 'area': ['JP31', 'JP32', 'JP33', 'JP34', 'JP35']},
    'JOZK': {'name': 'NHKラジオ第1（松山）', 'area': ['JP36', 'JP37', 'JP38', 'JP39']},
    'RKB': {'name': 'RKBラジオ', 'area': ['JP40', 'JP41']},
    'KBC': {'name': 'KBCラジオ', 'area': ['JP40', 'JP41']},
    'LOVEFM': {'name': 'LOVE FM', 'area': ['JP40']},
    'CROSSFM': {'name': 'cross fm', 'area': ['JP40']},
    'FMFUKUOKA': {'name': 'FM FUKUOKA', 'area': ['JP40']},
    'FMS': {'name': 'エフエム佐賀', 'area': ['JP41']},
    'NBC': {'name': 'NBCラジオ', 'area': ['JP41', 'JP42']},
    'FMNAGASAKI': {'name': 'FM長崎', 'area': ['JP42']},
    'RKK': {'name': 'RKKラジオ', 'area': ['JP43']},
    'FMK': {'name': 'FMKエフエム熊本', 'area': ['JP43']},
    'OBS': {'name': 'OBSラジオ', 'area': ['JP44']},
    'FM_OITA': {'name': 'エフエム大分', 'area': ['JP44']},
    'MRT': {'name': '宮崎放送', 'area': ['JP45']},
    'JOYFM': {'name': 'エフエム宮崎', 'area': ['JP45']},
    'MBC': {'name': 'ＭＢＣラジオ', 'area': ['JP46']},
    'MYUFM': {'name': 'μＦＭ', 'area': ['JP46']},
    'RBC': {'name': 'RBCiラジオ', 'area': ['JP47']},
    'ROK': {'name': 'ラジオ沖縄', 'area': ['JP47']},
    'FM_OKINAWA': {'name': 'FM沖縄', 'area': ['JP47']},
    'JOLK': {'name': 'NHKラジオ第1（福岡）', 'area': ['JP40', 'JP41', 'JP42', 'JP43', 'JP44', 'JP45', 'JP46', 'JP47']},
    'RN1': {'name': 'ラジオNIKKEI第1', 'area': ['JP1', 'JP2', 'JP3', 'JP4', 'JP5', 'JP6', 'JP7', 'JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14', 'JP15', 'JP16', 'JP17', 'JP18', 'JP19', 'JP20', 'JP21', 'JP22', 'JP23', 'JP24', 'JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30', 'JP31', 'JP32', 'JP33', 'JP34', 'JP35', 'JP36', 'JP37', 'JP38', 'JP39', 'JP40', 'JP41', 'JP42', 'JP43', 'JP44', 'JP45', 'JP46', 'JP47']},
    'RN2': {'name': 'ラジオNIKKEI第2', 'area': ['JP1', 'JP2', 'JP3', 'JP4', 'JP5', 'JP6', 'JP7', 'JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14', 'JP15', 'JP16', 'JP17', 'JP18', 'JP19', 'JP20', 'JP21', 'JP22', 'JP23', 'JP24', 'JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30', 'JP31', 'JP32', 'JP33', 'JP34', 'JP35', 'JP36', 'JP37', 'JP38', 'JP39', 'JP40', 'JP41', 'JP42', 'JP43', 'JP44', 'JP45', 'JP46', 'JP47']},
    'HOUSOU-DAIGAKU': {'name': '放送大学', 'area': ['JP1', 'JP2', 'JP3', 'JP4', 'JP5', 'JP6', 'JP7', 'JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14', 'JP15', 'JP16', 'JP17', 'JP18', 'JP19', 'JP20', 'JP21', 'JP22', 'JP23', 'JP24', 'JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30', 'JP31', 'JP32', 'JP33', 'JP34', 'JP35', 'JP36', 'JP37', 'JP38', 'JP39', 'JP40', 'JP41', 'JP42', 'JP43', 'JP44', 'JP45', 'JP46', 'JP47']},
    'JOAK-FM': {'name': 'NHK-FM（東京）', 'area': ['JP1', 'JP2', 'JP3', 'JP4', 'JP5', 'JP6', 'JP7', 'JP8', 'JP9', 'JP10', 'JP11', 'JP12', 'JP13', 'JP14', 'JP15', 'JP16', 'JP17', 'JP18', 'JP19', 'JP20', 'JP21', 'JP22', 'JP23', 'JP24', 'JP25', 'JP26', 'JP27', 'JP28', 'JP29', 'JP30', 'JP31', 'JP32', 'JP33', 'JP34', 'JP35', 'JP36', 'JP37', 'JP38', 'JP39', 'JP40', 'JP41', 'JP42', 'JP43', 'JP44', 'JP45', 'JP46', 'JP47']}
}

BASEKEY = "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";
