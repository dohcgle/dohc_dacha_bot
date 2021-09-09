# api lar yoziladi
# Dacha API
# examle_search = http://192.168.100.128/api/v1/search/?price_budniy=200&waymark=Chorvoq&guest_group=1
# example2 = http://192.168.100.128:8000/api/v1/search/?price_budniy_min=200&price_budniy_max=500&waymark=Burchmullo&guest_group=1

import requests

# search_url = 'http://192.168.100.128:8000/api/v1/search/'
search_url = 'http://192.168.2.155:1337/api/v1/search/'
headers = {'content-type': 'application/json'}


def search(request_list):
    print(request_list)
    house_list = []
    if request_list["waymark"] == 'Barchasi':
        waymark = ""
    else:
        waymark = request_list["waymark"]


    if request_list["price"] == "0-200":
        price_budniy_min = 0
        price_budniy_max = 200
    elif request_list["price"] == "200-400":
        price_budniy_min = 200
        price_budniy_max = 400
    elif request_list["price"] == "400-600":
        price_budniy_min = 400
        price_budniy_max = 600
    elif request_list["price"] == "600+":
        price_budniy_min = 600
        price_budniy_max = 10000

    if request_list["guest"] == "Ulfatlar":
        guest_group = 1
    elif request_list["guest"] == "Dugonalar":
        guest_group = 2
    elif request_list["guest"] == "Oila bilan":
        guest_group = 3
    elif request_list["guest"] == "Qizlar bilan":
        guest_group = 4

    request_url = f"{search_url}?price_budniy_min={price_budniy_min}&price_budniy_max={price_budniy_max}&waymark={waymark}&guest_group={guest_group}"
    # print(request_url)
    response = requests.get(url=request_url, headers=headers)


    any_list = [
    ]

    if response:
        houses_data = response.json()
        for x in houses_data:
            # house_detail_url = f"http://192.168.100.128:8000/property/detail/{x['id']}/"
            house_detail_url = f"http://192.168.2.155:1337/property/detail/{x['id']}/"
            text = f"Nomi: <b>{x['title']}</b>\n" \
                   f"Narxi: {x['price_budniy']} $\n" \
                   f"Yotoqxonalar soni: {x['bedrooms']} ta\n" \
                   f"Mehmonlar soni: {x['compatibility']} kishi\n" \
                   f"Batafsil: <a href='{house_detail_url}'>Havolani bosing</a>" \

            main_photo = "https://i1.wp.com/1dacha-sad.com/wp-content/uploads/2013/03/12-1.jpg"
            any_list.append(main_photo)
            any_list.append(text)

        return any_list

    else:
        any_list = []
        return any_list