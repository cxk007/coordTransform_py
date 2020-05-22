from coordTransform_utils import gcj02_to_bd09
import csv

file_location = r"C:\Users\chja7006\Google Drive\全能渠道项目\4.平台开发\Demo Data\20180607_店铺样例数据\linx_store_raw_data.csv"
new_file_location = r"C:\Users\chja7006\Google Drive\全能渠道项目\4.平台开发\Demo Data\20180607_店铺样例数据\linx_store_baidu_geocoding_data.csv"
header = ['ID',	'STORE_ID','STORE_TYPE','bd_lng', 'bd_lat', 'STORE_NAME','STORE_ADDR','STORE_PHONE','STORE_AREA',
          'STORE_POSTCOUNT','STORE_WORKTIME','STORE_RANKING','ADCODE','BRAND','PERIOD_TIME','GRID_ID','MESH_ID','GRID_TYPE']
with open(file_location, 'r', encoding='utf-8', newline='') as csv_file:
    with open(new_file_location, 'w', encoding='utf-8', newline="") as new_csv_file:
        file_dict = csv.DictReader(csv_file, delimiter='\t', dialect='excel')
        file_dict_writer = csv.DictWriter(new_csv_file, header, delimiter="|")
        file_dict_writer.writeheader()
        for item in file_dict:
            lng = float(item['LNG'])
            lat = float(item['LAT'])
            bd_geo_code = gcj02_to_bd09(lng, lat)
            bd_lng, bd_lat = bd_geo_code[0], bd_geo_code[1]
            item['bd_lng'] = bd_lng
            item['bd_lat'] = bd_lat
            del item['LNG']
            del item['LAT']
            print(item)
            file_dict_writer.writerow(item)

