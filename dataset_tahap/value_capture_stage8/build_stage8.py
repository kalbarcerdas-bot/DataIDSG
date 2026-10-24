import csv, os, re
from pathlib import Path
from datetime import date
from urllib.parse import quote

out=Path('/mnt/data/value_capture_stage8')
out.mkdir(exist_ok=True,parents=True)
base='https://sdmx.oecd.org/sti-public/rest/data/OECD.STI.PIE,DSD_TIVA_MAINLV@DF_MAINLV,1.1/'
source_explorer='https://data-explorer.oecd.org/vis?bp=true&df%5Bag%5D=OECD.STI.PIE&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_TIVA_MAINLV%40DF_MAINLV&df%5Bvs%5D=1.1&pg=0&snb=12&tm=TiVA'
source_imf='https://www.imf.org/-/media/files/publications/cr/2024/english/1sgpea2024001-print-pdf.pdf'
indicators=[
 {'indicator_id':'FFD_DVA_SGP_IDN','code':'FFD_DVA','origin':'SGP','partner':'IDN','label':'Singapore domestic value added absorbed in Indonesian final demand','family':'final_demand','role':'primary','note':'SGP origin of domestic VA; IDN economy of final absorption; indirect routes via third countries may be included'},
 {'indicator_id':'FFD_DVA_IDN_SGP','code':'FFD_DVA','origin':'IDN','partner':'SGP','label':'Indonesia domestic value added absorbed in Singaporean final demand','family':'final_demand','role':'primary_reverse','note':'IDN origin of domestic VA; SGP economy of final absorption'},
 {'indicator_id':'EXGR_DVA_SGP_IDN','code':'EXGR_DVA','origin':'SGP','partner':'IDN','label':'Singapore domestic value added embodied in gross exports to Indonesia','family':'gross_exports','role':'complementary','note':'Immediate export partner IDN, distinct from eventual final demand destination'},
 {'indicator_id':'EXGR_DVA_IDN_SGP','code':'EXGR_DVA','origin':'IDN','partner':'SGP','label':'Indonesia domestic value added embodied in gross exports to Singapore','family':'gross_exports','role':'complementary_reverse','note':'Immediate export partner SGP; not identical to Indonesian VA absorbed in Singapore final demand'},
 {'indicator_id':'EXGR_FVA_SGP_IDN','code':'EXGR_FVA','origin':'SGP','partner':'IDN','label':'Foreign value added content of Singapore gross exports to Indonesia','family':'gross_exports','role':'decomposition','note':'All foreign origin countries combined; NOT exclusively Indonesian value added'},
 {'indicator_id':'EXGR_FVA_IDN_SGP','code':'EXGR_FVA','origin':'IDN','partner':'SGP','label':'Foreign value added content of Indonesia gross exports to Singapore','family':'gross_exports','role':'decomposition_reverse','note':'All foreign origin countries combined; NOT exclusively Singaporean value added'},
]
def wr(name, records, fields=None):
    if not fields: fields=list(records[0].keys())
    with (out/name).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(records)

registry=[]
for i in indicators:
    query=base+f"{i['code']}.{i['origin']}..{i['partner']}..A?startPeriod=2003&endPeriod=2022&dimensionAtObservation=AllDimensions&format=csvfilewithlabels"
    registry.append({**i,'unit':'USD million, current prices','source_id':'OECD_TIVA_MAINLV_2025_REV_JAN2026','edition':'2025 revised Jan 2026','source_explorer':source_explorer,'api_query_url':query,'api_key_status':'KEY_SHAPE_EXTRAPOLATED_FROM_OECD_EXAMPLE_NOT_LIVE_TESTED','economic_activity':'TOTAL_ECONOMY_CODE_TO_CONFIRM_FROM_METADATA','double_count_warning':'Do not add final demand and gross exports measures together'})
wr('stage8_indicator_registry.csv',registry)

