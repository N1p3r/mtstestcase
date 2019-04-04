import textwrap

def card_mask(card_no):
    card_no = str(card_no)
    card_splited = textwrap.fill(card_no, 4).split("\n")
    if len(card_no) == 16:
        return f"{card_splited[0]} {card_splited[-1]}"
    elif len(card_no) == 18:
        return f"{card_splited[0]} {card_splited[-2]} {card_splited[-1]}"
    raise ValueError("Wrong string length")