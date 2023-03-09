from posgSQL import write_data_table

def test_in_dig(txt_msg: str):
    val = txt_msg.split(' ')[0]
    if val.isdigit():
        return int(val)
    else:
        try:
            float(val)
            return float(val)
        except Exception:
            return False


def record_notes(text: str, tg_id):
    item_price = str(test_in_dig(text))
    item_coment = ''
    item_cat = 11
    if text.split(' ')[-1].isdigit():
        if 2 <= int(text.split(' ')[-1]) <= 11:
            item_cat = int(text.split(' ')[-1])
            item_coment = text.replace(item_price, '', 1)[:-2]
    else:
        item_coment = text.replace(item_price, '', 1)
    main_info = (item_price, item_coment, item_cat)
    write_data_table(*main_info, tg_id)
