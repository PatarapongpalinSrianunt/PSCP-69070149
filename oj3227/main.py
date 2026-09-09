"""ไพ่ 44 ใบ"""
card = input().strip().upper()
# แยกส่วน Rank (ทุกตัวยกเว้นตัวสุดท้าย) และ Suit (ตัวสุดท้าย)
rank_code, suit_code = card[:-1], card[-1]
# Mapping ข้อมูล
ranks = {"A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"}
suits = {"D": "diamonds", "H": "hearts", "S": "spades", "C": "clubs"}
# ใช้ .get() เพื่อดึงค่า หากไม่เจอ key ใน dict จะคืนค่า rank_code เดิม (เช่น เลข 2-10)
rank_str = ranks.get(rank_code, rank_code)
suit_str = suits.get(suit_code, "")
print(f"{rank_str} of {suit_str}".lower())
