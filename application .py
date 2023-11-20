from flask import Flask, render_template
import requests
import json
import mysql.connector

try:
    mydb = mysql.connector.connect(
      host="awseb-e-tpu6nmxr29-stack-awsebrdsdatabase-4aups3b7vlmr.cugozql0nnse.eu-west-1.rds.amazonaws.com",
      user="user",
      password="Artdutemps92",
      database="lab2_elliot"
    )
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")


temp_data_url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%22TLIST(M1)%22,%22C02431V02938%22%5D,%22dimension%22:%7B%22TLIST(M1)%22:%7B%22category%22:%7B%22index%22:%5B%22202212%22,%22202211%22,%22202210%22,%22202209%22,%22202208%22,%22202207%22,%22202206%22,%22202205%22,%22202204%22,%22202203%22,%22202202%22,%22202201%22,%22202112%22,%22202111%22,%22202110%22%5D%7D%7D,%22C02431V02938%22:%7B%22category%22:%7B%22index%22:%5B%22007%22%5D%7D%7D%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22MTM02%22%7D,%22version%22:%222.0%22%7D%7D"

rain_data_url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%22TLIST(M1)%22,%22C02431V02938%22%5D,%22dimension%22:%7B%22TLIST(M1)%22:%7B%22category%22:%7B%22index%22:%5B%22202212%22,%22202211%22,%22202210%22,%22202209%22,%22202208%22,%22202207%22,%22202206%22,%22202205%22,%22202204%22,%22202203%22,%22202202%22,%22202201%22,%22202112%22,%22202111%22,%22202110%22%5D%7D%7D,%22C02431V02938%22:%7B%22category%22:%7B%22index%22:%5B%22007%22%5D%7D%7D%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22MTM01%22%7D,%22version%22:%222.0%22%7D%7D"

sun_data_url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%22TLIST(M1)%22,%22C02431V02938%22%5D,%22dimension%22:%7B%22TLIST(M1)%22:%7B%22category%22:%7B%22index%22:%5B%22202212%22,%22202211%22,%22202210%22,%22202209%22,%22202208%22,%22202207%22,%22202206%22,%22202205%22,%22202204%22,%22202203%22,%22202202%22,%22202201%22,%22202112%22,%22202111%22,%22202110%22%5D%7D%7D,%22C02431V02938%22:%7B%22category%22:%7B%22index%22:%5B%22007%22%5D%7D%7D%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22MTM03%22%7D,%22version%22:%222.0%22%7D%7D"

wind_data_url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%22TLIST(M1)%22,%22C02431V02938%22%5D,%22dimension%22:%7B%22TLIST(M1)%22:%7B%22category%22:%7B%22index%22:%5B%22202212%22,%22202211%22,%22202210%22,%22202209%22,%22202208%22,%22202207%22,%22202206%22,%22202205%22,%22202204%22,%22202203%22,%22202202%22,%22202201%22,%22202112%22,%22202111%22,%22202110%22%5D%7D%7D,%22C02431V02938%22:%7B%22category%22:%7B%22index%22:%5B%22007%22%5D%7D%7D%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22MTM04%22%7D,%22version%22:%222.0%22%7D%7D"

application = Flask(__name__)

def get_data(url):
   response = json.loads(requests.request("GET", url).text)
   data = response["result"]["value"]
   return data

