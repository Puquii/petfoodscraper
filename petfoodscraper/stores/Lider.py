import requests
import json

url = "https://apps.lider.cl/supermercado/bff/category"

querystring = {"":""}

payload = {
    "categories": "Mascotas/Gato/Alimento Gato",
    "page": 1,
    "facets": [],
    "sortBy": "",
    "hitsPerPage": 16,
    "storeId": 615
}

headers = {
    "cookie": "rxVisitor=1684334428700F8BRITVIGK76NI218RBKENBVMP845VSN; _tt_enable_cookie=1; _ttp=I-9XO8hdcp7tYi52UVm1VdeJbI9; _vwo_uuid_v2=D64AA47B2F027F2D7CD1C0EDB70E76062|e5131e1943f0ca04365cdcf561533b86; _ga_NSPSTRE0HE=GS1.2.1691338176.2.1.1691338182.54.0.0; _gcl_au=1.1.2017834227.1696871597; pxcts=2fa4433e-66c7-11ee-89bb-373768c9c3a1; _pxvid=2fa42f63-66c7-11ee-89bb-a7a09b317bab; __pxvid=33432a12-66c7-11ee-b2ad-0242ac120004; dtCookie=v_4_srv_71_sn_CT0DGLTRRMRDSQ93LGQ11IR2U3QE0JTV_app-3A43a5284704382d12_1_app-3A85a1427a87c10e7c_1_ol_0_perc_100000_mul_1_rcs-3Acss_0; mdLogger=false; kampyle_userid=62b6-0d05-d831-57fa-ba58-7847-d18e-61bc; cto_bundle=KmacUF96anFxakltWGxMMU9QeHk4Z3RZcjFRSXhqbTRsODVRdSUyRk5XREVSc2NCZ2FxVndReHFGYU5vZnFkUmNuS1lYOWlIdUs4NW96cTdEd2Z4Q2xxQVZSS29IWEpma1lMa1J0WFhPSDYzZGdRMUxjNFpWdm5Hd21QTk1DZmthOWZ2bHV3WjJEQ0FYOWZBU29YWWdiJTJCNmIwanZ3JTNEJTNE; dtSa=-; _clck=snqkx1|2|fg8|0|1232; kampyleUserSession=1698529368846; kampyleUserSessionsCount=6; kampyleSessionPageCounter=1; _ga_C3E4R66LJ8=GS1.1.1698529144.7.1.1698529381.14.0.0; _gid=GA1.2.1667968153.1699649788; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.lider.cl%252F; ABTasty=uid=cg5v3dxb218pj2fv&fst=1686694292761&pst=1698526739910&cst=1699649788025&ns=9&pvt=9&pvis=1&th=; cloud=GTP; _ga_LFTL75YJRF=GS1.1.1699649787.10.0.1699649792.0.0.0; _px3=d4edb254cb0aaf84169eaba3e2e87217ca4901a570565b608013e1dba56706c5:5i3EH4ygOBHM2zbXIg79ZEvc3/rtLlGULVsy3mVSVqscOFLy6aYu142IEvNmPqmKtgTfsBY8utF2knELsvMLQA==:1000:FLby9CzgJ2ZYghs+BpPlUgR30rHoDEDK/Y2a5S7vh8Gr9N2Hu6jcgqkTLlss9bt5qx8pqmDD4KlsJ19pPxm2LUibF3dRyfQs82n4RorUwSTkl5P1KaUZPLp8aFVfrhNjlqzw/UTbHIGG/cRVvW42AZW/lcSjPzCRZpLSU+cn9HnH3NIvTHnXyJRlIquE2ZW68uCNm7ms6PJy2eohInQXp2gpyfuL9Fuv5wb75UCQJgI=; _ga_LT7B42QQTE=GS1.1.1699649794.22.1.1699651142.0.0.0; _ga_835TB8N4KP=GS1.1.1699649793.23.1.1699651142.59.0.0; _ga_PNF51KE2NM=GS1.1.1699649794.18.1.1699651143.58.0.0; _ga_9FZFY51HX9=GS1.1.1699649794.18.1.1699651143.0.0.0; _ga_S5V4J9JZ4W=GS1.1.1699649794.18.1.1699651143.58.0.0; _ga=GA1.2.2109954198.1684334429; _gat_UA-378501-55=1; _dc_gtm_UA-378501-24=1; _dc_gtm_UA-378501-51=1; _gat_UA-378501-53=1; rxvt=1699652943272|1699649794627; TSe3289311027=0895f45a56ab2000fade0e5a988e40e96f38d4d1c490260baa98b819f2f1b6518a145184f73696040815b7d0451130006978d31a001ce3ccc169c828949a0b1a5a29f267eecf806d3555e23e86999d0e13176653a9dfb6bb8514112c22113087; _uetsid=a21124f0800b11ee83e9e7397842591e; _uetvid=c4a09a90f4c011ed900995788a9a010c; dtPC=71$451143204_521h-vTVINGEHFARQFPSODSUHEUFFDVURKHIMK-0e0; _ga_F0EXSQRJ7V=GS1.2.1699649795.11.1.1699651143.60.0.0; _ga_8MK6W43P8R=GS1.2.1699649788.15.1.1699651143.0.0.0; fs_lua=1.1699651143844; fs_uid=#16PCMB#4f65ed98-34ad-4900-a613-19402a9fd000:a7f7da82-532e-461b-9b7c-cf870a72f55e:1699649788588::4#/1715870428",
    "authority": "apps.lider.cl",
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-ES,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.lider.cl",
    "referer": "https://www.lider.cl/",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "tenant": "supermercado",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0",
    "x-channel": "SOD",
    "x-flowid": "990ffecd-b38c-40a9-b690-1fb995574c3d",
    "x-sessionid": "1f2816e3-58cc-46bb-8185-1f1d6661d7bf"
}

response = requests.post(url, json=payload, headers=headers, params=querystring).text

jdata = json.loads(response)
data = []

for x in range(0, len(jdata['products'])):
    data.append(jdata['products'][x]['description'])

print(response)