obs=[]
for yr in range(2003,2026):
 for i in registry:
    within=(yr<=2022)
    obs.append({'year':yr,'indicator_id':i['indicator_id'],'value_usd_million':'','value_status':'PENDING_SOURCE_EXTRACTION' if within else 'OUT_OF_COVERAGE_2025_TIVA','origin_economy':i['origin'],'partner_economy':i['partner'],'source_id':'OECD_TIVA_MAINLV_2025_REV_JAN2026','source_dataflow':'OECD.STI.PIE,DSD_TIVA_MAINLV@DF_MAINLV,1.1','unit':'USD million current prices','economic_activity':'TOTAL_ECONOMY_TBD','oecd_vintage':'2025_edition_revision_2026_01','value_added_concept':i['label'],'source_url':i['api_query_url'],'missing_reason':'Data series not successfully fetched in current runtime' if within else 'OECD TiVA 2025 edition ends in 2022','audit_note':'Null deliberately; never interpret as zero'})
wr('stage8_value_added_panel_2003_2025.csv',obs)

benchmark=[
 {'year':2018,'economy':'SGP','partner_economy':'IDN','metric':'Indonesia share of Singapore value added absorbed in total foreign final demand','value_approx':6.0,'unit':'percent','status':'APPROXIMATE_CHART_READ','range_low':5.5,'range_high':6.5,'source_id':'IMF_2024_ARTICLE_IV_FIG8','source_url':source_imf,'page_printed':'40','page_pdf_zero_index':43,'data_vintage':'OLDER_OECD_WTO_TIVA_NOT_2025','comment':'Approximate visual reading from IMF Fig.8 (green bar Indonesia); denominator is total foreign final demand absorbing Singapore VA; not percent of GDP; cannot merge with 2025-vintage series'},
 {'year':2018,'economy':'SGP','partner_economy':'IDN','metric':'Indonesia share of Singapore gross exports by destination','value_approx':8.0,'unit':'percent','status':'APPROXIMATE_CHART_READ','range_low':7.5,'range_high':8.5,'source_id':'IMF_2024_ARTICLE_IV_FIG8','source_url':source_imf,'page_printed':'40','page_pdf_zero_index':43,'data_vintage':'OLDER_OECD_WTO_TIVA_NOT_2025','comment':'Approximate visual reading from IMF Fig.8 (blue bar Indonesia); not a value-added estimate'},
]
wr('stage8_imf_2018_illustrative_benchmark.csv',benchmark)

sources=[
 {'source_id':'OECD_TIVA_MAINLV_2025_REV_JAN2026','publisher':'OECD','title':'Trade in Value Added 2025, Principal Indicators Levels; second revision January 2026','url':source_explorer,'coverage_start':1995,'coverage_end':2022,'data_type':'modeled bilateral value added data','status':'SOURCE_CONFIRMED_SERIES_DOWNLOAD_BLOCKED','units':'USD million current prices','access':'OECD Data Explorer / SDMX API; publicly available, no subscription','caution':'January 2026 revision; do not mix with earlier releases'},
 {'source_id':'OECD_TIVA_METHOD','publisher':'OECD','title':'Trade in value-added: methodologies and scope','url':'https://www.oecd.org/en/topics/sub-issues/trade-in-value-added.html','coverage_start':1995,'coverage_end':2022,'data_type':'methodology','status':'SOURCE_CONFIRMED','units':'','access':'open','caution':'Gross trade and value added measures not additive'},
 {'source_id':'OECD_ICIO_2025','publisher':'OECD','title':'Inter-Country Input-Output Tables 2025 regular version','url':'https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html','coverage_start':1995,'coverage_end':2022,'data_type':'inter-country input output matrices','status':'SOURCE_CONFIRMED','units':'USD million current prices','access':'open zipped files','caution':'Regular and extended ICIO cannot be interchanged without mapping'},
 {'source_id':'OECD_TIVA_FDVA','publisher':'OECD','title':'Trade in Value Added 2025 Origin of Value Added in Final Demand','url':'https://data-explorer.oecd.org/vis?bp=true&df%5Bag%5D=OECD.STI.PIE&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_TIVA_FDVA%40DF_FDVA&df%5Bvs%5D=1.1&pg=0&snb=12&tm=TIVA','coverage_start':1995,'coverage_end':2022,'data_type':'origin value added by source industry, destination industry and economy','status':'SOURCE_CONFIRMED_NO_BILATERAL_EXTRACTION','units':'USD million current prices','access':'open','caution':'Very high-dimensional; use after validating principal indicator values'},
 {'source_id':'OECD_API_DOC','publisher':'OECD','title':'OECD Data via API','url':'https://www.oecd.org/en/data/insights/data-explainers/2024/09/api.html','coverage_start':'','coverage_end':'','data_type':'API documentation','status':'SOURCE_CONFIRMED','units':'','access':'open','caution':'Respect rate limiting and check SDMX dimensions'},
 {'source_id':'IMF_2024_ARTICLE_IV_FIG8','publisher':'IMF','title':'Singapore 2024 Article IV Report No.24/255 Figure 8','url':source_imf,'coverage_start':2018,'coverage_end':2018,'data_type':'published graphical secondary evidence based on earlier OECD-WTO TiVA','status':'FIGURE_VERIFIED_SCREENSHOT','units':'percent','access':'open PDF page 40 printed / 44th PDF page','caution':'Illustrative vintage-incompatible approximate readings'},
]
wr('stage8_source_registry.csv',sources)

