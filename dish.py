import requests
from datetime import datetime
import re, json



#filename = f"EPG_{time}.txt"


def get_auth_token():
	headers = {
		'Host': 'www.dishtv.in',
		# 'Content-Length': '0',
		'Sec-Ch-Ua-Platform': '"Windows"',
		'X-Requested-With': 'XMLHttpRequest',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Sec-Ch-Ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
		'Csrf-Token': 'undefined',
		'Sec-Ch-Ua-Mobile': '?0',
		'Sec-Gpc': '1',
		'Accept-Language': 'en-US,en;q=0.6',
		'Origin': 'https://www.dishtv.in',
		'Sec-Fetch-Site': 'same-origin',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Referer': 'https://www.dishtv.in/channel-guide.html',
		# 'Accept-Encoding': 'gzip, deflate, br',
		'Priority': 'u=1, i',
	}

	token = requests.post('https://www.dishtv.in/services/epg/signin', headers=headers).json()['token']

	return token

def get_epg(ch_id, dt, token):
	headers = {
		'Host': 'epg.mysmartstick.com',
		'Sec-Ch-Ua-Platform': '"Windows"',
		'Authorization': f'{token}',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
		'Accept': '*/*',
		'Sec-Ch-Ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
		'Content-Type': 'application/json',
		'Sec-Ch-Ua-Mobile': '?0',
		'Sec-Gpc': '1',
		'Accept-Language': 'en-US,en;q=0.6',
		'Origin': 'https://www.dishtv.in',
		'Sec-Fetch-Site': 'cross-site',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Referer': 'https://www.dishtv.in/',
		'Priority': 'u=1, i',
	}

	json_data = {
		'channelid': f'{ch_id}',
		'date': f'{dt}',
		'allowPastEvents': True,
	}

	epg_res = requests.post(
		'https://epg.mysmartstick.com/dishtv/api/v1/epg/entities/programs',
		headers=headers,
		json=json_data
	).json()

	return epg_res


def get_channels_data():

	all_channels ='''[
			  {
				"id": "10000000000350000",
				"title": "Super Hungama",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-35365-jr3xz4uo-v5/imageContent-35365-jr3xz4uo-m6.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000000340000",
				"title": "Disney",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-1356-j5tdnwmw-v1/imageContent-1356-j5tdnwmw-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000039210000",
				"title": "Nick HD+",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-11658-j9k5lvgo-v1/imageContent-11658-j9k5lvgo-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000001010000",
				"title": "Nick",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-465-j5jw9va0-v1/imageContent-465-j5jw9va0-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000000760000",
				"title": "Cartoon Network",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-11161-j99h67u8-v1/imageContent-11161-j99h67u8-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000000860000",
				"title": "Pogo",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-2694-j638bugw-v1/imageContent-2694-j638bugw-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "159011",
				"title": "Discovery Kids",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-24724-jgvwokqw-v1/imageContent-24724-jgvwokqw-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000007610000",
				"title": "Sonic Nickelodeon",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-8018-j7a7n1a8-v1/imageContent-8018-j7a7n1a8-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000051840000",
				"title": "SONY YAY",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-132-j5fpedbs-v4/imageContent-132-j5fpedbs-m6.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000075992191",
				"title": "ETV Bal Bharat",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-62236-kny7yzaw-v1/imageContent-62236-kny7yzaw-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000013230000",
				"title": "Nick Jr",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-390-j5jpps1s-v1/imageContent-390-j5jpps1s-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000012870000",
				"title": "Disney Junior",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-35368-jr3xz7xs-v1/imageContent-35368-jr3xz7xs-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000001690000",
				"title": "Hungama",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-11479-j9jr9a8o-v1/imageContent-11479-j9jr9a8o-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000001770000",
				"title": "Chutti TV",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-11278-j9j4h4s0-v1/imageContent-11278-j9j4h4s0-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000007490000",
				"title": "Kochu TV",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-258-j5fz98sg-v1/imageContent-258-j5fz98sg-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "142737",
				"title": "Chintu TV",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-12092-j9ogyoig-v1/imageContent-12092-j9ogyoig-m1.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000075992767",
				"title": "Disney Channel HD",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/DISNHD_Thumbnail-v1/DISNHD_Thumbnail.png",
				"channel_genre": "Kids"
			  },
			  {
				"id": "10000000075990144",
				"title": "Gubbare",
				"logo": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/imageContent-57985-khvdchrs-v2/imageContent-57985-khvdchrs-m2.png",
				"channel_genre": "Kids"
			  }
		]'''

	all_channels = json.loads(all_channels)

	return all_channels

# Function to append data to an existing JSON file
def append_to_existing_json(file_path, new_data):
	try:
		# Load existing data
		with open(file_path, "r") as file:
			existing_data = json.load(file)
	except (FileNotFoundError, json.JSONDecodeError):
		# If file doesn't exist or is invalid, initialize empty data
		existing_data = {"epg": {}}
	
	# Merge new data into existing data
	for date, channels in new_data.items():
		if date not in existing_data["epg"]:
			existing_data["epg"][date] = []
		existing_data["epg"][date].extend(channels)
	
	# Save the updated data back to the file
	with open(file_path, "w") as file:
		json.dump(existing_data, file, indent=4)
	print(f"Data successfully appended to {file_path}")


# Function to generate new EPG data for specified dates and channels
def generate_new_epg_data():
	epg = {}

	token = get_auth_token()
	channels = get_channels_data()
	date_str = datetime.now().strftime("%Y-%m-%d")
	dt = datetime.now().strftime("%d/%m/%Y")
	epg[date_str] = []
	
	for x in channels:
		
		epg_res = get_epg(x['id'], dt, token)

		channel_data = {
			"channelId": x['id'],
			"channelName": x['title'],
			"programs": []
		}
		
		for program in epg_res:
			program_data = {
				"title": program["title"],
				"Series Number": program["seriesnumber"],
				"Episode Number": program["episode-num"],
				"startTime": program["start"],
				"endTime": program["stop"],
			}
			channel_data["programs"].append(program_data)
		
		epg[date_str].append(channel_data)
	
	append_to_existing_json('EPG.json', epg)

generate_new_epg_data()