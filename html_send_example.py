text =  "<b>bold</b>, <strong>bold</strong>\n"\
                    "<i>italic</i>, <em>italic</em>\n"\
                    "<u>underline</u>, <ins>underline</ins>\n"\
                    "<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>"\
                    "<b>bold <i>italic bold <s>italic bold strikethrough</s> <u>underline italic bold</u></i> bold</b>"\
                    "<a href='http://www.example.com/'>inline URL</a>"\
                    "<a href='tg://user?id=123456789'>inline mention of a user</a>"\
                    "<code>inline fixed-width code</code>"\
                    "<pre>pre-formatted fixed-width code block</pre>"\
                    "<pre><code class='language-python'>pre-formatted fixed-width code block written in the Python programming language</code></pre>"

response = requests.get(url=dacha_url, headers=headers)
houses_data = response.json()
for item in houses_data:
    text = f"{item['title']}\n" \
           f"Narxi: {item['price_budniy']}\n" \
           f"Yotoqxonalar soni: {item['price_budniy']}\n" \
           f"Mehmonlar soni: {item['price_budniy']}\n" \
           f"Yotoqxonalar soni: {item['price_budniy']}\n"

    main_photo = "https://i1.wp.com/1dacha-sad.com/wp-content/uploads/2013/03/12-1.jpg"