requests=[]
for i in registry:
 requests.append({'task_id':'T8_'+i['indicator_id'],'source_id':'OECD_TIVA_MAINLV_2025_REV_JAN2026','method':'Official OECD SDMX API','api_url':i['api_query_url'],'response_format':'csvfilewithlabels','start_year':2003,'end_year':2022,'country_source':i['origin'],'partner_country':i['partner'],'measure':i['code'],'frequency':'A','filter_economic_activity':'Use official OECD structure codelist total-economy activity; verify correct code before extraction','validate':'Single series per year after total-economy selection; published unit USD million; no duplicates','current_status':'NOT_RUN_API_NETWORK_UNAVAILABLE','fallback':'Open OECD Data Explorer -> filter counterpart/reference/total activity -> Export CSV -> upload to this conversation','notes':'URL key syntax inferred from published OECD example; needs live API verification for exact structure/measure availability'})
wr('stage8_public_api_fetch_manifest.csv',requests)

rules=[
 ('V01','Completeness','OECD_2025','Official data 2003-2022; 2023-2025 null until another explicitly labeled version selected'),
 ('V02','Nulls','ALL','Missing values must remain null; zero is not allowed to represent missing'),
 ('V03','Unit','ALL','Preserve USD million at current prices; no silent conversions'),
 ('V04','Vintage','ALL','Series must be all January 2026 revision; never merge earlier 2023/2025 vintages silently'),
 ('V05','Sector_total','ALL','Identify official aggregate total-economy activity from data structure; do not sum aggregates together with constituent sectors'),
 ('V06','Direction','ALL','Reference economy is value-added origin (or exporter for exports), counterpart is final demand absorber or export destination as appropriate'),
 ('V07','No_additivity','ALL','Do not add FFD_DVA to EXGR_DVA; overlapping representations of value added'),
 ('V08','Ownership','ALL','Location of value-added production is not identity of final profit beneficiary or citizenship of shareholder'),
 ('V09','Mirror','FFD_DVA','SGP VA in Indonesian demand and IDN VA in Singapore demand are different directional measures and need not be equal'),
 ('V10','Benchmark','IMF_2018','Approximate 2018 bar chart readings may be used only as context; never inserted into revised 2025 dataset'),
 ('V11','Foreign_va','EXGR_FVA','Foreign VA in SG exports to IDN is from all non-SG economies, not specifically Indonesia'),
 ('V12','Comparison','ALL','Trade in value-added final demand is not equivalent to direct exports or bilateral services surplus'),
 ('V13','API_verification','ALL','Key shape, total activity aggregate code, and observation values must be validated on actual CSV before publishing'),
]
wr('stage8_validation_protocol.csv',[{'rule_id':a,'category':b,'applies_to':c,'requirement':d,'status':'SPECIFIED_NOT_EXECUTED_ON_OECD_OBSERVATIONS'} for a,b,c,d in rules])

coverage=[]
for i in registry:
 coverage.append({'indicator_id':i['indicator_id'],'target_years':23,'published_coverage_2003_2022':20,'out_of_coverage_2023_2025':3,'actual_observations_extracted':0,'expected_value_rows':20,'status':'DATA_ACCESS_PENDING','next_step':'Use official OECD SDMX response and load country/industry filtering; not scrape individual HTML pages'})
wr('stage8_coverage_audit.csv',coverage)

# format independent validation
for name in [p.name for p in out.glob('*.csv')]:
 with (out/name).open('r',encoding='utf-8-sig',newline='') as f:
  rows=list(csv.DictReader(f))
  assert rows and len(rows[0])>=4, (name,len(rows))
 print(name,len(rows))
assert len(obs)==138 and len(benchmark)==2