@application.route("/")
def index():
   temp_data = get_data(temp_data_url)
   rain_data = get_data(rain_data_url)
   sun_data = get_data(sun_data_url)
   wind_data = get_data(wind_data_url)

   for i in range(len(wind_data)):
      wind_data[i] = round(1.852*wind_data[i], 1)


   mycursor = mydb.cursor()
   
   for i in range(15): 
      sql_query = "UPDATE weather_data SET Avg_Max_Temp = %s, Avg_Min_Temp = %s, Mean_Temp = %s, Highest_Temp = %s, Lowest_Temp = %s, Total_Rain = %s, Most_Rain = %s, Raindays = %s, Total_Sun = %s, Most_Sun = %s, Max_Wind = %s WHERE Month_ID = '" + str(12-i) + "'"
      sql_values = (str(temp_data[0+i]), str(temp_data[12+i]), str(temp_data[24+i]), str(temp_data[36+i]), str(temp_data[48+i]), str(rain_data[0+i]), str(rain_data[12+i]), str(rain_data[24+i]), str(sun_data[0+i]), str(sun_data[12+i]), str(wind_data[0+i]))
      mycursor.execute(sql_query, sql_values)
   
   mydb.commit()

   return render_template("index.html", avg_max_temp_oct=temp_data[0],
                                        avg_max_temp_nov=temp_data[1],
                                        avg_max_temp_dec=temp_data[2],
                                        avg_max_temp_jan=temp_data[3],
                                        avg_max_temp_feb=temp_data[4],
                                        avg_max_temp_mar=temp_data[5],
                                        avg_max_temp_apr=temp_data[6],
                                        avg_max_temp_may=temp_data[7],
                                        avg_max_temp_jun=temp_data[8],
                                        avg_max_temp_jul=temp_data[9],
                                        avg_max_temp_aug=temp_data[10],
                                        avg_max_temp_sep=temp_data[11],
                                        avg_max_temp_oct1=temp_data[12],
                                        avg_max_temp_nov1=temp_data[13],
                                        avg_max_temp_dec1=temp_data[14],

                                        avg_min_temp_oct=temp_data[15],
                                        avg_min_temp_nov=temp_data[16],
                                        avg_min_temp_dec=temp_data[17],
                                        avg_min_temp_jan=temp_data[18],
                                        avg_min_temp_feb=temp_data[19],
                                        avg_min_temp_mar=temp_data[20],
                                        avg_min_temp_apr=temp_data[21],
                                        avg_min_temp_may=temp_data[22],
                                        avg_min_temp_jun=temp_data[23],
                                        avg_min_temp_jul=temp_data[24],
                                        avg_min_temp_aug=temp_data[25],
                                        avg_min_temp_sep=temp_data[26],
                                        avg_min_temp_oct1=temp_data[27],
                                        avg_min_temp_nov1=temp_data[28],
                                        avg_min_temp_dec1=temp_data[29],

                                        mean_temp_oct=temp_data[30],
                                        mean_temp_nov=temp_data[31],
                                        mean_temp_dec=temp_data[32],
                                        mean_temp_jan=temp_data[33],
                                        mean_temp_feb=temp_data[34],
                                        mean_temp_mar=temp_data[35],
                                        mean_temp_apr=temp_data[36],
                                        mean_temp_may=temp_data[37],
                                        mean_temp_jun=temp_data[38],
                                        mean_temp_jul=temp_data[39],
                                        mean_temp_aug=temp_data[40],
                                        mean_temp_sep=temp_data[41],
                                        mean_temp_oct1=temp_data[42],
                                        mean_temp_nov1=temp_data[43],
                                        mean_temp_dec1=temp_data[44],

                                        high_temp_oct=temp_data[45],
                                        high_temp_nov=temp_data[46],
                                        high_temp_dec=temp_data[47],
                                        high_temp_jan=temp_data[48],
                                        high_temp_feb=temp_data[49],
                                        high_temp_mar=temp_data[50],
                                        high_temp_apr=temp_data[51],
                                        high_temp_may=temp_data[52],
                                        high_temp_jun=temp_data[53],
                                        high_temp_jul=temp_data[54],
                                        high_temp_aug=temp_data[55],
                                        high_temp_sep=temp_data[56],
                                        high_temp_oct1=temp_data[57],
                                        high_temp_nov1=temp_data[58],
                                        high_temp_dec1=temp_data[59],

                                        low_temp_oct=temp_data[60],
                                        low_temp_nov=temp_data[61],
                                        low_temp_dec=temp_data[62],
                                        low_temp_jan=temp_data[63],
                                        low_temp_feb=temp_data[64],
                                        low_temp_mar=temp_data[65],
                                        low_temp_apr=temp_data[66],
                                        low_temp_may=temp_data[67],
                                        low_temp_jun=temp_data[68],
                                        low_temp_jul=temp_data[69],
                                        low_temp_aug=temp_data[70],
                                        low_temp_sep=temp_data[71],
                                        low_temp_oct1=temp_data[72],
                                        low_temp_nov1=temp_data[73],
                                        low_temp_dec1=temp_data[74],

                                        total_rain_oct=rain_data[0],
                                        total_rain_nov=rain_data[1],
                                        total_rain_dec=rain_data[2],
                                        total_rain_jan=rain_data[3],
                                        total_rain_feb=rain_data[4],
                                        total_rain_mar=rain_data[5],
                                        total_rain_apr=rain_data[6],
                                        total_rain_may=rain_data[7],
                                        total_rain_jun=rain_data[8],
                                        total_rain_jul=rain_data[9],
                                        total_rain_aug=rain_data[10],
                                        total_rain_sep=rain_data[11],
                                        total_rain_oct1=rain_data[12],
                                        total_rain_nov1=rain_data[13],
                                        total_rain_dec1=rain_data[14],

                                        most_rain_oct=rain_data[15],
                                        most_rain_nov=rain_data[16],
                                        most_rain_dec=rain_data[17],
                                        most_rain_jan=rain_data[18],
                                        most_rain_feb=rain_data[19],
                                        most_rain_mar=rain_data[20],
                                        most_rain_apr=rain_data[21],
                                        most_rain_may=rain_data[22],
                                        most_rain_jun=rain_data[23],
                                        most_rain_jul=rain_data[24],
                                        most_rain_aug=rain_data[25],
                                        most_rain_sep=rain_data[26],
                                        most_rain_oct1=rain_data[27],
                                        most_rain_nov1=rain_data[28],
                                        most_rain_dec1=rain_data[29],

                                        raindays_oct=int(rain_data[30]),
                                        raindays_nov=int(rain_data[31]),
                                        raindays_dec=int(rain_data[32]),
                                        raindays_jan=int(rain_data[33]),
                                        raindays_feb=int(rain_data[34]),
                                        raindays_mar=int(rain_data[35]),
                                        raindays_apr=int(rain_data[36]),
                                        raindays_may=int(rain_data[37]),
                                        raindays_jun=int(rain_data[38]),
                                        raindays_jul=int(rain_data[39]),
                                        raindays_aug=int(rain_data[40]),
                                        raindays_sep=int(rain_data[41]),
                                        raindays_oct1=int(rain_data[42]),
                                        raindays_nov1=int(rain_data[43]),
                                        raindays_dec1=int(rain_data[44]),

                                        total_sun_oct=sun_data[0],
                                        total_sun_nov=sun_data[1],
                                        total_sun_dec=sun_data[2],
                                        total_sun_jan=sun_data[3],
                                        total_sun_feb=sun_data[4],
                                        total_sun_mar=sun_data[5],
                                        total_sun_apr=sun_data[6],
                                        total_sun_may=sun_data[7],
                                        total_sun_jun=sun_data[8],
                                        total_sun_jul=sun_data[9],
                                        total_sun_aug=sun_data[10],
                                        total_sun_sep=sun_data[11],
                                        total_sun_oct1=sun_data[12],
                                        total_sun_nov1=sun_data[13],
                                        total_sun_dec1=sun_data[14],

                                        most_sun_oct=sun_data[15],
                                        most_sun_nov=sun_data[16],
                                        most_sun_dec=sun_data[17],
                                        most_sun_jan=sun_data[18],
                                        most_sun_feb=sun_data[19],
                                        most_sun_mar=sun_data[20],
                                        most_sun_apr=sun_data[21],
                                        most_sun_may=sun_data[22],
                                        most_sun_jun=sun_data[23],
                                        most_sun_jul=sun_data[24],
                                        most_sun_aug=sun_data[25],
                                        most_sun_sep=sun_data[26],
                                        most_sun_oct1=sun_data[27],
                                        most_sun_nov1=sun_data[28],
                                        most_sun_dec1=sun_data[29],

                                        max_wind_oct=wind_data[0],
                                        max_wind_nov=wind_data[1],
                                        max_wind_dec=wind_data[2],
                                        max_wind_jan=wind_data[3],
                                        max_wind_feb=wind_data[4],
                                        max_wind_mar=wind_data[5],
                                        max_wind_apr=wind_data[6],
                                        max_wind_may=wind_data[7],
                                        max_wind_jun=wind_data[8],
                                        max_wind_jul=wind_data[9],
                                        max_wind_aug=wind_data[10],
                                        max_wind_sep=wind_data[11],
                                        max_wind_oct1=wind_data[12],
                                        max_wind_nov1=wind_data[13],
                                        max_wind_dec1=wind_data[14])

if __name__ == "__main__":
   application.run()

